#!/usr/bin/env bash
set -euo pipefail

# Dépendance système requise par python-olm (chiffrement E2E)
apt-get update
apt-get install -y libolm-dev

# Dépendances Python du script send_tchap.py
pip install -r "$(dirname "$0")/requirements_tchap.txt"
