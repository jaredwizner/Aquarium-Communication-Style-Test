import requests
import csv

# URL to the raw CSV file in GitHub repository
CSV_URL = "https://raw.githubusercontent.com/jaredwizner/Aquarium-Communication-Style-Test/main/question_pool.csv"
GITHUB_TOKEN = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN_HERE"

def fetch_csv_data():
    """
    Fetches the CSV data from the GitHub URL.

    Returns:
        list: A list of dictionaries where each dictionary represents a row of the CSV.
    """
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    try:
        response = requests.get(CSV_URL, headers=headers)
        response.raise_for_status()  # Ensure the request was successful
        csv_data = list(csv.DictReader(response.text.splitlines()))
        return csv_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CSV data: {e}")
        return []

def get_question_by_number(question_number):
    """
    Retrieves a specific question from the CSV data based on the question number.

    Args:
        question_number (int): The number of the question to retrieve.

    Returns:
        dict: A dictionary containing the question and its options, or None if not found.
    """
    csv_data = fetch_csv_data()
    if not csv_data:
        return None

    for row in csv_data:
        if int(row.get("question_number", -1)) == question_number:
            return row

    print(f"Question number {question_number} not found in the CSV data.")
    return None

# Example usage
if __name__ == "__main__":
    question_number = 1
    question_data = get_question_by_number(question_number)
    if question_data:
        print(f"Question {question_number}: {question_data}")
    else:
        print(f"Question {question_number} could not be found.")
