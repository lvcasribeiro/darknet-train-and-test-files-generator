## Darknet *train* and *test* Files Generator

This code aims to segment the annotated files of the darknet custom dataset into two text files, segmenting 20 % in the first one, for testing, and 80 % in the second one, for training your convolutional neural network. It'll be used just the python programming language.

##

### Basic information about the usage of the script

###### 1. Usage operation flow:

1. Create a folder named `dataset`;
2. Upload the desired images and annotations to the folder;
3. Run the notebook cells in order or just run the **.py** file in the same path of your `dataset`, as shown below:

```python
.
├── dataset
│   ├── image-0.txt
│   ├── image-0.jpg
│   ├── image-1.txt
│   └── image-1.jpg
└── darknet-train-and-test-files-generator.py
```

<br>

###### 2. Script changes needed:
Create and configure your path to fit it on your files:
```python
# Adicione o caminho da sua pasta dataset aqui:
caminho = '/your/dataset/path/here';
```

##

### Remider

Sometimes, if there is an odd number of annotated samples, the number of test images will be truncated to the lower value, so I believe it is more beneficial to choose to have a little more than 80 % of images for training.

