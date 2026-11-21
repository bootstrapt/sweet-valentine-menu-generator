# Sweet Valentine Bakery Menu Generator
Generates .png files to display on TVs as in store menus at Sweet Valentine Bakery in Carson.
Output is 3840x2160 (4K) for the TCL 58S470G TVs.

## Pre-requisites
- (optional) pyenv
- Python 3.11
- Google Chrome (Selenium finds the matching chromedriver automatically)

## Installation
`$ pip install -r requirements.txt`

## Usage
1. Edit prices/items in `menu.json`. Each screen (`menu-left`, `menu-right`) has a `sidebar`
   (shown under the logo) and up to 3 `columns` of categories. One category alone in a column is
   centred vertically; two stacked categories share the column height.
2. Run `$ python output-menus.py`. This regenerates `html/<screen>.html` from `menu.json` and
   saves `output-menus/<screen>.png`.

Don't edit `html/menu-left.html` / `html/menu-right.html` by hand — they are overwritten on each run.
Styling lives in `html/css/style.css`.

Options:
- `--menu menu-left` — only generate one screen
- `--shrink-left 0.9` / `--shrink-right 0.9` — shrink that screen's content to 90%
- `--stretch-bg` — stretch the background image to fill the screen
- `--no-build` — screenshot the existing HTML without regenerating it from `menu.json`

To only regenerate the HTML (e.g. to preview in a browser): `$ python build_menus.py`
