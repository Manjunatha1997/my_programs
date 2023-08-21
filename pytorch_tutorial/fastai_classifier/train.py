from fastai2.vision import * 
from fastai.vision.data import Path
from fastai.vision.all import *


# path = r'/media/lincode3090/Backup/manju/indomim_tirupati/classification_det/classifiaction/classfy_seg_data/'
path = r'/media/lincode3090/Backup/manju/indomim_tirupati/classification_det/classifiaction/dataset_view7/'

epochs = 100
batch_size = 32


data_ = DataBlock(
    blocks=(ImageBlock, CategoryBlock), 
    get_items=get_image_files, 
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=Resize(128),

    )

dls = data_.dataloaders(path,bs=batch_size)
learn = vision_learner(dls, resnet101, metrics=error_rate)
learn.fine_tune(epochs)
learn.export('weights/view7.pkl')




