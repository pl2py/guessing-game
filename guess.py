#Hour 23 Exercise  guess.py
#guessing-game
"""
   guessing-game
"""
from random import randint


def main():
        """
        """
        print "Guess a number from 0 to 10"
        num=randint(0,10)
        print 'num=', num

        while True:
                print
                guess=raw_input("Enter your guess:")
                try:
                   guess=int(guess)
                   print 'guess=', guess
                except:
                   print "Sorry, not a number!"
                   continue
                #endtry
                if guess==num:
                   print "That's correct!"
                   break
                else:
                   print "Keep trying..."     
                #endif
        #endwhile
#enddef main()
                   
if __name__=="__main__":
        main()
