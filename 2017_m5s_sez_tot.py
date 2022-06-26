
with open('m5s_2017_cand_sez_tab.csv', 'r') as f :
    lista = f.readlines()
# lista.pop(0)
sezioni = [0] * 30
for linea in lista :
    riga = linea.split(' ')
    for i in range(2,30) :
        sezioni[i] += int(riga[i])
        # print('Sezione :'  + str(i-1) + ' parziale sez :' + str(sezioni[i]) + ' Preferenza :' + riga[i])
sez = ''
prefereze  = ''
for i in range (2,30) :
    sez += str(i-1) + '\t'
    prefereze += str(sezioni[i]) +'\t'
print (sez)
print (prefereze)