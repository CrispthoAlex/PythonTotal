
"""
https://pypi.org/project/colored/

|> pip install colored

from colored import Fore, Back, Style
|> color: str = f'{Style.BOLD}{Fore.YELLOW}{Back.BLUE}'
|> print(f'{color}Background color blue with bold yellow text!{Style.reset}')

from colored import fore, back, style
|> color: str = f"{style(9)}{fore(0)}{back(5)}"
|> print(f'{color}Background color magenta with bold black text!{style("reset")}')

-------------------------------------------------------------------------------

pip install openpyxl

"""
