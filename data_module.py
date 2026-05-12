import pandas as pd
dataset_df = pd.read_csv('Data/breakfast.csv')


def display_dataset_preview():
    print("\n========== FULL DATASET ==========")
    print(dataset_df)

def display_single_country_averages(country_name):
    