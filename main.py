import os
import random
import pandas as pd
from importer import name_to_index
df = pd.read_csv("data.csv")
won = False
selected = ""
checker = {
    0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False
}
checked = []
guessed = []


def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_info(name, column_index):
    row_index = name_to_index[name]
    row_info = df.iloc[row_index - 1]
    return row_info.iloc[column_index]


def get_selected():
    global selected
    selected_key, _ = random.choice(list(name_to_index.items()))
    selected = str(selected_key)
    # print(selected)


def guess(champ):
    global won
    w = 0
    for i in range(0, 8):
        # print(get_info(champ, i))
        # print(get_info(selected, i))
        if get_info(champ, i) == get_info(selected, i):
            checker[i] = True
            if get_info(champ, i) not in checked:
                checked.append(get_info(champ, i))
            for j in checker:
                if j == True:
                    w += 1
                    if w == 8:
                        print("Won")
                        won = True
                        break
def main():
    cls()
    get_selected()
    while not won:
        cls()
        print(selected)
        print(checked)
        print("Guessed:")
        print(guessed)
        print("\n \n")
        while True:
            guesser = input()
            try:
                guess(guesser.title())
                break
            except KeyError:
                print("Esse campeão não existe")

while True:
    main()
    won = False
    guessed = []
    checked = []
            

            