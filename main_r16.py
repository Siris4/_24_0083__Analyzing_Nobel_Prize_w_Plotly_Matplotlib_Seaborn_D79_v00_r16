import pandas as pd
import plotly.express as px

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Group by category and sex, and count the occurrences
gender_category_counts = df.groupby(['category', 'sex']).size().reset_index(name='count')

# Create a stacked bar chart
fig = px.bar(gender_category_counts,
             x='category',
             y='count',
             color='sex',
             barmode='stack',  # Stacks the bars on top of each other
             labels={'count': 'Number of Prizes', 'category': 'Category'},
             title='Nobel Prizes Awarded by Category and Gender')

# Show the figure
fig.show()
