from data_module import(
    display_dataset_preview,
    display_single_country_averages,
    display_all_country_inflation,
   
)




def main_menu():
    while True:
        print("\n----Data Viewer Interface -----")
        print('1. View dataset')
        print("2. View Single country inflation")
        print('3. View all country inflation prices for breakfast basket')
        print('4. View ')
        print('5. Exit')

        choice = input("Select an option between 1-5").strip()

        if choice =='1':
            print('display_dataset_preview')
        elif choice == '2':
            print('\n Which country would you like to select:')
            print('1. Australia')
            print('2. Brazil')
            print("3. Canada")
            print('4. China')
            print('5. France')
            print('6. Germany')
            print('7. India')
            print('8. Italy')
            print('9. Japan')
            print('10. Mexico')
            print('11. Netherlands')
            print('12. New Zealand')
            print('13. Norway')
            print('14. Singapore')
            print('15. South Africa')
            print('16. South Korea')
            print('17. Spain')
            print('18. Sweden')
            print('19. United Kingdom')
            print('20. United States of America')

        elif choice == '3':
            print('display_all_country_inflation')
        elif choice == '4':
            print('')
        elif choice == '5':
            print('Exiting Program')
            break
        else:
            print('Invalid selection. Please choose a section between 1 and 5')

if __name__ == "__main__":
    main_menu()