import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.model_selection import train_test_split
import joblib 

# 1. Veriyi oku
df = pd.read_csv("data.csv")

# 2. Özellik ve hedef
X = df[['Height']]
y = df['Weight']

# 3. Eğitim/Test böl
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model,'linear_model.pkl') 

# 5. Örnek tahmin
print("180 boy için kilo tahmini:", model.predict([[180]])[0])


