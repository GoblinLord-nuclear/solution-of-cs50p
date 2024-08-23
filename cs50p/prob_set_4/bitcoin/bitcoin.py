import requests
import sys
import json
try:
    n=float(sys.argv[1])
    response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o=response.json()
    price=o["bpi"]["USD"]["rate_float"]
    print(f"${n*price:,.4f}")
except IndexError:
    sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()