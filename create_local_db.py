import numpy as np
import pandas as pd
from sqlalchemy import create_engine


if __name__ == '__main__':
    # scrape databases
    npatlas = pd.read_csv('db/npatlas_ccs/target_book_output.csv')
    #coconut = pd.read_csv('db/coconut_ccs/coconut.csv')
    #gnps = pd.read_csv('db/gnps_ccs/gnps.csv')

    #ccsdex = pd.concat([npatlas, coconut, gnps])
    ccsdex = npatlas

    engine = create_engine('sqlite:///db/ccsdex.db')

    ccsdex.to_sql('ccsdex', con=engine, if_exists='append')
