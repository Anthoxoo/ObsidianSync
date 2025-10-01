- Il n'y a que des jsons
- Il n'y a que des blocs
- permet de changer par la suite la texture d'un bloc si jamais celui-ci évolue avec le temps exemple : le blé n'a pas tout le temps la meme forme
- Comment ca s'écrit : 
- ```java
  
  {
	"variants" : {
	"" : {
		"model" : "testmod:block/pink_garnet_block"
		}
	}  
  }
  //Pas de changement de bloc dans cet exemple
  
  
  {
  "variants": {
    "": { "model": "testmod:block/pink_garnet_block" },
    "facing=north": { "model": "testmod:block/pink_garnet_block", "y": 0 },
    "facing=east": { "model": "testmod:block/pink_garnet_block", "y": 90 }
  }
}
//Ici changement du bloc en fonction de sa position
  ```