#피처임포턴스가 0인 컬럼들을 제거하여 데이터셋을 재구성후 Desisiontree 모델을 재구성
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_iris,load_breast_cancer,load_wine,load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = load_diabetes()
print(dataset.feature_names)
x_train,x_test,y_train,y_test = train_test_split(dataset.data,dataset.target,train_size = 0.8, random_state = 33)
model1 = DecisionTreeRegressor(max_depth = 5)
model1.fit(x_train, y_train)
acc = model1.score(x_test,y_test)

print(model1.feature_importances_)
print('acc before delete columns: ', acc)

f_importance = model1.feature_importances_
f_data = []
f_columns =[]
for i in range(len(f_importance)):
    if f_importance[i] !=0:
        f_data.append(dataset.data[:,i])
        f_columns.append(dataset.feature_names[i])

f_data = np.array(f_data)
f_data = np.transpose(f_data)

x_train2, x_test2, y_train2, y_test2 = train_test_split(
    f_data,dataset.target,train_size=0.8,random_state=44)


model2 = DecisionTreeRegressor(max_depth=4)
model2.fit(x_train2,y_train2)

acc2 = model2.score(x_test2,y_test2)

print(model2.feature_importances_)
print("acc delete 0 columns:",acc2)

def plot_feature_importances_dataset(model):
    n_features = f_data.shape[1]
    plt.barh(np.arange(n_features), model.feature_importances_,align='center')
    plt.yticks(np.arange(n_features),f_columns)
    plt.xlabel("Feature Importances")
    plt.ylabel("Features")
    plt.ylim(-1,n_features)

plot_feature_importances_dataset(model2)
plt.show()

# [3.87884504e-02 2.10240926e-03 3.11664627e-01 5.60347647e-02
#  1.11925454e-03 8.14312698e-02 1.88802823e-04 9.13699855e-03
#  4.46537416e-01 5.29960076e-02]
# acc before delete columns:  0.3544016887800495
# [0.03097671 0.         0.31926815 0.         0.01831924 0.06084404
#  0.         0.         0.57059185 0.        ]
# acc delete 0 columns: 0.31490122539834386

#컬럼삭제후 오히려 나빠짐...