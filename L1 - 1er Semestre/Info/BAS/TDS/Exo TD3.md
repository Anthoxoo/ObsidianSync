# Exercice 4 :
```sh
#!/bin/sh

if ls -l "$1" | grep '^...x'; then
  echo "1"
  exit 1

else
  echo "0"
  exit 0
fi
```

# Exercice 5 :
```sh
#!/bin/sh

if test "$1" != '' && test $2 = '';then
  exit 0
else
  exit 1
```