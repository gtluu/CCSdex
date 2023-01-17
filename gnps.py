import numpy as np
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


def get_gnps_df():
    gnps = pd.read_json('https://gnps-external.ucsd.edu/gnpslibraryjson')
    colnames = ['spectrum_id', 'Compound_Name', 'Adduct', 'Precursor_MZ', 'Charge', 'Smiles', 'INCHI']
    gnps = gnps[colnames]
    gnps = gnps.rename(columns={'spectrum_id': 'ID',
                                'Compound_Name': 'Compound',
                                'Adduct': 'Adduct',
                                'Precursor_MZ': 'mz',
                                'Charge': 'Charge',
                                'Smiles': 'SMILES',
                                'INCHI': 'InChI'})

    # prioritizing SMILES formulas here
    gnps['SMILES'].replace('N/A', np.nan, inplace=True)
    gnps['SMILES'].replace(' ', np.nan, inplace=True)
    gnps.dropna(subset=['SMILES'], inplace=True)
    gnps['SMILES'] = gnps['SMILES'].apply(lambda x: x.strip())
    gnps['SMILES'].replace('', np.nan, inplace=True)
    gnps.dropna(subset=['SMILES'], inplace=True)

    return gnps


if __name__ == '__main__':
    gnps = get_gnps_df()
    gnps.to_csv('data/gnps.csv', index=False)
