"""
Tamar Ervin
Date: November 11, 2022

Settings file: primarily for file organization
"""

import os
import datetime


class BaseDir:
    """
    Base directory.
    """
    BASE_DIR = os.path.realpath('../../')


class CsvDir:
    """
    CSV directories
    """
    CSV_DIR = os.path.join(BaseDir.BASE_DIR, 'csv_files')
    CALC = os.path.join(CSV_DIR, 'calcs')


class DataDir:
    """
    Data directory
    """
    DATA_DIR = os.path.join(BaseDir.BASE_DIR, 'data')
    GONG = os.path.join(DATA_DIR, 'gong')
    PSP = os.path.join(DATA_DIR, 'psp')
    SO = os.path.join(DATA_DIR, 'so')


class ImgDir:
    """
    Image directories
    """
    IMG_DIR = os.path.join(BaseDir.BASE_DIR, 'images')
