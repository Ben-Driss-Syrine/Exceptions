"""
SelfCheckout within main ;
    1. it allows the user to scan up to 12 items
    2. paying methods
    -> while dealing with unexpected errors from users

"""


def main():
    global order, cash
    print(
        " Thank you for shopping with TheDarkWeb 2.0 \n Please insert your items' prices into our App interface \n You can not go over 12 items thank you for understanding")

    maximum = 0
    order_total = 0
    scanning = False
    while not scanning and maximum < 12:
        try:
            order = input("Scan your item :  ")
            if float(order) <= 0 or not isinstance(order, str):
                raise ValueError
        except ValueError:
            if order == 'pay':
                break
            else:
                if not isinstance(order, float):
                    print(
                        f"Scanning failed: Self Checkout don't recognize || {order} || as a numerical item, try again")
                elif float(order) < 0:
                    print(f"Scanning failed:Self Checkout can't take || {order} || as a  negative item, try again")
        else:
            order_total += float(order)
            maximum += 1
    scanning = True

    paying = True
    while paying:
        try:
            print(f"your total = {order_total} $")
            cash = float(input("Insert your cash payment$: "))

            if float(cash) > order_total or float(cash)< order_total:
                raise ArithmeticError
        except ValueError:

            print(f"Payment failed: SelfCheckout can't accept this payment, please try again")
        except ArithmeticError:
            if float(cash) < 0:
                print(f"||{cash}|| :make sure you enter non negative cash ")
            elif float(cash) < order_total:
                print(f"||{cash}|| is less then total, make sure your cash is equal to your total")
            elif float(cash) > order_total:
                print(f"||{cash}|| is greater then total, make sure your cash is equal to your total")


        else:

            if float(cash) == order_total:
                print(f"Payment succeeded: Thank you for shopping with us")

                paying = False


if __name__ == '__main__':
    main()
