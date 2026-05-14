   select_single_item,
           elif choice == '5':
            print("Select from these Foods:")
            for food in foods:
                print(food)
            selected_food = input("\nType food name: ")
            select_single_item(selected_food)