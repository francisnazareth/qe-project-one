#Create a python program to draw barchart using seaborne libaries. 
import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}

# Create a bar plot
sns.barplot(x='Category', y='Values', data=data)

# Add title and labels
plt.title('Simple Bar Chart')
plt.xlabel('Category')
plt.ylabel('Values')

# Show plot
plt.show()
