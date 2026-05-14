from data_module import (
    display_hypothesis,
    display_dataset,
    plot_country_items,
    plot_all_country_basketprices,
 
)
 
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
        print(" ═════════════════════════════════════════════════")
        print("║ Data Viewer Interface - Breakfast foods tracker ║")
        print("║═════════════════════════════════════════════════║")
        print("║  1. View hypothesis                             ║")
        print("║  2. View full dataset                           ║")
        print("║  3. View item prices for each country           ║")
        print("║  4. View all country prices for breakfast basket║")
        print("║  5. Select single food for all countries        ║")
        print("║  6. Exit                                        ║")
        print(" ═════════════════════════════════════════════════")
 
        choice = input("\nSelect an option (1-6): ")
 
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
 

 
        elif choice == '6':
            print("Exiting program.")
            break
 
        else:
            print("Invalid selection. Please choose between 1 and 6.")
 
 
if __name__ == "__main__":
    main_menu()