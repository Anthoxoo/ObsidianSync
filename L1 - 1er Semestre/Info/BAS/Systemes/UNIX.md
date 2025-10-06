### Systeme de fichiers UNIX
- voir cm et mettre ce qu'est inode
- bloc 0 --> bloc de boot
- bloc 1 --> nb de fichier que le systeme de fichier peut contenir, sa taille et des pointeurs sur la liste des blocs libres
- la taille es blocs dépend du systeme ( ex : 512octets,8192octes... )

### Structure d'une inode
**Bien relire ce qu'est une inode et son fonctionnement**
- chaque inode est repéré par son numéro
- la commande `ls -li` affiche les numéros d'inodes.
- Si la taille du fichier est supérieure à 10, le système lui attribue un nouveau bloc contenant les adresses des blocs de données

### Repertoire
- Un répertoire est un fichier qui contient le nom et les inodes des fichiers qu'il contient
- 