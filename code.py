# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)

# convert state column in lower case
df['state'] = df['state'].apply(lambda x: x.lower())

# Calculate the total
df["total"] = df["Jan"] + df["Feb"] + df["Mar"]

# sum of amount
sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()

# append the row
df_final = df.append(sum_row, ignore_index=True)

# Code ends here


# --------------
import requests

# Code starts here
url = 'https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations'
response = requests.get(url)

# read the html file 
df1 = pd.read_html(response.content)[0]
df1 = df1.iloc[11:, :]
df1 = df1.rename(columns=df1.iloc[0, :]).iloc[1:, :]
df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(" ", "")).astype(object)



# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = df1.set_index('United States of America')['US'].to_dict()
df_final.insert(6, 'abbr', np.nan)
df_final['abbr'] = df_final['state'].map(mapping)
print(df_final.head(15))


# Code ends here


# --------------
# Code stars here
df_mississipi = df_final[df_final['state'] == 'mississipi'].replace(np.nan, 'MS')

df_tenessee = df_final[df_final['state'] == 'tenessee'].replace(np.nan, 'TN')


# replace the final_df
df_final.replace(df_final.iloc[6], df_mississipi, inplace=True)
df_final.replace(df_final.iloc[10], df_tenessee, inplace=True)


# Code ends here


# --------------
# Code starts here
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))


# Code ends here


# --------------
# Code starts here
sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum()

df_sub_sum = pd.DataFrame(data=sum_row).T
#apply $ to the sum 
df_sub_sum = df_sub_sum.applymap(lambda x: "${:,.0f}".format(x))

# append the sum
print(formatted_df)
final_table = formatted_df.append(df_sub_sum)
print(final_table)
# rename the index
final_table = final_table.rename(index={0: "Total"})
print(final_table)


# Code ends here


# --------------
# Code starts here
df_sub['total']=df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']
plt.pie(df_sub['total'])
# Code ends here


