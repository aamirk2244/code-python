import pandas as pd

filename = 'transactions'
df = pd.read_csv(filename + '.csv')
df['timestamp'] = pd.to_datetime(df['timestamp']).sort_values()
suffix = 1
row_length = 10000000         # 1 carod (10 million rows)
for i in range(len(df)):
   
    if i % row_length == 0:
        df[i:i+row_length].to_csv(f"processed/{filename}_{suffix}.csv", sep ='|', index=False, index_label=False)
        suffix += 1
