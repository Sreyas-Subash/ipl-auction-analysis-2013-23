import pandas as pd

df_team = pd.read_csv('data/ipl_team_13-23.csv')
df_player = pd.read_csv('data/ipl_player_13-23.csv')

df_team.season = df_team.season.astype('str')
df_player.season = df_player.season.astype('str')
# print(df_team.dtypes)
# print(df_player.dtypes)

df = df_team.loc[:,['index','season','team_name']].copy()

# print(df)

df_dict = df.set_index('index').T.to_dict('list')

print(df_dict)

for i,row in df_player.iterrows():
    for k in df_dict:
        if (df_dict[k][0] == row.season) and (df_dict[k][1] == row.team_name):
            df_player.loc[i, 'index'] = k
            break
df_player.season = df_player.season.astype('int64')
print(df_player.dtypes)
df_player.to_csv('ipl_player_13-23.csv')