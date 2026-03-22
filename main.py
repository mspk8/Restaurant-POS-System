from run_salesfuncs import Cart, Display_menu, choice_menu_loop, load_coupons, load_menu_categories


coupon_codes = load_coupons()
menu_categories = load_menu_categories()
cart_option = len(menu_categories) + 1

print("|| WELCOME TO KARACHI KABAB HOUSE ||\n    __________________________\n")
user_name = input("Please Enter Your Name: ")

exit_status = False
user_cart = Cart()

print(f"\nWelcome {user_name}!\n")

while not exit_status:
    choice = choice_menu_loop(menu_categories).strip()

    if choice.lower() == "exit":
        print(f"Thank you {user_name}!")
        break

    if (not choice.isdigit()) or (int(choice) < 1) or (int(choice) > cart_option):
        print("Invalid input. Please choose a valid menu option.\n")
        continue

    choice = int(choice)

    if choice == cart_option:
        if not user_cart.cart_items:
            print("CART IS EMPTY. Please add items before checkout.\n")
            continue

        while True:
            print(user_cart.get_cart_items())
            print(" | Enter item code to remove item from cart")
            print(" | Type 'M' to return to menu")
            print(" | Type 'Done' to continue to checkout")
            print(" | Type 'Exit' to cancel order")
            cart_choice = input("Enter >>> ").strip().lower()

            if cart_choice == "m":
                break
            if cart_choice == "exit":
                print(f"Thank you {user_name}!")
                exit_status = True
                break
            if cart_choice == "done":
                if not user_cart.cart_items:
                    print("CART IS EMPTY. Add at least one item to proceed.\n")
                    continue

                while True:
                    coupon_ask = input(
                        "Please enter a valid coupon code to avail discounts, or 'N' to skip: "
                    ).strip().upper()

                    if coupon_ask == "N":
                        coupon_discount = 0
                        cart_total, net_total, net_afterVAT = user_cart.CalcTotals()
                        break

                    if coupon_ask not in coupon_codes:
                        print("Invalid code. Type 'N' to skip or enter a valid code.")
                        continue

                    coupon_discount = coupon_codes[coupon_ask]
                    print(
                        f"COUPON CODE '{coupon_ask}' APPLIED | {coupon_discount}% DISCOUNT!!"
                    )
                    cart_total, net_total, net_afterVAT = user_cart.CalcTotals(coupon_discount)
                    break

                print("\n                                YOUR RECIPT")
                print("                            _____________________\n")
                user_cart.get_cart_items()
                print(
                    f"""
SUBTOTAL:              {cart_total:.2f}
Discount ({coupon_discount}%):   -{(coupon_discount / 100) * cart_total:.2f}
NET AFTER DISCOUNT:    {net_total:.2f}
VAT (5%):              {0.05 * net_total:.2f}
GRAND TOTAL:           {net_afterVAT:.2f}
Payment Method:        Cash
~ All prices are exclusive of VAT
Thank you for shopping with us!
"""
                )

                exit_status = True
                break

            removed = user_cart.Remove_item(cart_choice)
            if not removed:
                print(f"Code '{cart_choice}' not found in cart.\n")

        continue

    chosen_cat = Display_menu(choice)
    if not chosen_cat:
        print("Invalid category selection.\n")
        continue

    while True:
        print(" | Enter item code to add item to cart")
        print(" | Enter 'M' to return to previous menu")
        print(" | Enter 'Exit' to cancel your order\n")
        item_choice = input("Enter >>> ").strip().lower()

        if item_choice == "m":
            break
        if item_choice == "exit":
            print(f"Thank you {user_name}!")
            exit_status = True
            break

        added = user_cart.add_items_tocart(item_choice)
        if not added:
            print("Invalid item code. Please re-enter.\n")
