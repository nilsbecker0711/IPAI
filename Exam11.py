
import gensim
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import numpy as np

words = [['space'], ['languages'], ['geography'], ['easter'], ['cryptocurrency'], ['chemistry'], ['Internet'], ['social networks'], ['ancient Rome'], ['ships'], ['electricity'], ['ancient world'], ['geology'], ['religion'], ['travel'], ['memes'], ['education'], ['education'], ['vaccinations'], ['computers'], ['flu'], ['google'], ['browsers'], ['games'], ['easter eggs'], ['search engines'], ['English'], ['ancient Greece'], ['health'], ['smartphones'], ['psychology'], ['psychotherapy']]
print(len(words))
model = gensim.models.Word2Vec(words, min_count=1)
#holds all similarities for each word with every other word
X =np.array([[model.wv.similarity(w1[0],w2[0]) for w1 in words]for w2 in words])


score = -1
clusters = 0
for i in range(3,21):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(X)
    current = silhouette_score(X, kmeans.labels_, metric='euclidean')
    if current > score:
        score = current
        clusters = i

kmeans = KMeans(n_clusters = clusters, random_state=0).fit(X)
centroids = kmeans.cluster_centers_
print(centroids)

