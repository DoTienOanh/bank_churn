import pickle as pickle
import pandas as pd
model = pickle.load(open("bank_churn_prediction.pkl","rb"))
new_customer = [[
