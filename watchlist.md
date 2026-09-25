# Watchlist entreprises — pilotage de la veille

<!--
Fichier d'état lu et mis à jour par la routine à chaque run.
« Dernier check » = AAAA-MM-JJ du dernier balayage par entité.
Tiers : A = quotidien · B = hebdomadaire (si dernier check > 7 j) · C = bimensuel / sur signal (> 21 j).
URL « (à confirmer) » : à compléter par l'URL réelle du newsroom/blog au premier balayage.

## Cadence

* **Tier A** (5 entreprises) : vérifié chaque jour — web\_fetch de la source primaire.
* **Tier B** : vérifié si dernier check > 7 jours.
* **Tier C** : vérifié si dernier check > 21 jours, ou si un signal externe le fait remonter.
* Complément indépendant des tiers : newsletters (boîte de veille dédiée) et sources.md,
qui peuvent faire remonter n'importe quelle entreprise hors planning.

\---

## Tier A — vérifié chaque jour

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|Mistral|2026-09-25|https://mistral.ai/news/|Modèles de fondation (France)|
|OpenAI|2026-09-25|https://openai.com/news/|Modèles de fondation|
|Anthropic|2026-09-25|https://www.anthropic.com/news|Modèles de fondation|
|Google DeepMind|2026-09-25|https://deepmind.google/discover/blog/|Recherche \& modèles|
|NVIDIA|2026-09-25|https://blogs.nvidia.com/|Semi-conducteurs / GPU|

\---

## Tier B — vérifié si > 7 jours

### France — Écosystème IA

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|AMI Labs|—|https://amilabs.xyz/updates|Recherche IA / world models|
|H Company|—|https://www.hcompany.ai/|Agents IA|
|Hugging Face|—|https://huggingface.co/blog|Plateforme open source|
|Kyutai|—|https://kyutai.org/|Recherche audio/voix, modèles ouverts|
|Photoroom|—|https://www.photoroom.com/blog|IA générative d'images|
|Pleias|—|https://huggingface.co/PleIAs|LLM open source / données ouvertes|
|Pruna AI|—|https://www.pruna.ai/blog|Optimisation / compression de modèles|
|Dust|—|https://blog.dust.tt/|Agents \& assistants en entreprise|
|Dataiku|—|https://blog.dataiku.com/|Plateforme data science / MLOps|
|Owkin|—|https://www.owkin.com/newsfeed|IA santé / biotech|
|Bioptimus|—|https://www.bioptimus.com|Modèles de fondation pour la biologie|
|Aqemia|—|https://www.aqemia.com|IA découverte de médicaments|
|Wandercraft|—|https://www.wandercraft.eu|Robotique (exosquelettes / humanoïdes)|
|Jimini AI|—|https://www.jimini.ai/en/blog|IA juridique|

### Monde — Grands acteurs

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|Meta AI|—|https://ai.meta.com/blog/|Modèles ouverts / recherche|
|xAI|2026-09-23|https://x.ai/news|Modèles de fondation|
|Microsoft|—|https://blogs.microsoft.com/ai/|Cloud \& IA|
|Amazon / AWS|—|https://aws.amazon.com/blogs/machine-learning/|Cloud \& IA|
|Google|—|https://blog.google/technology/ai/|Cloud \& IA|

### Chine

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|DeepSeek|—|https://www.deepseek.com/en|Modèles de fondation|
|Alibaba (Qwen)|—|https://qwenlm.github.io/blog/|Modèles de fondation|
|Moonshot AI|—|https://www.moonshot.cn|Modèles de fondation (Kimi)|
|Z.ai (Zhipu)|—|https://z.ai|Modèles de fondation (GLM)|
|MiniMax|—|https://www.minimax.io/news|Modèles de fondation|
|Tencent|—|https://hunyuan.tencent.com|Modèles de fondation / cloud IA|

\---

## Tier C — vérifié si > 21 jours ou sur signal

### France — Écosystème IA

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|Gobano Robotics|—|https://www.gobano.ai|Robotique|
|Doctrine|—|https://www.doctrine.fr|Legaltech|
|Neuralk-AI|—|https://www.neuralk-ai.com|IA données tabulaires|
|Prisme.ai|—|https://www.prisme.ai|Plateforme IA générative en entreprise|
|Delos|—|https://www.delos.so|Suite bureautique IA (agents en entreprise)|
|Gradium|—|https://gradium.ai/blog|Voix IA temps réel (issu de Kyutai)|
|Genesis|—|https://www.genesis.ai/press|Robotique (IA physique)|

### Golfe

|Entreprise|Dernier check|Source primaire|Domaine|
|-|-|-|-|
|G42|—|https://g42.ai|IA \& infrastructures (Émirats)|
|MGX|—|https://www.mgx.ae|Fonds d'investissement IA (Émirats)|
|Stargate|—|(à confirmer — coentreprise sans site dédié, suivre via https://openai.com/news/)|Projet d'infrastructure (coentreprise)|



