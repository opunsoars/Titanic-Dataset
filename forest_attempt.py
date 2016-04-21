import pandas as pd

train_df = pd.read_csv(r'C:\Users\Vinay\PycharmProjects\Titanic-from-Kaggle\Data\train.csv', header=0)# Load the train file into a dataframe
train_df.describe()
train_df.dtypes
train_df.head(3)