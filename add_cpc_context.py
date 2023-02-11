import pandas as pd


train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
cpc_df = pd.read_csv('titles.csv')

train_df['context_text'] = train_df['context'].map(cpc_df.set_index('code')['title']).str.lower()
test_df['context_text'] = test_df['context'].map(cpc_df.set_index('code')['title']).str.lower()

train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)
