products = ['skovodka', 'skovorodki', 'chainick', 'kniga', 'shkag', 'sigara', 'pampersi', 'istoria']
skovorodki = [] 
#представим, что у нас этот список неизмеримо больше (к примеру, размером хотя бы с половину товаров Ozon)
for word in products:
    if word.startswith("sko") == True:
        skovorodki.append(word)
print(skovorodki)

