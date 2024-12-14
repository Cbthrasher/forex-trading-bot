from forex_python.converter import CurrencyRates
import ccxt
import pandas as pd

# Forex rates test
c = CurrencyRates()
rate = c.get_rate('USD', 'EUR')
print(f"1 USD to EUR: {rate}")

# CCXT test
binance = ccxt.binance()
markets = binance.load_markets()
print(f"Binance supports {len(markets)} markets")

# Pandas test
data = {'Price': [1.1, 1.2, 1.15], 'Volume': [1000, 1200, 1100]}
df = pd.DataFrame(data)
print(df)
