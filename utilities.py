"""
Tamar Ervin
Date: September 19, 2022
Utility functions for reading and writing data
"""

import os
import csv
import datetime

import numpy as np
import pandas as pd

from astropy.time import Time


def read_csv(csv_file_path):
    """
    function to read csv file and return list of dates
    Parameters
    ----------
    csv_file_path : str
        path to csv file
    Returns
    -------
    csv_list : str, list
        list of elements in csv file
    """

    with open(csv_file_path, newline='') as f:
        reader = csv.reader(f)
        csv_list = list(reader)

    return csv_list


def get_dates(date):
    """
    function to convert dates from either JD, string, or datetime
    to a Sunpy usable date form
    Parameters
    ----------
    date
        date in any form (JD, string, datetime)
    Returns
    -------
    date_str : str
        UT datetime as string
    date_obj : datetime
        UT datetime object
    date_jd : float
        UT datetime as float (JD)
    """
    if isinstance(date, str):
        date_str = date
        date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
        date_jd = Time(date_str)
        date_jd.format = 'jd'
    elif isinstance(date, float):
        t = Time(date, format='jd')
        date_obj = t.datetime
        date_str = date_obj.strftime('%Y-%m-%dT%H:%M:%S.%s')
        date_jd = date
    else:
        date_obj = date
        date_str = date_obj.strftime('%Y-%m-%dT%H:%M:%S.%s')
        date_jd = Time(date_str)
        date_jd.format = 'jd'

    return date_str, date_obj, date_jd

