# File: aquarium_communication_style_chart.py

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Data for radar chart
labels = ['Visionary', 'Planning', 'People-Oriented', 'Doing']
scores = [15, 25, 15, 5]

# Number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Complete the loop for the radar chart
scores += scores[:1]
angles += angles[:1]

# Define the colors for each communication style
style_colors = {
    'Visionary': 'yellow',
    'Planning': 'blue',
    'People-Oriented': 'green',
    'Doing': 'red'
}

# Plotting the radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw the outline of the chart with the primary color as Planning (blue)
ax.fill(angles, scores, color='blue', alpha=0.4)
ax.plot(angles, scores, color='blue', linewidth=2)

# Removing degree labels (spokes around the chart)
ax.set_yticks([5, 10, 15, 20, 25])
ax.set_yticklabels(['5', '10', '15', '20', '25'], color="black", size=10, backgroundcolor='white')
ax.set_xticks([])  # Removing the angle ticks to eliminate degree labels

# Assigning specific colors to each label individually, with bold font
for label, angle in zip(labels, angles):
    ax.text(angle, 26, label, horizontalalignment='center', size=12, color=style_colors[label], weight='bold', backgroundcolor='white')

# Update the title position to create a larger gap
plt.title('Aquarium Communication Style Test Result', size=16, weight='bold', color='black', backgroundcolor='white', pad=50)

# Display the updated chart
plt.show()
