import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import joblib 

# veriyi oku
df = pd.read_csv("data.csv")

# özeellik ve hedef
X = df[['Height']]
y = df['Weight']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model,'linear_model.pkl') 

# örnek
print("180 boy için kilo tahmini:", model.predict([[180]])[0])


