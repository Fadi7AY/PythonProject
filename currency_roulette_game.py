# from currency_converter import CurrencyConverter
import random
import app
import requests


formatted_rate=0
def get_money_interval():

   # global formatted_rate

   url = 'https://api.exchangerate.host/convert?from=USD&to=ILS'
   response = requests.get(url)

   if response.status_code == 200:
        data = response.json()
        current_exchange_rate = data['info']['rate']

        random_number = random.randint(1, 100)
        formatted_rate= float(f"{current_exchange_rate:.2f}")
        usd_ils = formatted_rate*random_number
        #print("The current USD to ILS rate is :\n",formatted_rate)
        print(f"\nyou will need to guess how much {random_number} USD is equal in ILS \n ")
        return float(usd_ils)  # the number is in USD

   else :
       print("Something is wrong ! Try again later")
       return False




def get_guess_from_user():

    user_guess = input(f"Enter a guess :\n")

    while True:

        if app.is_float(user_guess):
            user_guess = float(user_guess)
            return user_guess
        user_guess=input(f"Invalid input , Enter a number\n")


def is_list_equal(difficulty):
    allowed_difference = 10 - (difficulty)
    money=get_money_interval()
    user_guess =get_guess_from_user()
    if abs(money-user_guess)<=allowed_difference :
        print("There is a match")
        return  True
    print("No match")
    return  False


def play(difficulty):

    # get_money_interval()
    # get_guess_from_user()
    # user_rate_guess = is_list_equal()
    if is_list_equal(difficulty) :
        return True
    return False




