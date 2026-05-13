from data_module import (
    display_hypothesis,
    display_dataset,
    plot_country_items,
    plot_all_country_basket_prices,
)

countries = [
    "Australia", "Brazil", "Canada", "China", "France",
    "Germany", "India", "Italy", "Japan", "Mexico",
    "Netherlands", "New Zealand", "Norway", "Singapore",
    "South Africa", "South Korea", "Spain", "Sweden",
    "United Kingdom", "United States"
]


def main_menu():
    while True:
        print(" ═════════════════════════════════════════════════")
        print("║ Data Viewer Interface - Breakfast foods tracker ║")
        print("║═════════════════════════════════════════════════║")
        print("║  1. View hypothesis                             ║")
        print("║  2. View full dataset                           ║")
        print("║  3. View item prices for each country           ║")
        print("║  4. View all country prices for breakfastbasket ║")
        print("║  5. Exit                                        ║")
        print(" ═════════════════════════════════════════════════")
        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            display_hypothesis()

        elif choice == '2':
            display_dataset()

        elif choice == '3':
            print("\nCountries:")
            for country in countries:
                print(country)
            selectedcountry = input("\nType country name: ")
            plot_country_items(selectedcountry)

        elif choice == '4':
            plot_all_country_basket_prices()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid selection. Please choose between 1 and 5.")


if __name__ == "__main__":
    main_menu()