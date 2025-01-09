import pandas as pd

input_file = 'letterboxd-anora.csv'
output_file = 'letterboxd-anora-cleaned.csv'


reviews_df = pd.read_csv(input_file)


reviews_df['reviews'] = reviews_df['reviews'].str.replace('"', '', regex=False)

reviews_df.to_csv(output_file, index=False, encoding='utf-8')