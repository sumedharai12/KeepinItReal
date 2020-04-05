#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import pandas as pd
from pathlib import Path

from balance import SMOTE

def read_file(file, debug=False):
    '''Helper procedure to load one file.
    
    Parameters
    ----------
    file : string
        'train' | 'val'
        
    debug : boolean to set debugging verbosity 
    
    Returns
    -------
    Dataframe with either 'train' or 'val' data loaded.
    '''
    train = "train.csv"
    val = "dev.csv"
    
    train = "train.csv"
    val = "dev.csv"
    
    if debug:
        print("inside read_file")
    
    try:
        train_df = pd.read_csv(train)
        val_df = pd.read_csv(val)
    except:
        try:
            if debug:
                print("try")
            data_folder = Path(os.path.dirname(__file__).replace('src', 'data'))
        except:
            if debug:
                print("except")
            data_folder = Path(os.path.abspath('').replace('src', 'data'))
        finally:
            if debug: 
                print("finally")
            train = data_folder / "train.csv"
            val = data_folder / "dev.csv"
            train_df = pd.read_csv(train)
            val_df = pd.read_csv(val)
    
    if debug:
        print("past try-except")
    
    if file=='train':
        loaded_file = train_df
    elif file=='val':
        loaded_file = val_df
    else:
        loaded_file = None
        
    if debug:
        print(f'loaded: {file}')
        print("exiting read_file")
    
    return loaded_file
    
def read_data(debug=False, balance=False):
    '''Helper procedure to load dataset.
    
    Parameters
    ----------
    balance : boolean
        Specifies whether to apply SMOTE (from balance.py) to the data
    
    debug : boolean to set debugging verbosity
    
    Returns
    -------
    Four pandas dataframes:
        train_X, val_X, train_y, val_y
    '''
    if debug:
        print("inside read_data")

    train_df = read_file('train', debug)
    val_df = read_file('val', debug)
    
    if debug:
        print("data loaded")
        
    if balance:
        train_df = SMOTE(df=train_df, debug=debug)
        val_df = SMOTE(df=val_df, debug=debug)
    
    X_col = ['ex_id', 'user_id', 'prod_id', 'rating', 'date', 'review']
    y_col = ['label']
    
    train_X = train_df.filter(X_col, axis='columns')
    val_X = val_df.filter(y_col, axis='columns')
    train_y = train_df.filter(X_col, axis='columns')
    val_y = val_df.filter(y_col, axis='columns')
    
    if debug:
        print("exiting read_data")
    
    return train_X, val_X, train_y, val_y