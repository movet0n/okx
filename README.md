# OKX API Fund Withdrawal

A basic guide to securely and efficiently withdraw funds from OKX using their API.

**Note**: One needs to whitelist addresses to be able to withdraw funds to them via API.

## Prerequisites

1. Create OKX API key, secret key, and passphrase:
   
   - Visit [https://www.okx.com/account/my-api](https://www.okx.com/account/my-api)

2. Clone or download the OKX project from GitHub.

## Installation

3. Install Python (if not already installed):

```bash
sudo apt install python3
```

4. Install pipenv on Ubuntu:

- More details can be found on the [Pipenv project page](https://pypi.org/project/pipenv/)

```bash
sudo apt install pipenv
```

5. Navigate to the OKX project folder.

6. Install dependencies:

```bash
pipenv install
```

7. Spawn a shell within the virtual environment:

```bash
pipenv shell
```

## Configuration

8. Update the `COLD_WALLET_ADDRESSES` list of addresses within the `main.py` file.

9. Update the `token`, `chain`, `min_amount`, `max_amount`, `fee`, and `sleep_duration` values within the `main.py` file.

## Usage

9. Run the `main.py` file to withdraw your funds:

```bash
python3 main.py
```

10. Monitor the output for any errors or confirmations.