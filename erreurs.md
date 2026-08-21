# Journal d'erreurs — Veille IA & Souveraineté

> Format : date | étape | description | statut

---

## 31/07/2026

| Date | Étape | Description | Statut |
|------|-------|-------------|--------|
| 31/07/2026 | Envoi Tchap (étape 4) | `scripts/send_tchap.py` a terminé avec exit code 1. Avertissements "Megolm session missing" normaux (bot dans une room chiffrée existante). L'envoi effectif du message `send_text_message` n'a pas pu être confirmé. Note complète (16 292 car.) et version tronquée (<10 000 car.) toutes deux tentées. | Non résolu — commit repo `cc13ddd` sur `main` est la source de vérité. À rediagnostiquer lors de la prochaine session. |

---

## 21/08/2026

| Date | Étape | Description | Statut |
|------|-------|-------------|--------|
| 21/08/2026 | Envoi Tchap (étape 4) | `scripts/send_tchap.py` a terminé avec les mêmes avertissements "Megolm/Olm session missing" que le 31/07. Aucun Python Exception ni message d'erreur d'envoi explicite dans la sortie. Statut d'envoi non confirmé — comportement identique au pattern documenté le 31/07. | Non résolu (problème persistant) — commit repo `fb2d684` sur `main` est la source de vérité. Note complète disponible à https://github.com/DGE-SEN-DPIA/DPIA_veille/blob/main/veilles/2026-08-21.md |

---

*Créé le 31/07/2026*
