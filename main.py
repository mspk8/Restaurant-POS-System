from functions.sales_functions import*


coupon_codes=load_coupons()
print("|| WELCOME TO KARACHI KABAB HOUSE || \n    __________________________ \n ")
user_name=input("Please Enter Your Name: ")

#flags
exit_status=False
invalid_msg=False


print(f"\n Welcome {user_name} !\n" )
user_cart=Cart() #creates user's cart instance
print(user_cart.get_cart_items())
while not exit_status:
      #flags
      in_main_menu=True
      cart_actions=False
      checkout_status=False

      
      choice=choice_menu_loop() #calls menu function
      if choice.lower()=="exit":
            print(f"Thank You {user_name}!")
            exit_status=True
            break #terminates loop if user inputs exit
      if (choice=="" or not choice.isdigit()) or (choice.isdigit() and ((int(choice)<1) or int(choice)>6)): #checks if input is invalid
            print("Invalid Input")
            continue #restarts loop from beginning in case of invalid input

      #reaches here if its a valid input
      leave_category_menu=False
      valid_input=True
      while not leave_category_menu: #inside menu category list, loops while leave status is false

            choice=int(choice)
            if choice==6:
                  if not user_cart.cart_items:
                        print("CART IS EMPTY, PLEASE ADD ITEMS TO PROCEED TO CART :) ")
                        break #user message and termination if cart is empty and user proceeds to cart actions. 
                  else: #cart has items and user proceeded to cart actions
                        cart_actions=True 
                        break #breaks out of current loop and enters cart_actions loop 
            else:
                  chosen_cat=Display_menu(choice) #any other input other than 6 --> display menu for the desired menu category 

            print(" | Enter Item Code to add item to cart \n | Enter 'M' to return to previous menu \n | Enter 'Exit' to cancel your order \n")
            item_choice=input("Enter >>> ")
            deciding_item_menu=category_menu_codes(str(choice))#fetches dictionary of desired menu
            if item_choice.lower()=="m":
                  leave_category_menu=True 
                  break #exits category menu and is not looped again due to positive flag
            if item_choice.lower()=='exit':
                  print(f"Thank You {user_name}")
                  exit_status=True
                  break #exits current loop and nothing is looped again due to positive exit flag
            if item_choice.lower() not in deciding_item_menu[0]: 
                  print("Invalid Code, Please Re-enter\n") 
                  continue #error message amnd retry for user if user enters item code that is not in the desired menu
            
            user_cart.add_items_tocart(item_choice.lower()) #reaches here with a valid item code and add item func is called


      while cart_actions and not exit_status: #begins cart actions loop if exit status is false

            #default purpose is to remove items from cart

            user_cart.get_cart_items()
            print(" | Enter Item code to remove item from Cart\n | Type 'M' to return to Menu \n | Type 'Done' to continue to checkout or 'Exit' to cancel order")
            while True: # loops until broken
                  cart_choice=input("Enter >>> ")
                  if cart_choice.lower()=='m':
                        break
                  elif cart_choice.lower()=='exit':
                        print(f"Thank You {user_name}!")
                        exit_status=True
                        break
                  elif cart_choice.lower()=='done':
                        checkout_status=True  # flag to initiate checkout

                  elif cart_choice.lower() in user_cart.cart_items.keys():
                        user_cart.Remove_item(cart_choice.lower())
                        print(user_cart.get_cart_items())
                        print(" | Enter Item code to remove item from Cart\n | Type 'M' to return to Menu \n | Type 'Done' to continue to checkout or 'Exit' to cancel order")

                  else:
                        print(f"Code {cart_choice} not found in Cart")
                        continue


                  while checkout_status: #begins checkout
                        user_cart.checkout()
                        exit_status=True 
                        cart_actions=False # turns active flags to opposite to finish session.
                        checkout_status=False
                  break
            break








 



      
      
