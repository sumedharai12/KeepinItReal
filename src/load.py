#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import pandas as pd
from pathlib import Path

def read_data(debug=False):
    '''Helper procedure to load dataset.
    
    Returns
    -------
    Four pandas dataframes:
        train_X, val_X, train_y, val_y
    '''
    train = "train.csv"
    val = "dev.csv"
    
    if debug:
        print("inside read_data")
    
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
    
    X_col = ['ex_id', 'user_id', 'prod_id', 'rating', 'date', 'review']
    y_col = ['label']
    
    train_X = train_df.filter(X_col, axis='columns')
    val_X = val_df.filter(y_col, axis='columns')
    train_y = train_df.filter(X_col, axis='columns')
    val_y = val_df.filter(y_col, axis='columns')
    
    if debug:
        print("return")
    
    return train_X, val_X, train_y, val_y