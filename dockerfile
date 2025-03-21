# Utilisation d'une image Python officielle comme base
FROM python:3.9-slim

# Création et définition du répertoire de travail
WORKDIR /app

# Copie du code source dans le conteneur
COPY ./app /app

# Exposition du port sur lequel le serveur s'exécute
EXPOSE 8000

# Commande pour démarrer le serveur
CMD ["python", "server.py"]