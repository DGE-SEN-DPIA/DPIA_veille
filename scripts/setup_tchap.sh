#!/usr/bin/env bash
# setup_tchap.sh — Installe les dépendances de scripts/send_tchap.py.
#
# Lancé à chaque run de la routine (le conteneur est neuf à chaque fois).
# Sortie non nulle si une étape échoue (set -e) : l'envoi ne doit pas être
# tenté avec un environnement incomplet.
set -euo pipefail

# matrix-nio 0.26+ utilise vodozemac (Rust) pour le chiffrement E2E ; libolm n'est
# plus requis, mais on l'installe en best-effort pour la rétrocompatibilité.
apt-get update -qq
apt-get install -y --no-install-recommends libolm-dev 2>/dev/null || true

# Toujours cibler l'interpréteur du script (python3), pas pip/pip3 qui peut
# pointer sur une version différente (ex. Python 3.13 au lieu de 3.11).
PIP="python3 -m pip"

# --- atomicwrites -----------------------------------------------------------
# Pourquoi : matrix-nio[e2e] exige atomicwrites~=1.4 (importé par
# nio/crypto/key_export.py et nio/store/file_trustdb.py). send_tchap.py active
# le chiffrement (encryption_enabled=True), l'extra [e2e] est donc indispensable.
#
# Problème : atomicwrites n'est plus maintenu depuis 2022 ; la 1.4.1 n'existe
# qu'en source (pas de wheel) et n'a qu'un setup.py. Sans pyproject.toml, pip 24
# (Debian) la construit par l'ancienne voie « python setup.py bdist_wheel » avec
# le setuptools système (/usr/lib/python3/dist-packages, 68.x patché Debian),
# qui plante : AttributeError: install_layout. L'échec annule TOUT le
# « pip install -r », donc nio n'est jamais installé
# → ModuleNotFoundError: No module named 'nio' (runs du 08 et 09/10/2026).
#
# Correctif : --use-pep517 fait construire la wheel dans un environnement
# temporaire isolé, avec un setuptools récent téléchargé depuis PyPI, via
# l'interface standard build_wheel() ; le setuptools Debian n'est jamais
# utilisé. La wheel produite est installée avec ses métadonnées (.dist-info),
# donc l'exigence atomicwrites~=1.4 est satisfaite à l'étape suivante.
#
# (L'ancien contournement — un atomicwrites/__init__.py écrit à la main dans
# site-packages — ne fonctionnait pas : sans .dist-info, pip considère le
# paquet absent et retente la construction.)
$PIP install --use-pep517 "atomicwrites==1.4.1"

# --- matrix-nio et vodozemac ------------------------------------------------
$PIP install -r "$(dirname "$0")/requirements_tchap.txt"

# Vérification : échoue ici, avec un message clair, plutôt qu'au moment de l'envoi.
python3 -c "import nio, vodozemac, atomicwrites" \
  || { echo "[setup_tchap] échec : dépendances Tchap non importables" >&2; exit 1; }
echo "[setup_tchap] OK"
