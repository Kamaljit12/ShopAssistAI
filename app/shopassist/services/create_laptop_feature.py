"""
create_laptop_feature.py

This module processes the laptop dataset by extracting and mapping key product features 
from the `Description` column and appending them as a new column `laptop_feature` in the dataset. 
It prepares the dataset for further steps in the pipeline, such as product comparison and recommendations.

Key Functionality:
- Reads the raw laptop dataset from a CSV file (`laptop_data.csv`).
- Extracts features such as GPU Intensity, Display Quality, Portability, Multitasking, 
  Processing Speed, and Budget using the `product_map_layer` helper function.
- Creates a new column, `laptop_feature`, containing these extracted features as Python dictionaries.
- Saves the processed dataset to a new CSV file (`updated_laptop.csv`) for use in later stages of the pipeline.

Files:
- Input: `data/laptop_data.csv` - The raw dataset with laptop descriptions.
- Output: `data/updated_laptop.csv` - The updated dataset with the `laptop_feature` column.

Dependencies:
- pandas: Used for reading, manipulating, and saving datasets.
- shopassist.utils.helper: Contains the `product_map_layer` function for feature extraction.

Usage:
Run this script once to process the dataset:
    `python create_laptop_feature.py`

The updated dataset will be saved and ready for use in subsequent stages of the ShopAssist pipeline.
"""


import os
import pandas as pd
from shopassist.utils.helper import product_map_layer


DATA_PATH = os.path.join('data', 'laptop_data.csv')
UPDATED_DATA_PATH = os.path.join('data', 'updated_laptop.csv')

def add_laptop_feature_col():

    laptop_df= pd.read_csv(DATA_PATH)

    ## Create a new column "laptop_feature" that contains the dictionary of the product features
    laptop_df['laptop_feature'] = laptop_df['Description'].apply(lambda x: product_map_layer(x))

    laptop_df.to_csv(UPDATED_DATA_PATH, index=False, header = True)

    return True


if __name__ == "__main__":

    add_laptop_feature_col()
