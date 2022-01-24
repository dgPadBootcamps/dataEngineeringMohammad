import pandas as pd

df = pd.read_json("C:/Users/MOHD/Documents/PythonProjects/dgPad2/data_saving/tweets_lebanon_2021-11-25.json")

df["Username"] = df.User.apply(lambda x: x['UserName'])

top_user = df.groupby(['Username']).favorite_count.sum().sort_values(ascending=False)
print(top_user)
print(df.loc[df.Username == str(df.Username).find("a")])
