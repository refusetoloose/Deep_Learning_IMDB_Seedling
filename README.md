# Deep Learning with Fastai: Sentiment Analysis of IMDb Movie Reviews and Image Classification of Seedling:

This repository contains two projects on Deep Learning using fastai, a widely-used deep learning Python library. You will explore deep learning techniques on text and image data through the following activities:

1. **Sentiment Analysis**: Apply a language model on movie reviews and train a classifier to determine the sentiments of those reviews.
2. **Image Classification**: Train a convolutional neural network (CNN) to classify seedlings based on their images.

## Table of Contents

- [Setup](#setup)
- [Equipment and Materials](#equipment-and-materials)
- [Sentiment Analysis Using a Language Model](#sentiment-analysis-using-a-language-model)
- [Image Classification Using CNN](#image-classification-using-cnn)
- [Results](#results)
- [Resources](#resources)
- [License](#license)

## Setup

### Prerequisites  
- A Google account for using Google Colab.  
- Fastai library installed (installation is done within the provided notebooks).  
  
### Lab Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/refusetoloose/Deep_Learning_IMDB_Seedling
   cd Deep_Learning_IMDB_Seedling
   
2. Download all the data files listed in the Materials and Equipment section above.
3. Access your Google Drive at [Google Drive](https://drive.google.com/) and create a folder in the root.
   - Note: If you don’t have a Google account, you’ll need to create one.
3. Upload the `plant-seedlings-classification.zip` and other 3 parts of zip with .z01,.z02,.z03 file to your folder.
4. Inside your folder, create a folder named `imdb`.
5. Upload the `train.csv` and `test.csv` files to your `imdb` folder.
   - Your layout should now resemble the following structure:
     ```
     /My Drive/Folder
     ├── plant-seedlings-classification.zip
     ├── plant-seedlings-classification.z01
     ├── plant-seedlings-classification.z02
     ├── plant-seedlings-classification.z03
     └── imdb
         ├── train.csv
         └── test.csv
     ```
### Colab Setup

1. Open Google Colab and upload the provided notebooks (`language_model.ipynb` and `image_classification.ipynb`).
2. Follow the instructions within the notebooks to mount Google Drive and access the data files.

## Equipment and Materials

- BYOD laptop
- Google account
- Data files: 
  - `train.csv` 
  - `test.csv`
  - `plant-seedlings-classification.zip`
- Sentiment Analysis Using a Language Model File:
  - `language_model.ipynb`
- Image Classification Using CNN File:
  - `image_classification.ipynb`
    
## Sentiment Analysis Using a Language Model:  

This project involves performing sentiment analysis on IMDb movie reviews using a language model.

### Steps

1. **Data Preparation**:
   - Load `train.csv` and `test.csv` files.
   - Create `TextLMDataBunch` and `TextClasDataBunch`.

2. **Model Training**:
   - Use AWD_LSTM architecture for the language model.
   - Fine-tune the language model.
   - Train the sentiment classifier.

3. **Evaluation**:
   - Predict the next 20 words for a given prompt.
   - Classify sentiments of example reviews.
   - Compute accuracy on the test dataset.

### Notebook

- `language_model.ipynb`: Notebook for performing sentiment analysis.

## Image Classification Using CNN

This project involves classifying images of seedlings using a convolutional neural network (CNN).

### Steps

1. **Data Preparation**:
   - Unzip `plant-seedlings-classification.zip`.
   - Load and preprocess images.

2. **Model Training**:
   - Create `ImageDataBunch` with data augmentation.
   - Use ResNet34 architecture for the CNN.
   - Fine-tune the model.

3. **Evaluation**:
   - Interpret results using a confusion matrix.
   - Identify the most confused classes.

### Notebook

- `image_classification.ipynb`: Notebook for performing image classification.

## Results

- **Sentiment Analysis**: Achieved an accuracy of over 80% on the test dataset.
- **Image Classification**: Achieved an accuracy of over 90% on the validation dataset.

## Resources

- [fastai documentation](https://docs.fast.ai/)
- [Google Colab](https://colab.research.google.com/)
- [IMDb Movie Reviews Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)
- [Plant Seedlings Classification Dataset](https://www.kaggle.com/c/plant-seedlings-classification)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
