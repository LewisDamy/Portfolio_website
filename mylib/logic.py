import pandas as pd
import sqlite3

########    DATA CODE    ########
data = {
        'product_name': ['Computer', 'Tablet', 'Monitor', 'Printer'],
        'price': [900, 300, 450, 150]
        }

df = pd.DataFrame(data, columns= ['product_name', 'price'])
print(df)

########    SAVING TO DB    ########

# my_db = sqlite3.connect('myDB')
# c = my_db.cursor()

# c.execute('CREATE TABLE IF NOT EXISTS ucs (nome_uc, categoria, CH_total, pre_requisitos)')

# df.to_sql('rawData', my_db, if_exists='replace', index=False)
# c.execute('''SELECT * FROM rawData''')

# for row in c.fetchall():
#     print(row)
