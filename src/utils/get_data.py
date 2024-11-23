import os
import requests

def download_file_auto(url, save_directory, filename=None):
    # Crée le répertoire si nécessaire
    os.makedirs(save_directory, exist_ok=True)
    
    # Utilise le nom par défaut si aucun nom n'est spécifié
    if filename is None:
        # Essaie de deviner le nom du fichier depuis l'en-tête HTTP "Content-Disposition"
        response = requests.head(url)
        if "Content-Disposition" in response.headers:
            filename = response.headers["Content-Disposition"].split("filename=")[-1].strip('"')
        else:
            # Utilise une valeur par défaut si le nom de fichier ne peut pas être déterminé
            filename = "etsScolaireMater.csv"

    # Chemin complet pour enregistrer le fichier
    save_path = os.path.join(save_directory, filename)
    
    try:
        # Téléchargement du fichier
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Vérifie les erreurs HTTP
        
        # Sauvegarde du fichier en blocs
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):  # Télécharge par blocs de 8 Ko
                file.write(chunk)
        
        print(f"Fichier téléchargé avec succès : {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement : {e}")


UrlList=list()
save_directory = "../../data/raw/"
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/labouref-france-departement-quarter-jobseeker/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/correspondance-code-insee-code-postal/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
UrlList.append("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/base-cc-caract-emploi-2012-arm/exports/csv?lang=fr&timezone=Europe%2FBerlin&use_labels=true&delimiter=%3B")
for url in UrlList:
    download_file_auto(url, save_directory)











