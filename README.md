## Exécution avec Docker

Construire l’image :

```bash
docker build -t dimred .

Lancer le conteneur :

docker run --rm dimred

Le conteneur exécute automatiquement le script de comparaison des méthodes de réduction de dimensionnalité (PCA et t-SNE).

Résultat attendu :

Trustworthiness PCA : 0.9363
Trustworthiness t-SNE : 0.97

Ces résultats montrent que la méthode t-SNE préserve mieux les voisinages locaux que la PCA sur ce jeu de données.

Si l’image DockerHub n’est pas disponible, les résultats peuvent être reproduits en construisant l’image avec le Dockerfile fourni et en exécutant les commandes ci-dessus.


---

Ensuite dans Git Bash :

```bash
git add README.md
git commit -m "Ajout instructions Docker"
git push
