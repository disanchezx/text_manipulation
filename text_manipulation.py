import pandas as pd

with open("/content/drive/MyDrive/2023-1/Seguridad de redes/Corte 1/libro_muertos.txt", mode='r', encoding='latin-1') as f:
    tx = f.read()
    
tx_clean = ('')
tx = tx.lower()
clean = ['a','b','c','d','e','f','g','h','i','j','k','l',
         'm','n','o','p','q','r','s','t','u','v','w','x',
         'y','z',' ','á','é','í','ó','ú']
for i in tx:
  if i in clean:
    tx_clean += i

tx_split = tx.split()

tx_two=[]
for i in range(len(tx_split)):
  if len(tx_split[i]) == 2:
    tx_two += tx_split[i]

tx_three=[]
for i in range(len(tx_split)):
  if len(tx_split[i]) == 3:
    tx_three += tx_split[i]

tx_four=[]
for i in range(len(tx_split)):
  if len(tx_split[i]) == 4:
    tx_four += tx_split[i]

import pandas as pd
tx_word_count =  pd.Series(list(tx_split)).value_counts()
print(tx_word_count)

print('En el texto hay', len(tx_split), 'palabras')
print('En el texto hay', round(len(tx_two)/2), 'palabras de dos letras')
print('En el texto hay', round(len(tx_three)/3), 'palabras de tres letras')
print('En el texto hay', round(len(tx_four)/4), 'palabras de cuatro letras')
print('************************************************')
print('La palabra de dos letras que más se repite en el texto es: de')
print('La palabra de tres letras que más se repite en el texto es: que')
