# Crypto
Crypto and Altcoins stuff

Some python code dedicated to Altcoins.

## General

## Install

- Install dependancies :
`pip install --user -r requirements.txt`

- For setting a specific conda environnment :
```
conda create -n python3 python=3.6 anaconda
source activate python3
```

- Copy example.xml file somewhere and rename it to something else.
- You will use this file using `--params file.xml`

### Support

Those tools are still in active dev, but we try to support :
- binance (working)
- kucoin (not so far)
- poloniex (in progress)
- gdax (in progress)

### Binance

Binance is one of the best trading platform.
If you don't have an account yet, please use my referral link :
https://www.binance.com/?ref=18697575

- Generate API key & secret https://www.binance.com/userCenter/createApi.html
- Add to your config file

- This code uses python-binance SDK - https://github.com/sammchardy/python-binance
- Documentation : https://python-binance.readthedocs.io/en/latest/
- Binance fees : https://www.binance.com/fees.html

### KuCoin

In progress

- This code uses python-kucoin SDK - https://github.com/sammchardy/python-kucoin
- Documentation : https://python-kucoin.readthedocs.io

### Poloniex

In progress

- Generate API key & secret https://poloniex.com/apiKeys
- Add to your config file

- This code uses poloniex Aula13 SDK - https://github.com/Aula13/poloniex
- Poloniex API documentation here https://poloniex.com/support/api/

### GDAX

This code use GDAX danpaquin SDK : https://github.com/danpaquin/gdax-python

### Bitfinex (not yet)

- Use public API
- https://github.com/scottjbarr/bitfinex

## Portfolio

Show a status of your finance portfolio in real-time, with pending transactions

- Launch : `python portfolio_watch.py --params ../crypto.xml`
To see dust assets (< 5 usd), use `--dust`

```
    ---------- Portfolio ----
          quantity       eth       btc     usd Percent
    BNB      0.869  0.012123  0.001111   12.64      2%
    BTC      0.016  0.172864  0.015832  180.25     22%
    ...

    ---------- Active Trades ----
           quantity    target     price  side   type
    symbol
    OMGBTC    2.500  0.001915  0.001613  SELL  LIMIT
    ...

```

## Market watch

Record Binance real time market price in a csv file for further analysis

- Update output line in your conf file
- Launch : `python market_watch.py --params ../crypto.xml --loop 10`
- File is updated every 10sec

# Market history (works with binance, kucoin and poloniex)

Record 5 minutes candles for further analysis (and model training)
On first launch, save historical data since exchange opening
If relaunch, it updates file since last record

- Launch : `python get_historical_klines.py --params ../crypto.xml`

Can launch with a special pair (exchange dependant) `--pair ETHBTC` or on a given exchange `--exchange binance`.

```
$ head -n 3 crypto/history/binance/history_BNBBTC.csv
time,Open,High,Low,Close,Volume
2017-07-14 04:00:00,5e-05,5.3e-05,1e-05,3.615e-05,1469912.0
2017-07-14 04:05:00,3.9e-05,4e-05,3.655e-05,4e-05,1031546.0
```

Be carefull, it can be heavy
```
du -hs crypto/history/*
376M    crypto/history/binance
119M    crypto/history/kucoin
734M    crypto/history/poloniex/
``
