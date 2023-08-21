from fastai.vision.widgets import *
from fastbook import *




path = Path (r'D:\indomim_tirupati\indoData\segregated\chamfer_thread_out')




data= ImageDataLoaders.from_folder(path,train = "train", valid_pct=0.2, item_tfms=Resize(128), batch_tfms=tfms, bs = 1, num_workers = 8)


Data = DataBlock( blocks=(ImageBlock, CategoryBlock), get_items=get_image_files, 
splitter=RandomSplitter(valid_pct=0.2, seed=42), get_y=parent_label, item_tfms=Resize(128))
dls = Data.dataloaders(path)


learn = cnn_learner(data, resnet34, metrics=error_rate)

