import os
from typing import Optional, Tuple, List

import pandas as pd
import requests
import tempfile
from glob import glob
from tqdm import tqdm
from zipfile import ZipFile


class LahmanDatasets:
    def __init__(self):
        self.__url = "https://github.com/chadwickbureau/baseballdatabank/archive/master.zip"
        self.__target_filename = os.path.join(tempfile.gettempdir(), "master.zip")
        self.__extract_folder = os.path.join(tempfile.gettempdir(), "lahman_csv")
        self.__zip_file: Optional[ZipFile] = None
        self.__dataframes_lookup: List[Tuple[str, pd.DataFrame]] = []

    @property
    def dataframe_names(self):
        return [tup[0] for tup in self.__dataframes_lookup]

    def __getitem__(self, item):
        dfs = [tup[1] for tup in self.__dataframes_lookup if tup[0] == item]

        if len(dfs) == 1:
            return dfs[0]

    def load(self) -> None:
        self.__download(self.__target_filename)
        self.__extract_zip_files()

    @staticmethod
    def __get_filename_without_extension(filename: str) -> str:
        return os.path.splitext(filename)[0].split("\\")[-1]

    def __download(self, target_filename: str) -> None:
        result = requests.get(self.__url, stream=True)

        with open(target_filename, "wb") as file:
            for chunk in tqdm(result.iter_content(chunk_size=1000000)):
                file.write(chunk)

        self.__zip_file = ZipFile(target_filename, "r")

    def __extract_zip_files(self):
        if not os.path.exists(self.__extract_folder):
            os.makedirs(self.__extract_folder)

        self.__zip_file.extractall(self.__extract_folder)

    def __get_dataframe_descriptors(self) -> List[Tuple[str, str]]:
        return [(LahmanDatasets.__get_filename_without_extension(filename), filename) for filename in
                glob(os.path.join(self.__extract_folder, "baseballdatabank-master", "core", "*.csv"),
                     recursive=False)]

    def __load_dataframes(self) -> None:
        for df_name, filename in self.__get_dataframe_descriptors():
            df = pd.read_csv(filename)
            self.__dataframes_lookup.append((df_name, df))
