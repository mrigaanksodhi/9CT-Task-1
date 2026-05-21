import pandas as pd
import matplotlib.pyplot as plt
dataset_df = pd.read_csv('Data/breakfast.csv')
pd.set_option('display.max_rows', None)     
pd.set_option('display.max_columns', None)   
pd.set_option('display.max_colwidth', None)  
countries = [
    "Australia", "Brazil", "Canada", "China", "France",
    "Germany", "India", "Italy", "Japan", "Mexico",
    "Netherlands", "New Zealand", "Norway", "Singapore",
    "South Africa", "South Korea", "Spain", "Sweden",
    "United Kingdom", "United States"
]
 
foods = [
    'Milk (1L) USD', 'Bread (500g) USD', 'Eggs (12) USD',
    'Bananas (1kg) USD', 'Oranges (1kg) USD',
    'Cheese (1kg) USD', 'Tomatoes (1kg) USD', 'Chicken (1kg) USD'
]
 

def display_hypothesis():
    print("========== HYPOTHESIS ==========")
    print("Supermarkets worldwide are taking advantage of inflation to overcharge on necessary goods, primarily to cover rising costs for labor, energy, and supply chains. ")


def display_dataset():
    print("========== FULL DATASET ==========")
    print(dataset_df)
 
 
def plot_country_items(country_input):
    country_name = None
    for country in countries:
        if country.lower() == country_input.lower():
            country_name = country

    if country_name is None:
        print("Country " + country_input + " not found. Please check the spelling.")
        return

    country_df = dataset_df[dataset_df['Country'] == country_name]
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

def select_single_food(food_input):
    matched_food = None
    for food in foods:
        if food_input.lower() in food.lower():
            matched_food = food

    if matched_food is None:
        print("Food item " + food_input + " not found. Please check the spelling.")
        return

    for country in dataset_df['Country'].unique():
        country_df = dataset_df[dataset_df['Country'] == country]
        plt.plot(country_df['Month'], country_df[matched_food], label=country)

    plt.title('Price of ' + matched_food + ' - All Countries')
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

    print("========== PRICE ANALYSIS ==========")

    print("Highest Average Basket Price:")
    print(highest_country, "-", round(highest_price, 2), "USD")

    print("Lowest Average Basket Price:")
    print(lowest_country, "-", round(lowest_price, 2), "USD")
