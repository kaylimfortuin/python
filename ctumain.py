
from ctuclass import shops

def main():
    while True:
        # Main menu
        print("Welcome to CTU Technologies")
        print()
        print("1. Shop Management")
        print("2. Sales")
        print("3. Returns")
        print("4. Stock")
        print("99. Exit")
        print()
        mainMenuChoice = int(input("Select an option or 99 to exit: "))

        if mainMenuChoice == 1:
            # Shop management menu
            while True:
                print("Shop Management Menu")
                print("1. Change shop Name")
                print("2. Change shop location")
                print("3. Display current shops")
                print("4. Display all shops information")
                print("0. Back")
                print()
                shopManagementChoice = int(input("Select an option: "))

                if shopManagementChoice == 1:
                    # Change shop name
                    for i, shop in enumerate(shops):
                        print(f'{i+1}. {shop.shopName}, {shop.shopLocation}')
                    shopIndex = int(input("Select an option: ")) - 1
                    newShopName = input("Type in new shop name: ")
                    shops[shopIndex].changeShopName(newShopName)
                    print("Shop name successfully changed to", newShopName)
                    
                elif shopManagementChoice == 2:
                    print()
                    # Change shop location
                    for i, shop in enumerate(shops):
                        print(f"{i+1}. {shop.shopName}, {shop.shopLocation}")
                    shopIndex = int(input("Select a shop to change its location: ")) - 1
                    newShopLocation = input("Enter the new shop location Free state, Gauteng, Limpopo, KZN: ")
                    shops[shopIndex].changeShopLocation(newShopLocation)
                    print("Shop location successfully changed to", newShopLocation)
                elif shopManagementChoice == 3:
                    # Display current shops
                    for i, shop in enumerate(shops):
                        print(f"{i+1}. {shop.shopName}, {shop.shopLocation}")
                elif shopManagementChoice == 4:
                    # Display all shops information
                    for i, shop in enumerate(shops):
                        print(f"Shop {i+1}:")
                        shop.displayShopInfo()
                        
                elif shopManagementChoice == 0:
                    break
        elif mainMenuChoice == 2:
            # Sales menu (not implemented)
            pass
        elif mainMenuChoice == 3:
            # Returns menu (not implemented)
            pass
        elif mainMenuChoice == 4:
            # Stock menu (not implemented)
            pass
        elif mainMenuChoice == 99:
            break

if __name__ == "__main__":
    main()
