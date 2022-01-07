# This is a sample Python script.
import logging
from telegram.ext import *
# api_key = os.environ['API_KEY']
api_key = '5066015679:AAFJzkzf6dN513gH06zU_uVYRlKsS22vqlY'
updater = Updater(api_key, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
