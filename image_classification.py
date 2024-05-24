# -*- coding: utf-8 -*-
"""image_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hfkx1nPAbuv9PvCueriLwhLV1gnVWF84
"""

from google.colab import drive
drive.mount('/content/drive')

! zip -s- "/content/drive/My Drive/Praj/plant-seedlings-classification.zip" -O plant-seedlings-classification.zip
! unzip plant-seedlings-classification.zip -d plant-seedlings-classification

import os
import warnings
warnings.filterwarnings("ignore")

labels = os.listdir("plant-seedlings-classification/train")
print(labels)

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


fig, axs = plt.subplots(nrows=3, ncols=4)
fig.tight_layout()
for index, label in enumerate(labels):
    image = np.random.choice(os.listdir(f"plant-seedlings-classification/train/{label}"))
    im = Image.open(f"plant-seedlings-classification/train/{label}/{image}")
    ind = int(index/4), index % 4
    axs[ind].imshow(im)
    axs[ind].set_title(label.replace(" ", "\n"))
    axs[ind].axis("off")

from fastai.vision.all import *
from fastai.metrics import accuracy

# Use from_folder factory method from ImageDataBunch to create a dataset
# configure:
#   path
#   size
#   ds_tfms, to flip the image randomly and allow fliping vertically
#   valid_pct， 20%

path = "plant-seedlings-classification/train"
size = 224
ds_tfms = aug_transforms(do_flip=True, flip_vert=True, max_rotate=30.0)
valid_pct = 0.2
data = ImageDataLoaders.from_folder(path, train=".", valid_pct=valid_pct, item_tfms=Resize(size), batch_tfms=ds_tfms)

# normalize with imagenet_stats
normalize = Normalize.from_stats(*imagenet_stats)

# create a CNN learner named "learner" with resnet34
learner = cnn_learner(data, models.resnet34, metrics=accuracy)

# find a learning rate
learner.lr_find()

# fit one cycle
learner.fit_one_cycle(5, lr_max=0.0010000000474974513)

learner.show_results()

# interpret the result and see the most confused classess
interp = ClassificationInterpretation.from_learner(learner)
interp.most_confused(min_val=2)

#plot confusion matrix
interp.plot_confusion_matrix(figsize=(12,12))

learner.lr_find()

# fine tune the model and check the result again
learner.unfreeze()
learner.fit_one_cycle(5, lr_max=0.00363078061491251)

interp_after_fine_tune = ClassificationInterpretation.from_learner(learner)
interp.most_confused(min_val=2)

learner.show_results()

interp_after_fine_tune.plot_confusion_matrix(figsize=(12,12))

print("Accuracy:", learner.validate())

learner.export("/content/drive/My Drive/Praj/plant_seedlings_classifier.pkl")