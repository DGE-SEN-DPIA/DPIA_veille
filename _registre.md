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

14/06/2026 | PRIVÉE-MONDE | Anthropic | suspension mondiale Fable 5/Mythos 5 sur ordre du gouvernement US (sécurité nationale) | [NOUVEAU]
14/06/2026 | PUBLIQUE-EU | Commission européenne | paquet souveraineté technologique + proposition CADA (cadre cloud sovereignty 4 niveaux, triplement capacité datacenter UE) | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | Mistral | négociations levée ~3 Md€ à ~20 Md€ de valorisation | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | SoftBank / Hauts-de-France | annonce 75 Md€ datacenters IA en France, dont 45 Md€ Hauts-de-France (5 GW) | [NOUVEAU]
14/06/2026 | PUBLIQUE-INT | Chine (MIIT/SASAC) | directive 10 000 robots humanoïdes opérationnels fin 2026 | [NOUVEAU]
14/06/2026 | PUBLIQUE-INT | États-Unis | executive order pré-accès 30j modèles frontières + BIS ferme faille export puces IA vers Chine | [NOUVEAU]
14/06/2026 | PUBLIQUE-EU | Espagne / Italie | course aux AI Gigafactories : calendrier espagnol (600-800 M€) + inauguration SOL/LISA EuroHPC Bologne | [NOUVEAU]
14/06/2026 | PUBLIQUE-FR | Gouvernement | plan formation 15M professionnels IA (Farandou) + clôture AAP Pionniers de l'IA (France 2030) | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | Wandercraft / Renault | robot humanoïde Calvin déployé en test à l'usine de Douai | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | H Company | rejoint la Nemotron Coalition de Nvidia + lance Surfer H / Runner H / Tester H | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | Owkin | extension partenariat Sanofi, licence 5 ans plateforme K Pro | [NOUVEAU]
14/06/2026 | PRIVÉE-FR | Outscale (Dassault Systèmes) | 4 annonces souveraineté cloud/IA (AI Factories, K8s visant SecNumCloud 3.2) à OUTSCALE Experiences | [NOUVEAU]
14/06/2026 | PRIVÉE-MONDE | OpenAI / Anthropic | dépôts S-1 confidentiels quasi simultanés, course à l'IPO (965 Md$ / ~1000 Md$ visés) | [NOUVEAU]
14/06/2026 | PRIVÉE-MONDE | NVIDIA | partenariats "AI factories souveraines" Corée du Sud (NAVER, SK Telecom) | [NOUVEAU]
14/06/2026 | PRIVÉE-MONDE | Alibaba (Qwen) / Moonshot AI | lancement Qwen3.7-Plus + nouvelle levée Moonshot visant valorisation 30 Md$ | [NOUVEAU]
14/06/2026 | ACADÉMIQUE | World models robotique | OSCAR (arXiv 2606.04463) + Cosmos 3 NVIDIA (arXiv 2606.02800) + bilan ICRA 2026 Vienne | [NOUVEAU]
14/06/2026 | NOUVEL-ENTRANT | Probabl (spin-off Inria, scikit-learn) | levée seed 13 M€ (total 18,5 M€), record européen COSS | [NOUVEAU]
14/06/2026 | INFRA | Mistral Compute | datacenter Bruyères-le-Châtel (44 MW, 13 800 GPU GB300) attendu opérationnel fin juin 2026 | [NOUVEAU]
