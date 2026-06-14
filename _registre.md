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


