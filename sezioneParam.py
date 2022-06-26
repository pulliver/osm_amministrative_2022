lista = []
for i in range (1,280, 10):
    lista.append(i)
print(lista)
print(len(lista))
with open("sezioneParam.txt", 'w') as f:
    f.write(str(lista))