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