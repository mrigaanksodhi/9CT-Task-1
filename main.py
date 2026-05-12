from data_module import (
    display_dataset_preview,
    display_single_country_averages,
    display_all_country_inflation,
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
        print("\n------ Data Viewer Interface ------")
        print("1. View full dataset")
        print("2. View single country average price")
        print("3. View all country breakfast basket average prices")
        print("4. Exit")

        choice = input("\nSelect an option (1-5): ")

        if choice == '1':
            display_dataset_preview()

        elif choice == '2':
            print("\nCountries:")
            for country in countries:
                print(country)
            selected = input("\nType country name: ")
            display_single_country_averages(selected)

        elif choice == '3':
            display_all_country_inflation()

        elif choice == '4':
            print("Exiting program.")
            break

        else:
            print("Invalid selection. Please choose between 1 and 4.")


if __name__ == "__main__":
    main_menu()