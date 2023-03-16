# Importação de bibliotecas:
import os

arquivos_txt = os.listdir(r'dataset');
arquivos_jpg = [];
arquivos_path = [];

caminho = '/content/dataset/';

# Capturando os arquivos com label em formato ".txt":
for i in range(len(arquivos_txt)):
    if(arquivos_txt[i][-3:] == 'txt'):
        # print(arquivos_txt[i]);
        arquivos_jpg.append(f'{arquivos_txt[i][0:9]}JPG');

# for j in range(len(arquivos_jpg)):
#     print(arquivos_jpg[j]);

for k in range(len(arquivos_jpg)):
    arquivos_path.append(f'{caminho}' + f'{arquivos_jpg[k]}');
    # print(arquivos_path[k]);
    
# Separando 20% para teste e 80% para treino:
limite_teste = int(len(arquivos_path) * .2);

print('[!] - Arquivos para teste:\n');
for l in range(limite_teste):
    print(arquivos_path[l]);

    # Escrevendo o arquivo teste.txt:
    with open('teste.txt', 'a') as arquivo:
        arquivo.write(f'{arquivos_path[l]}\n');

m = limite_teste;

print('\n\n[!] - Arquivos para treino:\n');
while m < len(arquivos_path):
    print(arquivos_path[m]);

    # Escrevendo o arquivo treino.txt:
    with open('treino.txt', 'a') as arquivo:
        arquivo.write(f'{arquivos_path[m]}\n');

    m += 1;