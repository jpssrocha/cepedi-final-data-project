from functools import reduce
from typing import Callable
from pathlib import Path
from time import perf_counter

import pandas as pd

def _pipe_list(transformations: list[Callable], df: pd.DataFrame) -> pd.DataFrame:
    """Pipe a dataframe over a list of tranformations"""
    return reduce(lambda _df, trans: _df.pipe(trans), transformations, df)


def init_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Desired procedures before starting up pipeline"""
    return df.copy()
    

def format_columns(df: pd.DataFrame, regex) -> pd.DataFrame:
    """Given dataframe format columns into conventional format"""    
    df.columns = df.columns.str.lower().str.replace(regex, "_", regex=True)
    return df


def parse_date(df: pd.DataFrame, date_col: str, format: str) -> pd.DataFrame:
    """Parse date stamp"""
    df[date_col] = pd.to_datetime(df[date_col], format=format)
    return df


def parse_categorical(df: pd.DataFrame, to_categorical_percent: float = 10) -> pd.DataFrame:
    """
    Get columns with unique values corresponding to a certain percentage (`to_categorical_percentage`) 
    of the total and convert it to 
    """
    for col in df.columns:
        unique = df[col].unique().shape[0]
        unique_percentage = unique/df.shape[0]*100
        #print(df[col].unique().shape[0], f"{unique_percentage:.2f}%")
        if (unique_percentage <= to_categorical_percent): #and df[col].dtype == "object":
            print(f"Parsed to categorical :: {col}: {unique} categories, {unique_percentage:.2f}% unique")
            df[col] = df[col].astype("category")
    
    return df
    

def load_and_process(
    raw_dataset_path: Path, 
    pipeline: list[Callable[[pd.DataFrame], pd.DataFrame]] | None = None
    ) -> pd.DataFrame:
    """
    Apply a pipeline (list of processing functions) to a dataset from a given
    set of raw files
    """


    pkl_file = raw_dataset_path.parent / "../" / Path(f"{raw_dataset_path.stem}.pkl")

    if pkl_file.exists():

        now = perf_counter()

        ds = pd.read_pickle(pkl_file)

        print(f"Loaded from pickle, took: {(perf_counter() - now):.2f} s")

        return ds
    
    elif not pipeline:
        print("Warning: No processed pkl, neither pipeline. Simply loading the file")
        
        ds = pd.read_csv(raw_dataset_path)
        
        return ds

    else:

        now = perf_counter()
        
        unprocessed_dataset = pd.read_csv(raw_dataset_path)

        ds = _pipe_list(pipeline, unprocessed_dataset)

        print(f"Loaded and processed from csv, took: {(perf_counter() - now):.2f} s")

        ds.to_pickle(pkl_file)

        return ds
