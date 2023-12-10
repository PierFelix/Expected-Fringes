"""
Part of repository: 
https://github.com/PierFelix/Interfometer-Refractive-Index-Measurements

@author: PierFelix
"""

from traceback import format_exc
# from expected_fringes import *
# from refractiveindex_calculations import *
from data import *

try:
    import eel
except Exception as e:
    print("Following exception occurred: ")
    print(format_exc())
    # Pause on exception before closing
    print("\nIf Eel does not work, use the designated .py files themself\nAnything inside the last if statement of the files can be edited.\n")
    input("Press Enter to close the application")
    exit()

# Start the localhost
try:
    if __name__ == "__main__":
        eel.init('web_interface')

        eel.start('main.html', mode='custom-app', cmdline_args=['--start-maximized'])

except Exception as e:
    print("Following exception occurred: ")
    print(format_exc())
    # Pause on exception before closing
    input("Press Enter to close the application")
    exit()
