import fastai
from fastai.vision import *

def inf(img):
    path = ("./")
    learn = load_learner(path)
    pred_class,pred_idx,outputs = learn.predict(img)

    return str(pred_class)