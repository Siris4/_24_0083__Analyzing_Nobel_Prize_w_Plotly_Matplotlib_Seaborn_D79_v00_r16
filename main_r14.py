import pandas as pd

# Load the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0083__Day79_Analyzing_Nobel_Prize_w_Plotly_Matplotlib_Seaborn__240827\NewProject\r00-r09 START\r00_env_START\nobel_prize_data.csv"
df = pd.read_csv(file_path)

# Filter the dataset to include only prizes in the field of Economics
economics_prizes = df[df['category'] == 'Economics']

# Find the year of the first prize in Economics
first_economics_prize_year = economics_prizes['year'].min()

# Display the result
print(f"The first Nobel Prize in Economics was awarded in: {first_economics_prize_year}")