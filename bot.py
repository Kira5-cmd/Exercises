#this is the bot that guesses our input()
#you can modify its time.

import time
import os
def bot_name(data, name="assistance bot : ",t=.1):
    time.sleep(t)
    print(name + data)

def bot(no, start, end):
    guess_no = (end - start)//2 + start
    time.sleep(.5)
    os.system("cls")
    bot_name(f"I guess {guess_no}", "Decoder Bot : ",0)
    
    if guess_no == no:
        bot_name(f"You craked it {guess_no} is the answer.",t=2)
        bot_name("congratulations!",t=.5)
        bot_name("Thankyou sir!","Decoder bot : ",t=2)
        
    elif guess_no > no:
        bot_name("guessing is high")
        bot_name("then i will take shorter num", "Decoder Bot : ")
        bot(no, start, guess_no)
        
    elif guess_no < no:
        bot_name("guessing is short.")
        bot_name("then i will take greater num", "Decoder Bot : ")
        bot(no, guess_no, end)

if __name__ == "__main__":
    bot(int(input("input any num:")), 0, 10000000000)