import pandas as pd
import argparse
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', help='output directory', default='', type=str)
    return vars(parser.parse_args())


def get_coconut_df():
    coconut = pd.read_csv('https://coconut.naturalproducts.net/download/absolutesmiles',
                          sep=' ', header=None, names=['SMILES', 'ID'])
    return coconut


if __name__ == '__main__':
    args = get_args()
    coconut = get_coconut_df()
    coconut.to_csv(os.path.join(args['output'], 'coconut.csv'), index=False)
