# Utilisation d'une image Python officielle
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY /user_service/requirements.txt /app/

# Installer venv pour créer un environnement virtuel
RUN apt-get update && apt-get install -y python3-venv && apt-get clean

# Créer un environnement virtuel
RUN python -m venv venv

# Installer les dépendances dans l'environnement virtuel
RUN ./venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copier tout le code dans le conteneur
COPY . /app/

# Définir la variable d'environnement pour Flask
ENV FLASK_APP=run.py

# Exposer le port 5001 pour accéder à l'application
EXPOSE 5001

# Commande pour démarrer l'application
CMD ["./venv/bin/python", "user_service/run.py"]