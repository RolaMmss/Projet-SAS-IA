# Projet-SAS-IA


    • Contexte du projet : 

        ◦ une API :  ImageRecognition
        ◦ un mode d'emploi de l'utilisation de l'API : 
            ▪ Est-ce qu'il y a une limite de requêtes par jour ? 
              Il y a une limite de 100 requêtes par jour
              
            ▪ Comment gérer l'API-key ? (Attention à ne pas exposer de secret sur github) 
              Les Api-keys ont été fourni dans la documentation de l’API . Il y a un client ID et un secret. Par soucis de sécurité, nous avons mis ces API-keys dans un fichier privé local qui seront appelés par les opérations

            ▪  Définir ce que vous allez envoyer à l'API et ce que vous allez récupérer. 
              Nous devons fournir à l’API une image, celle-ci nous renvoie des prédictions sur cette image telles que le nombre d’individus, leur âge etc ..
              

    • Le pitch du projet
      Nous avons décidé de vous présenter un projet d’application Web basé sur la reconnaissance d’image. Cette API nous offre plusieurs services de prédiction sur l’image que l’utilisateur fournit.  Nous en avons sélectionné trois : la prédiction par mots-clés, le score de qualité de l’image et la prédiction du nombre de personnes et auquel cas leur age. L'image doit être spécifiée par son URL ou téléchargée avec un formulaire.




            1. La prédiction par mots-clés :
               L’utilisateur peut obtenir une liste de mots-clés suggérés. Il peut spécifier un nombre de mots renvoyés ou un seuil de score minimum. 



            2. Qualité de l’image : 
               L’utilisateur peut obtenir le score de qualité de sa photo. Ce service ne mesure pas à quel point une personne ou un objet sur une photo peut paraître cool ou beau. Il ne se soucie que des parties techniques telles que la luminosité, le contraste, le bruit, etc. 
               
            3. Nombre(s) personne(s) et age :
               Ce service permet de trouver des visages sur la photo de l’utilisateur et d'en estimer l'âge. La sortie est une liste des âges estimés. Il obtiendra également un score de confiance de la reconnaissance faciale. 
               
    • La source utilisée pour les images libres de droit est Pexels.com


    • La structure de l’application web :
      L’application Web est divisée en 5 pages : page d’accueil, page d’inscription,page de connexion,  pages upload + choix service, page prédictions demandées 

