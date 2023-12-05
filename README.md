# Phemex Margin Example

Using the testnet you can create a margin account and trade with leverage. This example shows how to open and close a position using the [example client from Phemex](https://github.com/phemex/phemex-python-api/).

## Quickstart

```
$ conda create -n margins python=3.10
$ conda activate margins
$ pip install -r requirements.txt
$ python main.py
```

## Environment Variables

```
# .env

# Testnet
PHEMEX_API_ID=
PHEMEX_API_SECRET=
```