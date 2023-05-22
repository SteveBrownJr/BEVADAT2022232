import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree

#1.1
data = pd.read_csv("iris.csv")
#1.2
for column in data:
    data=data.rename(columns={column:column.replace('.','_')})
#1.3
data.dropna()

#1.4
for x in data['variety'].unique():
    print(x)

#1.5
#print(data.corr(method=))
    
#1.7
data=data.drop(columns=['sepal_width'])

#1.8
fig1,ax1 = plt.subplots()
ax1.pie(data['variety'].value_counts().values,labels = data['variety'].value_counts().index)

#1.6
def VarietyChange(x):
    if  'Setosa' in x:
        return 0
    if 'Versicolor' in x:
        return 1
    if 'Virginica' in x:
        return 2
    return 0
data['variety'] = data['variety'].apply(VarietyChange)

#1.9
def getcolors():
    from random import randint

    color = []
    n = 3
    for i in range(n):
        color.append('#%06X' % randint(0, 0xFFFFFF))
    colors = []
    n = 149
    for i in range(n):
        x = data['variety'][n]
        colors.append(color[x])
    colors.append(color[0])
    return colors
colors=getcolors()    
fig2,ax2 = plt.subplots()
ax2.scatter(data['petal_length'],data['petal_width'],data['variety'],color=colors)


#2.1
train_data = pd.DataFrame(data, columns=['sepal_length', 'petal_length', 'petal_width'])
target_data = pd.DataFrame(data, columns=['variety'])

#2.2
Train_data, Test_data, Train_target, Test_target = train_test_split(train_data, target_data, train_size=0.4, random_state=42)
#3.1
model = tree.DecisionTreeClassifier()
model = model.fit(Train_data,Train_target)
#3.2
predicted_y = model.predict(Test_data.values).reshape(-1,1)
egyezes = 0
for i in range(len(Test_target.values)):
    if Test_target.values[i] == predicted_y[i]:
        egyezes+=1

egyezes = (float) (egyezes) / len(Test_target.values)
print(f'Pontossag {egyezes}')

_ = tree.plot_tree(model, 
                   feature_names=['sepal_length','petal_length','petal_width'],  
                   class_names=['Setosa','Versicolor','Virginica'],
                   filled=True)
plt.show()