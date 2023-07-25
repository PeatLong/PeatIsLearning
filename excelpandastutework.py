import pandas as pd

df = pd.read_csv('Pensforwards9293on.csv')
df2 = pd.read_csv('DucksF9293.csv')

con_df = pd.concat([df, df2])

df3 = con_df[con_df.duplicated('Player')]

print(df3)
