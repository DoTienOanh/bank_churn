import pickle as pickle
import pandas as pd
model, encoded_test, scaler = pickle.load(open("bank_churn_prediction.pkl","rb"))
new_customer_original =pd.DataFrame( [
  480,
  'France',
  'Male',
  40,
  5,
  100000,
  1,
  1,
  1
])
df_encoded_test = pd.concat([df_test.drop(columns=categorical_vars), encoded_test], axis =1)
new_customer = [[0.472, 0.067568, 0.2, 0.000000, 0.333333, 0.0, 1.0, 0.804903, 1.0]]
result = model.predict(new_customer)
print(result)
