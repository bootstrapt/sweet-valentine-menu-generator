# Sweet Valentine Bakery Menu Generator
Generates .png files to display on TVs as in store menus at Sweet Valentine Bakery in Carson. GPT-4 was used to generate a script to automate launching Chrome and capturing a screenshot.

## Pre-requisites
- (optional) pyenv
- Python 3.11

## Installation
`$ pip install -r requirements.txt`

## Usage
- updates the `MENUS` list in `output-menus.py` with the name of html files in `./html`
- run `$ python output-menus.py`