"""
stage2.py
=========

This module handles the information extraction and product mapping layers in the laptop recommendation pipeline. 

Stage 2 is responsible for:
1. Extracting laptop features from their descriptions and mapping them into a structured format.
2. Comparing the extracted features with the user's requirements to find the best matches.
3. Validating the top recommendations based on their relevance and suitability.

The key functions included in this module are:
- `product_map_layer()`: Extracts key features from laptop descriptions and maps them to user-defined categories such as GPU Intensity, Display Quality, Portability, Multitasking, Processing Speed, and Budget.
- `compare_laptops_with_user()`: Compares the extracted features of laptops with the user's requirements and identifies the top 3 recommendations.
- `recommendation_validation()`: Validates the recommendations by ensuring they meet the user's minimum requirements.

This module interacts with the user requirements dictionary generated in Stage 1, processes the dataset of laptops, and outputs validated recommendations for use in the next stage.

Dependencies:
- pandas: For data manipulation and filtering.
- json: For handling and formatting JSON objects.
"""


import pandas as pd
import os
import json
from shopassist.services.stage1 import dictionary_present


UPDATED_DATA_PATH = os.path.join('data', 'updated_laptop.csv')


def compare_laptops_with_user(user_req_dict):
    """
    Compares user requirements with a dataset of laptops and recommends the top 3 laptops based on feature matching.

    This function takes user requirements in the form of a dictionary, filters the laptops dataset based on budget,
    calculates a matching score for each laptop, and returns the top 3 laptops as a JSON-formatted string.

    Args:
        user_req_dict (dict): A dictionary containing the user's requirements, 
                               such as budget and feature preferences.

    Returns:
        str: A JSON-formatted string containing the top 3 laptop recommendations. 
             Each recommendation includes laptop details and a score indicating how well it matches the user's needs.

    Process:
        1. Reads the laptop dataset from a CSV file (`updated_laptop.csv`).
        2. Extracts and cleans the user's budget from the input dictionary.
        3. Filters laptops within the user's budget.
        4. Matches user requirements with laptop features (stored in the `laptop_feature` column).
        5. Calculates a score for each laptop based on how well it matches the user's requirements.
        6. Sorts laptops by score in descending order and selects the top 3 recommendations.
        7. Returns the recommendations as a JSON-formatted string.
    """

    laptop_df = pd.read_csv(UPDATED_DATA_PATH)

    # Extracting user requirements from the input string (assuming it's a dictionary)

    # Extracting the budget value from user_requirements and converting it to an integer
    budget = int(user_req_dict.get('Budget', '0').replace(',', '').split()[0])
    # budget
    # # Creating a copy of the DataFrame and filtering laptops based on the budget
    filtered_laptops = laptop_df.copy()
    filtered_laptops['Price'] = filtered_laptops['Price'].str.replace(',', '').astype(int)
    filtered_laptops = filtered_laptops[filtered_laptops['Price'] <= budget].copy()
    # filtered_laptops
    # # # Mapping string values 'low', 'medium', 'high' to numerical scores 0, 1, 2
    mappings = {'low': 0, 'medium': 1, 'high': 2}

    # # # Creating a new column 'Score' in the filtered DataFrame and initializing it to 0
    filtered_laptops['Score'] = 0

    # # # Iterating over each laptop in the filtered DataFrame to calculate scores based on user requirements
    for index, row in filtered_laptops.iterrows():
        user_product_match_str = row['laptop_feature']
        laptop_values = user_product_match_str
        laptop_values = dictionary_present(user_product_match_str)
        score = 0

    #     # Comparing user requirements with laptop features and updating scores
        for key, user_value in user_req_dict.items():
            # if key.lower() == 'budget':
            if key == 'Budget':
                continue  # Skipping budget comparison
            laptop_value = laptop_values.get(key, None)
            # print(key, laptop_value)
            laptop_mapping = mappings.get(laptop_value, -1)
            user_mapping = mappings.get(user_value, -1)
            if laptop_mapping >= user_mapping:
                score += 1  # Incrementing score if laptop value meets or exceeds user value

        filtered_laptops.loc[index, 'Score'] = score  # Updating the 'Score' column in the DataFrame

    # Sorting laptops by score in descending order and selecting the top 3 products
    top_laptops = filtered_laptops.drop('laptop_feature', axis=1)
    top_laptops = top_laptops.sort_values('Score', ascending=False).head(3)
    top_laptops_json = top_laptops.to_json(orient='records')  # Converting the top laptops DataFrame to JSON format

    # top_laptops
    return top_laptops_json



def recommendation_validation(laptop_recommendation):
    """
    Validates the laptop recommendations by filtering those that meet a minimum score threshold.

    This function takes a JSON-formatted string of laptop recommendations, verifies if the recommendations 
    have a score greater than 2, and returns a filtered list of valid recommendations.

    Args:
        laptop_recommendation (str): A JSON-formatted string containing a list of laptop recommendations.
                                     Each recommendation should include a `Score` key.

    Returns:
        list: A list of dictionaries representing valid laptop recommendations with a `Score` greater than 2.
    """

    data = json.loads(laptop_recommendation)
    data1 = []
    for i in range(len(data)):
        if data[i]['Score'] > 2:
            data1.append(data[i])

    return data1