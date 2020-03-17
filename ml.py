import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split



corona = pd.read_csv("data.csv")

X = corona[['DayNumber']]
Y = corona[['Cases Till Date']]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=29)


from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,Y_train)

predictions = lm.predict(X_test)

# print(predictions)
# print(X_test)
# print(Y_test.to_numpy())
# print(X_test.to_numpy())
# print(Y,Y_test[0])
# print(predictions)

Y = Y.to_numpy()
Y = [i[0] for i in Y]

X = X.to_numpy()
X = [i[0] for i in X]

# print(Y)
acc = []
ctr=0
for i in X_test.to_numpy():
    acc+=[100 - abs(predictions[ctr][0]-Y[i[0]-1])/Y[i[0]-1] * 100]
    ctr+=1
    
# print(sum(acc)/len(acc))
    
# if sum(acc)/len(acc) > 71:
#     print(rs, sum(acc)/len(acc))
    # break

# exit(0)


population = 1000000

for i in range(10**10):
    # print(i)
    x = lm.predict([[i]])
    print(i,x[0][0]/population * 100)

    if x[0][0] >= population:
        print("Print asn is ", i)
        break


