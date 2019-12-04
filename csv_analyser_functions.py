'''
CSV Analyser Functions

A file containing functions for the Analyse CSV package
'''

# Library Imports
import pandas as pd


def read_file(path):
    '''
    Read a CSV into a Pandas DataFrame

    Parameters
    ----------
    path: string
        File path to the CSV file

    Returns
    -------
    data: DataFrame
        A DataFrame containing the contents of the CSV
    '''

    df = pd.read_csv(path)

    return(df)


def get_column_names(df):
    '''
    Get a list of DataFrame column names

    Parameters
    ----------
    df: DataFrame
        A DataFrame containing named columns

    Returns
    -------
    names: list
        List of column names
    '''

    names = list(df.columns.values)

    return(names)


def missing_values(series, sf=1):
    '''
    Get the number and percentage of empty elements in a Pandas Series

    Parameters
    ----------
    series: Series
        Pandas Series containing data to analyse

    sf: int, default = 1
        Number of significant figures to round percentage to

    Returns
    -------
    values: list
        A list containing the Count [0] and Percentage [1] of missing values
    '''

    # Create empty list to store values
    values = []

    # Calculate number of blank rows
    values.append(series.isnull().sum())

    # Calculate percentage of blank rows
    values.append(round((values[0] / series.count()) * 100, int(sf)))

    return(values)


def get_unique_values(series):
    '''
    Returns a list of unique values in a Pandas series

    Parameters
    ----------
    series: series
        Pandas series to analyse

    Returns
    -------
    values: List
       A list of unique values
    '''

    values = list(series.unique())

    return(values)
