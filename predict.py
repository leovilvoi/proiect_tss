import pandas as pd
import random
from pub import Pub

def generate_data(nr):
    data = []
    item_types = ['breakfast', 'lunch', 'dinner', 'desserts', 'drinks']
    for _ in range (nr):
        pub = Pub()
        transactions = random.randint(0, 10) # nr de tranzactii pe proba
        for _ in range(transactions):
            item = random.choice(item_types)
            quantity = random.randint(-10, 100) # includem si negativ pt edge cases
            pub.sell_item(item, quantity)

        total_sales = pub.calculate_total_sales()
        profit = pub.calculate_profit()
        data.append([transactions, item, quantity, total_sales, profit])

    return pd.DataFrame(data, columns=['tranzactii', 'produs', 'cantitate', 'vanzari', 'profit'])


dataset = generate_data(100000)
# print(dataset)

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

le = LabelEncoder()
dataset['produs'] = le.fit_transform(dataset['produs'])

# proceseaza datele pt training

X = dataset[['tranzactii', 'produs', 'cantitate', ]]
y = (dataset['profit'] > 0).astype(int) # profitabil sau nu

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

# train train train
model = DecisionTreeClassifier(random_state=6)
model.fit(X_train, y_train)

# predict on the test set
y_pred = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))

def predict_outcome(tranzactii, produs, cantitate):
    item_encoded = le.transform([produs])[0]
    sales = tranzactii * Pub().prices[produs] * cantitate
    if sales >= 1200:
        profit = model.predict([[tranzactii, item_encoded, cantitate]])
        return "Profitabil" if profit[0] == 1 else "Deloc profitabil"
    else:
        return "Deloc profitabil"
        
print(predict_outcome(5, 'breakfast', 50))
# print(predict_outcome(1, 'inexistent', 10))
