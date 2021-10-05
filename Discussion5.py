''' Discussion 5 '''
import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence) - 1):
		if sentence[i] == 'a' or sentence[i] == "A":
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
        if item not in self.items:
            self.items[item].append(item)       #UNKNOWN INDENTATION ERROR BUT EVERYTHING ELSE SHOULD BE GOOD CODE-WISE, SORRY :(
            return self.items[-1]


	# Returns the item in the warehouse with the lowest stock		
	def get_min_stock(self):
        #checks each key's value and chooses the lowest to return 
        lowest_stock = self.items[0]

        for lowest in self.items:     # does it check till the last one?
            if lowest.stock < lowest_stock.stock:
                lowest_stock = lowest
            return lowest_stock.name 


	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
        highest_stock = self.items[0]

        for highest in self.items:     # does it check till the last one?
            if highest.price > highest_stock.price:
                highest_stock = highest
            return highest_stock.name


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

        self.warehouse2 = Warehouse([self.item3, self.item4])
        self.warehouse3 = Warehouse([self.item1, self.item2])
	## Check to see whether count_a works
	def test_count_a(self):
        #test with no a's in the sentence 
        self.assertEqual(count_a("none"), 0)
        #test with a's in the sentence
		self.assertEqual(count_a("we have one a"), 1)
		self.assertEqual(count_a("now we have two of letter a"), 2)

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
        self.assertEqual(self.warehouse2.add_item("Cider"), "Cider")
        self.assertEqual(self.warehouse3.add_item("Water"), "Water")
        

	## Check to see whether warehouse correctly returns the item with the lowest stock
	def test_warehouse_min_stocks(self):
		self.assertEqual(self.warehouse2.get_min_stock(), "Cider")
        self.assertEqual(self.warehouse3.get_min_stock(), "Beer")
        

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(self.warehouse2.get_max_price(), "Cider")
        self.assertEqual(self.warehouse3.get_max_price(), "Beer")
        
		

def main():
	unittest.main(verbosity = 2)

if __name__ == "__main__":
	main()