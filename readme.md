# Projet Docker Python Minimaliste

Mettre en place une application simple avec Docker qui utilise uniquement les bibliothèques 
standards de Python pour créer un serveur HTTP minimaliste.

## Structure du projet

```
basic-docker-project/
├── app/
│   ├── server.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Prérequis

- [Docker]
- [Docker Compose]
- Python 3.x 

## Description des fichiers

- `server.py`: Contient le code du serveur HTTP minimaliste utilisant le module `http.server` de Python.
- `Dockerfile`: Définit comment l'image Docker doit être construite.
- `docker-compose.yml`: Facilite l'orchestration du conteneur Docker.

## Exécution du projet

### Option 1: Avec Docker Compose (recommandé)

1. avoir docker et docker compose
2. Dans le répertoire racine du projet, exécutez:

```bash
docker-compose up
```

3. Accédez à l'application dans votre navigateur à l'adresse [http://localhost:8000](http://localhost:8000).
4. Pour arrêter l'application, appuyez sur `Ctrl+C` dans le terminal où Docker Compose s'exécute, ou exécutez:

```bash
docker-compose down
```

### Option 2: Avec Docker sans Docker Compose

1. Construction de l'image Docker:

```bash
docker build -t python-http-server .
```

2. Exécution d'un conteneur à partir de l'image:

--il se peut qu'il ait un containeur qui utilise le poet ,faudra d'abord l'arreter
```bash
docker run -p 8000:8000 python-http-server
```

3. Se connecter à DockerHub
Avant de pousser une image, vous devez vous authentifier auprès de DockerHub :
```bash 
docker login
```

3. Tagger l'image pour DockerHub en choisissant la version
```bash
docker tag python-http-server majulde/python-http-server:latest
```
4. Pousser l'image vers DockerHub
```bash
docker push majulde/python-http-server:latest
```
Utiliser l'image depuis DockerHub
```bash 
docker pull majulde/python-http-server:latest