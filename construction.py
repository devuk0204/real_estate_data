import pandas as pd

df = pd.read_csv("/home/devuk/code/real_estate_data/feature_target.csv")
df['new_construction'] = 0
df_temp = df[['dedicated_area', 'deposit', 'rent', 'new_construction', 'cvs_distance', 'station_distance', 'hospital_distance', 'suitability']]

for i in range(len(df)) :
    if df.year_of_construction[i] >= 2010 :
        df_temp.new_construction[i] = 1
    else :
        df_temp.new_construction[i] = 0


df_temp.to_csv("/home/devuk/code/real_estate_data/feature_target.csv", index = False)