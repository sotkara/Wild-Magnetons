import pandas as pd
from IPython.display import display

df = pd.read_csv('dscovr_data_2018.txt', delim_whitespace=True)
output = df.loc[df['field'] <= -5]
entries_num = len(df)
output_num = len(output)

perc = output_num/entries_num

print(perc)

#output.to_csv('dscovr_data_jan.csv', index=False)


