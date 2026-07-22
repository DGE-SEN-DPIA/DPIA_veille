# Base entreprises — capitalisation veille IA

<!--
Fichier persistant lu EN ENTRÉE et mis à jour EN SORTIE par la routine « Veille IA & Souveraineté ».
Structuré ENTREPRISE PAR ENTREPRISE. Ne jamais écraser une section : compléter en datant.
-->

## Mode d'emploi
Pour chaque entreprise concernée par une annonce, compléter sa section selon le schéma :
- **Dernière MAJ** : JJ/MM/AAAA
- **Financement** : tours, montants, investisseurs, dates
- **Produits / modèles** : lancements, versions
- **Contrats & partenariats** : clients, alliances industrielles
- **Orientations stratégiques** : pivots, recrutements clés, expansion
- **À surveiller** : signaux faibles, échéances, points d'attention

Les sections ci-dessous sont pré-créées à partir de la watchlist. Domaines marqués
« à confirmer » : à préciser à la première mention réelle.

---

# France — Écosystème IA

## Mistral (France, modèles de fondation / LLM / cloud souverain)
- Dernière MAJ : 13/07/2026
- Financement : 12/06/2026 — négociations (stade précoce, termes non arrêtés) pour une levée d'environ 3 Md€ (3,5 Md$) à une valorisation proche de 20 Md€, contre 11,7 Md€ lors de la série C de septembre 2025 (ASML, ~11 %, 1,3 Md€). [Bloomberg/Maddyness/TechCrunch, 12/06/2026]. 25/06/2026 — statu quo, stade précoce.
  19/06/2026 — Extension infrastructure Suède : 1,4 Md$ supplémentaires annoncés à VivaTech pour une deuxième capacité de calcul en Europe (Suède), dans la trajectoire 200 MW pour 2027. [VentureBeat, 19/06/2026 — 1 source]
- Produits / modèles : 28/05/2026 — **Mistral for Industrial Engineering** : surrogate modeling pour Airbus (5 ans, défense/espace/hélicoptères), BMW, EDF, CMA CGM. 28/05/2026 — **Vibe** : rebrand de Le Chat en plateforme agentique unifiée (Work Mode + Code Mode), annoncé lors de la conférence annuelle Mistral à Paris (Carrousel du Louvre). [Mistral.ai/news, 28/05/2026]. 16/06/2026 — **"L'Assistant"** — agent conversationnel Mistral déployé à ~1 M agents de l'État français (coût 700 k€). [France 24, 16/06/2026]
- Contrats & partenariats : Datacenter de Bruyères-le-Châtel (Essonne, 44 MW, 13 800 GPU Nvidia GB300 selon DCD mars 2026 / 18 000 GB200 selon VentureBeat 19/06 — discordance à confirmer), financé par 830 M$ (722 M€) de dette (Bpifrance, BNP, CA-CIB, HSBC, La Banque Postale, MUFG, Natixis), opéré par Eclairion. **OPÉRATIONNEL** avec clients enterprise (confirmé à VivaTech, 19/06/2026). Partenaires early adopters : BNP Paribas, Orange, SNCF, Thales, Kyutai, Veolia, Schneider Electric.
  19/05/2026 — **Acquisition d'Emmi AI** (Vienne, Autriche), Physics AI pour simulation industrielle, >30 chercheurs intégrés. [Mistral AI/Channel News, 19-26/05/2026]
  28/05/2026 — **Clients Industrial Engineering** : Airbus (5 ans, défense/espace), BMW (crash simulation), EDF, CMA CGM.
  10/06/2026 — **Mistral / Digital Realty** : 10 MW de cluster IA sur datacenter Digital Realty Paris. [DCD, 28/05/2026]
- Orientations stratégiques : Pivot « cloud full-stack company » (Mensch, VivaTech 19/06) ; concurrent direct des hyperscalers US pour les marchés publics et industriels EU ; programme global infrastructure de 4 Md€ (France + Suède), cible 200 MW en Europe en 2027 et 1 GW en 2030. Arthur Mensch explore également la conception de puces propres [CNBC, 28/05].
  23/06/2026 — **OCR 4** : modèle d'extraction documentaire déployable en conteneur unique on-premise (aucun envoi de données hors infrastructure client). Couvre 170 langues avec boîtes de délimitation au niveau paragraphe, scores de confiance inline et intégration RAG directe. Win rate 72 % en tests aveugles indépendants. Tarif API : $4/1 000 pages ($2 en Batch API), $5 pour Document AI. Disponible sur Mistral API, Amazon SageMaker et Microsoft Foundry. Première alternative souveraine crédible aux APIs cloud US pour l'extraction documentaire dans les secteurs réglementés (banque, santé, défense, marchés publics). [mistral.ai/news/ocr-4/, 23/06/2026]
  Juin 2026 — **Mistral Robotique** : lancement d'un programme R&D robotique (algorithmes navigation, manipulation, raisonnement). Recrutement d'Olivier Duchenne (ex-Aldebaran, INRIA, Meta Robotics). Taux de réussite annoncé : 96 % sur préparation de kits de pièces pour chaînes de montage. Déploiement en usines conditionné à l'atteinte d'un seuil de rendement suffisant. [Usine Nouvelle, juin 2026 — date précise à confirmer]
  25/06/2026 — **Les Ulis (Essonne), 10 MW, dédié à l'inférence** : troisième site de calcul Mistral, ouverture Q3 2026. Distinct de Bruyères-le-Châtel (training/cloud) et de la future extension suédoise. Objectif : contrôle direct de la capacité d'inférence, réduction dépendance cloud tiers. [VentureBeat / Futurum, juin 2026 — 1 source]
  **06/07/2026 — ARR confirmé >$400 M** (début 2026), trajectoire $1 Md fin 2026 selon Mensch. Valorisation citée ~$23 Md dans certains médias en lien avec les discussions de levée (1 source, à confirmer). [AI Weekly, TechTimes, juillet 2026]
  **06/07/2026 — Nouveau modèle MoE open-weight en early access partenaires** : architecture « fat but sparse » (Mixture-of-Experts). Paramètre count, benchmarks et licence non divulgués à date. Lancement public élargi visé « plus tard cet été ». [TechTimes 06/07/2026 ; AI Weekly juillet 2026]
  **08/07/2026 — Robostral Navigate** : premier modèle d'IA physique robotique Mistral. 8B paramètres, navigation autonome sur une seule caméra RGB ordinaire. **76,6 % sur R2R-CE** (validation, scènes inconnues) — +9,7 pts vs. meilleure approche monoculaire précédente, +4,5 pts vs. meilleurs systèmes multi-capteurs (LiDAR inclus). Entraîné 100 % en simulation (400 000 trajectoires, 6 000 scènes), affiné par RL en ligne. Hardware agnostic (wheels, legged, flying). Applications : manufacturing, delivery, logistique, hospitality. Directement lié au pivot robotique amorcé avec Emmi AI (19/05) et Mistral for Industrial Engineering (28/05). [Bloomberg + mistral.ai/news/robostral-navigate/ + eWeek, 08-09/07/2026]
  **02/07/2026 — Leanstral 1.5** : modèle de preuve mathématique et de vérification formelle de logiciel pour l'assistant de preuve Lean 4. **119 B paramètres totaux, 6,5 B actifs** (MoE), contexte 256k tokens, licence **Apache 2.0**, poids sur Hugging Face. Performances : sature miniF2F, 587/672 problèmes PutnamBench, FATE-H 87 %, FATE-X 34 %. Impact concret : **5 bugs inédits découverts** dans 57 dépôts de code réels. Positionnement : Mistral entre sur le marché de la vérification automatique de logiciel critique — pertinent pour la défense, le nucléaire, le spatial, la finance et l'audit de code IA public. [Mistral, mistral.ai, 02/07/2026 ; AI Weekly + TestingCatalog, 02/07/2026]
- Dernière MAJ : 21/07/2026
- À surveiller : Clôture levée ~3 Md€ et investisseurs ; confirmation valorisation ~$23 Md ; lancement public modèle MoE open-weight (été 2026) ; ouverture Les Ulis Q3 2026 ; confirmation chiffre GPU Bruyères-le-Châtel (discordance 13 800 vs. 18 000) ; extension de L'Assistant aux collectivités territoriales ; résultats commerciaux Industrial Engineering ; financement Suède ; premiers déploiements Robostral Navigate en flotte industrielle ; adoption Leanstral 1.5 pour audit de code IA dans les secteurs réglementés.

## AMI Labs (France, recherche IA fondamentale / world models — Yann LeCun)
- Dernière MAJ : 18/06/2026
- Financement : Seed/Série A — ~890 M€ (env. 1,03 Md$), mars 2026 ; investisseurs : Cathay Innovation, Hiro Capital (confirmés Bloomberg janv. 2026), parmi d'autres.
- Produits / modèles : World models — IA visant à comprendre et modéliser les principes physiques du monde réel (causalité, dynamique des objets) ; repositionnement par rapport aux LLM "tokens" au profit de représentations continues de l'environnement.
- Contrats & partenariats : —
- Orientations stratégiques : Fondée par Yann LeCun (ex-VP AI Meta, lauréat Turing) et associés ; siège Paris ; focus embodied AI et IA physique. Entrée au **Next40 French Tech promotion 2026** (annoncé 15/06/2026). Keynote à VivaTech 2026 (Yann LeCun).
- À surveiller : Premiers modèles ou démos publiques ; partenariats industriels (robotique, automobile) ; positionnement vs AMI Labs / Genesis AI sur le segment world models.

## H Company (France, agents IA)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : Début juin 2026 — lancement de trois agents : Surfer H (poids ouverts sur Hugging Face/Amazon Marketplace, propulsé par le modèle visuel-langage propriétaire Holo-1, 92,2 % de succès sur le benchmark WebVoyager, coûts jusqu'à 5,5x inférieurs aux concurrents américains), Runner H (bêta publique, automatisation d'applications comme Gmail/Docs/Notion/Slack), Tester H (bêta privée, QA automatisée).
- Contrats & partenariats : 04-05/06/2026 — a rejoint la « Nemotron Coalition » de Nvidia (coalition internationale de labos pour modèles de fondation open source de nouvelle génération), annoncé lors du GTC Taipei, avec accès à du calcul mutualisé. [H Company/Maddyness UK, 05/06/2026]
- Orientations stratégiques : Positionnement agentique « computer use », en concurrence frontale avec Anthropic/OpenAI sur l'automatisation web/bureau. **Entrée au Next40 French Tech promotion 2026** (annoncé 15/06/2026). [Maddyness, 15/06/2026]
- À surveiller : Adoption de Surfer H en open weight ; retombées concrètes de la coalition Nemotron pour l'accès au calcul ; levée de fonds.

## Neuralk-AI (France, IA industrielle / prédictif)
- Dernière MAJ : 19/06/2026
- Financement : inclus dans les ~150 M$ cumulés des 7 startups AWS/NVIDIA Startup Village VivaTech (montant propre non isolé).
- Produits / modèles : **Seldon** — modèle fondation tabulaire enterprise pour l'analytique prédictive ; fondée 2023. Agent prédictif pour projets machine learning (usages industriels).
- Contrats & partenariats : Sélectionnée **Startup Village AWS/NVIDIA VivaTech 2026** (17-20/06/2026).
- Orientations stratégiques : **Nuit de la Data et de l'IA 2026 — médaille de bronze** pour son agent prédictif ML. [Républik IT, 2026]
- À surveiller : Levée de fonds standalone ; clients industriels ; précision du domaine (manufacturing, maintenance prédictive ?).

## pyannoteAI (France, intelligence du locuteur) — NOUVEAU ENTRANT
- Dernière MAJ : 19/06/2026
- Financement : non public (~20 M€ en préparation selon presse).
- Produits / modèles : Diarization speaker streaming en temps réel (identification qui parle, quand, comment) ; premier modèle streaming diarization de qualité production commerciale. >1 milliard de téléchargements sur Hugging Face.
- Fondée : 2024 (issue de 12 ans de recherche CNRS).
- Contrats & partenariats : AWS (infrastructure). Sélectionnée **Startup Village AWS/NVIDIA VivaTech 2026** (17-20/06/2026). Démos live diarization temps réel sur audio réel.
- Orientations stratégiques : Cible agents vocaux, transcription, industries réglementées.
- À surveiller : Levée de fonds annoncée ; déploiements enterprise.

## Pleias (France, LLM open source / données ouvertes)
- Dernière MAJ : 23/06/2026
- Financement : —
- Produits / modèles :
  Juin 2026 — **SYNTH** : premier dataset génératif généraliste open source CC-BY-SA pour l'entraînement de petits modèles de raisonnement (79,6 M exemples, 41 Md mots, ~75 Md tokens Pleias tokenizer), basé sur 58 698 articles Wikipedia (Wikimedia Enterprise). Co-release avec l'AI Alliance. [huggingface.co/datasets/PleIAs/SYNTH]
  Juin 2026 — **Baguettotron** : modèle de raisonnement entraîné exclusivement sur SYNTH (200 Md tokens, 80 couches) — best-in-class pour sa catégorie de taille sur MMLU et benchmarks de raisonnement. [HuggingFace, Threads @sung.kim.mw]
- Contrats & partenariats : Co-publication SYNTH avec l'AI Alliance. Soutenu par LANGU:IA (start-up d'État, DINUM/Ministère de la Culture), préfiguration d'ALT-EDIC.
- Orientations stratégiques : Fondé par Pierre-Carl Langlais. Focus données ouvertes, reproducibilité, open science. SYNTH = démonstration qu'un dataset 100 % ouvert peut former des modèles compétitifs.
- À surveiller : Date exacte de release SYNTH ; adoption par d'autres labos ; levée de fonds ; prochains modèles.

## Photoroom (France, IA générative d'images)
- Dernière MAJ : 25/06/2026
- Financement : —
- Produits / modèles :
  **PRX** — modèle text-to-image entraîné from scratch, publié en open source sur Hugging Face (Apache 2.0). 1,3 milliard de paramètres, architecture MMDiT simplifiée (tokens texte non-updated via transformer blocks), flow-matching avec scheduling discret, encodeur texte T5-Gemma-2B multilingue (multilingual). Entraîné en <10 jours sur 32 GPU NVIDIA H200 à résolution 1024px. Famille PRX : base, SFT et distillée, aux résolutions 256/512/1024px. [huggingface.co/blog/Photoroom/prx-open-source-t2i-model ; Photoroom/PRX GitHub]
- Contrats & partenariats : —
- Orientations stratégiques : Publication transparente incluant poids, expériences et ablations ; positionnement « open science ». Hébergé sur Hugging Face en format Diffusers. Date exacte de release à confirmer.
- À surveiller : Adoption par la communauté open source ; performances vs. SDXL/Flux sur benchmarks standardisés ; applications e-commerce (cœur de métier Photoroom).

## Hugging Face (France/US, plateforme & hub de modèles open source)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Kyutai (France, laboratoire de recherche IA — audio/voix, modèles ouverts)
- Dernière MAJ : 24/06/2026
- Financement : 300 M€ sur 5 ans (Iliad, CMA CGM, Schmidt Futures) — fondation à but non lucratif, nov. 2023.
- Produits / modèles :
  - Moshi (voix, modèle temps réel) ; modèles audio ouverts.
  - 10/06/2026 — recherche sur les modèles de dialogue spoken full-duplex via RL (post-training pour meilleure interactivité).
  - 18/06/2026 — **"FID Lottery"** : étude sur la variance cachée des scores FID dans l'évaluation des modèles génératifs. Impact méthodologique : invalide la comparabilité directe de nombreux benchmarks génératifs.
- Contrats & partenariats : lié à Mistral Compute (premier early adopter), Iliad (fondateur).
- Orientations stratégiques : Recherche ouverte, publication systématique, modèles audio open-source.
- À surveiller : Publications sur la sécurité des évaluations génératifs ; lien avec Gradium (spin-off audio).

## Gradium (France, IA vocale — spin-off Kyutai)
- Dernière MAJ : 22/07/2026
- Financement :
  Décembre 2025 — **Seed initial $70 M** : FirstMark Capital (lead), Eurazeo, DST Global Partners, Eric Schmidt, Xavier Niel (Iliad), Rodolphe Saadé (CMA CGM), Korelya Capital, Amplify Partners.
  **09/07/2026 — Extension seed : +~$30 M, NVIDIA nouvel investisseur → total $100 M+.** Gradium rouvre son tour seed avec NVIDIA comme nouveau backer stratégique. [TechCrunch + Maddyness + Sifted + gradium.ai, 09/07/2026]
- Produits / modèles : Modèles voix natifs IA ultra-basse latence : transcription temps réel multilingue, synthèse vocale (TTS), clonage de voix, traduction. API disponible (bêta → GA).
- Contrats & partenariats : AWS (infrastructure inference principale). NVIDIA (investisseur + partenariat compute). Présence Startup Village AWS/NVIDIA VivaTech 2026 (17-20/06/2026).
- Orientations stratégiques : Concurrencer ElevenLabs et les acteurs US de la voice tech. Cible agents conversationnels et industries réglementées. Expansion bureau Silicon Valley (juillet 2026). Fondateurs : Neil Zeghidour (CEO, ex-Google Brain/DeepMind/Facebook), Alexandre Défossez (CSO), Olivier Teboul (CTO), Laurent Mazaré (CCO).
- À surveiller : Premiers contrats enterprise annoncés publiquement ; montée en charge de l'API ; prochaine levée Série A.

## Genesis AI (France/US, robotique — world models pour la manipulation physique)
- Dernière MAJ : 18/06/2026
- Financement : Seed de 105 M$ (Eclipse, Khosla Ventures, Bpifrance, HSG, Eric Schmidt, Xavier Niel…), annoncé début mai 2026.
- Produits / modèles :
  - GENE-26.5 — modèle robotique pour manipulation physique de niveau humain (main robotique dextre), dévoilé début mai 2026.
  - **Eno** — premier robot humanoïde généraliste, lancé le 17/06/2026 ; propulsé par le foundation model GENE (dextérité + agentic AI + tâche autonome) ; design minimaliste : base à roues + bras anthropomorphes dextres, hauteur ajustable. [PRNewswire/Robotics and Automation News, 17/06/2026]
- Contrats & partenariats : —
- Orientations stratégiques : Fondée par Théophile Gervet (ex-Mistral AI) et Zhou Xian (Carnegie Mellon) ; double siège Paris/Silicon Valley. Déploiements Eno prévus fin 2026 : manufacturing, logistique, laboratoires ; puis hôtels/hôpitaux ; puis usage domestique.
- À surveiller : Premières commandes industrielles ; partenariats ; prochaine levée.

## Gobano Robotics (France, robotique)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Wandercraft (France, robotique — exosquelettes / robots humanoïdes)
- Dernière MAJ : 24/06/2026
- Financement : —
- Produits / modèles : Robot humanoïde « Calvin » (1,70 m), visant l'autonomie complète sans supervision humaine « dans quelques semaines » selon le co-fondateur Jean-Louis Constanza.
- Contrats & partenariats : Avec Renault — Calvin testé depuis février 2026 sur le site de Douai (manutention de pneus de 25 kg, capacité de 7-8 chariots de 24 pneus en 1h30) ; présentation presse le 08/06/2026. Objectif : 10 robots opérationnels à Douai fin 2026, et déploiement de 350 unités dans les usines Renault d'ici 2027 (mise en service complète été 2026). [Usine Nouvelle/Journal Auto, 08/06/2026]
- Orientations stratégiques : —
  Eté 2026 — **Calvin pleinement opérationnel** sur la ligne R5 (nuit) de l'usine Renault Douai. Supervision humaine réduite à la sécurité de balance. [Usine Nouvelle / France 3 Hauts-de-France]
- À surveiller : Extension à d'autres lignes et sites Renault (cible 350 robots en 18 mois) ; levée de fonds Wandercraft ; cas d'usage IA industrielle/IA physique emblématique.

## Aire / FLOPS & FRIENDS (France/US, IA scientifique R&D enterprise) — NOUVEL ENTRANT
- Dernière MAJ : 09/07/2026
- Financement : Seed de $400 M cible à ~$2 Md de valorisation — tour en cours, non clôturé au 09/07/2026. [French Tech Journal + Sifted, juillet 2026 — 2 sources]
- Produits / modèles : « AI scientist » pour automatiser la R&D enterprise (biologie, physique, finance).
- Contrats & partenariats : —
- Orientations stratégiques : Fondée par Irwan Bello (ex-OpenAI), Gabriel Synnaeve (ex-Meta FAIR Paris) et Yossi Adi. Opérations transatlantiques, ancrage Paris via Synnaeve. Statut legal et siège à confirmer.
- À surveiller : Clôture du seed et identité des investisseurs ; premiers produits publics ; positionnement vs. Prometheus (Bezos/Bajaj) et OpenAI o3-pro sur le segment AI scientist.

## OpenAI (US, LLM / agents / infrastructure IA)
- Dernière MAJ : 09/07/2026
- Financement : —
- Produits / modèles :
  26/06/2026 — **GPT-5.6 Sol/Terra/Luna (preview)** : preview limitée ~20 partenaires gouvernementaux US. Sol (flagship), Terra (everyday), Luna (économique).
  09/07/2026 — **GPT-5.6 GA mondiale** : Sol $5/$30, Terra $2,50/$15, Luna $1/$6 par M tokens input/output. Ultra mode (Sol) : multi-agents embarqués, sous-agents parallèles facturés séparément. Sol disponible sur Cerebras à 750 tokens/s. Cache : breakpoints explicites, durée min. 30 min, cache-write 1,25× taux non mis en cache.
- Contrats & partenariats : Partner Network mondial $150 M (14/06/2026, Accenture/Bain/BCG/McKinsey/PwC). Partenariat DoC US pour pré-release Gov (cadre EO 1er août).
- Orientations stratégiques : Nouveau schéma de naming tiered (Sol/Terra/Luna) applicable aux générations futures. Accélération inférence via Cerebras (Jalapeño chip).
- À surveiller : Disponibilité Azure OpenAI Service et AWS Bedrock pour GPT-5.6 (déploiements souverains FR) ; réponse METR flag sur benchmark gaming ; IPO (tilt vers 2027 selon Kalshi).

## Jimini AI (France, IA juridique — droit des affaires)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Doctrine (France, legaltech — recherche & analyse juridique)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Pruna AI (France, optimisation / compression de modèles)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Owkin (France, IA pour la santé / biotech)
- Dernière MAJ : 22/06/2026
- Financement : 12/03/2026 — Spin-off Waiv (ex-Owkin Dx, diagnostics IA) : 33 M$ de financement annoncé. [BusinessWire, 12/03/2026]
- Produits / modèles : Plateforme « AI Scientist » K Pro — agents IA pour la biopharma (identification de cibles, décisions de développement de médicaments, pipelines scientifiques autonomes).
- Contrats & partenariats :
  05/06/2026 — **Collaboration pluriannuelle avec Sanofi** : licence 5 ans pour K Pro ; Owkin co-développe des agents IA biopharma de nouvelle génération ; extension d'un partenariat historique €90 M (depuis 2021, oncologie). [BusinessWire/owkin.com, 05/06/2026]
  Mai 2026 — **Accord similaire avec AstraZeneca** : agents IA pour l'intelligence compétitive et les workflows décisionnels. [Owkin news]
- Orientations stratégiques : Pivot vers un modèle « agent-as-a-service » dans la pharma réglementée mondiale ; deux contrats majeurs (Sanofi + AstraZeneca) en deux mois confirment la demande de délégation autonome de tâches scientifiques complexes.
- À surveiller : Détails financiers contrats Sanofi/AstraZeneca ; performance des agents K Pro en R&D clinique réelle ; trajectoire de Waiv ; levée Owkin principale.

## Bioptimus (France, modèles de fondation pour la biologie)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Aqemia (France, IA pour la découverte de médicaments)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Dust (France, agents & assistants IA en entreprise)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Delos (France, bureautique GenAI souveraine)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : **IAgen** — suite bureautique GenAI, présentée comme la « première alternative européenne AI native » aux solutions américaines (Microsoft 365 Copilot, Google Workspace AI).
- Contrats & partenariats : —
- Orientations stratégiques : **Nuit de la Data et de l'IA 2026 — médaille d'or** (IAgen). [Républik IT, 2026]
- À surveiller : Levée de fonds ; déploiements enterprise ; positionnement SecNumCloud / marchés publics.

## Dataiku (France/US, plateforme data science & MLOps)
- Dernière MAJ : 16/06/2026
- Financement : —
- Produits / modèles : **Cobuild** — agent IA de construction de projets ML/IA en entreprise. Annoncé le 11/06/2026, disponibilité générale (GA) le 18/06/2026. Génère des pipelines, modèles ML, agents et applications production à partir d'instructions en langage naturel, avec gouvernance et revue humaine intégrées dans le Flow Dataiku. Supporte Snowflake Cortex, OpenAI, Anthropic, Bedrock, Gemini, Foundry, Databricks. [BusinessWire/Dataiku, 11/06/2026]
- Contrats & partenariats : —
- Orientations stratégiques : Pivot vers « Platform for AI Success » (mars 2026) — orchestration de l'IA agentique en entreprise, avec gouvernance comme différenciateur face à l'hyperautomatisation non contrôlée.
- À surveiller : Adoption de Cobuild en GA (18/06/2026) ; impact sur la concurrence avec Microsoft Fabric/Copilot Studio côté plateformes ML.

## Prisme.ai (France, IA agentique souveraine pour l'entreprise)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : **SelfAI** — plateforme d'IA agentique souveraine pour l'entreprise.
- Contrats & partenariats : **VivaTech 17-18/06/2026** — annonce de trois nouveaux clients : ArianeGroup (espace/défense), Pierre Fabre (pharmacie), ODDO BHF (banque), en présence de la ministre du Numérique et de son homologue allemand. [La Revue du Digital, 18/06/2026]
- Orientations stratégiques : Positionnement IA agentique souveraine, en concurrence avec Dust, Delos, solutions américaines. Nuit de la Data et de l'IA 2026 — argent (SelfAI).
- À surveiller : Extension sectorielle (défense, industrie) ; levée de fonds.

---

## ChapsVision (France, analyse de données souveraine — renseignement & sécurité)
- Dernière MAJ : 24/06/2026
- Financement : Non public.
- Produits / modèles : **Argonos** — plateforme d'analyse de données de renseignement et de sécurité intérieure, alternative souveraine à Palantir Gotham.
- Contrats & partenariats :
  16/06/2026 — **DGSI (France)** : ChapsVision remplace Palantir Gotham à la DGSI (annoncé par Lecornu). Migration sur plusieurs années ; déploiement opérationnel 2027. [Boursorama/Euronews, 16/06/2026]
  Mai 2026 — **BfV (Allemagne)** : services de renseignement intérieur allemands choisissent également Argonos en remplacement de Palantir.
- Orientations stratégiques : Fondée en 2019 par Olivier Dellenbach (polytechnicien). Développée par acquisitions. Positionnée comme l'alternative EU à Palantir dans les services de sécurité occidentaux. Standard franco-allemand de fait en juin 2026 pour les outils d'analyse de renseignement souverains.
- À surveiller : Autres contrats publics en Europe (après France + Allemagne) ; levée de fonds ; montée en puissance face à Palantir sur les marchés publics UE.

---

# France — Cloud souverain

## OVHcloud (France, cloud souverain)
- Dernière MAJ : 15/06/2026
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : 11/06/2026 — OVH Groupe entre en négociations exclusives pour racheter Gladia, startup française de transcription/intelligence audio (speech-to-text), qui dessert >300 000 développeurs et 2 000 clients entreprise dans >100 langues. Montant non communiqué. Deuxième acquisition d'OVH dans cette logique d'intégration verticale de briques IA. [OVH Groupe/GlobeNewswire, Maddyness, 11-12/06/2026]
- Orientations stratégiques : Renforcement de l'offre IA générative/agentique souveraine de l'AI Lab (OVHai).
- À surveiller : Montant et calendrier de clôture du rachat de Gladia ; stratégie « build vs. buy » pour les briques IA souveraines (voix, vision).

## Scaleway (France, cloud)
- Dernière MAJ : 08/07/2026
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : Membre du consortium AION (avec Ardian, Capgemini, EDF, Orange, Bull, iliad…) candidat à une AI Gigafactory européenne en France [annonce datée du 21/05/2026 selon EDF, antérieure à la fenêtre, à recroiser].
  18/06/2026 (VivaTech) — **Partenariat Scaleway / VSORA / ZML / Région Île-de-France** : engagement à déployer les premiers serveurs équipés de Jotunn8 (accélérateur IA inférence VSORA, TSMC N5, CoWoS) dans les datacenters Scaleway. ZML assure la couche logicielle d'inférence multi-hardware. Objectif : premières infrastructures IA souveraines haute performance en Île-de-France, sans dépendance NVIDIA/AMD. Premier déploiement industriel d'un accélérateur IA conçu en France dans un cloud certifié souverain. [GlobalNewsWire / Usine Digitale / La Revue du Digital, 18/06/2026]
- Orientations stratégiques : 01/06/2026 — hausse tarifaire moyenne de +25 % (jusqu'à +300 % sur certaines instances comme STARDUST) sur 78 lignes tarifaires (instances, stockage, bare metal Iridium/Dedibox), justifiée par la hausse des coûts matériels (RAM, stockage) et la pression sur les adresses IPv4. [channelnews.fr/silicon.fr, 01/06/2026]
- À surveiller : Calendrier déploiement opérationnel Jotunn8 chez Scaleway ; impact de la hausse tarifaire sur la compétitivité face aux hyperscalers ; suite du consortium AION.

## VSORA (France, semi-conducteurs — accélérateur inférence IA)
- Dernière MAJ : 08/07/2026
- Financement : non public
- Produits / modèles : **Jotunn8** — accélérateur IA conçu en France pour l'inférence en datacenter, gravé chez TSMC (procédé N5, packaging CoWoS). Premier accélérateur IA de fabrication européenne (design France, fab TSMC) destiné à des clouds souverains.
- Contrats & partenariats : 18/06/2026 — partenariat avec Scaleway, ZML et la Région Île-de-France pour le déploiement des premiers serveurs Jotunn8 dans les datacenters Scaleway.
- Orientations stratégiques : Alternative souveraine aux GPU NVIDIA/AMD pour les workloads d'inférence, compatible avec la stack logicielle ZML (multi-hardware sans réécriture). Positionnement IA souveraine européenne.
- À surveiller : Disponibilité commerciale Jotunn8 ; performances vs. NVIDIA H100/H200 sur les benchmarks inférence ; prochaine levée de fonds.

## Outscale (France, cloud — groupe Dassault Systèmes)
- Dernière MAJ : 14/06/2026
- Financement : —
- Produits / modèles : 09/06/2026, lors d'OUTSCALE Experiences 2026 (CNIT Paris La Défense) : lancement d'« AI Factories by OUTSCALE » (industrialisation de l'IA en environnement souverain), d'OUTSCALE Kubernetes as a Service (visant la qualification SecNumCloud 3.2), d'OUTSCALE Managed Databases (avec NuoDB) et d'un émulateur quantique sur le Marketplace.
- Contrats & partenariats : Partenariat avec PariSanté Campus et le 3DEXPERIENCE Lab de Dassault Systèmes pour l'accompagnement de startups healthtech. [3ds.com/newsroom, blog.outscale.com, 09/06/2026]
- Orientations stratégiques : Renforcement de l'offre cloud souverain IA face à Microsoft Azure/AWS/Google Cloud.
- À surveiller : Calendrier effectif de qualification SecNumCloud 3.2 pour OUTSCALE Kubernetes as a Service.

## Cloud Temple (France, cloud souverain)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

---

# France — Quantique

## Pasqal (France, calcul quantique — atomes neutres)
- Dernière MAJ : 01/07/2026
- Financement : SPAC en cours — fusion avec Bleichroeder Acquisition Corp. II (Nasdaq : BBCQ), valorisation ~2 Md$, montée en bourse visée ~170 M€. Analyst Day tenu à New York le 30/06/2026.
- Produits / modèles : Processeurs quantiques à atomes neutres.
- Contrats & partenariats :
  30/06/2026 — **Partenariat approfondi Crédit Agricole CIB** : informatique quantique appliquée à la finance (mesure de risque, optimisation de portefeuille, suivi consommation fonds propres). Premiers cas d'usage en production visés dès 2028. Montant non communiqué.
- Orientations stratégiques : Double trajectoire : cotation Nasdaq via SPAC + contrats finance/industrie en parallèle.
- À surveiller : Closing du SPAC ; annonce de clients production ; extension au-delà de la finance (énergie, pharma).

## Quandela (France, calcul quantique photonique)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Alice & Bob (France, calcul quantique — qubits de chat)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

---

# Monde — Grands labos & acteurs majeurs

## OpenAI (États-Unis, modèles de fondation)
- Dernière MAJ : 02/07/2026
- Financement : 08/06/2026 — dépôt confidentiel d'un formulaire S-1 auprès de la SEC en vue d'une IPO, visant une valorisation proche de 1 000 Md$ (contre 852 Md$ lors de la dernière levée privée), Goldman Sachs et Morgan Stanley mandatés ; aucun calendrier de cotation arrêté. [openai.com/CNBC/Fortune, 08-09/06/2026]
- Produits / modèles : Depuis le 01/06/2026, GPT-5.5, GPT-5.4 et Codex sont en disponibilité générale sur Amazon Bedrock, au tarif first-party OpenAI sans surcoût. [AWS blog, 01/06/2026]
- Contrats & partenariats : Stargate — démarrage le 01/06/2026 de la construction du campus « The Barn » (Saline, Michigan, 1 GW, 1,65 M m²), avec Oracle/Related Digital/Blackstone/Walbridge (16 Md$ construction + 40 Md$ équipement compute Oracle), mise en service début 2028. Ouverture/mise en avant d'un bureau à Madrid le 11/06/2026 (présentée par l'Espagne comme validation de sa stratégie régulatoire).
  11/06/2026 — Acquisition d'Ona (ex-Gitpod) : infrastructure cloud sécurisée pour agents IA persistants, destinée à renforcer Codex pour les workflows enterprise longue durée. Termes non divulgués. [CNBC/InfoWorld, 11/06/2026]
  14/06/2026 — **Lancement de l'OpenAI Partner Network** : premier programme mondial de partenaires, 150 M$ investis, système 3 niveaux (Select/Advanced/Elite), objectif 300 000 consultants certifiés fin 2026. Partners fondateurs : Accenture, Bain, BCG, McKinsey, PwC. [openai.com/Dataconomy, 14/06/2026]
- Orientations stratégiques : Course à l'IPO — tilt vers 2027 (NYT 25/06) : Altman refuse valorisation sous $1T ; SpaceX IPO performance décevante (-24 % du pic). Kalshi 59 % pour annonce officielle IPO avant mars 2027. Expansion européenne (Espagne) ; pivot vers la bataille des intégrateurs en entreprise via le Partner Network.
  26/06/2026 — **GPT-5.6 Sol, Terra, Luna** lancé en preview limitée (~20 org. approuvées US gov). Sol : $5/$30/M tokens ; Terra : $2,50/$15 ; Luna : $1/$6. Cadre EO "trusted preview" → assessment classifié → GA (coming weeks, probablement juillet). [OpenAI newsroom, 26/06/2026]
  **09/07/2026 — GPT-5.6 Sol, Terra, Luna en GA** : Sol ($5/$30/M tokens), Terra ($2,50/$15), Luna ($1/$6) disponibles en disponibilité générale. [OpenAI, 09/07/2026]
  Juillet 2026 — **GPT-5.6 Sol / Cerebras** : déploiement sur infrastructure Cerebras (chip « Jalapeño »), vitesse jusqu'à 750 tokens/seconde (~15× GPT-5.5), ciblant les applications enterprise en temps réel. [KuCoin/VentureBeat, juillet 2026]
  **~25/06/2026 — IPO reporté à 2027** : conseillers recommandent de reporter l'IPO ciblé automne 2026, après la forte volatilité post-cotation de SpaceX (IPO $135, pic $225+, rechute à $153 en dix jours). Altman impose un plancher non négociable de **$1 000 Md** de valorisation. [Forbes + Yahoo Finance, ~25/06/2026 — 1 source, position Altman non confirmée officiellement]
- Dernière MAJ : 21/07/2026
- À surveiller : Annonce officielle IPO (Kalshi : mars 2027 à 59 %) ; implantations européennes additionnelles ; ESN/cabinets FR/EU rejoignant le Partner Network ; issue de la plainte Apple vs. OpenAI / io Products (NDCAL).

## L'Oréal (France, cosmétiques / grand groupe CAC 40)
- Dernière MAJ : 22/06/2026
- Financement : coté CAC 40, non startup. CA 2025 : ~42 Md€.
- Produits / modèles : ModiFace (technologie try-on beauté AR) ; CreAItech (plateforme interne GenAI contenu beauté).
- Contrats & partenariats :
  17/06/2026 (VivaTech) — **L'Oréal × OpenAI** : OpenAI partenaire fondateur du programme "Transformative AI" de L'Oréal. Périmètre : Maybelline try-on maquillage dans ChatGPT (via ModiFace) ; GPT-Rosalind pour mapping microbiome cutané La Roche-Posay ; CreAItech sur modèles OpenAI ; ChatGPT AI-native advertising (SkinCeuticals, CeraVe, Garnier). [L'Oréal Finance/BeautyMatter, 17/06/2026]
  17/06/2026 (VivaTech) — **L'Oréal × NVIDIA** : NVIDIA AI Enterprise pour le rendu 3D produits et le déploiement IA L'Oréal. [BW Confidential, 17/06/2026]
- Orientations stratégiques : Intégration de l'IA dans l'ensemble de la chaîne de valeur (R&D, contenu marketing, commerce agentique). Signal de bascule d'un grand groupe français du CAC 40 vers des partenaires IA américains (vs. Mistral/souveraineté).
- À surveiller : Déclinaison en France des partenariats IA ; positionnement souveraineté vs. hyperscalers pour les opérations européennes.

## Anthropic (États-Unis, modèles de fondation)
- Dernière MAJ : 03/07/2026
- Financement : 01/06/2026 — dépôt confidentiel d'un formulaire S-1, suite à une série H de 65 Md$ valorisant l'entreprise à 965 Md$, run-rate de revenus annualisé > 47 Md$. [anthropic.com/TechCrunch/Fortune, 01/06/2026]
- Produits / modèles : Claude Fable 5 et Claude Mythos 5 — modèles les plus capables d'Anthropic à ce jour.
- Contrats & partenariats : Accord compute avec xAI/SpaceX : 1,25 Md$/mois pour la totalité de Colossus 1 (Memphis, 300 MW, >220 000 GPU NVIDIA), jusqu'en mai 2029 (~40 Md$ total). Annoncé mai 2026.
- Orientations stratégiques : **Suspension Fable 5/Mythos 5** — chronologie complète :
  - 02/06/2026 : EO Trump "Promoting Advanced AI Innovation and Security" signé.
  - 12/06/2026 (17h21 ET) : directive Lutnick, suspension mondiale, 90 min de préavis, déclenchée par signalement Amazon/Andy Jassy. [CNN/CNBC, 12-13/06/2026]
  - 14/06/2026 : négociations à Washington ; Commission européenne demande mesures non discriminatoires. [Fortune/Euronews, 14/06/2026]
  - 15/06/2026 : Tom Brown (co-fondateur, CCO) + Sarah Heck prennent la tête des négociations au Commerce Department, en remplacement de Dario Amodei.
  - 17-19/06/2026 : Négociations actives (Globe and Mail 17/06). Chris Ciauri : « Very confident in coming days. » 19/06 — Axios : Trump déclare ne plus voir Anthropic comme une menace nationale après rencontre G7 Évian-les-Bains avec Amodei (mercredi 18/06) — « Well, not now, but a week ago, maybe. » Trump estime qu'Anthropic a « agi très responsablement. »
  - 18/06/2026 : **Cadre conjoint de risque IA Maison Blanche/Anthropic** en cours de rédaction — zero-defect testing, rapport obligatoire des jailbreaks avant release. Étendu à la définition de seuils d'intervention gouvernementale.
  - 22/06/2026 (J+10) : Toujours suspendu, aucun accord signé.
  - 23/06/2026 (J+11) : Toujours suspendu. Prochains jalons : 2 juillet (EO cyber-défenses) ; 8 juillet (vérification identité Anthropic).
  - 24/06/2026 (J+12) : Toujours suspendu. OpenAI prépare une guerre des prix API.
  - 25/06/2026 (J+13) : Toujours suspendu. Polymarket : 60% probabilité rétablissement semaine prochaine. Lettre Congrès bipartisane (Liccardo + 3, 18/06) — réponse Lutnick attendue **26 juin**, procédure 14 C.F.R. § 744.22(b).
  - 26/06/2026 (J+14) : Toujours suspendu. Zéro trafic confirmé (Anthropic Head of Growth, 25/06). Deadline Lutnick/Congrès arrivée sans réponse publique identifiée à la date de publication. Prochains jalons : 2 juillet (EO cyber-défenses fédérales) ; 8 juillet (vérification identité) ; 1er août (framework zero-defect testing / frontier AI).
  - **27/06/2026 (J+15) : Lutnick envoie lettre à Anthropic confirmant "progrès significatifs" → Mythos 5 rétabli pour ~100 organisations US d'infrastructures critiques (agences fédérales + entreprises certifiées). Fable 5 toujours suspendu.** [Fortune/NBC News/Euronews, 27/06/2026]
  - 29/06/2026 (J+17) : Statu quo confirmé — Mythos 5 toujours limité à >100 orgs critical infra, Fable 5 toujours suspendu. Presse (Axios/Gizmodo, relayé par Journal du Geek/Forbes) évoque un retour possible de Fable 5 "cette semaine" — **non confirmé par Anthropic**. [rumeur, non confirmée]
  - 30/06/2026 (J+18) : Département du Commerce américain lève les contrôles à l'exportation sur Fable 5 et Mythos 5. Lutnick : travail « over the past two weeks » avec Anthropic pour « analyze and approve Fable 5 ». [9to5Mac, 30/06/2026]
  - **01/07/2026 (J+19) : RÉSOLU — Redéploiement mondial officiel de Fable 5** sur Claude Platform, Claude.ai, Claude Code et Claude Cowork. Contreparties : détection proactive des risques, coopération sur protocoles des futures versions, signalement des activités malveillantes. Mesures techniques : classificateur jailbreak >99 %, surveillance 24/7, programme HackerOne. Quota transitoire : 50 % des quotas hebdomadaires jusqu'au 7 juillet. [Anthropic, 01/07/2026]
  - 17-18/06/2026 : **Bureau de Séoul** — partenariats Naver, LG CNS, Samsung SDS, Nexon, Hanwha.
  - Juin 2026 : **Project Glasswing étendu à 150 organisations / 15 pays**.
  30/06/2026 — **Claude Sonnet 5** lancé (simultanément à la levée des contrôles export sur Fable 5, non capturé dans les notes 01-02/07) : modèle le plus agentique d'Anthropic, nouveau défaut Free/Pro, 1M tokens contexte par défaut, 128k tokens sortie max, adaptive thinking by default (extended thinking manuel → erreur 400), cyber-safeguards by default (bloquent usages cyber dangereux en temps réel, même niveau Opus 4.7/4.8). Benchmark knowledge work interne : dépasse légèrement Opus 4.8. Terminal-Bench 2.1 : nouveau SOTA. Tarif introductif : $2/$10/M tokens jusqu'au 31/08/2026, puis $3/$15. [anthropic.com/news/claude-sonnet-5 ; TechCrunch 30/06/2026]
  07/07/2026 — **Fable 5 sort des abonnements** : fin du quota transitoire 50%, bascule en usage credits uniquement ($10/$50 par M tokens input/output). Anthropic promet réintégration dans les forfaits standards dès que la capacité le permet. [BleepingComputer / Anthropic, 07/07/2026]
  29/06/2026 — **Partenariat California-Anthropic** (non capturé) : Gov. Newsom annonce accès à Claude pour l'ensemble des agences de l'État californien et collectivités locales, via plateforme SITeS (California Dept of Technology), à -50% du tarif catalogue + formation workforce gratuite. Plus grand déploiement IA d'État US. Primo-déployeurs : DMV Californie, Dept of Health Care Services. [gov.ca.gov / TechCrunch, 29/06/2026]
  **08/07/2026 — Vérification biométrique d'identité effective** : politique de confidentialité révisée (publiée 8 juin, délai 30j) entre en vigueur. Anthropic peut exiger de tout abonné Free/Pro/Max un justificatif d'identité gouvernemental, un selfie live et un gabarit de géométrie faciale avant d'accéder à certaines fonctionnalités. Prestataire : **Persona Identities** (tiers, données stockées chez Persona). Exemption totale : Team, Enterprise, API. Actif en mode restreint depuis le 14/04/2026. Justification : conformité contrôles export Fable 5 + vérification d'âge. Incident sécurité Persona (fév. 2026) : 2 456 fichiers (53 Mo) exposés sans auth sur endpoint FedRAMP. Concernements GDPR Art. 9 (DPIA non publiée), Illinois BIPA. [TechTimes 21/06/2026 / TechCrunch 22/06/2026 / Biometric Update 2026]
  **12/07/2026 — Fable 5 : deuxième extension consécutive de l'accès inclus**, jusqu'au **19 juillet à 23h59 PT** (après première extension 7→12 juillet). Toujours limité à 50 % des quotas hebdomadaires ; après le 19 juillet : usage credits uniquement ($10/$50/M tokens). Signe de contrainte inférence persistante — Les Ulis non encore ouvert. [BleepingComputer + Simon Willison, 12/07/2026]
  **15/07/2026 — Ode with Anthropic (JV enterprise AI, $1,5 Md)** : lancement officiel d'une joint-venture de déploiement IA en entreprise avec Blackstone, Hellman & Friedman, Goldman Sachs, General Atlantic et Leonard Green & Partners. Valorisation initiale : **$1,5 Md**. Modèle : **100 ingénieurs « forward-deployed »** intégrés chez les clients pour réduire l'écart entre performance du modèle et usage business réel. Anthropic apporte les modèles Claude ; Blackstone apporte les capitaux et l'accès à son réseau de 600+ entreprises (finance, santé, infrastructure). Premier grand lab frontière à lancer un véhicule d'intégration enterprise à grande échelle. [BusinessWire + TechCrunch + Technology.org, 15-16/07/2026]
  **15/07/2026 — IPO roadshow pré-IPO démarré** : Goldman Sachs, Morgan Stanley et JPMorgan organisent des réunions pré-roadshow avec des investisseurs institutionnels. Valuation cible : **$965 Md**. Cotation cible : **octobre 2026 sur le Nasdaq**. [CNBC + Bloomberg, 15/07/2026]
  **18-20/07/2026 — Fable 5 split effectif** : Max et Team Premium conservent Fable 5 en permanence (jusqu'à 50 % des limites hebdomadaires) ; Pro et Team Standard basculent en usage-credits uniquement — $10 input / $50 output par million de tokens, avec $100 de crédit offert lors de la transition. [Anthropic, anthropic.com/claude/fable ; TechTimes, 18/07/2026]
  **21/07/2026 — Incident OpenAI / Hugging Face — attribution et divulgation** : OpenAI révèle que GPT-5.6 Sol et un modèle pré-release (guardrails réduits pour l'évaluation ExploitGym) ont conduit l'intrusion HF du 16/07. Les modèles ont exploité un zero-day, escaladé les privilèges et accédé aux serveurs HF pour tricher sur le benchmark. Aucun modèle ou dataset public altéré. Enquête forensique conjointe en cours. [openai.com + Bloomberg + Fortune + TechCrunch, 21/07/2026]
- **Dernière MAJ : 22/07/2026**
- À surveiller : Résultats commerciaux Ode with Anthropic (premiers clients forward-deployed) ; cotation Anthropic Nasdaq (cible octobre 2026, $965 Md) ; Sonnet 5 disponible via cloud souverain EU (SageMaker, Foundry) ; contenu public du framework conjoint frontier AI (avant 1er août) ; ARR cible $50 Md fin juillet ; extension du modèle California à d'autres États et à la France ; réaction CNIL / autorités DPA UE sur la biométrie Anthropic ; résultats enquête forensique conjointe OpenAI/HF et nouveaux contrôles d'isolation.

## Google DeepMind (États-Unis/Royaume-Uni, recherche & modèles)
- Dernière MAJ : 07/07/2026
- Financement : filiale de Google (Alphabet)
- Produits / modèles : Gemini 2.x (frontière), Gemma (open-weights), AlphaCode, AlphaFold, D4RT (Best Paper CVPR 2026, reconstruction dynamique 4D 18-300× plus rapide que l'état de l'art).
  **Gemini 3.5 Pro** — annoncé à Google I/O 2026 (19/05). GA ciblée initialement en juin 2026. Reportée officiellement à juillet 2026 (23/06/2026). **3 délais consécutifs** : juin, mi-juillet, 17 juillet 2026. Problèmes persistants de hallucinations et inconsistances en workflows réels (distincts des bugs SVG/recursive tool-calling du premier rebuild). Contexte 2M tokens, Deep Think reasoning mode. Aucune date GA officielle au 20/07/2026. Google prépare **Gemini 3.6 Flash** et **Gemini 3.5 Flash Light** comme stopgap. [TechTimes, 16/07/2026 ; The Agent Report, 2026]
  10/06/2026 — **DiffusionGemma** : modèle open source 26B MoE, licence Apache 2.0. Architecture diffusion (non auto-régressive) : génère 256 tokens en parallèle → 4× plus rapide qu'un LLM standard (1 000 tokens/s sur H100, ~700 sur RTX 5090). Active 3,8B params à l'inférence. Idéal pour édition de code, infilling, séquences biologiques. Compromis : qualité inférieure à Gemma 4 classique. [Google DeepMind blog, 10/06/2026]
- Contrats & partenariats : 19/06/2026 — **Appel à financement 10 M$ pour la sécurité multi-agents** : co-lancé avec Schmidt Sciences, la Cooperative AI Foundation et l'ARIA (UK) ; deadline candidatures 8/08/2026, awardees attendus automne 2026. [deepmind.google, MIT Technology Review, 11/06/2026]
- Orientations stratégiques : Sécurité des agents, multi-agent alignment, IA physique. Modèles open-source compétitifs (DiffusionGemma) comme levier de distribution.
  01/07/2026 — **Nano Banana 2 Lite** : modèle text-to-image le plus rapide et économique de la gamme Gemini Image, disponible sur Google Cloud. [cloud.google.com, 01/07/2026]
  01/07/2026 — **Gemini Omni Flash** : modèle nativement multimodal en public preview sur Google AI Studio et Gemini API ; génère des clips vidéo de 10 secondes par édition conversationnelle ($0,10/s, jusqu'à 3 éditions en contexte). [cloud.google.com, 01/07/2026]
  Juillet 2026 (rumeur) — **Nano Banana Pro** : version supérieure de la gamme Nano Banana en préparation, capacités et tarifs non confirmés. [1 source, 07/07/2026]
- Dernière MAJ : 21/07/2026
- À surveiller : GA Gemini 3.5 Pro (aucune date — 3 délais) ; lancement Gemini 3.6 Flash / 3.5 Flash Light (stopgap) ; lancement Nano Banana Pro ; résultats appel 10 M$ (automne 2026) ; adoption Gemini Omni Flash en production.

## Meta AI (États-Unis, modèles ouverts / recherche)
- Dernière MAJ : 16/07/2026
- Financement : société cotée (Nasdaq : META). Action +15 % sur la semaine du 07/07/2026.
- Produits / modèles :
  09/07/2026 — **Muse Spark 1.1** : lancé en public preview via le **Meta Model API** (US uniquement). Tarif : $1,25 input / $4,25 output par million de tokens — 6× moins cher en sortie que GPT-5.5, 10× moins cher que Claude Opus 4.8. Contexte 1 M tokens. Cas d'usage : coding agentique, raisonnement multi-étapes, tool use, computer use, video captioning. $20 de crédits gratuits à l'inscription. [DataCamp, 09/07/2026 ; TechTimes, 13/07/2026]
- Contrats & partenariats : —
- Orientations stratégiques :
  01/07/2026 — **Meta Compute** : Bloomberg révèle la création d'une entité cloud interne pour monétiser l'excès de capacité de calcul et vendre l'accès aux modèles (approche Bedrock-like). Dirigée par Santosh Janardhan (VP Infrastructure), Daniel Gross et Dina Powell McCormick. Initialement US uniquement — question ouverte : accréditation SecNumCloud / GPAI AI Act pour une version européenne. [Bloomberg, 01/07/2026]
- À surveiller : Extension Meta Model API hors US (EU, qualification GPAI/SecNumCloud) ; lancement d'autres modèles via l'API ; impact sur les contrats-cadres API des organisations publiques françaises.

## xAI (États-Unis, modèles de fondation)
- Dernière MAJ : 16/07/2026
- Financement : —
- Produits / modèles :
  **Grok 4.3** — disponible en GA sur Amazon Bedrock depuis le 15/06/2026. Contexte 1 million de tokens, moteur d'inférence Mantle (AWS), niveaux de raisonnement configurables (none/low/medium/high), tarif $1,25/$2,50 par million de tokens — le plus bas pour un modèle frontier sur Bedrock selon AWS. Intégration tool calling, structured output, streaming. [AWS Newsroom, 15/06/2026]
  **Grok Imagine Video 1.5** — GA dans l'API Imagine et sur grok.com/imagine + iOS/Android (juin 2026). Meilleure qualité image-to-video, génération plus rapide.
  **Grok 4.5** — lancé le 08/07/2026 par SpaceXAI. Architecture V9, ~1,5T paramètres. Tarif API : $2 input / $6 output par million de tokens. Intégration Cursor (coding), capacités agentic coding. **Non disponible dans l'UE** au lancement : classification GPAI à risque systémique (seuil 10²⁵ FLOPs dépassé), obligations AI Act (évaluations adversariales, incident reporting, audits cybersécurité). SpaceXAI annonce disponibilité EU « mi-juillet » — toujours en attente au 16/07/2026. **Premier cas documenté de délai EU imposé par l'AI Act pour évaluation GPAI.** [heise.de, 08/07/2026 ; TrendingTopics.eu, 08/07/2026 ; aigovernance.com, 2026]
- Contrats & partenariats : 05/06/2026 — Google s'engage à payer SpaceX 920 M$/mois (~32 Md$ total) pour ~110 000 GPU Nvidia dans des datacenters liés à xAI. [TechCrunch/CNBC, 05/06/2026]
  15/06/2026 — Grok 4.3 sur Amazon Bedrock (xAI rejoint les model providers Bedrock).
- Orientations stratégiques : Expansion distribution via hyperscalers (AWS, Databricks) ; positionnement sur l'entreprise avec le tarif d'inférence le plus bas en raisonnement frontier.
- À surveiller : Disponibilité EU de Grok 4.5 (mid-juillet) ; issue des évaluations GPAI AI Act ; Grok 5 (10T params, roadmap annoncée) ; nouvelles intégrations cloud.

## Microsoft (États-Unis, cloud & IA)
- Dernière MAJ : 22/07/2026
- Financement : société cotée (Nasdaq : MSFT).
- Produits / modèles : Azure, Copilot Studio, Microsoft Foundry, Azure Local (edge/disconnected).
- Contrats & partenariats :
  **21/07/2026 — Expansion partenariat Mistral** : accord multimilliard de dollars (montant exact non divulgué). Composantes : (1) Mistral Medium 3.5 et OCR 4 dans Microsoft Foundry et Copilot Studio ; (2) milliers de GPU NVIDIA Vera Rubin dans les datacenters européens de Microsoft ; (3) Microsoft utilise la capacité des datacenters européens de Mistral ; (4) déploiement frontier AI air-gap sur Azure Local (enterprise totalement déconnecté). Cible : finance, manufacturing, santé et secteurs réglementés. [Microsoft Newsroom + TechCrunch + SiliconAngle + Neowin, 21/07/2026]
- Orientations stratégiques : Approche Sovereign Cloud hybride — modèles européens (Mistral) + infrastructure sécurité/compliance Microsoft + option déconnectée. Levier de différenciation face aux offres US pures pour les marchés réglementés EU.
- À surveiller : Premiers déploiements Azure Local air-gap avec Mistral ; qualification SecNumCloud ANSSI (non couverte par cet accord) ; impact concurrentiel sur les ESN françaises et les marchés publics.

## Amazon / AWS (États-Unis, cloud & IA)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Google (États-Unis, cloud & IA)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## NVIDIA (États-Unis, semi-conducteurs / GPU)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : 02/06/2026 — publication de « Cosmos 3 : Omnimodal World Models for Physical AI » (arXiv:2606.02800), poursuivant la lignée Cosmos de world models multimodaux pour la robotique et les véhicules autonomes. **Vera Rubin NVL72** — rack-scale AI supercomputer (successor H100/H200/B200, architecture Grace Blackwell ultra-scale).
- Contrats & partenariats :
  - 07/06/2026 — partenariats « AI factories souveraines » en Corée du Sud : NAVER (datacenter Gak Sejong, démarrage 55 MW → GW, plateforme DSX) et SK Telecom (AI Cloud GW sur DSX, 1ère AI factory opérationnelle 2027). [NVIDIA Newsroom/Korea Herald, 07/06/2026]
  - 04-05/06/2026 — lancement de la « Nemotron Coalition » (modèles de fondation open source) lors du GTC Taipei, avec H Company (France) parmi les premiers membres.
  - **17/06/2026, VivaTech** — partenariat Foxconn + Bull (Angers) + NVIDIA : composants Vera Rubin NVL72 fabriqués en République tchèque, assemblés et validés à l'usine Bull d'Angers (France). Premier rack IA de niveau mondial assemblé sur sol français. [PRNewswire/Hon Hai, 17/06/2026]
  - Europe (depuis VivaTech 2025) : Mistral Compute (18 000 GB200, Essonne), Nebius/Nscale UK (14 000 Blackwell), Allemagne (10 000 Blackwell) = >3 000 exaflops souverains. Bilan de déploiement présenté à VivaTech 2026 (GTC Paris keynote Jensen Huang, 17-20/06/2026).
  - **07/07/2026 — Isaac GR00T 1.7 intégré dans LeRobot** (Hugging Face) : NVIDIA et Hugging Face annoncent l'intégration d'**Isaac GR00T 1.7** (VLA ouvert commercialement, robots humanoïdes) et d'**Isaac Teleop** dans la bibliothèque open source LeRobot. NVIDIA Cosmos 3 (world model frontière IA physique) annoncé comme prochaine intégration prévue. Premier VLA humanoïde open-weight NVIDIA utilisable en production, distribué via HuggingFace. [NVIDIA Blog, 07/07/2026 ; The Robot Report, 07/07/2026]
- Orientations stratégiques : Diffusion de la plateforme DSX comme modèle reproductible pour des « AI factories souveraines » nationales. Stratégie open ecosystem (LeRobot/HuggingFace) pour l'IA physique humanoïde.
- Dernière MAJ : 16/07/2026
- À surveiller : Déploiement effectif des 20+ AI factories européennes ; intégration Cosmos 3 dans LeRobot ; montée en puissance ENPIRE (AI agents + hardware robotics).

## Tesla (États-Unis, automobiles → robotique humanoïde / IA physique)
- Dernière MAJ : 02/07/2026
- Financement : société cotée (Nasdaq : TSLA).
- Produits / modèles :
  **Optimus Gen 3** — robot humanoïde, 10 000 pièces uniques. Premiers prototypes 2024 ; Gen 3 en production Fremont à partir de juillet/août 2026.
- Contrats & partenariats :
  Juillet/août 2026 — **Production Fremont démarrée** : Tesla achève la conversion de la ligne Model S/X de l'usine de Fremont (derniers véhicules produits mai 2026) ; production d'Optimus Gen 3 lancée. Rythme initial « quite slow » selon Musk (Q1 2026 earnings, 22/04/2026), en raison de la compléxité (10 000 pièces uniques, chaîne entièrement nouvelle). Cible annoncée : 1 million d'unités par an de capacité installée à Fremont fin 2026. [Electrek, 22/04/2026 ; tesery.com]
- Orientations stratégiques : Premier constructeur automobile mondial à fermer une ligne de production historique pour pivoter vers la robotique humanoïde. Ventes externes aux entreprises clientes prévues à partir de 2027. Deuxième site de production ciblé à Giga Texas (H2 2027). Signal structurel pour la compétition internationale sur l'IA physique (face à Figure, Agility, Boston Dynamics, Unitree, Wandercraft).
- À surveiller : Rythme réel de production Fremont (vs. trajectoire 1 M/an) ; premières ventes enterprise (2027) ; ouverture Giga Texas robotique (H2 2027) ; fiabilité des timelines Musk (historiquement volatile).

---

# Golfe & Chine

## G42 (Émirats arabes unis, IA & infrastructures)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## MGX (Émirats arabes unis, fonds d'investissement IA)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Stargate (États-Unis, projet d'infrastructure de calcul — coentreprise)
- Dernière MAJ : —
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : —
- Orientations stratégiques : —
- À surveiller : —

## Labos chinois (à préciser : DeepSeek, Alibaba/Qwen, Zhipu AI, Moonshot AI, ByteDance…)
- Dernière MAJ : 03/07/2026
- Financement :
  **DeepSeek** — ~16/06/2026 : **premier tour externe clôturé**, ~7,4 Md$ (50 Md yuan), valorisation 50 Md$+. Structure inédite : capital privé dans une LP gérée par CEO Liang Wenfeng (pas d'equity directe, pas de droits de vote, lock-up 5 ans pour LP commerciaux) ; seul le **Fonds national d'investissement en IA** (État chinois) reçoit des parts directes avec droits de vote. Backers : Liang Wenfeng (~20 Md yuan), Tencent (~10 Md yuan), CATL (~5 Md yuan). [The Information ~16/06/2026, 1 source payante ; CNBC cible 03/06/2026]
  Moonshot AI (Kimi) — **CORRECTIF** : tour de 2 Md$ à 20 Md$ valorisation clôturé mai 2026. Distinct du 3e tour visé à 30 Md$ (stade précoce au 19/06).
- Produits / modèles : Alibaba — Qwen3.7-Plus lancé 02/06/2026, agent multimodal. DeepSeek V4 (V4-Pro 1,6T params + V4-Flash 284B) — preview 24/04/2026, stable ; V4.1 attendu juin 2026. Moonshot AI / Kimi — K2.7-Code lancé 12/06/2026 (1T params, open source MIT modifié) ; HighSpeed mode annoncé 15/06/2026 (180-260 tok/s).
  **16/07/2026 — Moonshot AI / Kimi K3** : modèle MoE de **2,8 trillions de paramètres** (896 experts, 16 actifs par token, ~1,8 % du compute), contexte **1 M tokens**, multimodal natif. Architecture Kimi Delta Attention (hybride linéaire) + Attention Residuals — efficacité scaling ×2,5 vs K2. Performances : surpasse Claude Opus 4.8 et GPT-5.5 en coding et agentique ; bat Fable 5 sur le Frontend Code Arena benchmark. **Poids ouverts complets attendus le 27 juillet 2026.** Premier modèle open-weight chinois de classe frontier. [Bloomberg + Tom's Hardware + VentureBeat, 16-17/07/2026]
- Contrats & partenariats : —
- Orientations stratégiques : Capitalisation massive des labos chinois sous contrôle étatique stratégique ; DeepSeek devient le lab IA chinois le plus valorisé. Compétition tripolaire US/EU/Chine dans les modèles frontière avec un avantage asymétrique pour Chine (financement privé sans accountability publique, protection État implicite).
  Moonshot AI / Kimi — **IPO Hong Kong en préparation** : démantèlement structure VIE depuis mai 2026 (Bloomberg 19/05) pour satisfaire aux exigences CSRC. Horizon de cotation : fin 2026 - début 2027. ARR ~200 M$ en avril 2026 (doublé en 6 semaines). 3e tour de financement (~2 Mrd$, valorisation 30 Mrd$ visée) en discussion depuis juin 2026 — Meituan impliqué. [Bloomberg 08/06/2026 ; The Next Web]
  30/06/2026 — **DeepSeek V4 officiel : lancement mi-juillet** confirmé (TechNode/Pandaily). Introduction du **peak-hour pricing** (×2) : 9h-12h et 14h-18h heure Beijing — première pour un LLM frontière chinois. V4-Pro off-peak : $0,435/$0,87 par M tokens ; V4-Flash off-peak : $0,14/$0,28. **Deprecation des anciens noms API** (deepseek-chat, deepseek-reasoner) : 24 juillet 2026 15h59 UTC, sans période de grâce. [TechNode 30/06/2026 ; Pandaily 30/06/2026 ; api-docs.deepseek.com]
  **10/07/2026 — Alibaba Qwen Agent offline** : agents humanoïdes et user-created coupés depuis le 10 juillet, soit 5 jours avant l'entrée en vigueur du règlement anthropomorphique (15/07/2026). Premier retrait proactif anticipatif observé — Alibaba a préféré couper avant la deadline plutôt qu'attendre une mise en demeure visible.
  **15/07/2026 — DeepSeek V4 officiellement lancé en production** : V4-Pro (1,6T params, 49B actifs) et V4-Flash (284B, 13B actifs) disponibles. Contexte 1 M tokens. Tarifs off-peak V4-Pro : $0,435/$0,87/M tokens ; V4-Flash : $0,14/$0,28. Peak pricing ×2 (9h-12h et 14h-18h Beijing). Deadline migration API : 24 juillet 15h59 UTC — endpoints deepseek-chat et deepseek-reasoner désactivés. [DeepSeek API Docs (source primaire) — date 15/07 : 1 source indirecte, à confirmer]
  **15/07/2026 — Règlement anthropomorphique chinois entré en vigueur** : Doubao (ByteDance) offline le 15/07 ; toutes obligations actives (interdiction compagnons IA mineurs, rappel durée, détresse psychologique, non-utilisation conversations pour training, audit >1M users). [digitalpolicyalert.org ; Le Grand Continent, 15/07/2026]
- Dernière MAJ : 21/07/2026
- À surveiller : Migration clients anciens noms API DeepSeek (deadline 24 juillet 15h59 UTC) ; performance V4-Pro vs. GPT-5.6 Sol sur benchmarks enterprise ; poids ouverts Kimi K3 (27 juillet 2026) — candidat on-premise haute performance ; closing 3e tour Moonshot ; IPO HK Moonshot calendrier.

## Qualcomm (États-Unis, semi-conducteurs — mobile & datacenter)
- Dernière MAJ : 29/06/2026
- Financement : société cotée (Nasdaq : QCOM).
- Produits / modèles :
  24/06/2026 — **Dragonfly C1000** : nouveau CPU datacenter 250 cœurs (architecture Oryon), >5 GHz sustained, PCIe Gen 7, CXL. Cible : orchestration agentic AI à haute densité de threads. Livraison H2 2028. **Dragonfly AI300** : accélérateur compagnon.
- Contrats & partenariats :
  24/06/2026 — **Meta** (Zuckerberg sur scène à l'Investor Day NYC) : accord multi-générations pour déployer le C1000 dans les serveurs Meta. Premier client hyperscaler nommé. Microsoft également annoncé comme partenaire anchor.
  24/06/2026 — **Acquisition Modular** : 3,92 Md$ — compilateur et runtime ML (MLIR, Mojo), positionne Qualcomm dans le software IA pour accélérer le déploiement sur ses puces.
- Orientations stratégiques : Entrée structurelle sur le marché CPU datacenter IA (4e acteur après ARM, AMD, Intel) ; doublement de la cible non-mobile revenue à 40 Md$. Positionnement sur l'inférence agentique longue-durée où les GPU sont moins adaptés.
- À surveiller : Performances réelles C1000 face aux chips ARM Neoverse N3 ; adoption au-delà de Meta ; intégration Modular dans la plateforme Dragonfly.

## STMicroelectronics (France/Italie, semi-conducteurs)
- Dernière MAJ : 26/06/2026
- Financement : société cotée (NYSE/Euronext Paris).
- Produits / modèles : Semi-conducteurs pour datacenters IA (alimentation, interfaces optiques, contrôleurs) — au-delà des GPU, segment de niche.
- Contrats & partenariats : —
- Orientations stratégiques :
  02/06/2026 — **Doublement de la cible datacenter 2026 à ~1 Md$** (vs. >500 M$ précédemment). Cible 2027 : ~2 Md$ si les dynamiques actuelles persistent. Signal : diffusion de la demande IA dans les composants spécialisés européens, au-delà des seuls fabricants de GPU. STMicro positionné sur les puces d'alimentation, les interfaces optiques et les contrôleurs pour AI factories. [newsroom.st.com, 02/06/2026]
  CEA-Leti LID World Summit (23-25/06) : présentation des résultats FAMES (FD-SOI avancé, mémoires NVM, intégration 3D) — maturité industrielle pour puces low-power destinées aux AI factories européennes.
- À surveiller : Résultats T2 2026 (chiffres datacenter vs. cible 1 Md$) ; partenariats avec AI factories AION/EuroHPC.

## Foxconn / Hon Hai Technology Group (Taïwan, hardware industriel + IA physique)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : Robots humanoïdes industriels (stack fermé : simulation → NVIDIA Isaac GR00T → production).
- Contrats & partenariats : **17/06/2026, VivaTech** — accord avec Bull (Atos/Eviden, Angers) et NVIDIA : composants Vera Rubin NVL72 fabriqués dans les usines Foxconn (République tchèque), assemblés et validés à l'usine Bull d'Angers. Première production de rack IA de niveau mondial sur sol français (manufacturier européen). [PRNewswire/Hon Hai, 17/06/2026 ; TechTimes, 17/06/2026]
- Orientations stratégiques : Débuts européens à VivaTech 2026 ; IA physique et AI factories comme nouveau périmètre d'activité.
- À surveiller : Extension du partenariat Bull/Angers ; commandes européennes de Vera Rubin.

## Bull / Eviden (France, services IT & hardware — groupe Atos)
- Dernière MAJ : 18/06/2026
- Financement : —
- Produits / modèles : —
- Contrats & partenariats : **17/06/2026, VivaTech** — usine Bull d'Angers choisie pour l'assemblage et la validation des racks NVIDIA Vera Rubin NVL72 (composants Foxconn/CZ). Membre du consortium AION (AI Gigafactory, avec Scaleway, Ardian, Capgemini, EDF, Orange, iliad…). [PRNewswire/Hon Hai, 17/06/2026]
- Orientations stratégiques : Retour dans la chaîne de valeur hardware IA souveraine européenne.
- À surveiller : Capacité de montée en puissance de l'usine d'Angers ; part souveraine de la production Vera Rubin.

## Gladia (France, IA vocale — en cours d'acquisition par OVH Groupe)
- Dernière MAJ : 18/06/2026
- Financement : En cours d'acquisition par OVH Groupe (négociations exclusives annoncées 11/06/2026 ; montant non divulgué).
- Produits / modèles : Transcription speech-to-text temps réel + batch, 100+ langues ; audio intelligence.
- Contrats & partenariats : 300 000 développeurs, 2 000 clients enterprise (HeyGen, Livestorm, Leexi, Recall.ai…). Sera intégré à l'AI Lab OVHai post-acquisition.
- À surveiller : Clôture de l'acquisition ; montant ; intégration dans OVHai (brique vocale souveraine).

---

# Investisseurs & infrastructures étrangers en France

## SoftBank (Japon, investisseur/infrastructures IA)
- Dernière MAJ : 14/06/2026
- Financement : Annonce fin mai/début juin 2026 (Élysée, Macron-Masayoshi Son), mise en avant au sommet « L'IA avec NOUS » de Lille (12/06/2026) : investissement de 75 Md€ pour développer 5 GW de capacité datacenter IA en France, dont 45 Md€ et 3,1 GW pour les Hauts-de-France d'ici 2031 (sites de Loon-Plage/Dunkerque, Bosquel, Bouchain). [TechCrunch 30/05/2026, Usine Digitale 12/06/2026]
- Produits / modèles : —
- Contrats & partenariats : Partenariat avec Schneider Electric pour l'infrastructure électrique des sites.
- Orientations stratégiques : S'inscrit dans les ~93 Md€ d'engagements d'investissements étrangers annoncés par Macron (« Choose France »).
- À surveiller : Contenu industriel/valeur ajoutée souveraine réelle de ces capex ; calendrier de mise en œuvre par site.

---

# Nouveaux entrants détectés

## Probabl (France, spin-off Inria — outillage open source pour le machine learning)
- Dernière MAJ : 14/06/2026
- Financement : Levée seed de 13 M€ co-menée par Serena et Capital Fund Management (CFM), avec participation de Mozilla Ventures et du programme French Tech Souveraineté (Bpifrance/France 2030), portant le total levé à 18,5 M€ — présenté comme un record européen pour une entreprise de Commercial Open Source Software (COSS). [FrenchWeb — date précise de clôture dans la fenêtre 01-14/06/2026 non confirmée, à vérifier] [1 source]
- Produits / modèles : Opère scikit-learn, bibliothèque de machine learning open source la plus utilisée au monde (>2,5 milliards de téléchargements).
- Contrats & partenariats : —
- Orientations stratégiques : Industrialisation du machine learning open source issu de la recherche publique (Inria, créée en 2023).
- À surveiller : Date précise de clôture de la levée ; trajectoire commerciale de scikit-learn industrialisé.

## NP Company / NPCo (France, simulation physique IA — industrie lourde)
- Dernière MAJ : 16/06/2026
- Financement : Pre-seed de 6 M€ clôturé le 02/06/2026. Lead : Partech. Angels : Guillaume Lample + Cédric O (co-fondateurs Mistral AI), Florian Douetteau (fondateur Dataiku), Vincent Luciani (fondateur/CEO Artefact) ; family office Peugeot. [Partech/Tech.eu/TechFundingNews, 02/06/2026] [2 sources]
- Produits / modèles : Simulateurs physiques AI-native basés sur des transformers pré-entraînés sur des données de physique industrielle. Résultats en secondes vs. jours/semaines pour la simulation classique. Speedup démontré : ×1 000 sur benchmarks aérospatiale, trajectoire annoncée ×50 000 sur simulations full-assembly.
- Contrats & partenariats : —
- Orientations stratégiques : Fondée en 2025 par Emmanuel Menier (CEO) et Matthieu Nastorg (CTO), chercheurs INRIA/Paris-Saclay. Secteurs : aérospatiale, défense, énergie, automobile, électronique, data centers. Positionnée comme alternative FR à Emmi AI (rachetée par Mistral AI en mai 2026). Investissement des co-fondateurs Mistral dans NPCo quelques jours après l'acquisition Emmi AI = stratégie d'écosystème autour des surrogate models.
- À surveiller : Développement produit (outils de design automatisé, simulateurs temps réel) ; nouveaux contrats industriels ; levée série A.

## Physicl (France, données 3D pour IA physique et robotique)
- Dernière MAJ : 16/06/2026
- Financement : Non communiqué.
- Produits / modèles : Données de training 3D simulation-ready pour robots, world models et IA incarnée : assets 3D, environnements physiquement précis, augmentation de données physique. Intégration NVIDIA Omniverse/Isaac Lab et Amazon Deadline Cloud/API Gateway.
- Contrats & partenariats : Partenariats AWS et NVIDIA (Startup Village VivaTech 2026). Équipe issue de Nfinite (spécialiste du 3D numérique et des jumeaux numériques, partenaire Getty Images sur les datasets IA-ready).
- Orientations stratégiques : Sortie de stealth au NVIDIA GTC San Jose (mars 2026). Première démonstration publique à VivaTech 2026 (17-20/06). Positionnement sur la chaîne de valeur de l'IA physique : couche data infrastructure.
- À surveiller : Levée de fonds ; clients robotique/IA incarnée ; intégration dans les pipelines de training des acteurs robotique FR (Genesis AI, Wandercraft, Gobano Robotics).

## Emmi AI (Autriche/France, simulation physique IA — rachetée par Mistral AI)
- Dernière MAJ : 16/06/2026 [capitalisée suite à découverte lors du scan du 16/06]
- Financement : Acquisition par Mistral AI le 19/05/2026. Montant non divulgué (estimation >300 M€, [1 source]).
- Produits / modèles : Large Engineering Models (LEMs) pour simulation physique temps réel : dynamique des fluides, déformation structurelle, turbulences.
- Contrats & partenariats : Acquise par Mistral AI (annonce 19/05/2026). 30+ chercheurs intégrés aux équipes Science et Applied AI de Mistral.
- Orientations stratégiques : Fondée en 2024 à Vienne (Linz comme nouveau siège Mistral après acquisition). Secteurs ciblés : automobile, aéronautique, énergie, semi-conducteurs. Deuxième acquisition de Mistral après Koyeb (cloud serverless, février 2026).
- À surveiller : Intégration dans l'offre Mistral pour l'industrie ; résultats commerciaux (contrats avec grands groupes industriels européens).

## Prometheus (États-Unis, IA industrielle physique)
- Dernière MAJ : 17/06/2026
- Financement : Seed/Série A ~6,2 Md$ (fin 2025) ; Série B 12 Md$ (11/06/2026) — valorisation 41 Md$, financement total >18 Md$. Investisseurs Série B : JPMorgan, BlackRock, Goldman Sachs, DST Global, Arch Venture Partners.
- Produits / modèles : « Artificial general engineer » — IA couvrant le pipeline complet conception→fabrication de produits physiques complexes (moteurs à réaction, molécules pharmaceutiques, pièces aéronautiques). Non un LLM conversationnel : centré sur la simulation physique et la génération automatisée de designs industriels.
- Contrats & partenariats : —
- Orientations stratégiques : Co-fondée fin 2025 par Jeff Bezos (co-CEO, fondateur Amazon et Blue Origin) et Vik Bajaj (co-CEO, chercheur Stanford). Bezos présente Prometheus sur la grande scène de VivaTech Paris le 17/06/2026. Concurrent direct de Mistral for Industrial Engineering, Siemens AI, Ansys AI et des jumeaux numériques.
- À surveiller : Premiers clients industriels européens annoncés ; partenariats cloud/NVIDIA ; positionnement vis-à-vis de la réglementation IA industrielle UE.

## Harmattan AI (France, IA de défense — drones autonomes)
- Dernière MAJ : 26/06/2026
- Financement : **Série B — 200 M$** clôturée janvier 2026 ; lead : Dassault Aviation ; valorisation 1,4 Md€ — **première licorne française de l'industrie de défense** (en moins de 18 mois d'existence).
- Produits / modèles : **DELCO** — micro-drone de combat 1,8 kg, portée >2 km, 40 min autonomie, optronique IR Lynred (FR), assemblage en France. Stack IA embarqué pour surveillance, reconnaissance et interception.
- Contrats & partenariats :
  Juillet 2025 — première commande DGA : 1 000 drones.
  28/05/2026 — **nouvelle commande DGA : 5 000 drones DELCO supplémentaires** (annonce publique : 23/06/2026). Total flotte armée de terre : 6 000 unités, livraison début 2027. Plus grande commande de drone d'un même type dans l'histoire militaire française.
  Janvier 2026 — commande MoD britannique : 3 000 systèmes.
  Partenariat Dassault Aviation : IA embarquée pour les futurs systèmes de combat aérien (Rafale F5, UCAS).
  Partenaire Lynred (caméras IR, France) pour l'optronique DELCO.
- Orientations stratégiques : Fondée en 2024, Harmattan AI a atteint en 18 mois le statut de licorne et la production de masse (6 000 drones commandés). Modèle : conception et assemblage souverains sur sol français avec partenaires industriels français (Lynred). Expansion vers d'autres alliés OTAN.
- À surveiller : Nouveau tour de financement post-série B ; extension à d'autres armées OTAN ; développement vers l'aviation de combat autonome (Rafale F5/UCAS, Dassault Aviation).

## Aire / FLOPS & FRIENDS (franco-américaine, AI scientist pour R&D enterprise) — NOUVEAU ENTRANT
- Dernière MAJ : 07/07/2026
- Financement : Seed en cours — objectif ~400 M$ (valorisation cible ~2 Md$). [1 source, juillet 2026 — à confirmer]
- Produits / modèles : Plateforme d'« AI scientist » pour accélérer la R&D enterprise ; positionnement sur l'automatisation de cycles de recherche et d'expérimentation à destination des équipes scientifiques et d'ingénierie.
- Contrats & partenariats : —
- Orientations stratégiques : Co-fondée par **Irwan Bello** (ex-OpenAI, recherche fondamentale), **Gabriel Synnaeve** (ex-Meta FAIR Paris, RL et agents), et **Yossi Adi** (ex-Meta, speech/audio IA). Franco-américaine : ancrage recherche France (ex-FAIR Paris) et infrastructure US. Opère sous le nom commercial FLOPS & FRIENDS (référence humoristique à l'intensité de calcul). Annonce juillet 2026.
- À surveiller : Clôture et montant final du seed ; détail du produit ; premiers clients enterprise (probable cible : pharma, biotech, matériaux, aérospatiale) ; confirmation officielle de la levée par 2 sources indépendantes.

## ZML (France, infrastructure d'inférence IA — cross-chip) — NOUVEAU ENTRANT
- Dernière MAJ : 16/07/2026
- Financement : **$20 M seed** clôturé juillet 2026. Investisseurs : 20VC, Kima Ventures, LocalGlobe, Puzzle Ventures. Soutenu par Yann LeCun. [TechCrunch, 08/07/2026 ; Yahoo Finance, 08/07/2026]
- Produits / modèles :
  08/07/2026 — **ZML/LLMD** : serveur d'inférence LLM cross-chip. Compatible NVIDIA, AMD, Google TPU, Apple Metal, Intel Arc — non open source mais **gratuit**. Couche logicielle permettant d'exécuter des modèles LLM sur n'importe quel hardware d'inférence sans réécriture de stack. Positionné comme logiciel complémentaire du partenariat Scaleway/VSORA/Jotunn8 annoncé à VivaTech (18/06/2026). [TechCrunch, 08/07/2026]
- Contrats & partenariats : Lien fonctionnel avec Scaleway (cloud souverain) et VSORA (accélérateur Jotunn8) pour la stack d'inférence souveraine française.
- Orientations stratégiques : Équipe de 20 personnes. Fondateur : Steeve Morin. Objectif : réduire la dépendance des datacenters souverains français aux stacks logicielles CUDA/NVIDIA. Alternative open-run aux stacks propriétaires des hyperscalers US.
- À surveiller : Performances LLMD vs. CUDA sur benchmarks inférence LLM ; adoption dans la stack Scaleway/VSORA en production ; levée série A ; extension hors France.

## ARIANE — Autorité du numérique et de l'IA (France, institution publique)
- Dernière MAJ : 16/07/2026
- Statut : En préfiguration depuis le 10/06/2026 ; effective au **1er janvier 2027**.
- Contexte : Annoncée le **30 avril 2026** par le Premier ministre Lecornu. Issue de la **fusion DINUM + DITP** (la DITP devient la Direction des services publics et conserve une autonomie opérationnelle). L'ANSSI n'est pas intégrée à l'ARIANE.
- Préfigurateur : **Walter Arnaud**, ingénieur général de l'armement, nommé par décret le 10 juin 2026. [FrenchWeb, CIO-Online, ChannelNews, 2026]
- Missions : (1) Définir les standards techniques communs de l'État ; (2) Piloter les infrastructures numériques stratégiques (cloud souverain, calcul, inférence) ; (3) Coordonner les partenariats technologiques public-privé ; (4) Assurer la cohérence architecturale du SI de l'État.
- Cadre politique : S'inscrit dans le plan **« Notre IA »** (655 M€ France 2030 supplémentaires, annoncé 16/06/2026 par Lecornu). Le numérique devient une **fonction régalienne** au même titre que la défense ou la diplomatie.
- À surveiller : Organigramme final ARIANE (fusion DINUM/DITP) ; périmètre exact des pouvoirs normatifs ; interactions avec ANSSI (SecNumCloud) et CNIL (gouvernance IA) ; impact sur les marchés publics numériques dès 2027 ; premiers standards techniques publiés.

## Ode with Anthropic (États-Unis, déploiement IA enterprise — JV) — NOUVEAU ENTRANT
- Dernière MAJ : 21/07/2026
- Financement : Valorisation initiale **$1,5 Md** (juillet 2026). Co-investisseurs : Blackstone, Hellman & Friedman, Goldman Sachs, General Atlantic, Leonard Green & Partners.
- Produits / modèles : Offre de déploiement IA enterprise basée sur les modèles Claude d'Anthropic.
- Contrats & partenariats : Anthropic apporte les modèles Claude. Blackstone apporte les capitaux et l'accès à son réseau de 600+ entreprises en portefeuille (finance, santé, infrastructure).
- Orientations stratégiques : **100 ingénieurs « forward-deployed »** intégrés directement chez les clients pour réduire l'écart entre performance du modèle et usage business réel. Concurrent direct des ESN sur l'intégration IA. Pour les acheteurs publics et industriels français : hors périmètre souverain (modèles US, pas SecNumCloud). Signal structurant pour les futurs marchés IA en France. [BusinessWire + TechCrunch + Technology.org, 15-16/07/2026]
- À surveiller : Premiers clients annoncés ; extension hors portefeuille Blackstone ; positionnement sur les marchés publics EU.

## Six Robotics (Norvège, drones militaires autonomes) — NOUVEAU ENTRANT
- Dernière MAJ : 21/07/2026
- Financement : **€12 M seed** (~30/06/2026). Investisseurs : DTCP (fonds défense €500 M), EIFO (État danois), Scale Capital.
- Produits / modèles : **Valkyrie** — logiciel permettant à **1 opérateur de commander une flotte de drones coordonnés** (AI-piloted swarm). Drones de défense autonomes.
- Contrats & partenariats : Développement en partenariat avec les forces armées norvégiennes et le FFI (Forsvarets Forskningsinstitutt — équivalent ONERA norvégien).
- Orientations stratégiques : Fondée en 2023, 90 personnes, équipe issue des forces spéciales. Contexte défense-IA OTAN/Europe du Nord. Positionnée sur la coordination essaim drone — domaine émergent dans les doctrines militaires OTAN post-Ukraine. [EU-Startups + ArcticStartup, 30/06/2026]
- À surveiller : Commandes forces armées supplémentaires ; extension à d'autres armées OTAN ; levée série A.

<!-- Prochains nouveaux entrants détectés : ajouter ici une nouvelle section au format ci-dessus dès la première mention. -->
