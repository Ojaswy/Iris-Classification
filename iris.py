import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


if __name__ == '__main__':
    df = pd.read_csv("iris_data.csv")
    df.columns = ['sepal length','sepal width','petal length','petal width','iris class']
    #print("Test Data: ",'\n',df)
    print("Description: ",'\n', df.describe())
    df.hist(bins=20)
    plt.show()
    data_array = df.values
    shuffled = data_array
    np.random.shuffle(shuffled)
    X_Learn = shuffled[:80][:,0:4]
    Y_learn = shuffled[:80][:,4]
    svc = SVC()
    svc.fit(X_Learn,Y_learn)
    X = shuffled[-20:][:,0:4]
    Y = shuffled[-20:][:,4]
    predictions = svc.predict(X)
    accuracy = accuracy_score(Y,predictions)

    print("Predicted Results: ",'\n', predictions)
    print("Actual Results",'\n', Y)
    print("Accuracy: ", accuracy*100,"%")
    
