Projet de Prédiction de Demande de Vélos (Bike Sharing)📝 Présentation du ProjetLes systèmes de vélos en libre-service, déployés aujourd'hui dans plus de 500 villes, agissent comme de véritables capteurs virtuels de la mobilité urbaine grâce à l'enregistrement précis des trajets.C'est dans ce contexte que nous avons choisi d'analyser le Bike Sharing Dataset, issu du UCI Machine Learning Repository. Ce jeu de données regroupe l'historique des locations de vélos à Washington D.C., enrichi de données contextuelles exogènes essentielles telles que les conditions météorologiques (température, humidité) et les informations calendaires (jours fériés, vacances).Dans ce projet, nous abordons une problématique de régression supervisée sur série temporelle visant à anticiper les flux de déplacements. L'objectif principal est de prédire la demande horaire de vélos (variable cible cnt) à un horizon futur défini via des modèles de Machine Learning (XGBoost) et de Deep Learning (LSTM).📂 Arborescence du ProjetVoici la structure des fichiers du projet :Plaintext.
├── data/
│   ├── for_models/     # Données prêtes pour l'entraînement
│   ├── processed/      # Données nettoyées et transformées
│   └── raw/            # Données sources (day.csv, hour.csv)
├── docs/               # Documentation et rapport de projet
├── img/                # Images et schémas pour le notebook/README
├── notebook/           # Notebooks Jupyter (Analyse exploratoire et modèles)
├── src/                # Scripts sources Python
│   └── utils.py        # Fonctions utilitaires (Visualisation, calculs)
├── .gitignore          # Fichiers à exclure du versioning
├── pyproject.toml      # Configuration du projet et dépendances
├── README.md           # Documentation principale
└── uv.lock             # Fichier de verrouillage des dépendances (gestionnaire uv)
📊 Description des VariablesLe jeu de données hour.csv contient les colonnes suivantes :VariableDescriptiondtedayDate de l'observationseasonSaison (1: Printemps, 2: Été, 3: Automne, 4: Hiver)hrHeure (0 à 23)holidaySi le jour est férié (1) ou non (0)weathersitÉtat météo (1: Clair, 2: Brume, 3: Pluie/Neige légère, 4: Orage/Neige forte)temp / atempTempérature réelle / ressentie (normalisée)humHumidité (normalisée)windspeedVitesse du vent (normalisée)cntCible : Nombre total de locations (casual + registered)🚀 Installation et Utilisation1. Cloner le projetOuvrez votre terminal et exécutez les commandes suivantes :Bashgit clone https://github.com/votre-utilisateur/Projet_MLDL_Roland_Lina_Maeva.git
cd Projet_MLDL_Roland_Lina_Maeva
2. Configuration de l'environnementLe projet utilise uv pour une gestion rapide des dépendances, mais vous pouvez utiliser pip :Via pip :Bashpython -m venv .venv
source .venv/Scripts/activate  # Sur Windows: .venv\Scripts\activate
pip install -r requirements.txt
Via uv (recommandé) :Bashuv sync
3. ExécutionLancez le notebook pour visualiser l'analyse :Bashjupyter notebook notebook/modele_v1.ipynb
