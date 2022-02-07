# Lahman Baseball Datasets

This package consists of the [Lahman Baseball Database](http://www.seanlahman.com/baseball-archive/) with the intent 
of consuming it from Python code via the [Pandas](https://pandas.pydata.org/docs/) library.
The package was inspired from the book [Analyzing Baseball Data with R](https://www.routledge.com/Analyzing-Baseball-Data-with-R-Second-Edition/Marchi-Albert-Marchi-Albert-Baumer/p/book/9780815353515). Obviously R is not
Python so this package allows one to do the analyses covered in the book (as well as you own) using Python.

## Installation
Install using pip:

```pip install tq-lahman-datasets```

## Usage

Download and load the Pandas ```DataFrames``` into memory:
```python
from teqniqly.lahman_datasets import LahmanDatasets

ld = LahmanDatasets()
ld.load()
```

Get the dataframe names. Each dataframe corresponds to a CSV file in the Lahman database:

```python
df_names = ld.dataframe_names
```

Load datasets by providing the dataset name as an indexer to the ```LahmanDatasets``` instance:

```python
batting_df = ld["Batting"]
```

The datasets are Pandas ```DataFrames``` so work with them as you would with other DataFrames.