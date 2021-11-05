#Author: Nils Becker

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn import svm
from mlxtend.plotting import plot_decision_regions
from sklearn.preprocessing import MultiLabelBinarizer
import seaborn as sns
import numpy as np
import mlflow.sklearn
import matplotlib.pyplot as plt



#Getting dataset
dataset = open("SMSSpamCollection.txt")
classifiers = []
data = []
contents = dataset.readlines()
for content in contents:
    current = content.split("\t")
    classifiers.append(current[0])
    data.append(current[1])

#Split dataset into training and testing (5074*0.9 = 5016)
trainingClassifiers, trainingData = np.array(classifiers[0:5016]), np.array(data[0:5016])
testClassifiers, testData = np.array(classifiers[5016:]), np.array(data[5016:])

#Convert data to vectors and trains
cv = CountVectorizer()
features = cv.fit_transform(trainingData)
model = svm.SVC(kernel = 'linear')
model.fit(features, trainingClassifiers)

counter = 1
while True:
    try:
        #saving of model, commented out
        #mlflow.sklearn.save_model(model, "SpamClassifier" + str(counter))
        break
    except:
        counter+=1
        continue
#Test of accuracy
test = cv.transform(testData)
result = "Training Finished for {} objects. Accuracy for test set= ".format(len(trainingData)) +  str(model.score(test, testClassifiers))
test = test.toarray()
#draw decision boundaries
plt.figure(figsize=(10, 5))

#Line 52-56 from is a mix from stackoverflow, to get at least something to show up
d = {'ham': 1, 'spam': -1}
testClassifiers = np.array(list(map(lambda i: d[i], testClassifiers)))
pca = PCA(n_components = 2)
testData2 = pca.fit_transform(test)
model.fit(testData2, testClassifiers)

plot_decision_regions(testData2, testClassifiers, clf=model)
plt.title(result)
plt.show()