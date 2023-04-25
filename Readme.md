# IMDB Data Analysis with Python Pandas

This repository contains Python Pandas code for exploring the IMDB dataset. The dataset consists of information about movies, including their titles, directors, ratings, release years, and countries.

## Data Exploration

The code in this repository explores the dataset in several ways, including:

- Merging the data into one DataFrame
- Cleaning the data by removing the last unknown character from the movie titles
- Finding the directors with the most movies
- Checking for empty columns
- Saving all movies directed by Christopher Nolan in a variable
- Calculating the average rating of Christopher Nolan's movies
- Selecting non-USA movies made after 1960 by Hayao Miyazaki
- Describing the basic statistics of the dataset
- Finding the year that produced the most movies

## Dataset

The IMDB dataset is available in an Excel file called `imdb.xlsx`. The file contains three separate sheets: `imdb`, `directors`, and `countries`. The data is merged into one DataFrame using the `merge()` function in Pandas.

## Dependencies

This code requires the Pandas library for Python. You can install it using pip:

```
pip install pandas
```

## Usage

To use this code, simply download or clone this repository and run the Python script `imdb_analysis.py`. The script will read the `imdb.xlsx` file and perform the data exploration tasks described above.

Best of Luck,

Aayush Doshi.
