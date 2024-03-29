from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_iris,load_breast_cancer,load_wine
from sklearn.model_selection import train_test_split

dataset = load_wine()
x_train, x_test, y_train, y_test = train_test_split(
    dataset.data,dataset.target,train_size=0.8,random_state=44)

model = DecisionTreeRegressor(max_depth=4)

model.fit(x_train,y_train)

acc = model.score(x_test,y_test)

print(model.feature_importances_)
print("acc:",acc)

#[0.00625261 0.         0.01606923 0.97767816]
#acc: 0.8993288590604027

import matplotlib.pyplot as plt
import numpy as np

def plot_feature_importances_dataset(model):
    n_features = dataset.data.shape[1]
    plt.barh(np.arange(n_features), model.feature_importances_,align='center')
    plt.yticks(np.arange(n_features),dataset.feature_names)
    plt.xlabel("Feature Importances")
    plt.ylabel("Features")
    plt.ylim(-1,n_features)

plot_feature_importances_dataset(model)
plt.show()