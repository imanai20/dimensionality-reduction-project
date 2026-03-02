import pandas as pd
from sklearn.manifold import trustworthiness
from sklearn.preprocessing import StandardScaler

# charger données originales
df = pd.read_csv("data/city_lifestyle_dataset.csv")

X = df.select_dtypes(include=["number"]).copy()
X = X.fillna(X.median(numeric_only=True))

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# charger projections 2D
pca_2d = pd.read_csv("outputs/pca_2d.csv").values
tsne_2d = pd.read_csv("outputs/tsne_2d.csv").values

# calcul trustworthiness
tw_pca = trustworthiness(X_scaled, pca_2d, n_neighbors=10)
tw_tsne = trustworthiness(X_scaled, tsne_2d, n_neighbors=10)

print("Trustworthiness PCA :", round(tw_pca, 4))
print("Trustworthiness t-SNE :", round(tw_tsne, 4))