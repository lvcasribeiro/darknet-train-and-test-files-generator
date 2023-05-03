# Libraries import:
import os

def create_dataset(dataset_path):
    # Directory measurement variable:
    dataset_existente = os.path.exists(f'{dataset_path}');

    # Creation of the 'dataset' directory, if it does not exist:
    if not dataset_existente:
        os.system(f'mkdir {dataset_path}');
        print('- Dataset folder created. Populate it with images!');
    else:
        # Dataset directory benchmarking:
        dataset_diretorio = os.listdir(f'{dataset_path}');

        if len(dataset_diretorio) == 0:
            print('- Dataset folder already exists, necessary to populate the dataset directory with images.');
        else:
            print('- Dataset folder already exists.');

    refine_dataset(f'{dataset_path}');


def refine_dataset(dataset_path):
    global dataset;
    dataset = [];
    dataset_original = os.listdir(f'{dataset_path}');

    for file in range(len(dataset_original)):
        if dataset_original[file][-3:] == "jpg" or dataset_original[file][-3:] == "png":
            dataset.append(dataset_original[file]);

    print(f'- Dataset list created. {len(dataset)} files available.');


def train_test_file_split(dataset_path):
    if len(dataset) == 0:
        print('- Dataset directory is empty!');
    else:
        arquivos_jpg = [];
        arquivos_path = [];

        # Capturing the files:
        for i in range(len(dataset)):
            if(dataset[i][-3:] == 'jpg'):
                # print(arquivos_txt[i]);
                arquivos_jpg.append(f'{dataset[i][:-3]}jpg');

        # for j in range(len(arquivos_jpg)):
        #     print(arquivos_jpg[j]);

        for k in range(len(arquivos_jpg)):
            arquivos_path.append(f'{dataset_path}' + '\\' + f'{arquivos_jpg[k]}');
            # print(arquivos_path[k]);
            
        # Splitting:
        limite_teste = int(len(arquivos_path) * .2);

        print('\n- Test files:');
        for l in range(limite_teste):
            print(arquivos_path[l]);

            # Writing test.txt:
            with open(f'{dataset_path[:-8]}\\test.txt', 'a') as arquivo:
                arquivo.write(f'{arquivos_path[l]}\n');

        m = limite_teste;

        print('\n\n- Train files:');
        while m < len(arquivos_path):
            print(arquivos_path[m]);

            # Writing train.txt:
            with open(f'{dataset_path[:-8]}\\train.txt', 'a') as arquivo:
                arquivo.write(f'{arquivos_path[m]}\n');

            m += 1;

if __name__ == '__main__':
    # Input the path where the dataset folder ll be created:
    dataset_path = r'C:\Users\lucas.ribeiro\Downloads';

    create_dataset(dataset_path + '\dataset');
    train_test_file_split(dataset_path + '\dataset');
