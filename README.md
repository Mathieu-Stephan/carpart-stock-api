
# Gestion des Stocks - CarPart API

**Université de Bretagne Sud (UBS) - I.U.T de Vannes**  
**Département Informatique - BUT 3e année**  
**Encadré par :** Matthieu Le Lain, Xavier Roirand  
**TP 1 - R5.A.09**

---

## Objectif du TP

L'entreprise CarPart, spécialisée dans la vente de pièces détachées pour voitures, souhaite moderniser son parc informatique pour se préparer à une transition vers le cloud. Votre mission est de développer une API web de gestion des stocks qui servira de base pour les développements futurs.

### Spécifications

1. **Création d’une API web de gestion des stocks.**

L'API devra permettre de gérer les stocks de produits avec les fonctionnalités suivantes :

- **Ajouter un produit** (nom, description, quantité, prix)
- **Modifier un produit** (modifier le descriptif, ajouter ou réduire la quantité)
- **Supprimer un produit**
- **Accéder au descriptif d’un produit** ainsi qu’à la quantité restante

#### Contraintes techniques :

- **Technologie** : L'API doit être développée avec **FastAPI** (version Python > 3.9)
- **Base de données** : Utilisation de **MongoDB** pour stocker les informations sur les produits
- **Format de réponse** : Les retours devront être effectués en **JSON**

Pour plus d'informations sur FastAPI, vous pouvez consulter la documentation officielle :  
[https://fastapi.tiangolo.com/tutorial/first-steps/](https://fastapi.tiangolo.com/tutorial/first-steps/)

2. **Création des DockerFile**

L'entreprise souhaite également que vous fournissiez deux Dockerfiles pour faciliter le déploiement :

- **Dockerfile pour l'application API**
- **Dockerfile pour la base de données MongoDB**

Ces Dockerfiles devront être lancés séparément et manuellement à ce stade.

---

### Structure du projet

- `main.py` : Contient l'implémentation de l'API FastAPI
- `crud.py` : Fonctions pour ajouter, modifier, supprimer et lire les produits
- `Dockerfile` : Pour construire l'image de l'API
- `docker-compose.yml` : Permet de lancer l'application API et MongoDB ensemble
- `requirements.txt` : Dépendances Python pour l'API
- `.dockerignore` : Fichiers à exclure lors de la construction Docker
- `.github/workflows/docker-publish.yml` : Workflow GitHub Actions pour déployer les conteneurs sur Docker Hub

---

### Instructions pour lancer l'application

1. **Construire et lancer la base de données MongoDB :**

   Depuis le répertoire `mongo`, exécutez la commande suivante pour construire et démarrer le conteneur MongoDB :

   ```bash
   docker build -t mongo .
   docker run -d -p 27017:27017 --name mongodb mongo
   ```

2. **Construire et lancer l'API FastAPI :**

   Depuis le répertoire racine du projet, exécutez les commandes suivantes :

   ```bash
   docker build -t carpart_api .
   docker run -d -p 8000:8000 --name carpart_api --link mongodb:mongo carpart_api
   ```

3. **Accéder à la documentation interactive :**

   Une fois les deux conteneurs démarrés, vous pouvez accéder à la documentation interactive de l'API via Swagger à l'adresse suivante :  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Ressources supplémentaires

- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Documentation Docker](https://docs.docker.com/)
- [Documentation MongoDB](https://www.mongodb.com/docs/)

---

**Auteur :** Mathieu Stephan  
**Date :** 2024
```
