# Registre de veille — anti-redondance

<!--
Fichier persistant lu EN ENTRÉE et mis à jour EN SORTIE par la routine « Veille IA & Souveraineté ».
Règle absolue : ne jamais réécrire l'historique. On AJOUTE en fin de section « Journal ».
-->

## Rôle
Ce fichier liste tout item déjà sorti dans une note de veille, afin d'éviter les redites.
Avant chaque exécution, la routine relit ce fichier. Un sujet déjà présent n'est ressorti
que s'il existe un fait nouveau depuis la dernière mention — il est alors marqué `[SUITE]`.

## Format d'une ligne
`JJ/MM/AAAA | sphère | entité ou sujet | empreinte (1 ligne) | [NOUVEAU] ou [SUITE]`

Sphères admises :
`PUBLIQUE-INT` · `PUBLIQUE-EU` · `PUBLIQUE-FR` · `PRIVÉE-FR` · `PRIVÉE-MONDE` ·
`NOUVEL-ENTRANT` · `ACADÉMIQUE` · `INFRA`

L'« empreinte » est une formulation courte et stable du fait, qui sert à reconnaître
le même sujet d'un jour à l'autre (ex. « levée série B 30 M€ », « publication CADA »).

## Journal

<!-- Les lignes réelles s'ajoutent ici, une par item, ordre chronologique. -->

15/06/2026 | PRIVÉE-MONDE | Anthropic | accès Fable 5/Mythos 5 toujours suspendu, rôle déclencheur d'Amazon révélé, réaction officielle de la Commission européenne (souveraineté) | [SUITE]
15/06/2026 | PRIVÉE-FR | OVHcloud / Gladia | négociations exclusives de rachat de Gladia (IA vocale) pour l'AI Lab souverain d'OVHcloud | [NOUVEAU]
15/06/2026 | PUBLIQUE-EU | Italie | décrets d'application de l'AI Act adoptés en examen préliminaire, 1 Md€ pour la gouvernance IA nationale | [NOUVEAU]
15/06/2026 | PUBLIQUE-FR | Festival IA avec NOUS / Lille | Tech & Business Day + forum Apec Job Connect IA & Tech, suite du sommet du 12/06 | [SUITE]
15/06/2026 | ACADÉMIQUE | Robotique / world models | arXiv 2606.06556 (interfaces manquantes VLA/world models) + arXiv 2606.09499 (sécurité world models, data poisoning) + VLA-JEPA dans LeRobot + CVPR 2026 Best Paper D4RT | [NOUVEAU]
15/06/2026 | PRIVÉE-FR | Mistral | statu quo levée ~3 Md€ (stade précoce), rendez-vous attendu à VivaTech | [SUITE]
15/06/2026 | PRIVÉE-MONDE | Moonshot AI | statu quo levée 1-2 Md$ visant ~30 Md$ de valorisation, non clôturée | [SUITE]
15/06/2026 | PUBLIQUE-EU | CADA | toujours bloqué entre États membres, critique de la CCIA | [SUITE]
16/06/2026 | PRIVÉE-MONDE | Anthropic | équipe Washington identifiée (Carlini, Graham, Orr, Brown, Heck) face à Lutnick/Cairncross, aucun accord au 15/06 | [SUITE]
16/06/2026 | PRIVÉE-MONDE | OpenAI | Partner Network mondial $150M, 300K certif fin 2026, Accenture/Bain/BCG/McKinsey/PwC, lancé 14/06/2026 | [NOUVEAU]
16/06/2026 | PRIVÉE-MONDE | Moonshot AI / Kimi | K2.7 Code HighSpeed annoncé 15/06 (1T params, 180-260 tok/s) ; CORRECTIF : tour $2Md à $20Md clôturé mai 2026 (distinct du 3e tour à $30Md cherché) | [SUITE]
16/06/2026 | PUBLIQUE-EU | Commission européenne / AI Office | Code de conduite marquage contenu IA publié 10/06 (voluntary, icônes EU, mécanismes watermarking/métadonnées, AI Act août 2026) | [NOUVEAU]
16/06/2026 | PRIVÉE-FR | Dataiku | Cobuild agent IA annoncé 11/06 (GA 18/06) — build-to-govern enterprise AI sans code | [NOUVEAU]
16/06/2026 | NOUVEL-ENTRANT | NP Company / NPCo (France) | pre-seed 6M€ Partech, backed par co-fondateurs Mistral, simulation physique IA aéro/défense/énergie, 02/06/2026 | [NOUVEAU]
16/06/2026 | NOUVEL-ENTRANT | Physicl (France) | spin-off Nfinite, données 3D pour IA physique/robotique, sortie stealth GTC mars 2026, VivaTech 2026 | [NOUVEAU]
16/06/2026 | PUBLIQUE-INT | Colorado | SB 26-189 signé 14/05/2026 : AI Act révisé retardé au 1er janv 2027, périmètre ADMT réduit, pivot délibéré du modèle EU | [NOUVEAU]
17/06/2026 | PRIVÉE-MONDE | Anthropic | accès suspendu J+5 ; réunions Washington 16/06 ; Bloomberg 16/06 « policy reversal » évoquée sans accord signé | [SUITE]
17/06/2026 | PRIVÉE-MONDE | Prometheus (Bezos / Bajaj) | Série B 12 Md$ à 41 Md$ val. (11/06) — « artificial general engineer » physique (moteurs, médicaments, pièces industrielles) ; Bezos sur scène VivaTech 17/06 | [NOUVEAU]
17/06/2026 | PRIVÉE-FR | Mistral / Industrial Engineering | lancement 28/05 : surrogate models Airbus (5 ans, défense/espace), BMW, EDF, CMA CGM ; non capturé avant 17/06 | [NOUVEAU]
17/06/2026 | PUBLIQUE-EU | VivaTech 2026 / NVIDIA GTC Paris | J1 17/06 : Jensen Huang keynote AI factories / IA souveraine / physique Europe ; Bezos (Prometheus) grande scène | [NOUVEAU]
17/06/2026 | PUBLIQUE-INT | Inde-France / Bharat Innovates | Modi-Macron Nice 14/06 ; Modi à VivaTech 18/06 avec cadre MANAV (gouvernance IA) ; Inde partenaire IA officiel VivaTech | [NOUVEAU]
17/06/2026 | PUBLIQUE-FR | France / AI Act | applicable intégralement 2/08/2026 ; CNIL autorité pilote (loi DDADUE 17/02/2026) ; sandbox réglementaire obligatoire d'ici l'échéance | [SUITE]
17/06/2026 | PRIVÉE-FR | Dataiku / Cobuild | GA confirmée le 18/06/2026 | [SUITE]
17/06/2026 | NOUVEL-ENTRANT | Physicl (France) | démonstration au Startup Village AWS/NVIDIA VivaTech 2026 (17-20/06) | [SUITE]
18/06/2026 | PUBLIQUE-FR | "L'Assistant" / fonction publique | généralisé à ~1 M agents de l'État le 16/06, propulsé par Mistral, coût 700 k€, après pilote DINUM oct. 2025 | [NOUVEAU]
18/06/2026 | PUBLIQUE-FR | 655 M€ France 2030 IA | Lecornu 16/06 : investissement supplémentaire infrastructures/calcul/recherche/filières + données publiques IA + assistant Ameli | [NOUVEAU]
18/06/2026 | PUBLIQUE-INT | Inde / MANAV | cadre de gouvernance IA présenté par Modi à VivaTech 18/06 ; Inde partenaire IA officiel VivaTech 2026 | [NOUVEAU]
18/06/2026 | PRIVÉE-MONDE | Foxconn + Bull + NVIDIA | Vera Rubin NVL72 fabriqué CZ / assemblé Angers (France) ; debut humanoïdes Europe VivaTech 17/06 | [NOUVEAU]
18/06/2026 | PRIVÉE-FR | AMI Labs | entrée Next40 French Tech promotion 2026 (annoncé 15/06) ; 890 M€ mars 2026, world models, Yann LeCun | [NOUVEAU]
18/06/2026 | PRIVÉE-FR | H Company | entrée Next40 French Tech promotion 2026 (annoncé 15/06) | [SUITE]
18/06/2026 | PRIVÉE-FR | Prisme.ai | VivaTech 17-18/06 : nouveaux clients ArianeGroup, Pierre Fabre, ODDO BHF | [NOUVEAU]
18/06/2026 | PRIVÉE-MONDE | Genesis AI / Eno | premier humanoïde généraliste lancé 17/06, foundation model GENE, 105 M$ seed Khosla ; déploiements fin 2026 | [NOUVEAU]
18/06/2026 | PRIVÉE-MONDE | Anthropic | accès Fable 5/Mythos 5 toujours suspendu au 16/06 (J+4) ; seul délai officiel = vérification identité à partir du 8 juillet | [SUITE]
18/06/2026 | PRIVÉE-FR | Mistral Compute | bilan VivaTech 2026 (annoncé VivaTech 2025) ; datacenter Bruyères-le-Châtel attendu Q2 2026 | [SUITE]
18/06/2026 | PRIVÉE-FR | Neuralk-AI | Nuit de la Data et de l'IA 2026 — bronze (agent prédictif ML) | [NOUVEAU]
18/06/2026 | PRIVÉE-FR | Delos | Nuit de la Data et de l'IA 2026 — or (IAgen, suite bureautique GenAI « 1ère alternative EU ») | [NOUVEAU]
19/06/2026 | PUBLIQUE-FR | France 2030 / Lecornu | 655 M€ supplémentaires pour l'IA (16/06) ; assistant conversationnel Mistral généralisé à ~1 M agents de l'État d'ici fin 2026 | [SUITE]
19/06/2026 | PUBLIQUE-EU | VivaTech 2026 J1-J2 | Jeff Bezos + Yann LeCun grandes scènes J1 ; Modi-Macron "troisième voie IA" J2 (18/06) ; datacenter Mistral Bruyères "going live" fin juin (1 source) — keynote NVIDIA au programme, présence Huang non confirmée indépendamment au 19/06 | [SUITE]
19/06/2026 | PRIVÉE-MONDE | Anthropic Fable 5/Mythos 5 | Négociations Anthropic-Trump confirmées Globe and Mail 17/06 ; Chris Ciauri "confiant pour les prochains jours" ; accès toujours suspendu au 19/06 | [SUITE]
19/06/2026 | PUBLIQUE-EU | AI Act / Digital Omnibus | Consultation haute-risque ouverte jusqu'au 23/06 ; report Annexe III → 2 déc. 2027 (accord prov. 7/05/2026) | [SUITE]
19/06/2026 | PRIVÉE-MONDE | Google DeepMind / multi-agents safety | Appel à financement 10 M$ avec Schmidt Sciences, ARIA, Cooperative AI Foundation ; sécurité systèmes multi-agents ; deadline candidatures 8/08/2026 | [NOUVEAU]
19/06/2026 | PRIVÉE-FR | Neuralk AI / Gradium / pyannoteAI | Startup Village AWS/NVIDIA VivaTech 2026 (17-20/06) ; 7 startups européennes, ~470 emplois, >150 M$ cumulé | [SUITE / NOUVEAU]
19/06/2026 | PRIVÉE-MONDE | OpenAI GPT-5.5 Instant santé | Améliorations santé (18/06) : niveau comparable aux modèles de raisonnement frontier sur benchmarks santé ; 230 M utilisateurs/sem | [NOUVEAU]
19/06/2026 | NOUVEL-ENTRANT | pyannoteAI (France) | Spinout CNRS 2024, diarization speaker temps réel, >1 Md téléchargements HuggingFace, présente au Startup Village AWS/NVIDIA VivaTech | [NOUVEAU]
22/06/2026 | PUBLIQUE-FR | Tibi 3 / Bercy | 13 Md€ engagés (cible 15 Md€ fin 2026), ~40 partenaires dont SNCF/RATP/Eutelsat (première fois entreprises publiques), moitié deeptech IA/quantique/biotech/spatial, annoncé par Roland Lescure à VivaTech 19/06/2026 | [NOUVEAU]
22/06/2026 | PRIVÉE-FR | Mistral Compute | Datacenter Bruyères-le-Châtel opérationnel avec clients enterprise (19/06 VivaTech) ; 18 000 GB200 déployés [à confirmer vs. 13 800 GB300 DCD mars 2026] ; annonce extension Suède 1,4 Md$ ; cible 200 MW Europe 2027 ; Mensch : Mistral "full-stack cloud company" | [SUITE]
22/06/2026 | PUBLIQUE-EU | AI Act haute-risque consultation | Délai prolongé de 4 semaines : nouvelle échéance 23 juillet 2026 (était 23 juin) ; lignes directrices finales attendues fin 2026 | [SUITE]
22/06/2026 | PRIVÉE-FR | L'Oréal × OpenAI + NVIDIA | Deux partenariats stratégiques annoncés à VivaTech 17/06 (non capturés) : OpenAI partenaire fondateur "Transformative AI" L'Oréal (ChatGPT/ModiFace/GPT-Rosalind/CreAItech) + NVIDIA AI Enterprise pour rendu 3D et IA L'Oréal | [NOUVEAU]
22/06/2026 | PRIVÉE-FR | Owkin × Sanofi | Licence K Pro 5 ans (agents IA biopharma next-gen) annoncée 05/06/2026 (non capturée) ; extension partenariat €90M depuis 2021 ; second contrat similaire avec AstraZeneca mai 2026 | [NOUVEAU]
22/06/2026 | PRIVÉE-MONDE | Anthropic Fable 5/Mythos 5 | J+10 au 22/06, toujours suspendu, aucun accord signé ; négociations Trump-Anthropic en cours ; prochain jalon 8 juillet | [SUITE]
22/06/2026 | PUBLIQUE-EU | VivaTech 2026 bilan final | 200 000 visiteurs, 165 nationalités, ×4 fréquentation en 10 ans, festival J4 grand public (20/06), Thomas Pesquet ESA | [SUITE]
22/06/2026 | PUBLIQUE-EU | AION / EuroHPC gigafactory | Deadline candidatures EuroHPC AI Gigafactories fermée 23/06 ; candidature AION déposée (~10 Md€, 100 MW→1 GW) ; sélection attendue fin 2026 | [SUITE]
23/06/2026 | PUBLIQUE-INT | EO Trump "Promoting Advanced AI Innovation and Security" | Signé 02/06/2026 (non capturé) ; accès gouvernemental volontaire 30j pré-release modèles frontière ; délais 2 juillet (cyber-défenses fédérales) et 1er août (framework frontier AI) | [NOUVEAU]
23/06/2026 | PRIVÉE-MONDE | DeepSeek | 1er tour externe ~16/06/2026 : 7,4 Md$ (50 Md yuan), val. 50 Md$+ ; structure : LP sans equity/vote pour investisseurs privés, seul le Fonds national IA État reçoit droits de vote directs ; backers : Liang Wenfeng, Tencent, CATL | [NOUVEAU]
23/06/2026 | PRIVÉE-MONDE | Anthropic Fable 5/Mythos 5 | J+11 au 23/06 ; cadre conjoint Maison Blanche/Anthropic en rédaction depuis 18/06 (TheStreet/Politico) ; prochains jalons 2 juillet (EO) et 8 juillet (vérification identité) | [SUITE]
23/06/2026 | PUBLIQUE-FR | France 2030 filière robotique | 31 lauréats Eurosatory 15-19/06 (non capturé) ; 60 entreprises/labos, 135 M€ investissements, 68 M€ aide publique ; total depuis 2023 : 250 M€ aides, 100+ projets | [NOUVEAU]
23/06/2026 | PRIVÉE-MONDE | Automate 2026 Chicago | 23-24/06/2026 ; NVIDIA Pavilion humanoïdes en production ; Figure 03 à 1 robot/h (BotQ) ; Amazon 1M robots entrepôt ; Boston Dynamics Atlas livré à Hyundai/DeepMind | [NOUVEAU]
23/06/2026 | ACADÉMIQUE | Pleias / SYNTH + Baguettotron | Dataset génératif généraliste open source CC-BY-SA (79,6M exemples, 75B tokens) ; Baguettotron best-in-class raisonnement pour sa taille sur MMLU ; date exacte non confirmée | [NOUVEAU]
23/06/2026 | PUBLIQUE-EU | AI Act applicabilité 2 août 2026 | J-40 ; Article 50 transparence + enforcement GPAI Commission ; consultation haute-risque jusqu'au 23 juillet ; contexte rappelé face à EO Trump 1er août | [SUITE]

