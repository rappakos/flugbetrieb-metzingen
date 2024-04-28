import os
from dotenv import load_dotenv
from zipfile import ZipFile 
import pandas as pd

HANNOVER_DWD_CODE = '02014'

FLUGBAHN_DIR = 30 # 03 & 21

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


def _base_wind_data(timeframe_start:int, timeframe_end:int):
    """
        timeframe_start, timeframe_end format YYYYMMDDhh        
    """
    raw_dataframes = load_raw_dataframes()
    #print(raw_dataframes)
    df = raw_dataframes['FF']['hist']    

    df_akt = raw_dataframes['FF']['akt']
    histor_max_date = df['MESS_DATUM'].max()
    df_akt = df_akt[(df_akt['MESS_DATUM'] >= timeframe_start) & ( df_akt['MESS_DATUM'] > histor_max_date) & (df_akt['MESS_DATUM'] <= timeframe_end) ]
    if not df_akt.empty:
        df = pd.concat([df,df_akt])        

    df = df.drop(['STATIONS_ID','QN_3','eor'], axis=1).rename(columns={'   F': 'strength', '   D': 'direction'})
    mask = (df['MESS_DATUM'] >= timeframe_start) & (df['MESS_DATUM'] <= timeframe_end)
    df = df[mask]

    return df

def _base_rain_data(timeframe_start:int, timeframe_end:int):
    """
        timeframe_start, timeframe_end format YYYYMMDDhh        
    """

    # R1;stdl. Niederschlagshoehe;mm;
    # RS_IND;Indikator Niederschlag ja/nein;numerischer Code;
    # WRTR;stdl. Niederschlagsform (=Niederschlagshoehe_ind);numerischer Code;
    raw_dataframes = load_raw_dataframes()
    df = raw_dataframes['RR']['hist']  

    df_akt = raw_dataframes['RR']['akt']
    histor_max_date = df['MESS_DATUM'].max()
    df_akt = df_akt[(df_akt['MESS_DATUM'] >= timeframe_start) & ( df_akt['MESS_DATUM'] > histor_max_date) & (df_akt['MESS_DATUM'] <= timeframe_end) ]
    if not df_akt.empty:
        df = pd.concat([df,df_akt])        

    df = df.drop(['STATIONS_ID','QN_8','eor','RS_IND','WRTR'], axis=1).rename(columns={'  R1':'precip'})
    mask = (df['MESS_DATUM'] >= timeframe_start) & (df['MESS_DATUM'] <= timeframe_end)

    df = df[mask]

    return df

def get_wind_data(timeframe_start:int, timeframe_end:int, hour_of_day:int):
    df = _base_wind_data(timeframe_start,timeframe_end)
    mask = (df['MESS_DATUM'] % 100 == hour_of_day) & (df['direction'] >= 0)
    df = df[mask] # reduce size
    
    return df

def get_rain_data(timeframe_start:int, timeframe_end:int, hour_of_day:int):

    df = _base_rain_data(timeframe_start, timeframe_end)
    mask = (df['MESS_DATUM'] % 100 == hour_of_day)
    df = df[mask] # reduce size

    return df 



def get_combined_data(timeframe_start:int, timeframe_end:int,day_of_week:str, from_hour:int, to_hour:int):
    """
        timeframe_start, timeframe_end format YYYYMMDDhh
        day_of_week format "Sat", "Sun" 
    """
    from datetime import datetime
    import numpy as np

    df_w = _base_wind_data(timeframe_start,timeframe_end)
    mask = (df_w['direction'] >= 0)
    mask = mask & (df_w['MESS_DATUM'] % 100 >= from_hour) & (df_w['MESS_DATUM'] % 100 <= to_hour)

    df_w = df_w[mask] # reduce size

    df_w[['wind_alignment', 'meas_hour', 'meas_day',  'day_of_week' ]] = df_w.apply(lambda row: pd.Series([ np.sin((row['direction'] - FLUGBAHN_DIR )* np.pi / 180.)**2, 
                                                int(row['MESS_DATUM'] % 100),
                                                str(row['MESS_DATUM'])[:8],
                                                datetime.strptime(str(row['MESS_DATUM'])[:8], "%Y%m%d").strftime('%a') ]), axis=1)

    df_r = _base_rain_data(timeframe_start,timeframe_end)
    mask = (df_r['MESS_DATUM'] % 100 >= from_hour) & (df_r['MESS_DATUM'] % 100 <= to_hour)
    df_r = df_r[mask] # reduce size

    df_w = df_w.join(df_r.set_index("MESS_DATUM"), on="MESS_DATUM", validate="1:1" )
    mask = (df_w['day_of_week']==day_of_week)    
    df_w = df_w[mask] # reduce size
    df_w = df_w.drop(['direction','day_of_week'], axis=1)

    return df_w.pivot(index='meas_day',columns='meas_hour', values=['strength','wind_alignment','precip'])


if __name__=='__main__':
    load_dotenv()

    #df = get_wind_data(2021050100, 2023123123, 13)

    #print(df.tail())

    #df = get_rain_data(2021050100, 2023123123, 13)

    #print(df.tail())

    df = get_combined_data(2021050100, 2023123123, 'Sun', 11,16 )

    print(df.head())

    print(df.tail())

