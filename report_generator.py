# report_generator.py

import json

# Load the Results JSON, which contains user communication styles and profile analysis
with open('Results.JSON', 'r') as file:
    results = json.load(file)

# Load Profile formatting JSON
with open('Profile.JSON', 'r') as file:
    profile_formatting = json.load(file)

def generate_report(user_id):
    """
    Generate a comprehensive report for the user, including text-based analysis and visuals.
    
    Parameters:
        user_id (str): The unique identifier for the user.
        
    Returns:
        dict: A dictionary containing the full report for the user.
    """
    # Extract user profile information
    user_profile = results['aquarium_communication_results']['profile_summary']
    
    # Format the report
    report = {
        "user_id": user_id,
        "primary_style": user_profile['primary_style']['description'],
        "secondary_style": user_profile['secondary_style']['description'],
        "tertiary_style": user_profile['tertiary_style']['description'],
        "blended_style": user_profile['blended_style']['description'],
        "strengths": user_profile['primary_style']['elements']['strengths'],
        "challenges": user_profile['primary_style']['elements']['challenges']
    }
    
    # Load visual results based on user styles
    visuals = results['aquarium_communication_results']['result_visuals']['types']
    
    if user_profile.get('blended_style'):
        report['visual'] = visuals['primary_visual']['description']
    else:
        report['visual'] = visuals['radar_chart']['description']
    
    return report

# Example usage:
user_id = "user_123"
user_report = generate_report(user_id)
print("User Report:", user_report)
