# results_visualizer.py

import json
import matplotlib.pyplot as plt
import numpy as np

# Load the Results JSON for visual references
with open('Results.JSON', 'r') as file:
    results = json.load(file)

def generate_radar_chart(scores, user_id):
    """
    Generates a radar chart to visualize the user's scores for different communication styles.
    
    Parameters:
        scores (dict): A dictionary containing scores for Visionary, People-Oriented, Doing, and Planning.
        user_id (str): A unique identifier for the user.
        
    Returns:
        None: The function saves the radar chart as an image file.
    """
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
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Draw the outline of the radar chart
    ax.plot(angles, values, color='blue', linewidth=2)
    ax.fill(angles, values, color='blue', alpha=0.25)
    
    # Set the labels and title
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    ax.set_title(f"Communication Style Radar Chart for {user_id}", size=16, weight='bold', pad=20)
    
    # Save the chart as an image file
    plt.savefig(f"{user_id}_radar_chart.png")
    plt.close()

# Example usage:
user_scores = {
    "Visionary": 30,
    "People-Oriented": 45,
    "Doing": 25,
    "Planning": 40
}
user_id = "user_123"
generate_radar_chart(user_scores, user_id)
print(f"Radar chart for {user_id} has been generated and saved.")
