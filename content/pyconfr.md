title: PyConFr - un rapport
slug: pyconfr2014
date: 06-10-2014
tags: python, fr
summary: Un bref résumé de ce que j'ai vu à la conférence python francophone 2014


Je reviens tout juste de [PyConFr 2014](http://www.pycon.fr/2014/),
qui se déroulait ce week end (les sprints sont toujours en
court). C'était chouette, et je voudrais fixer un ou deux trucs ici -
surtout pour avoir une trace pour plus tard.

Ma propre présentation c'est bien passée, je pense. J'espère avoir été
à peu près clair, après j'aurai peut-être dû être plus technique, mais
c'est difficile sans expliquer la biologie avant.


D'abord merci beaucoup à Xavier qui a nous a conduit de Marseille à
Lyon et retour tout en souplesse, et à son copilote Victor...

C'était la première fois que j'assistais à cette conf, et j'ai trouvé
des intervenants de qualité et un audience attentive. C'est aussi la
première fois qu'il y avait une programation dédiée à l'enseignement
et la recherche, auquel j'ai eu l'honneur de participer et que j'ai
suivi toute la journée de samedi.

Voici quelques unes des choses que j'ai retenues:

## Sage

Deux conférences parlaient de
[Sage](https://en.wikipedia.org/wiki/Sage_%28mathematics_software%29)
qui est utilisé par les mathématiciens, et paraît être le standard _de
facto_ pour un certain nombre de sous-domaine des mathématiques. La
première conférence, de Thierry Dumont dressait un parallèle
intéressant entre programmation orientée objet et théorie des ensemble
(une structure d'anneau hérite des propriétés d'un groupe, par
exemple) et présentait le notebook Sage, prédécesseur de ipython
Notebook. La deuxième, par Viviane Pons, présentait l'application de
cet outil à l'étude de la combinatoire. J'ai trouvé cette intervention
très vivante, et j'aime quand les matheux partagent leur recherche, ça
casse un peu cette impression d'ésotérisme complet de leur boulot.

Apparemment il y a la possiblité d'une adoption du notebook Ipython
par la communauté Sage, même si le créateur William Stein a plutôt
l'air de tendre vers un modèle tout cloud, et un développement
spécifique. Pour ma part je trouverai ça dommage (ça me fait un peu
penser à Mir/Wayland, avec l'impression que c'est l'égo du créateur
qui prime sur l'efficacité). L'avantage du libre, c'est que personne
n'est obligé de le suivre dans ses choix...

## Marc-André Delsuc et l'enseignement à des biologistes

Bien sûr la problématique m'intéresse tout particulièrement, et en
plus M.A.D. a lancé une boîte - [casc4de](http://www.casc4de.eu/) - qui
fait du python scientifique pour la biophysique. On a eu quelques
brèves discussions, mais j'espère qu'on trouvera d'autres occasions
d'interagir. Sinon sur la conf elle même, un point que j'ai trouvé très marrant:

Marc-André explique qu'il utilise le notebook pour ses cours de
programmation aux biologistes. Bien sûr, ce cours fait peur
(physique+maths+info pour des biologistes ça fait beaucoup). Pour ces
étudiant.e.s, un effet inatendu pour moi de l'utilisation d'une
interface de programmation web est que ça dédramatise complètement
l'usage, parce qu'il est _naturel_ pour eux de rentrer du texte dans
des petites cases dans le navigateur, alors qu'ils sont complètement
bloqués devant un terminal ou un éditeur de texte en monospace, un
effet très innatendu pour moi.


## Un survol des autres interventions du samedi

J'ai bien aimé la présentation de Yannick Chopin, qui montre notemment
que Python et le stack scipy est le standard en astrophysique, avec
[astropy](http://www.astropy.org/) comme lieu commun.

Dans _Du Python qui ne manque pas d'air_ Romaric David a présenté
l'utilisation de python comme glue pour configurer freefem++ à partir
d'une spécification en fichier texte d'une sale de serveur, pour
calculer les flux d'air et éviter la surchauffe. Je pense que
[OpenSCAD](http://www.openscad.org/) pourrait l'aider à dessiner la
salle de manière plus simple...

Nicolas Rougier m'a convaincu d'essayer [Vispy](http://vispy.org),
surtout pour la visualisation des simulations d'épithélium, qui sont
impossible à afficher dynamiquement avec matplotlib. Blender c'est
bien, mais le développement est vraiment trop pénible (redémarer
Blender à chaque bug par exemple). Je suis aussi impatient de voir ce
que ce projet donnera avec WebGL.

Une autre bibliothèque que je veux intégrer dans mes projets
prochainement est [sympy](http://sympy.org), présentée par Kamel Ibn
Aziz Derouiche, et qui est beaucoup plus riche, notemment pour des
aspects de mécanique, que ce que je pensais.

Les autres conférences me concernaient moins, ou parlaient de choses
que je connaissais déjà, je vous laisse aller voir le programme...

C'est tout pour l'aspect purement python scientifique, les confs du
dimanche portaient sur des aspects plus généraux du langage.

## Dimanche

J'ai suivi la présentation des APIs hypermedia par Olivier Hervieu. Ça
a l'air d'être compliqué de mettre tout le monde d'accord pour avoir
des API web robustes et où tout le monde parle le même sabir. Si j'ai
bien compris, l'idée est d'éviter d'avoir à coder des URLs en dur dans
l'API, mais plutôt d'avoir une couche de description plus abstraite,
qui ne dépend pas des détails de la structure du site... J'ai aussi
suivi les deux présentations sur AsyncIO, ça a l'air d'être tout à
fait passionant, et big upà Victor Stinner pour sa présentation hyper
pédagogique de cet aspect. Je ne suis pas sûr d'avoir besoin de ce
type de mécanisme, mais c'est toujours bien de se former un peu. Pour
le reste, je ne me suis pas trop senti concerné par _Bootstrapping
Machine Learning_ de Louis Dorard... Je crois que `scikit-learn` est
plus adapté à mes problématiques, et j'ai bien aimé la présentation
sur Kivy, même si j'ai vraiment le développement d'interface utilisateur en horreur.

Voilà c'est à peu près tout.. J'ai ramené un t-shirt trop petit et une
adhésion à l'Afpy dans mes bagages.
