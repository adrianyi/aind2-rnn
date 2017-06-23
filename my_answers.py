import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = [series[i-window_size:i] for i in range(window_size,len(series))]
    y = [series[i] for i in range(window_size,len(series))]
    
    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):
    pass


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
    # find all unique characters in the text
    # remove as many non-english characters and character sequences as you can
    for char in ['!', '"', '(', ')', '*', ',', '-', '.', '/',':',';','?','@']:
    text = text.replace(char,' ')
    
    # shorten any extra dead space created above
    text = text.replace('  ',' ')

    
### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    n_text = len(text)
    inputs = [text[i-window_size:i] for i in range(window_size,n_text,step_size)]
    outputs = [text[i] for i in range(window_size,n_text,step_size)]
    
    return inputs,outputs