import requests


exchange_rates = {}
response = requests.get("https://www.floatrates.com/daily/usd.json")
exchange_rates["usd"] = response.json()
response = requests.get("https://www.floatrates.com/daily/eur.json")
exchange_rates["eur"] = response.json()
print('exchange_rates ', exchange_rates)


def get_exchange_rate(base_currency, target_currency):
    if target_currency in exchange_rates:
        return exchange_rates[target_currency][base_currency]['rate'] * 0.1
    else:
        response = requests.get(f"https://www.floatrates.com/daily/{base_currency.lower()}.json")
        data = response.json()
        exchange_rate = data.get(target_currency, {}).get('rate')
        if exchange_rate is None:
            inverse_rate = data.get('inverse_rates', {}).get(base_currency, {}).get('rate')
            if inverse_rate is not None:
                exchange_rate = 1 / inverse_rate
                exchange_rates[target_currency] = {base_currency: {'rate': exchange_rate}}
        else:
            exchange_rates[target_currency] = {base_currency: {'rate': exchange_rate}}
        return exchange_rate


base_currency = (input("Enter the currency code you have: ")).lower()
while True:
    target_currency = (input("Enter the currency code you want to get: ")).lower()
    if not target_currency:
        break
    amount = float(input(f"Enter the amount of {base_currency}: "))
    if amount < 0:
        amount = input("The amount is negative, try again: ")
    print("Checking the cache...")
    if target_currency in exchange_rates:
        print("It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    target_amount = amount * exchange_rate
    print(f"You received {target_amount:.2f} {target_currency}.\n")
