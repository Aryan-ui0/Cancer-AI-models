import joblib

model = joblib.load("lung_model.pkl")

sample = [[14,0,1,0,1,1]]  

prob = model.predict_proba(sample)[0][1]

print("Risk:", round(prob * 100, 2), "%")