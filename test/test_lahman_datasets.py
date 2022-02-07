import pandas as pd

from teqniqly.lahman_datasets import LahmanDatasets


def test_load_lahman_datasets():
    ld = LahmanDatasets()
    ld.load()
    df_names = ld.dataframe_names

    for df_name in df_names:
        df = ld[df_name]
        assert df is not None
        assert type(df) == pd.DataFrame
        assert len(df) > 0
