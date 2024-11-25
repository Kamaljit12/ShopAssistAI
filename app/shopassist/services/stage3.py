"""
stage3.py
=========

This module implements the product recommendation layer in the laptop recommendation pipeline.

Stage 3 is responsible for:
1. Presenting the top laptop recommendations to the user in a clear and structured format.
2. Initializing a conversation context that leverages the recommendations to interact with the user.
3. Supporting user queries about the recommended products based on their profile and preferences.

The key function included in this module is:
- `initialize_conv_reco()`: Initializes the conversation with system-level guidelines and presents the top recommendations in a user-friendly format.

This stage builds upon the output from Stage 2 (validated recommendations) and prepares a chatbot interface to provide interactive and personalized assistance to the user.

Dependencies:
- json: For handling and passing product data in a structured format.

Usage:
- Call `initialize_conv_reco()` with the top 3 laptop recommendations as input to create a conversational context for user interaction.
"""


def initialize_conv_reco(products):
    """
    Initializes a conversation context for presenting laptop recommendations to the user.

    This function prepares the input for a chatbot by structuring the conversation with 
    system guidelines and user-provided product recommendations. The chatbot is expected 
    to act as a laptop gadget expert and present the recommendations in a user-friendly 
    and informative format.

    Args:
        products (str): A JSON-formatted string containing the top recommended laptops 
                        and their details, typically generated from the `compare_laptops_with_user` function.

    Returns:
        list[dict]: A list of dictionaries representing the conversation initialization.
                    Each dictionary contains the role (`system` or `user`) and the corresponding content.
    """
    system_message = """
    You are an intelligent laptop gadget expert and you are tasked with the objective to \
    solve the user queries about any product from the catalogue in the user message \
    You should keep the user profile in mind while answering the questions.\

    Start with a brief summary of each laptop in the following format, in decreasing order of price of laptops:
    1. <Laptop Name> : <Major specifications of the laptop>, <Price in Rs>
    2. <Laptop Name> : <Major specifications of the laptop>, <Price in Rs>

    """
    user_message = f""" These are the user's products: {products}"""
    conversation = [{"role": "system", "content": system_message },
                    {"role":"user","content":user_message}]
    
    return conversation