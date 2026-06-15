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

