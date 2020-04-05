#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import load

def main(debug=False):
    '''loads datasets into dataframes using load.py and prints head(2) for each
    '''
    if debug:
        print("reading data")
    train_X, val_X, train_y, val_y = load.read_data(debug)
    if debug:
        print("data read")
    print(f'train_X: cols={train_X.columns.values} shape={train_X.shape}\n')
    print(train_X.head(2))
    print(f'val_X: cols={val_X.columns.values} shape={val_X.shape}\n')
    print(val_X.head(2))
    print(f'train_y: cols={train_y.columns.values} shape={train_y.shape}\n')
    print(train_y.head(2))
    print(f'val_y: cols={val_y.columns.values} shape={val_y.shape}\n')
    print(val_y.head(2))

if __name__ == "__main__":
    debug = False
    if sys.argv=="debug":
        debug = True
    main(debug)