TLS ( transport layer security ) est utilisé en complément de http -> https

### Authentifier c'est avoir une preuve de l'identité
- on utilise la cryptographie pour avoir une preuve
		- utilisation de la méthode **RSA** ( chiffrage asymétrique ) -> **clé publique, clé privée** ![[schéma chiffrage rsa]]
		- mais possibilité de **man in the middle** -> il va remplacer les clés de 1 par les siennes et envoyer a 2, pareil dans l'autre sens
			- C'est pourquoi il existe des Infrastructures a clefs publiques : **Certificat** qui assure que tel clef est associée a tel identite. Les naviguateurs viennent avec une liste de certificats, le naviguateur demande le certificat a chaque fois
				- problème des certificats : personne malveillante peut installer des faux certificats et redirige un site vers un autre pour lui extorquer ses infos

--- 
### Plusieurs types virus : 
- cheval de troie
- virus informatique ( se propage entre machines et infecte des ordinateurs devenants des "hotes" )
- vers informatique ( virus réseau qui se déplace via les mails, partage de fichiers, messagerie, failles...)

--- 
### Risque des objets connectés :
- Vols de données personelles ( tres commun )