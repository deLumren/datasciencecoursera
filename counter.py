import pandas as pd
df = pd.read_csv("C:\\pythonz\\transactions.csv")

df=df[['DateTime']]

df["DateTime"] = df["DateTime"].str.split(" ").str[0]
# df["date_time"] = pd.to_datetime(df["date_string"])?\



# df = df.groupby(["date_time"]).sum("TokenId").reset_index() # for example
df['count'] = df.groupby('DateTime')['DateTime'].transform('count')
df.drop_duplicates(inplace=True)

df.to_csv("counted.csv", index=False)

# dfout = df.groupby(['date_time']).count()
# dfout.reset_index(level=0, inplace=True)
# finaldf = dfout[['date_time']]
# finaldf.columns = ['Date']
# finaldf.to_csv('count.csv', index=False)

# df['date_count'] = df.date.map(df.groupby('date_time').size())
# df.created_at = created_at.str.split(' ').str[0]
