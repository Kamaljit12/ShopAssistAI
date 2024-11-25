# ShopAssist AI: Intelligent Laptop Shopping Assistant

## 📖 Project Overview
ShopAssist AI is an innovative chatbot designed to transform the online laptop shopping experience. By leveraging the power of Large Language Models (LLMs) and rule-based functions, this intelligent assistant provides accurate and personalized laptop recommendations based on user requirements. 

`ShopAssist AI aims to simplify the overwhelming nature of online shopping by guiding users in finding the perfect laptop tailored to their needs.`

## 🛠️ Problem Statement
In the digital shopping era, the abundance of options can make it difficult for consumers to make informed decisions. 

`This project addresses the challenge of:`

- Interacting with users to gather their requirements.
- Parsing a dataset of laptops to extract relevant information.
- Recommending the most suitable laptops based on user preferences.

## Key Objectives:
- `Engage users:` Provide natural and interactive conversations to understand user requirements.
- `Extract insights:` Use LLMs and rule-based reasoning to map user preferences to the dataset.
- `Recommend effectively:` Suggest the top three laptops matching user needs and answer follow-up queries.

## High Level System Design
![system_design](https://github.com/user-attachments/assets/a9a8e6ae-9bd2-4d44-b51a-653324ebddba)


## 🚀 Solution Approach
#### 1. `Conversation and Information Gathering`
- The chatbot initiates a natural conversation to collect user requirements, such as budget, specifications, and usage needs.
Moderation checks ensure the conversation is safe and free of sensitive content.

#### 2. `Information Extraction`
- The system analyzes user requirements using natural language understanding (NLU).
It filters laptops from the dataset based on extracted features and calculates compatibility scores.

#### 3. `Personalized Recommendations`
- Presents a maximum of three laptops, ranked by relevance to user requirements.
- In cases where no laptops meet the threshold, the system connects the user with a human expert.

## 📂 Project Stages

#### `Stage 1: Intent Clarity and Confirmation`
This stage involves initiating and managing the conversation between the user and the AI system.

**Key Functions:**
- initialize_conversation(): Starts the conversation with the user.
- get_chat_completions(): Continuously processes user inputs and generates LLM responses.
- moderation_check(): Flags and halts conversations containing unsafe or sensitive content.

#### `Stage 2: Product Mapping and Information Extraction`
This stage filters laptops based on user requirements and identifies the top recommendations.

**Key Functions:**
- product_map_layer(): Extracts and maps key features (e.g., GPU intensity, display quality) from the dataset.
- compare_laptops_with_user(): Matches user requirements against the laptop features to calculate scores.
- recommendation_validation(): Validates the recommendations to ensure they meet quality thresholds.

#### `Stage 3: Product Recommendation`
This stage delivers recommendations and engages in further conversation.

**Key Functions:**
- initialize_conv_reco(): Generates a structured conversation with summarized laptop recommendations.
- get_chat_completions(): Facilitates follow-up queries and detailed discussions about the recommended laptops.

## 📊 Dataset Details
The project uses a dataset containing the following:

- Laptop Descriptions: Detailed specifications of each laptop.
- Features: Key attributes like GPU intensity, multitasking capability, portability, and price.

### Data Preparation:

- Input File: data/laptop_data.csv (raw dataset).
- Processed File: data/updated_laptop.csv (with extracted features).
- A separate preprocessing script, `create_laptop_feature.py`, processes the dataset to extract features and store them as a new column (laptop_feature).

## 💡 Key Features

- Interactive Conversations: Engages users with natural and context-aware responses.
- Advanced Filtering: Matches laptops to user preferences with high accuracy.
- Personalized Assistance: Provides tailored recommendations and supports follow-up queries.

## 🧩 Future Scope
- Enhanced Dataset: Include additional attributes like brand reputation and user reviews.
- Advanced Scoring: Use machine learning models to improve compatibility scoring.
- Multi-Language Support: Expand chatbot capabilities to support diverse user bases.

## Acknowledgements
- This Project is a part of my assignment for Post Graduate Diploma Degree in AI & ML at IIIT-Bangalore

## ✍️ Author
Developed by [Upendra Kumar]. For queries, reach out at [upendra.kumar48762@gmail.com].
