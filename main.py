import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finance_liquor_sales.csv")

zc = df.groupby(['zip_code', 'item_description']).sum().sort_values("bottles_sold", ascending=False)
item_description = zc.index.get_level_values('item_description')

plt.bar(item_description, zc['bottles_sold'])
plt.title('Bottles Sold')
plt.xlabel('item_description')
plt.xticks(rotation=90)
plt.ylabel('Bottles Sold')
plt.show()


