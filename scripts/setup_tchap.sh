#!/usr/bin/env bash
set -euo pipefail

# Dépendance système requise par python-olm (chiffrement E2E)
apt-get update
apt-get install -y libolm-dev

# Dépendances Python du script send_tchap.py
# SETUPTOOLS_USE_DISTUTILS=stdlib contourne un échec de build de la roue
# "atomicwrites" (dépendance de matrix-nio[e2e]) avec les setuptools récents
# (AttributeError: install_layout).
SETUPTOOLS_USE_DISTUTILS=stdlib pip install -r "$(dirname "$0")/requirements_tchap.txt"
