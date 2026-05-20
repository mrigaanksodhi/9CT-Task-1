# Breakfast Basket Price Tracker

## Overview
This project helps to analyse the cost of breakfast food items across 20 countries from October 2025 to March 2026. It investigates whether supermarkets World Wide are taking advantage of inflation to overcharge on necessary goods.

## Files

### main.py
This is the file you run to start the program. It displays a menu and lets the user navigate the data viewer.


### data_module.py
This file contains all the functions that read and display the data. It is imported by main.py and shouldn't be run directly on its own.

### Data/breakfast.csv
The dataset used in this project. It contains the price of 8 breakfast food items across 20 countries over 6 months.

---

## How to Navigate the Program

When you run main.py, you will see this menu:


Data Viewer Interface - Breakfast foods tracker  

1. View hypothesis                              
2. View full dataset                            
3. View item prices for each country            
4. View all country prices for breakfast basket
5. Select single food for all countries        
6. View Highest and Lowest Prices  
7. Exit                                        


### Option 1 - View hypothesis
This option prints the hypothesis for this project.

### Option 2 - View full dataset
Prints the entire breakfast.csv dataset to the terminal.

### Option 3 - View item prices for each country
Asks you to type a country name from the list provided, then displays a line graph showing the price of each food item over the 6 months for that country.

### Option 4 - View all country basket prices
Displays a bar graph comparing the average breakfast basket price across all 20 countries.

### Option 5 - Select single food for all countries
Asks you to type a food item from the list provided, then displays a line graph showing the price of that food item across all 20 countries over the 6 months.

### Option 6 - View what country has the highest and lowest breakfast basket price
Displays the countries with the highest and lowest average USD prices for breakfast basket. 

### Option 7 - Exit
Exits the program, ending the loop.

## Countries Available
These are the countries that are displayed in the dataset and can be chosen in Option 3: Australia, Brazil, Canada, China, France, Germany, India, Italy, Japan, Mexico, Netherlands, New Zealand, Norway, Singapore, South Africa, South Korea, Spain, Sweden, United Kingdom, United States

## Food Items Available 
These are the food items that can be chosen in Option 5: 
Milk (1L) USD
Bread (500g) USD
Eggs (12) USD
Bananas (1kg) USD
Oranges (1kg) USD
Cheese (1kg) USD
Tomatoes (1kg) USD
Chicken (1kg) USD

