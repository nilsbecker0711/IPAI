import spacy
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

distances = np.zeros(shape=(12,12))
cities = []
def evaluate(input):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(input)
    tokens = [token for token in doc]
    
    updateCities(tokens)
    for token in tokens:
        if token.dep_ == "acomp":
            if token.text =="equidistant":
                updateDistances(tokens, 2)
            else:
                #close
                updateDistances(tokens, 0)
        elif token.dep_ == "advmod":
            #far from
            updateDistances(tokens, 1)

def updateCities(tokens):
    for token in tokens:
        if token.dep_== "nsubj" or token.dep_=="pobj" or token.dep_ == "conj":
            if token.text not in cities:
                cities.append(token.text)

def updateDistances(tokens, index):
    currentCities =[]
    for token in tokens:
        if  token.dep_== "nsubj":
            currentCities.append(token.text)
        if token.dep_ == "pobj":
            currentCities.append(token.text)
        if token.dep_ == "conj":
            currentCities.append(token.text)
    #close
    if index == 0:
        i = cities.index(currentCities[0])
        j = cities.index(currentCities[1])
        distances[i][j] = 1
        distances[j][i] = 1   
    #far
    if index == 1:
        i = cities.index(currentCities[0])
        j = cities.index(currentCities[1])
        distances[i][j] = 10
        distances[j][i] = 10  
    #equidistant
    if index == 2:
        distance = distances[cities.index(currentCities[1])][cities.index(currentCities[2])]/2
        #print(currentCities[1], currentCities[2], distance)
        i = cities.index(currentCities[0])
        j = cities.index(currentCities[1])
        distances[i][j] = distance
        distances[j][i] = distance
        j = cities.index(currentCities[2])
        distances[i][j] = distance
        distances[j][i] = distance



statements = ["Moscow is far from Voronezh.","Kazan is far from Voronezh.","Kazan is far from Moscow.","Innopolis is close to Kazan.","Dolgoprudnyy is close to Moscow.","NizhniyNovgorod is equidistant to Moscow and Kazan.","Bor is close to NizhniyNovgorod.","Tula is equidistant to Moscow and Voronezh.","SaintPetersburg is far from Moscow.","Bologoe is equidistant to Moscow and SaintPetersburg.","Vyborg is close SaintPetersburg.","Zaymishche is equidistant to Innopolis and Kazan."]

for statement in statements:
    evaluate(statement)

print(cities)
print(distances)

g = nx.Graph()

g.add_nodes_from(cities)
edges = []
weights = []
for i in range(len(distances)):
    for j in range(len(distances[i])):
        if distances[i][j] != 0:
            edges.append((i,j))
            weights.append(distances[i][j])
g.add_edge(1,2)
nx.draw(g)
plt.show()

