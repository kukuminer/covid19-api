"""
FILE: observer.py
DESCRIPTION: Check databse status
AUTHOR: Liran Zheku
DATE: 21-Apr-2021
"""
import pandas as pd
from .file_paths import JHU_CSSE_FILE_PATHS
from .helper import helper_get_latest_data_url

class Observer:
    """ Checks JHU CSSE Database in case it is down """
    """ Get a dummy query, and check if it’s empty. If it is, the database is not functioning """
    def __init__(self) -> None:
        self.latest_base_url = helper_get_latest_data_url(JHU_CSSE_FILE_PATHS['BASE_URL_DAILY_REPORTS'])
        df = pd.read_csv(self.latest_base_url)
        self.IS_ACTIVE = !df.empty
 
    def get_active(self) -> bool
        return self.IS_ACTIVE
