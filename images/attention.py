import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Use LaTeX font
mpl.rcParams['text.usetex'] = True
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'

# Example sentence in the source language
source_sentence = ["The", "cat", "sat"]
# Example sentence in the target language
target_sentence = ["Le", "chat", "s'est", "assis"]

# Example attention matrix (fictional values for illustration)
attention_matrix = np.array([
    [0.8, 0.1, 0.1, 0.0],
    [0.2, 0.6, 0.1, 0.1],
    [0.0, 0.3, 0.5, 0.2]
])

# Create the heatmap with LaTeX font and source and target switched
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(attention_matrix.T, annot=True, cmap='viridis', xticklabels=source_sentence, yticklabels=target_sentence)

# Move x-axis labels to the top
heatmap.xaxis.set_label_position('top')
heatmap.xaxis.tick_top()

# Rotate y-axis labels
plt.yticks(rotation=0)

# Keep x-axis labels at 0 degrees
plt.xticks(rotation=0)

# Set labels with LaTeX font
plt.xlabel(r'\textbf{Source Sentence}')
plt.ylabel(r'\textbf{Target Sentence}')
plt.title(r'\textbf{Attention Matrix Heatmap}')
plt.savefig("attention.png")
# Show the plot
plt.show()