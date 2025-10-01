- Installer intellij IDEA
- Installer java 21 temurin depuis le fichier msi si on est sur windows
	- sinon aller sur IDEA et installer depuis les paramètres
- Faire le template [https://fabricmc.net/develop/template/](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbW9yczRZcVhqZ1NFYTRaTWllSV9EMTl5TkxLQXxBQ3Jtc0tuQ0c2TFFqNUtVRWVXdlczX1RKd1ptX2FBY0hkZXpFODdMbWRlcFpjSHpfV2tXX1ozRzZhR0xTYXBJRnVFQ21yRGZ6UU9Yc2huRDRSc0draGJWakR5TUduSmtmTUxnaVA3VnF3YUdnNnlQUVlndXVQdw&q=https%3A%2F%2Ffabricmc.net%2Fdevelop%2Ftemplate%2F&v=oU8-qV-ZtUY) et pas oublier de décocher "Split client and common sources" et de cocher "Data Generation" puis installer le zip
- Ouvrir un nouveau projet dans le dossier dezipé
- Vérifier dans le "project structure" que SDK est bien sur 21 et que language level aussi
- Aller dans les paramètres puis tools puis gradle et vérifier que l'on est bien sur temurin 21
- Aller dans "mixin" puis "exampleMixin"et de ctrl clique sur Minecraft server
- Mettre dans le cmd : ```./gradlew genSources ```

https://www.youtube.com/watch?v=oU8-qV-ZtUY&list=PLKGarocXCE1H_HxOYihQMq0mlpqiUJj4L&index=2


# ALLER VOIR ANCIEN CODE ( testmod ) POUR INFORMATIONS PRECISES