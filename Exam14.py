import streamlit as st
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


eps = st.sidebar.slider("Choose max distance for neighbourhood (eps)", 0.4, 1.5, 0.5, 0.1)
minPts = st.sidebar.slider("Choose min amount of neighbors for neighbourhood", 3,10,5, 1)
header = st.container()


#generate Dataset
@st.cache 
def generateData():
    '''
    Generates a dataset 
    @st.cache -> no new dataset with every streamlit rerun
    '''
    X,y = make_blobs(n_samples = 1000, n_features = 2)
    return X,y

X,y = generateData()
markers = ['ro', 'b*', 'g+', 'co', 'm*', 'y+']
dbscan = DBSCAN(eps = eps, min_samples=minPts).fit(X)
plt.figure(figsize=(10, 8))
fig, ax = plt.subplots()
for p, c in zip(X, dbscan.labels_):
    ax.plot(p[1:], p[:1], markers[c])

#streamlit
with header:
    st.title("Clusters by DBScan")
    st.pyplot(fig)

st.button("Re-run")