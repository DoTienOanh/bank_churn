import pickle as pickle
import pandas as pd
model = pickle.load(open("bank_churn_prediction.pkl","rb"))
new_customer = [[0.472, 0.067568, 0.2, 0.000000, 0.333333, 0.0, 1.0, 0.804903, 1.0]]
result = model.predict(new_customer)
print(result)
