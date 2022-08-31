from random import randint
from pyfiglet import Figlet
import emoji

fglt = Figlet()
fglt.setFont(font = "big")
print(fglt.renderText("Guess Number"))

def main():
    print(emoji.emojize("########### :large_blue_diamond: :game_die::game_die: :large_orange_diamond: ###############"))
    input_game()
    
def input_game():
    while True:
        try:
            print(emoji.emojize("Enter the number guess range :keycap_0:  to :infinity: : "))
            rng = int(input(emoji.emojize("---> ")))
            if rng > 0 :
                print(emoji.emojize("###########  Let's go ################"))
                print(emoji.emojize("###########  :large_blue_diamond: :grinning_face: :large_orange_diamond: ################"))
                break
        except ValueError:
            print(emoji.emojize(":no_entry:"))
            pass

    rndm = randint(1, rng)
    lvl = int(input("Level: "))
    i = 0
    n = 1
    while i < lvl:
        try:
            print(f"You are allowed to guess up to {lvl - i} times")
            print(emoji.emojize("----------------- :nine_o’clock: ------------------"))
            gss = int(input("Guess: "))
            if gss > 0 :
                if gss < rndm:
                    print(emoji.emojize("Too small! :expressionless_face:"))
                    i += 1
                    n += 1
                elif gss > rndm:
                    print(emoji.emojize("Too large! :expressionless_face:"))
                    i += 1
                    n += 1
                else:
                    print(emoji.emojize(":full_moon_face: Just right!!!:OK_hand:"))
                    print(emoji.emojize("       :1st_place_medal::1st_place_medal::1st_place_medal:"))
                    print(emoji.emojize(f":game_die: No. of Guess :game_die: --> {n}"))
                    break
        except ValueError:
            print(emoji.emojize(":no_entry:"))
            pass

    print(emoji.emojize("----------------- :END_arrow: ------------------"))
    if lvl == i :
        print(emoji.emojize("You lost :crying_face:"))
    print(emoji.emojize("---------------------------------------"))

    exit = input("Do you want to leave? (Y/N) :").casefold()
    if exit == "n" :
        print()
        main()
    else:
        input("please enter to exit ...")
        return

main()