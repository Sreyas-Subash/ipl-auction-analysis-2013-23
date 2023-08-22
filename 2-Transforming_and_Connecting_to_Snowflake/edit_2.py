import pandas as pd

team_df = pd.read_csv('data/ipl_team_13-23.csv')
player_df = pd.read_csv('data/ipl_player_13-23.csv')

# print(player_df[['id','price_paid(in rupee)']])

df = player_df.groupby('id')['price_paid(in rupee)'].sum()
print(df)
# print(type(df))

res = pd.merge(team_df,df,how='outer',on='id')

print(type(res))

res.rename(columns={'price_paid(in rupee)':'total_spent'},inplace=True)
print(res)

res['total_budget'] = res['remaining_fund(in rupee)'] + res['total_spent']

res.to_csv('ipl_team_13-23.csv', index=False)