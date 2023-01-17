import pandas as pd
import datetime
import pickle
from ccsp2.arguments import *
from ccsp2.data_io import *
from ccsp2.model import *
from ccsp2.predict import *


def get_args():
    parser = argparse.ArgumentParser()

    optional = parser.add_argument_group('Optional Parameters')
    optional.add_argument('--output', help='prediction results directory', default='', type=str)

    predict = parser.add_argument_group('Prediction Parameters')
    predict.add_argument('--model', help='model to be used to predict CCS. if not specified, a default model is used',
                         default='models/UnifiedCCSCompendium_cleaned_2022-10-25/model.ccsp2', type=str)

    return vars(parser.parse_args())


def get_coconut_df():
    coconut = pd.read_csv('https://coconut.naturalproducts.net/download/absolutesmiles',
                          sep=' ', header=None, names=['SMILES', 'ID'])
    return coconut


if __name__ == '__main__':
    coconut = get_coconut_df()
    coconut.to_csv('data/coconut.csv', index=False)
