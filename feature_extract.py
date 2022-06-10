import pandas as pd

df = pd.read_csv("/home/devuk/code/real_estate_data/real_estate.csv")

df_temp = df.drop(['address1', 'address2', 'deposit_rent', 'address3',
                   'type', 'latitude', 'longitude', 'nearest_cvs',
                   'nearest_station', 'nearest_hospital', 'jeonse_check',
                   'rent_check', 'monthly_payment'], axis = 1)

df_temp.to_csv("/home/devuk/code/real_estate_data/feature_target.csv", index = False)