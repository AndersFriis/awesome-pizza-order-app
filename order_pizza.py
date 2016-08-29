PIZZA = ( 
{

	"name": "Cheese Pizza",
	"cost": 5.00
},

{	"name": "Pepperoni",
	"cost": 7.50
},
)



def dispaly_invalid_option(menu_selection):
	if menu_selection.isdigit():
		print("\n{} is an invalid option, please try again".format(menu_selection))
	else:
		print("\n{} is not a number, please enter a number from the menu above".format (menu_selection)

def add _to_order()
"""

Prompts for adding pizza to order

"""
while True:
	print("\n")
	print ("0: Go back")
for index, pizza in enumerate(PIZZAS)
	print ("{}".format(pizza["name"]))

	pizza_selection = input("\nWhich pizza would you like to order?")

def main ():
	MENU ITEMS = (
		"1: Add Pizza to Order",
		"2: Remove Pizza from Order",
		"3 Display Order",
		"0: Exit",

	)

		while True
		
		for menu_item in MENU_ITEMS:
			print (menu_item)

		for meny_selection = input("\nplease select an option from above?")
		
		if meny_selection == "0":	
			break

	

	if menu_selection =="0":
		pass
	elif menu_selection =="1":
		add-to-order()
		pass
	elif menu_selection =="2":
		pass
	elif menu_selection =="3":
		pass
	elif menu_selection =="4":
		pass
	else:
		dispaly_invalid_option(menu_selection)


if __name__ == '__main__':
	main()			