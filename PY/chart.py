import matplotlib.pyplot as plt
import numpy as np

def generate_radar_chart(scores, username="User"):
    # Define the communication styles
    labels = list(scores.keys())
    num_vars = len(labels)

    # Create a list of values from the user's scores and add the first score to close the radar chart
    values = list(scores.values())
    values += values[:1]

    # Compute angle of each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    # Create the radar chart plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Draw one axe per variable + add labels
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Plot data
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, alpha=0.25)

    # Set labels and title
    ax.set_title(f"{username}'s Communication Style Profile", size=20, color='navy', y=1.1)
    
    # Show radar chart
    plt.show()

# Example usage
if __name__ == "__main__":
    sample_scores = {
        "Doing": 4,
        "Planning": 3,
        "People-Oriented": 5,
        "Visionary": 2
    }
    generate_radar_chart(sample_scores, username="Jared")
