Les systèmes de vélos en libre-service, déployés aujourd'hui dans plus de 500 villes, agissent comme de véritables capteurs virtuels de la mobilité urbaine grâce à l'enregistrement précis des trajets.

C'est dans ce contexte que nous avons choisi d'analyser le **Bike Sharing Dataset**, issu du *UCI Machine Learning Repository*. Ce jeu de données regroupe l'historique des locations de vélos à Washington D.C., enrichi de **données contextuelles exogènes** essentielles telles que les conditions météorologiques (température, humidité) et les informations calendaires (jours fériés, vacances).

Dans ce projet, nous abordons une problématique de **régression supervisée sur série temporelle** visant à anticiper les flux de déplacements.

L'objectif principal est de prédire la demande horaire de vélos (variable cible `cnt`) à un horizon futur défini. Pour y parvenir, nous mettrons en œuvre et comparerons des algorithmes de **Machine Learning** (ex: XGBoost) et de **Deep Learning** (ex: LSTM). Cette démarche nous permettra de démontrer l'apport prédictif spécifique des variables contextuelles sur la performance globale des modèles.
