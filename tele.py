# import requests

# def func(code):
#     try:
#         r = requests.get(f"https://www.freeforexapi.com/api/live?pairs={code}")
#         response = r.json()
#         rate = response["rates"][code]["rate"]
#         return f"{code} course of currency  {rate}"
#     except:
#         return "We couldn't find data about it"



import requests

# USD
# EUR
# RUB
# TRY
# KZT


def get_rates():
    r = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    our_rates = {}
    data = r.json()
    for rate in data:
        rate_code = rate["Ccy"]
        if rate_code in ["USD", "EUR", "RUB", "TRY", "KZT"]:
            our_rates[rate_code] = rate
    return our_rates