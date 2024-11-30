# score_analysis.py

import json
import csv

# Load the grading rubric
with open('Grading_Rubric.JSON', 'r') as file:
    grading_rubric = json.load(file)

# Load the question pool CSV
with open('question_pool.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    questions = list(reader)

def calculate_scores(responses):
    """
    Calculate the user's scores for each communication style.
    
    Parameters:
        responses (list): A list of user responses, each with question number and selected option.
        
    Returns:
        dict: A dictionary containing scores for Visionary, People-Oriented, Doing, and Planning.
    """
    scores = {
        "Visionary": 0,
        "People-Oriented": 0,
        "Doing": 0,
        "Planning": 0
    }
    
    for response in responses:
        question_number = response['question_number']
        selected_option = response['selected_option']
        
        # Find the matching question and calculate the score
        for question in questions:
            if question['number'] == question_number:
                if selected_option == 'A':
                    scores[grading_rubric['Definitions']['Visionary']] += int(question['rating_a'])
                elif selected_option == 'B':
                    scores[grading_rubric['Definitions']['People-Oriented']] += int(question['rating_b'])
                elif selected_option == 'C':
                    scores[grading_rubric['Definitions']['Doing']] += int(question['rating_c'])
                elif selected_option == 'D':
                    scores[grading_rubric['Definitions']['Planning']] += int(question['rating_d'])
                break
    
    return scores

# Example usage:
responses = [
    {"question_number": "1a", "selected_option": "A"},
    {"question_number": "2b", "selected_option": "C"},
    {"question_number": "3a", "selected_option": "B"},
]

user_scores = calculate_scores(responses)
print("User Scores:", user_scores)
