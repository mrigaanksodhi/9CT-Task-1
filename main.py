from data_module import (
    display_hypothesis,
    display_dataset,
    plot_country_items,
    plot_all_country_basketprices,
    select_single_food,
    highest_lowest_countries,

)
import time
def typewrite(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.025)
    print()
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
 
 
def main_menu():
    while True:
        typewrite(" ══════════════════════════════════════════════════")
        typewrite("║ Data Viewer Interface - Breakfast foods tracker  ║")
        typewrite("║══════════════════════════════════════════════════║")
        typewrite("║  1. View hypothesis                              ║")
        typewrite("║  2. View full dataset                            ║")
        typewrite("║  3. View item prices for each country            ║")
        typewrite("║  4. View all country prices for breakfast basket ║")
        typewrite("║  5. Select single food for all countries         ║")
        typewrite("║  6. View Highest and Lowest Prices               ║")
        typewrite("║  7. Exit                                         ║")
        typewrite(" ══════════════════════════════════════════════════")
 
        choice = input("\nSelect an option (1-7): ")
 
        if choice == '1':
            display_hypothesis()
 
        elif choice == '2':
            display_dataset()
 
        elif choice == '3':
            print("Select from these Countries:")
            for country in countries:
                print(country)
            selectedcountry = input("\nType country name: ")
            plot_country_items(selectedcountry)
 
        elif choice == '4':
            plot_all_country_basketprices()
 
        elif choice == '5':
            print('Select from these Foods:')
            for food in foods:
                print(food)
            selectedfood = input('\nType food name: ')
            select_single_food(selectedfood)
        
        elif choice == '6':
            highest_lowest_countries()

        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Please choose between 1 and 7.")
 
 
if __name__ == "__main__":
    main_menu()
