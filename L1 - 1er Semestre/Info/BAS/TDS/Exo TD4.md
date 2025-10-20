[[TD4 - BAS.pdf]]

# Exercice 1 
```sh
#! /bin/sh

for mot;do
  i=0
  i=`echo -n $mot | wc -m` #-m car problème avec le -c car si caractère spécial comme è ou à... compte pour 2 carac avec le -c mais -m 1 seul
  echo $mot\($i\)
done
exit 0
```

# Exercice 2 
```sh
#!/bin/sh
if [ $# -ne 1 ];then
  echo "Usage : $0 parametre" >&2
  exit 1
fi

if [ ! -f "$1" -o ! -r "$1" ];then
	echo "$1 n'est pas un fichier accessible en lecture"
	exit 2
fi
compteur=1
while read ligne;do
	echo "$compteur" : "$ligne"
	compteur=`expr $i + 1`
done < "$1"
exit 0
```

# Exercice 3
```sh
#!/bin/sh
if [ $# -ne 1 ];then
  echo "Usage : $0 répertoire" >&2
  exit 1
fi

if [ ! -d "$1" -o ! -r "$1" -o ! -x "$1" ];then
	echo "$1 n'est pas un répertoire accessible en lecture"
	exit 2
fi

for fichourep in "$1"/*;do
	ls -l $fichourep | grep '^-' | tr -s ' '|cut -f9 -d ' '
done
exit 0
```

# Exercice 4
```sh
#!/bin/sh
if [ $# -ne 1 -o $# -ne 0 ];then
	echo "Usage : $0 [] or $0 [file]"
fi
if [ $# -eq 1 ];then
	set -- "/users/linfg/linfg0/omar"
fi

numLigne=wc -l $1 | cut -f1 -d ' '
while read ligne;do
	tail -$numLigne | head -1
	numLigne=`expr numLigne - 1`
done < "$1"

```