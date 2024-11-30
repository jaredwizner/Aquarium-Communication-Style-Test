# style_chart.py

import json
import matplotlib.pyplot as plt
import numpy as np

# Load the merged Results JSON for visual references
with open('Results.JSON', 'r') as file:
    results = json.load(file)

# Load Profile formatting JSON to support consistent labeling
with open('Profile.JSON', 'r') as file:
    profile_formatting = json.load(file)

def generate_radar_chart(user_id):
    """
    Generates a radar chart to visualize the user's scores for different communication styles.
    
    Parameters:
        user_id (str): A unique identifier for the user.
        
    Returns:
        None: The function saves the radar chart as an image file.
    """
    # Retrieve user profile and scores from the Results JSON
    user_profile = results['aquarium_communication_results']['profile_summary']
    scores = results['aquarium_communication_results']['profile_summary']['scores']
    
    # Define the communication styles and corresponding scores
    labels = ['Visionary', 'People-Oriented', 'Doing', 'Planning']
    values = [
        scores.get('Visionary', 0),
        scores.get('People-Oriented', 0),
        scores.get('Doing', 0),
        scores.get('Planning', 0)
    ]
    
    # Radar chart requires values to be in a closed loop
    values += values[:1]
    
    # Set up the radar chart
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    
    # Draw the outline of the radar chart
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.fill(angles, values, color='blue', alpha=0.25)
    
    # Set the labels and title using formatting from Profile.JSON
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, size=profile_formatting.get('text_size', 12))
    ax.set_title(f"Communication Style Radar Chart for {user_id}", size=profile_formatting.get('title_size', 16), weight='bold', pad=20)
    
    # Configure grid and aesthetic settings
    ax.yaxis.set_tick_params(labelsize=profile_formatting.get('tick_label_size', 10))
    ax.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)
    
    # Save the chart as an image file
    plt.savefig(f"{user_id}_radar_chart.png")
    plt.close()

# Example usage:
user_id = "user_123"
generate_radar_chart(user_id)
print(f"Radar chart for {user_id} has been generated and saved.")
