# Neil Zeghidour — entretien podcast (2026)

Oct 28, 2026 · @Al

## Source et précautions

Tout ce qui suit est le récit de Gradium dans un podcast d'entrepreneurs : les chiffres de marché, de levée et de vitesse sont déclaratifs.

- **Source :** entretien avec Neil Zeghidour, 35 ans, CEO de Gradium (modèles d'IA vocale), cofondateur de Kyutai, passé par Google et Facebook AI Research, dans le podcast *Génération Do It Yourself* (GDIY) animé par Matthieu Stefani.
- **Date :** enregistré en octobre 2026, comme l'animateur le dit à l'antenne ; le jour exact n'est pas donné. Il évoque le nouveau modèle de Mistral sorti « ces derniers jours », et Zeghidour l'arrivée de Claude dans Google Slides, Docs et Sheets « hier ».

## Partie 1 — Feuille de route, ambitions, goulets d'étranglement

### Feuille de route

Gradium a un an et élargit ses modèles vocaux à de nouvelles langues et à de nouveaux appareils ; sa prochaine frontière de recherche est l'écoute dans des pièces bruyantes, avec plusieurs interlocuteurs.

- **Produits actuels** (uniquement des modèles, vendus par API et facturés au token audio) :
  - transcription et synthèse vocale conçues pour la conversation en direct ; Zeghidour revendique « les modèles les plus rapides du monde », avec une réponse en 50 ms
  - création de voix à partir d'une description, par exemple une femme d'un âge donné avec un accent québécois
  - traduction en temps réel
- **Langues :**
  - aujourd'hui : anglais, français, portugais, espagnol et allemand
  - « dès la semaine prochaine » : de nombreuses autres, dont le coréen, le japonais, l'arabe et le finnois
  - bientôt : une soixantaine de langues
- **Nouvelle gamme embarquée :** des modèles plus petits qui tournent sur le téléphone, pour les applications grand public gratuites dont le coût par API serait prohibitif.
- **Choix d'exclusion :** ni livres audio, ni narration, ni doublage de vidéos ; Gradium se spécialise dans l'interaction.
- **Prochaine frontière de recherche :** la voix pour les robots et les pièces. L'appareil doit localiser les sources sonores et comprendre qui s'adresse à lui. Selon lui, « personne n'est nulle part » sur ce sujet, qui touche autant le matériel que le logiciel.
- **Modèle d'assistant :** des assistants qui écoutent en permanence, travaillent en asynchrone et ne parlent que lorsqu'on les sollicite, en plus de la conversation en direct.
- **Financement** (vérifié dans la presse) :
  - un seed de 70 M$ fin 2025, mené par FirstMark et Eurazeo, puis une extension de 30 M$ de Nvidia en juillet 2026, soit un peu plus de 100 M$ au total ([Dealroom](https://dealroom.co/news/137701-gradium-adds-30m-from-nvidia-pushing-seed-round-past-100m/))
  - les donateurs de Kyutai (Xavier Niel, Rodolphe Saadé, Eric Schmidt) ont aussi investi
  - le même article mentionne un bureau à San Francisco et de nouveaux modèles « presque chaque mois »
- **Côté Kyutai :** le laboratoire travaille désormais sur les world models, avec d'autres projets « qui vont être annoncés bientôt ».

### Ambitions

Zeghidour veut faire de Gradium la couche de modèles de la voix, en pariant que la voix deviendra la principale manière d'utiliser les machines et restera longtemps un problème de recherche difficile.

- **La voix comme interface :**
  - « C'est une évidence que c'est ce qui va in fine être la manière dont on interagit avec la machine. » Il a « hâte d'arriver au moment où on va pouvoir se débarrasser du clavier ».
  - Le logiciel passe déjà au langage naturel : coder est devenu une conversation avec des agents, et Claude dans Google Sheets transforme les formules en simples demandes. Or le langage naturel s'exprime le plus naturellement à l'oral.
  - Les assistants personnels pourraient représenter 8 milliards de personnes qui leur parlent peut-être une heure par jour, soit des « volumes d'interaction vocale absolument gigantesques ».
  - Son pitch deck initial chiffrait le marché sur le jeu vidéo et le support client. Il n'avait pas anticipé que la voix deviendrait la manière de piloter les logiciels.
- **Uniquement des modèles :**
  - Gradium vend des modèles ; ses clients construisent les applications (exemples en partie 2).
  - Selon lui, la couche applicative se banalise plus vite : n'importe qui peut faire une maquette de Lovable ou de Cursor, personne ne peut faire une maquette de modèle.
  - À l'été 2025, des fonds l'ont éconduit en expliquant que « les modèles, c'est fini » et que seules les applications comptaient. Six mois plus tard, les nouveaux laboratoires levaient « un milliard tous les mois ».
- **La voix reste immature :**
  - Il s'oppose à Mati Staniszewski, cofondateur d'ElevenLabs, pour qui la technologie vocale se banalise et l'intégration chez les clients devient le principal avantage concurrentiel.
  - Pour départager les meilleurs modèles de texte, il faut des problèmes mathématiques qui résistent depuis des siècles. Un modèle vocal, lui, « se plante une fois sur deux » si on lui demande de prononcer un numéro de téléphone ou une URL.
  - Ce qui sépare la voix d'une « couche d'interaction permanente avec les machines » est donc « avant tout une amélioration technique des modèles sur leur fiabilité, sur la qualité des voix, sur la customisation », donc un savoir-faire de chercheur.
- **Un laboratoire de frontière géré comme une entreprise :** il qualifie Gradium de « frontier lab » de la voix, parce qu'il a les modèles les plus rapides et sort des premières mondiales. L'entreprise est pourtant « drivée que par la création de valeur, la satisfaction des utilisateurs et le revenu ».
- **Kyutai comme incubateur :**
  - Gradium est une spin-off de Kyutai, qui figure parmi ses principaux actionnaires ; les fondateurs ont cédé à Kyutai une partie de leurs parts.
  - L'objectif est que Kyutai se finance au-delà des seuls dons, comme le font certaines universités grâce à leurs spin-offs. Il estime que les laboratoires de recherche devraient organiser cette voie.
- **Les petites structures gagnent :** « À l'âge des agents, chaque individu est tellement multiplié dans son impact que les grosses boîtes sont plus limitées qu'autre chose. » Il y voit « l'âge d'or des boîtes à taille humaine » ; Gradium compte moins de 25 salariés.
- **Pourquoi il a quitté les grands groupes :**
  - Chez Google, son équipe est passée de 2 à 50 personnes, et les réunions de stratégie et d'alignement ont pris le pas sur la science.
  - Avant ChatGPT, les grands groupes retenaient leurs modèles génératifs par crainte des risques, et parce que l'IA menaçait leurs propres produits, comme la recherche Google et la publicité.
  - Il ajoute que certains acteurs ont « beaucoup joué sur les peurs », pour des raisons idéologiques ou « comme un argument de vente », sans nommer personne.
- **Les modèles de texte de pointe gardent leur valeur :** l'engouement grandit à chaque sortie, et les sorties s'accélèrent, ce qu'il attribue au fait que les laboratoires ont « craqué des trucs dans l'auto-amélioration des modèles ».
- **AGI :** « éduqué dans un très grand scepticisme », il voyait l'AGI comme un argument marketing jusqu'il y a environ un an. Il l'est moins aujourd'hui, car « les pessimistes ont toujours eu tort jusqu'ici ».
- **Les croyances orientent la recherche :** le Transformer s'est imposé en partie parce que beaucoup de chercheurs y ont cru et ont publié des dizaines de milliers d'articles pour l'améliorer. Selon lui, les world models de Yann LeCun ont besoin de la même masse de convaincus pour aboutir.

### Goulets d'étranglement

La voix est surtout freinée par des limites techniques : la fiabilité, et un arbitrage entre intelligence et naturel en temps réel. Sa dépendance au jugement humain ralentit aussi les itérations.

- **Fiabilité :** la plupart des agents vocaux sont fragiles. Les numéros, les URL et les plaques d'immatriculation les mettent encore en échec.
- **Intelligence contre latence :**
  - Les modèles voix-à-voix perdaient en intelligence quand on leur apprenait à parler : suffisant pour des démos, mais « impossible de mettre un truc pareil en production ».
  - Les agrandir (Moshi comptait 7 milliards de paramètres ; 30 à 50 milliards ont été envisagés) augmente les coûts d'entraînement et de service et la latence, car générer de l'audio en temps réel est difficile avec un gros modèle.
  - Le voix-à-voix ne remplacera la chaîne transcription-modèle-synthèse que « si l'intelligence est identique à celle qu'on aurait avec un modèle textuel ».
- **Pas de vérification automatique :**
  - La cible est une voix humaine, imperfections comprises : la qualité ne se vérifie pas automatiquement, contrairement aux mathématiques.
  - Les progrès reposent sur des tests à l'aveugle par des humains. On ne peut pas laisser un modèle s'améliorer seul pendant une semaine.
- **Langues que l'équipe ne sait pas juger :** le coréen, le finnois ou le norvégien exigent des linguistes extérieurs. Il veut éviter d'imposer sans le savoir un accent régional, comme les concurrents l'ont fait selon lui avec le français québécois.
- **Pièces et robots :** entendre à distance quand plusieurs personnes parlent reste non résolu, côté matériel comme côté logiciel.
- **Coût pour le grand public :** la tarification par API exclut les applications vocales gratuites, d'où la gamme embarquée.
- **Efficacité de l'apprentissage :**
  - Un bébé apprend sa langue avec quelques centaines d'heures de parole, venant surtout de deux personnes, sans annotation. La reconnaissance vocale utilisait des dizaines de milliers d'heures en 2015 et en utilise des millions aujourd'hui.
  - Dans les domaines pauvres en données (protéines, communication animale, matériaux), cela crée de « faux espoirs », et il est souvent difficile de savoir si un modèle a appris quelque chose.
- **Monétisation :** faire payer est « beaucoup plus dur » que l'open source, où « tout le monde est toujours ravi parce que c'est gratuit ».
- **Concurrence :**
  - OpenAI, ElevenLabs, Deepgram et d'autres occupent déjà le marché.
  - Sesame a levé 250 M$ avec ce qu'il décrit comme « une espèce de Moshi++ » **\[à vérifier\]**.
  - ElevenLabs a été valorisée environ 22 Md$ lors d'une vente de parts de salariés en juillet 2026, le double de sa série D à 11 Md$ de février ([ChatForest, d'après Bloomberg](https://chatforest.com/reviews/elevenlabs-22-billion-valuation-tender-offer-secondary-july-2026/)). La chronologie donnée à l'antenne par l'animateur est légèrement décalée.
- **Coût des talents :** dans les grands groupes, les rémunérations des chercheurs vedettes « peuvent atteindre des millions d'euros par an » ; les start-ups répondent par des parts du capital.
- **Sécurité des agents :** l'injection de prompt rend risqués les assistants qui ont accès aux e-mails et aux agendas (partie 2).
- **Transition humaine :** « le gain d'efficacité ne signifie pas moins de travail, il signifie juste plus d'attentes ». Les salariés, surtout en fin de carrière, devront être formés, et il s'attend à une transition douloureuse.

## Partie 2 — Enseignements techniques

### De la compression audio aux LLM audio

Les modèles vocaux reprennent la recette des LLM de texte sur des « tokens audio », issus d'un modèle de compression que Zeghidour a conçu chez Google.

- **Tokens audio :** son premier projet chez Google était un modèle neuronal de compression pour Google Meet, qui résume un signal audio riche en quelques tokens pour garder une bonne qualité sur une connexion faible.
- **Prédire la suite d'un son :** ces tokens étaient assez proches de tokens de texte pour entraîner un LLM à prédire les \~100 ms d'audio suivantes à partir de la dernière seconde.
- **Résultats obtenus en deux jours :**
  - cinq secondes de sa voix prolongées dans sa voix (clonage vocal)
  - cinq secondes de guitare prolongées en jeu de guitare (génération musicale)
- **Même architecture, autres données :** l'architecture était celle des modèles de texte, entraînée uniquement sur de l'audio. Générer de la musique ne demande aucune connaissance textuelle.
- **Sa version de la filiation :** cette approche sous-tend Suno, ElevenLabs et le mode vocal avancé d'OpenAI, et Suno serait né d'une réimplémentation sur GitHub de leur article sur la musique.
- **Taille :** les modèles de Gradium comptent 2 à 5 milliards de paramètres, contre environ 1 000 milliards pour le dernier modèle de Mistral ; les besoins d'infrastructure sont donc bien plus faibles.

### Chaîne classique contre voix-à-voix

- **Ce que perd la chaîne :** transcrire, répondre avec un LLM de texte puis synthétiser fait disparaître l'information paralinguistique : l'ironie, la confusion, les émotions, les rires et les petites relances (« ah oui »).
- **Moshi :** le modèle de Kyutai (2024, 7 milliards de paramètres) a été le premier modèle public de conversation voix-à-voix en temps réel, et longtemps le seul. GPT Live, d'OpenAI, est désormais dans la même catégorie.
- **Half-duplex contre full-duplex :**
  - La plupart des modèles vocaux fonctionnent comme un talkie-walkie : ils écoutent ou ils parlent. L'utilisateur s'adapte en ne parlant ni trop vite ni trop lentement, et en évitant de tousser pendant la réponse.
  - Un modèle full-duplex écoute en continu, peut être interrompu, et poursuit malgré une toux ou un acquiescement.

### Délégation : une petite voix devant un gros cerveau

- **Le dilemme :** un modèle vocal plus gros est plus intelligent mais plus coûteux et plus lent ; un petit modèle est naturel mais limité.
- **La réponse (MoshiRAG, article de Kyutai de février 2026) :**
  - Un petit modèle temps réel sert d'interlocuteur.
  - Il envoie certaines requêtes, « comme un appel à un ami », à un grand modèle dans le cloud, par exemple GPT-6.1.
  - Il réinsère ensuite la réponse naturellement dans la conversation.
- **Meubler l'attente :** ces quelques secondes sont « très difficilement compressibles ». Les clients les remplissent avec de la musique d'attente, de faux bruits de clavier, des formules de relance (« question très intéressante, attends, je regarde ») ou des informations utiles. Dans une démo de réservation d'hôtel, l'agent signalait un festival de cuisine à Tokyo pendant sa recherche.

### Gamme de produits

- Transcription, synthèse vocale, création de voix et traduction en temps réel, servies par API ; modèles embarqués pour téléphones.
- **La traduction est plus difficile que la transcription :** comme un interprète humain, le modèle doit attendre assez de contexte avant de poursuivre.
- **Entraînement de zéro :** Gradium entraîne ses propres modèles, « très inspirés des technologies qu'on a développées à Kyutai ». Aucun modèle n'est transféré de Kyutai ; repartir d'un modèle open source serait « limite plus compliqué ».

### Le jugement humain guide l'entraînement

La qualité d'une voix se juge à l'oreille : le retour humain fait partie de la boucle d'entraînement, y compris pour les agents d'IA.

- **Tests à l'aveugle à grande échelle :** des évaluateurs comparent les modèles sur la prononciation, l'accent, l'agrément de la voix et sa cohérence avec un personnage, « des dizaines de milliers de fois par jour ». Leurs retours orientent l'entraînement.
- **Objectif :** distiller le goût esthétique humain dans des modèles pour itérer plus vite. Il pense y parvenir un jour, mais les humains restent aujourd'hui au cœur du développement.
- **Des agents qui rémunèrent des humains :**
  - Sur des projets peu prioritaires, les agents de code reçoivent un budget de calcul (par exemple 32 machines) et une API pour demander des jugements humains.
  - L'agent commande des tests d'écoute quand il en a besoin, reçoit les résultats quelques heures plus tard et poursuit ses itérations.
  - En cas d'urgence, Zeghidour demande à son agent 500 exemples et les note lui-même de 1 à 5.

### Voix et accents

- **Le naturel l'emporte sur le soigné :**
  - Gradium achète des licences de voix à des comédiens, mais les voix publicitaires sur-articulent et les utilisateurs les jugeaient « trop robotiques » au téléphone.
  - L'équipe a enregistré ses propres membres en studio, en train de se raconter leurs vacances. Beaucoup de voix en production sont désormais celles des salariés, dont celle de Zeghidour.
- **Biais d'accent :** les voix françaises des concurrents sonnaient québécoises, probablement parce que leurs données ont été achetées en Amérique du Nord.
- **La culture compte plus que l'entraînement :**
  - Entraîner sur de nombreuses langues est simple ; choisir la voix que veulent les gens de chaque marché l'est beaucoup moins.
  - Des linguistes vérifient par exemple qu'une voix « bavaroise » n'est pas autrichienne.
  - L'arabe égyptien est largement accepté pour les agents téléphoniques, tandis que le Maroc demande de la darija, mélange de français, de berbère et d'arabe.

### Données synthétiques

Des LLM génèrent de faux dialogues pour entraîner les modèles vocaux à de nombreux scénarios. Cela consomme bien plus de calcul que les agents de code de l'équipe, dont les abonnements dépassent rarement les forfaits à 200 $ par mois.

### Efficacité de l'apprentissage

- **Bébés contre machines :** ses premiers travaux, à l'École normale supérieure (ENS), s'inspiraient de l'acquisition du langage chez le nourrisson. Selon les observations de familles menées par le laboratoire d'Emmanuel Dupoux, un enfant entend quelques centaines d'heures de parole, venant surtout de deux personnes, sans annotation.
- **Machines :** Deep Speech 2, de Baidu (2015), s'entraînait sur des dizaines de milliers d'heures ; les modèles actuels en utilisent des millions.
- **Langage animal :** consultant pour l'Earth Species Project, il s'est vu proposer « 5 heures de corbeau ». Les sons d'animaux n'ont pas d'annotations, et prouver une communication supposerait d'obtenir de l'animal qu'il réalise une tâche.
- **Leçon générale :** l'efficacité de l'apprentissage a peu été travaillée parce que les données abondaient. La biologie et les matériaux butent sur la même difficulté d'évaluation : il est dur de savoir si un modèle a appris quelque chose.

### L'IA dans la recherche en IA

- **Code :** Codex et Claude Code tournent « 24 heures sur 24 ». L'équipe code très peu et vérifie le code produit.
- **Vitesse :** une idée qui demandait trois mois d'implémentation donne ses premiers résultats en trois heures.
- **Qui s'en sort le mieux :** la recherche est « un travail de détective » (hypothèses, expériences, choix du prochain mouvement), indépendant de l'écriture du code. Les meilleurs chercheurs d'avant les agents restent les meilleurs, et les écarts se creusent.
- **Risque pour l'apprentissage :** les agents explorent seuls et ne rendent que la réponse finale ; les juniors perdent les tâtonnements qui forment un chercheur. Il veut préserver cette part d'apprentissage.

### Clients et cas d'usage

Les clients de Gradium sont des développeurs qui construisent des agents et des applications vocales ; l'entreprise mise sur la fiabilité dans les détails, comme les plaques d'immatriculation, plutôt que sur une voix générique.

- **Ce que construisent les clients :** prise de rendez-vous médicaux, recouvrement de dettes, sondages, apprentissage des langues, amis virtuels, personnages de jeux vidéo, et agents d'assurance auto qui doivent prononcer et comprendre des plaques d'immatriculation.
- **Une application de rencontres** fait passer à chaque utilisateur un entretien vocal d'une heure et demie, pour proposer des rencontres plus fines qu'avec des critères démographiques.
- **Renault, avec le groupe RMC BFM :** des playlists de podcasts personnalisées dans la voiture. Les transitions entre séquences sont générées avec la voix de journalistes connus, puisque l'ordre ne peut pas être connu à l'avance.
- **Accès aux grands comptes :** souvent via un intégrateur, même si certains disposent des équipes techniques pour intégrer les modèles eux-mêmes.
- **Avant Gradium :** un grand jeu en ligne (sous NDA) voulait des personnages non joueurs dotés de la parole, et des studios de jeux vidéo comme des fabricants de smartphones réclamaient une offre commerciale à Kyutai. Refuser toutes ces demandes a conduit à la spin-off.
- **Les idées qu'il aimerait voir éclore :** des jeux vocaux (négociateur lors d'une prise d'otages, détection de mensonges, jeux coopératifs), un concurrent de Duolingo pensé d'abord pour la voix, l'entraînement aux conversations difficiles ou aux pitchs, et des compagnons du quotidien. Il voit dans le support client un adéquation produit-marché parfaite.

### Les harnais d'agents

Le harnais (« harness ») est la couche qui organise un modèle en équipe d'agents ; Zeghidour y voit aujourd'hui le principal levier de productivité.

- **Son analogie :** le héros du film *Memento* oublie tout après quelques minutes. Si l'on confie une tâche à chacune de nombreuses personnes dans ce cas et que l'on répartit bien le travail, elles produisent malgré tout quelque chose qui s'accumule dans le temps.
- **Ce que fait un harnais :**
  - il organise un modèle manager et des sous-agents, et décide de ce qui tourne en parallèle ou en séquence
  - il donne accès à des outils comme Slack, les e-mails ou une carte bancaire
  - il conserve la mémoire dans des fichiers texte sur l'utilisateur et les sessions passées
- **Même modèle, résultats différents :** l'écart entre ceux qui conçoivent leur harnais et ceux qui utilisent la version standard est « titanesque », un facteur 10 de productivité.
- **Sa pratique :**
  - En fin de session de travail, le modèle documente tout ce qui est réutilisable (un nouveau modèle, un nouveau jeu de données) pour les agents futurs.
  - Des consignes contradictoires « contaminent » un harnais. Il évalue ses harnais de manière scientifique, avec un agent juge en boucle fermée.
- **Un champ ouvert :** personne n'a trouvé la bonne interface, et même les harnais d'OpenAI et d'Anthropic sont « très imparfaits ». Il s'attend à ce que des développeurs individuels en trouvent de meilleurs.
- **Ses modèles :**
  - le meilleur modèle (Astra ou Fable) comme manager, pour planifier la journée et répartir les tâches
  - des modèles moins chers (Opus, Sol) pour l'exécution
  - il paierait 2 000 $ par mois au lieu de 200 $ pour le meilleur modèle manager
- **Discipline :** il passe une heure à planifier avec l'agent et relit lui-même le plan avant de lancer le travail. Il met en garde contre la « LLM psychosis » et « l'illusion de la productivité », et reconnaît dormir peu à force de piloter ses agents depuis son téléphone.

### Sécurité des agents

- **Sa propre alerte :** il s'était codé un assistant vocal avec accès à ses e-mails, à Slack et à son agenda. Ses ingénieurs lui ont dit qu'il était « complètement fou », à cause de l'injection de prompt.
- **Exemple :** un invité peut modifier la description d'un événement d'agenda. Quand l'agent la lit, ce texte peut réécrire ses instructions et lui faire divulguer des informations confidentielles.
- **Son conseil :** laisser les agents rédiger des brouillons, sans jamais envoyer. Empiler les cloisonnements pour rendre l'exfiltration quasi impossible devient un métier à part entière.
- **En exploitation :** les agents de Gradium surveillent la production la nuit et alertent les ingénieurs d'astreinte (e-mail, puis SMS, puis appel), idéalement par l'appel téléphonique d'un agent vocal.

### Organisation et recrutement

- **Équipe :** moins de 25 salariés.
- **Fondateurs :** pour l'essentiel les cofondateurs de Kyutai, plus Olivier Teboul, avec qui Zeghidour a inventé les LLM audio chez Google.
- **Liens avec Kyutai :** le directeur scientifique Alexandre Défossez partage son temps entre les deux structures ; Zeghidour encadre toujours des doctorants à Kyutai ; les équipes partagent leurs bureaux et ont fait un séminaire commun.
- **Premiers recrutements :** la première recrue venait de la vente. Une designer à plein temps est arrivée il y a un mois ; l'équipe tient un « wall of shame » des sites conçus par IA, pour éviter ce style.
- **Épreuves de recrutement :** des exercices de maths et de code au tableau, qui selon lui prédisent encore la capacité à résoudre des problèmes. Les entretiens à distance souffrent désormais d'outils de triche en temps réel.

### Appareils et espaces de travail

- **Successeurs du smartphone :** tout remplaçant passera par une interface vocale, mais il ne voit pas encore quel problème il résoudrait ; l'écran garde son intérêt. Il croit en revanche aux petits appareils dédiés à la prise de notes, avec un bouton physique.
- **Bureaux :** l'open space fonctionnait parce que chacun portait un casque. Quand chacun parlera à ses agents, il s'attend au retour des box individuels, des parois absorbantes et des cabines téléphoniques.
