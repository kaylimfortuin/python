
class ctuStock:
    def __init__(self, shopName="Default", shopLocation="Default", customers=0, sales=0, returns=0):
        self.shopName = shopName
        self.shopLocation = shopLocation
        self.customers = customers
        self.sales = sales
        self.returns = returns

    def changeShopName(self, newShopName):
        self.shopName = newShopName

    def changeShopLocation(self, newShopLocation):
        self.shopLocation = newShopLocation

    def displayShopInfo(self):
        print(f"Shop Name: {self.shopName}")
        print(f"Shop Location: {self.shopLocation}")
        print(f"Number of Customers: {self.customers}")
        print(f"Current Sales: {self.sales}")
        print(f"Returns: {self.returns}")
        print('-'*20)
        print('-'*20)

# Create four objects representing the four shops
shop1 = ctuStock()

shop2 = ctuStock()

shop3 =ctuStock()

shop4 = ctuStock()

# List of shops
shops = [shop1, shop2, shop3, shop4]
