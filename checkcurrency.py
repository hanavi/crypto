#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

with open("api_key.txt") as fd:
    api_key = fd.readline().strip()

api_url = "https://api.nomics.com/v1/"
config_dir = "/home/james/files/projects/crypto"


def get_api_currencies():

    cmd = api_url + f"currencies?key={api_key}"
    req = requests.get(cmd)

    if req.status_code == 200:
        return req.json()
    else:
        print(req.content)
        sys.exit(1)


def get_api_prices():

    cmd = api_url + f"prices?key={api_key}"
    req = requests.get(cmd)

    if req.status_code == 200:
        return req.json()


def print_currency_value(local_currency, currency_prices):

    output = "Currency".rjust(9)
    output += "Value".rjust(9)
    output += "Qty.".rjust(14)
    output += "Cost".rjust(10)

    print()
    print("="*50)
    print(output)
    print("-"*50)
    total = 0
    total_cost = 0
    for currency_id, currency_info in local_currency.items():

        currency_amount = currency_info['amount']
        currency_cost = currency_info['cost']
        total_cost += int(currency_cost.replace("$", ""))

        for entry in currency_prices:

            if entry['currency'] == currency_id:

                value = float(entry['price'])*currency_amount
                total += value
                output = ""
                output += f" {currency_id}".rjust(6)
                output += ": " + f"${value:.2f}".rjust(11)
                output += "   " + f"{currency_amount}".rjust(11)
                output += f"{currency_cost}".rjust(10)

                print(output)
                break

    profit = total - total_cost
    profit_percent = profit/total_cost*100

    print("-"*50)
    print(f"  Total:    ${total:0.2f}")
    print(f"   Cost:    ${total_cost:0.2f}")
    print("-"*50)
    print(f" Profit:    ${profit:0.2f}", end='')
    print(f"{profit_percent:0.1f}%".rjust(23))
    print("="*50)
    print()


def load_local_data():

    fname = f"{config_dir}/crypto.json"

    with open(fname) as fd:
        data = fd.read()

    data = json.loads(data)
    return data


def main():

    local_data = load_local_data()
    prices = get_api_prices()
    print_currency_value(local_data, prices)


if __name__ == "__main__":
    main()
