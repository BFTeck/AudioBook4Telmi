import os
import shutil

def organiser_mp3(repertoire):
    # Liste tous les fichiers dans le répertoire
    fichiers = [f for f in os.listdir(repertoire) if f.endswith('.mp3')]

    for fichier in fichiers:
        # Extrait le numéro et le titre du fichier
        try:
            numero, titre = fichier.split('-', 1)
            numero = int(numero.strip())
            titre = titre.strip().rsplit('.', 1)[0]  # Enlève l'extension .mp3
        except ValueError:
            print(f"Fichier {fichier} ne correspond pas au format attendu.")
            continue

        # Détermine la dizaine et l'unité
        dizaine = (numero // 10) * 10
        unite = numero % 10

        # Crée les répertoires nécessaires
        repertoire_dizaine = os.path.join(repertoire, str(dizaine))
        repertoire_unite = os.path.join(repertoire_dizaine, str(unite))

        os.makedirs(repertoire_unite, exist_ok=True)

        # Crée le fichier texte avec le titre
        fichier_texte = os.path.join(repertoire_unite, 'titre.txt')
        with open(fichier_texte, 'w') as f:
            f.write(titre)

        # Déplace et renomme le fichier MP3
        nouveau_fichier_mp3 = os.path.join(repertoire_unite, 'story.mp3')
        shutil.move(os.path.join(repertoire, fichier), nouveau_fichier_mp3)

    print("Organisation des fichiers MP3 terminée.")

# Exemple d'utilisation
# Remplacez 'votre_repertoire' par le chemin de votre répertoire contenant les fichiers MP3
organiser_mp3('votre_repertoire')
