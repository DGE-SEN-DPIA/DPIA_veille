#!/usr/bin/env bash
set -euo pipefail

# matrix-nio 0.26+ utilise vodozemac (Rust) pour le chiffrement E2E ; libolm n'est
# plus requis, mais on l'installe en best-effort pour la rétrocompatibilité.
apt-get update -qq
apt-get install -y --no-install-recommends libolm-dev 2>/dev/null || true

# Toujours cibler l'interpréteur du script (python3), pas pip/pip3 qui peut
# pointer sur une version différente (ex. Python 3.13 au lieu de 3.11).
PIP="python3 -m pip"

# atomicwrites 1.4.1 n'a pas de wheel Python 3.11+ et son setup.py échoue
# avec setuptools ≥ 68 (AttributeError: install_layout). On crée un stub minimal
# si le paquet est absent — nio ne l'utilise que pour l'écriture atomique du store.
$PIP show atomicwrites &>/dev/null || python3 - <<'EOF'
import sys, os, textwrap
for base in sys.path:
    if "dist-packages" in base or "site-packages" in base:
        d = os.path.join(base, "atomicwrites")
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, "__init__.py")
        if not os.path.exists(p):
            open(p, "w").write(textwrap.dedent("""
                import contextlib, os, tempfile
                @contextlib.contextmanager
                def atomic_write(path, mode="w", overwrite=False, **kw):
                    d = os.path.dirname(os.path.abspath(path))
                    fd, tmp = tempfile.mkstemp(dir=d)
                    try:
                        with os.fdopen(fd, mode, **kw) as f:
                            yield f
                        (os.replace if overwrite else os.rename)(tmp, path)
                    except:
                        try: os.unlink(tmp)
                        except OSError: pass
                        raise
            """).lstrip())
        break
EOF

$PIP install -r "$(dirname "$0")/requirements_tchap.txt"
