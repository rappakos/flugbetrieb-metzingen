import os
from dotenv import load_dotenv
from zipfile import ZipFile 
import pandas as pd

HANNOVER_DWD_CODE = '02014'


def load_raw_dataframes():

    existing_files = os.listdir(os.environ['DWD_DATA'])
    #print(existing_files)

    raw_dataframes = {}
    for measure in ['FF','RR']:
        raw_dataframes[measure] = {}
        for section in ['akt','hist']:
            f = f'stundenwerte_{measure}_{HANNOVER_DWD_CODE}_{section}.zip'
            assert(f in existing_files)
            with ZipFile(f"{os.environ['DWD_DATA']}/{f}") as zip:
                prod_list = [df for df in zip.namelist() if df.startswith('produkt_')]
                assert(len(prod_list)==1)
                with zip.open(prod_list[0]) as product_file:
                    df =  pd.read_csv(product_file, sep=';')
                    #print(df.head())
                    raw_dataframes[measure][section] = df
    
    return raw_dataframes


def get_wind_data(timeframe_start:int, timeframe_end:int, hour_of_day:int):
    """
        timeframe_start, timeframe_end format YYYYMMDDhh        
    """
    raw_dataframes = load_raw_dataframes()
    #print(raw_dataframes)
    df = raw_dataframes['FF']['hist']    

    df = df.drop(['STATIONS_ID','QN_3','eor'], axis=1).rename(columns={'   F': 'strength', '   D': 'direction'})
    mask = (df['MESS_DATUM'] >= timeframe_start) & (df['MESS_DATUM'] <= timeframe_end)
    #mask = mask & (df['strength'] >= 0) & (df['strength'] < 6) # too strong wind
    mask = mask & (df['MESS_DATUM'] % 100 == hour_of_day) & (df['direction'] >= 0)
    df = df[mask] # reduce size
    
    return df

def get_rain_data(timeframe_start:int, timeframe_end:int, hour_of_day:int):
    """
        timeframe_start, timeframe_end format YYYYMMDDhh        
    """

    # R1;stdl. Niederschlagshoehe;mm;
    # RS_IND;Indikator Niederschlag ja/nein;numerischer Code;
    # WRTR;stdl. Niederschlagsform (=Niederschlagshoehe_ind);numerischer Code;
    raw_dataframes = load_raw_dataframes()
    df = raw_dataframes['RR']['hist']  
    df = df.drop(['STATIONS_ID','QN_8','eor','RS_IND','WRTR'], axis=1).rename(columns={'  R1':'precip'})
    mask = (df['MESS_DATUM'] >= timeframe_start) & (df['MESS_DATUM'] <= timeframe_end)
    mask = mask & (df['MESS_DATUM'] % 100 == hour_of_day)
    df = df[mask] # reduce size

    return df 



if __name__=='__main__':
    load_dotenv()

    df = get_wind_data(2021050100, 2021123123, 13)

    print(df.head())


