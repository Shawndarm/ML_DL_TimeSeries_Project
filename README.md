# 🚲 Projet de Prédiction de la Demande de Vélos (Bike Sharing)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.5+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.2+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Plotly](https://img.shields.io/badge/Plotly-5.x-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-blue?style=for-the-badge)](https://xgboost.readthedocs.io/)

## 📝 Présentation du Projet
Les systèmes de vélos en libre-service, déployés aujourd'hui dans plus de 500 villes, agissent comme de véritables capteurs virtuels de la mobilité urbaine grâce à l'enregistrement précis des trajets. 

C'est dans ce contexte que nous avons choisi d'analyser le **Bike Sharing Dataset**, issu du *UCI Machine Learning Repository*. Ce jeu de données regroupe l'historique des locations de vélos à Washington D.C. entre 2011 et 2012, enrichi de **données contextuelles exogènes** essentielles telles que les conditions météorologiques et les informations calendaires.

### Objectifs
* Aborder une problématique de **régression supervisée sur série temporelle**.
* Prédire la demande horaire de vélos (variable cible `cnt`).
* Comparer des algorithmes de **Machine Learning** (ex: XGBoost) et de **Deep Learning** (ex: LSTM).
* Démontrer l'apport prédictif des variables contextuelles (météo, jours fériés).

## 📊 Source des Données
Le jeu de données provient du système **Capital Bikeshare** (Washington D.C.) et les informations météo de **Freemeteo**.
* **Lien UCI Repository :** [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset)
* **Données sources :** [Capital Bikeshare System Data](http://capitalbikeshare.com/system-data)

## 📂 Arborescence du Projet
D'après la structure du répertoire `Projet_MLDL_Roland_Lina_Maeva` :

```text
.
├── .venv/                  # Environnement virtuel Python
├── data/                   # Dossier des données
│   ├── for_models/         # Données préparées pour l'entraînement
│   ├── processed/          # Données après nettoyage et feature engineering
│   └── raw/                # Données brutes (day.csv, hour.csv)
├── docs/                   # Documentation du projet
│   ├── Projet ML-Sorbonne_MOSEF.docx
│   └── Readme.txt
├── img/                    # Graphiques et illustrations
├── notebook/               # Notebooks Jupyter
│   ├── deleted_codes.ipynb
│   ├── modele_v1.ipynb     # Notebook principal
│   └── washington_weather_2013_Q1.csv
├── src/                    # Scripts sources
│   ├── __pycache__/
│   └── utils.py            # Fonctions utilitaires (visualisation, etc.)
├── .gitignore              # Fichiers ignorés par Git
├── .python-version         # Version de Python utilisée
├── LICENSE                 # Licence du projet
├── pyproject.toml          # Configuration des dépendances
├── README.md               # Ce fichier
└── uv.lock                 # Lockfile du gestionnaire de paquets

