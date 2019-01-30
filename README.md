# Unchained Ledger


### How to launch:

```shell
git clone https://github.com/ideal-money/unchained-ledger.git

cd unchained-ledger

virtualenv -p python3.6 venv
. venv/bin/activate

# Just for first time
pip install -e .
export FLASK_APP=node
export FLASK_ENV=development

# For running app, type this command
flask run
```
