import pandas as pd

df = pd.read_csv('data.csv')
print("\nThe 'title' field contains >>>{}<<< unique values.  'MURICA!\n".format(len(df['title'].unique())))
print("Disasters have occurred in {} states and territories.".format(len(df['state'].unique())))

volc = v for 