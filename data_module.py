import pandas as pd
import matplotlib.pyplot as plt
dataset_df = pd.read_csv('Data/breakfast.csv')


def display_hypothesis():
    print("\n========== HYPOTHESIS ==========\n")
    print("Supermarkets World Wide are taking advantage of inflation to overcharge on necessary goods, " \
    "primarily to cover rising costs for labor, energy, and supply chains. ")


def display_dataset():
    print("\n========== FULL DATASET ==========\n")
    print(dataset_df)
 
 
def plot_country_items(country_name):
    country_df = dataset_df[dataset_df['Country'] == country_name]
 
    if country_df.empty:
        print("\nCountry " + country_name + " not found. Please check the spelling and capitals.")
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
    plt.xticks(rotation=60)
    plt.show()

def select_single_food(food_name):
    # Plot the selected food item for all countries
    for country in dataset_df['Country'].unique():
        country_df = dataset_df[dataset_df['Country'] == country]
        plt.plot(country_df['Month'], country_df[food_name], label=country)
 
    plt.title('Price of ' + food_name + ' - All Countries')
    plt.xlabel('Month')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()
    
def highest_lowest_countries():

    average_prices = {}

    for country in dataset_df['Country'].unique():

        country_df = dataset_df[dataset_df['Country'] == country]

        average = country_df['Breakfast_Basket_USD'].mean()

        average_prices[country] = average

    highest_country = ""
    lowest_country = ""

    highest_price = 0
    lowest_price = 999999

    for country in average_prices:

        if average_prices[country] > highest_price:
            highest_price = average_prices[country]
            highest_country = country

        if average_prices[country] < lowest_price:
            lowest_price = average_prices[country]
            lowest_country = country

    print("\n========== PRICE ANALYSIS ==========\n")

    print("Highest Average Basket Price:")
    print(highest_country, "-", round(highest_price, 2), "USD")

    print("\nLowest Average Basket Price:")
    print(lowest_country, "-", round(lowest_price, 2), "USD")
