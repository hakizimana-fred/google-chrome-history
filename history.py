import sqlite3
import pandas as pd
from tabulate import tabulate
import os
import platform


def main():
    if platform.system() != 'Linux':
        print('Your google chrome path might be different')
        return
        
    chrome_path = f"{os.path.expanduser('~')}/.config/google-chrome/Default/History"
    con = sqlite3.connect(chrome_path)
    c = con.cursor()
    c.execute("SELECT * FROM urls")

    results = c.fetchall()

    count = 0
    histories = []

    for history in results:
        histories.append(history)
        count += 1
        if count == 100:
            break
    c.close()

    pd_data = pd.DataFrame(histories)
    return print(tabulate(pd_data, headers='keys', tablefmt='grid', showindex=False))


if __name__ == '__main__':
    main()