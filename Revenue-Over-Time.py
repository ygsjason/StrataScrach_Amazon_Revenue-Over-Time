# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
df = amazon_purchases
df['year_month'] = df['created_at'].dt.strftime('%Y-%m')
df1 = df[df['purchase_amt'] > 0]

df2 = df1.pivot_table(columns = 'year_month', values = 'purchase_amt', aggfunc = 'sum').melt()

df2['3-month'] = df2['value'].rolling(3).mean()

#rolling window calculation example
df_ex = pd.DataFrame({'B' : [0.0, 1.0, 2.0, np.nan, 4.0]})

#Rolling sum with a window length of 2 observations.
df_ex['B'].rolling(2).mean()

#Rolling sum with a window length of 2 observations, but only needs a minimum of 1 observation to calculate a value.
df_ex['B'].rolling(2, min_periods = 1).mean()
