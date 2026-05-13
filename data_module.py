import pandas as pd
import matplotlib.pyplot as plt
dataset_df = pd.read_csv('Data/breakfast.csv')


def display_hypothesis():
    print("\n========== HYPOTHESIS ==========\n")
    print("Supermarkets in Australia are taking advantage of inflation to overcharge on necessary goods.")


def display_dataset():
    print("\n========== FULL DATASET ==========\n")
    print(dataset_df)
 
 
def plot_country_items(country_name):
    # Filter the dataframe to only rows matching the country
    country_df = dataset_df[dataset_df['Country'] == country_name]
 
    if country_df.empty:
        print("\nCountry " + country_name + " not found. Please check the spelling.")
        return
 
    country_df.plot(
        kind='line',
        x='Month',
        y=['Milk (1L) USD', 'Bread (500g) USD', 'Eggs (12) USD',
           'Bananas (1kg) USD', 'Oranges (1kg) USD', 'Cheese (1kg) USD',
           'Tomatoes (1kg) USD', 'Chicken (1kg) USD'],
        title='Item Prices Over Time -' + country_name
    )
 
    plt.ylabel("Price (USD)")
    plt.show()
