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

## 24/08/2026

| Date | Étape | Description | Statut |
|------|-------|-------------|--------|
| 24/08/2026 | Envoi Tchap (étape 4) | `scripts/send_tchap.py` a terminé avec les mêmes avertissements "Megolm/Olm session missing" (2 401 lignes, aucun Python Exception ni confirmation d'envoi). Pattern identique aux 31/07 et 21/08 — problème persistant non résolu. | Non résolu — commit repo `b2eab34` sur `main` est la source de vérité. Note disponible à https://github.com/DGE-SEN-DPIA/DPIA_veille/blob/main/veilles/2026-08-24.md |

---

*Créé le 31/07/2026*
| 08/10/2026 | Envoi Tchap (étape 4) | `send_tchap.py` : ModuleNotFoundError: No module named 'nio' (setup_tchap.sh sans effet). Pas de relance (règle). | Non résolu — note sur main : veilles/2026-10-08.md |
| 09/10/2026 | Envoi Tchap (étape 4) | `send_tchap.py` : ModuleNotFoundError: No module named 'nio' (identique au 08/10). Pas de relance (règle). | Non résolu — note sur main : veilles/2026-10-09.md |
| 13/10/2026 | Sources directes | openai.com/news : HTTP 403 ; presscorner Commission : page vide au fetch. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 14/10/2026 | Sources directes | openai.com/news et sifted.eu/articles/nvidia-european-investments : HTTP 403 ; PitchBook (2 emails) : corps illisible ; Tier B/C (watchlist) non balayés ce jour. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 15/10/2026 | Sources directes | openai.com/news : HTTP 403 ; PitchBook (2 emails) sans fait exploitable ; Tier B/C non balayés. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 16/10/2026 | Sources directes | openai.com/news et sifted.eu : HTTP 403 ; PitchBook sans fait exploitable ; Tier B/C non balayés. Git : push sur branche désignée claude/gracious-thompson-236mq5 (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 19/10/2026 | Sources directes | openai.com non balayé (403 récurrent) ; Sifted web/Commission non balayés ; PitchBook (4 emails) sans fait exploitable ; Tier B/C hors Meta non balayés. Git : push sur branche désignée claude/gracious-thompson-oqmayb (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 20/10/2026 | Sources directes | openai.com/news et sifted.eu : HTTP 403 ; PitchBook sans fait exploitable ; Tier B/C non balayés (hors Meta). Git : push sur branche désignée claude/gracious-thompson-4tovzc (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 21/10/2026 | Sources directes | openai.com/news et sifted.eu (articles) : HTTP 403 ; DeepMind blog non balayé ; PitchBook sans fait exploitable ; Tier B/C non balayés. Git : push sur branche désignée claude/gracious-thompson-xo38p1 (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 22/10/2026 | Sources directes | openai.com/news et sifted.eu (articles) non balayés (403 récurrent) ; blog NVIDIA sans billets du 21-22/10 (keynote GTC Berlin non couverte) ; PitchBook sans fait exploitable ; Tier B/C non balayés. Git : push sur branche désignée claude/gracious-thompson-zmg6by (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 23/10/2026 | Sources directes | openai.com/news et sifted.eu (articles) non balayés (403 récurrent) ; keynote GTC Berlin non documentée (blog NVIDIA sans billet) ; PitchBook sans fait exploitable ; Tier B/C non balayés. Git : push sur branche désignée claude/gracious-thompson-8u3orb (consigne session) et non main. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 26/10/2026 | Sources directes | openai.com/news, sifted.eu, cnbc.com : HTTP 403 ; page Commission sans contenu ; PitchBook sans fait exploitable ; Tier B/C non balayés. Git : session sur branche claude/nifty-faraday-w4e7zb, push main selon consigne du prompt. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 27/10/2026 | Sources directes | openai.com/news : HTTP 403 ; DeepMind blog sans jours affichés ; blog NVIDIA sans billet postérieur au 22/10 ; PitchBook sans corps lisible ; S-1 Anthropic non confirmé par recherche web ; Tier B/C non balayés. Git : session sur branche claude/nifty-faraday-qos0er, push main selon consigne du prompt. | Non résolu — Dernier check OpenAI laissé au 12/10 |

| 28/10/2026 | Sources directes | openai.com/news non balayé (403 récurrent) ; PitchBook sans corps lisible ; S-1 SEC non consulté directement (chiffres via reprises) ; Tier B/C non balayés. Git : push main selon consigne du prompt. | Non résolu — Dernier check OpenAI laissé au 12/10 |
