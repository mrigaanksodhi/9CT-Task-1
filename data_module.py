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


def plot_all_country_basketprices():
    average_prices = []
    country_names = []
 
    for country in dataset_df['Country'].unique():
        country_df = dataset_df[dataset_df['Country'] == country]
        avg = country_df['Breakfast_Basket_USD'].mean()
        average_prices.append(avg)
        country_names.append(country)
 
    plt.bar(country_names, average_prices, color='blue')
    plt.title('Average Breakfast Basket Price - All Countries')
    plt.xlabel('Country')
    plt.ylabel('Price (USD)')
    plt.show()

def select_single_item(food_name):
    for country in dataset_df['Country'].unique
        country_df = dataset_df