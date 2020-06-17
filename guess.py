#Hour 23 Exercise  guess.py
#guessing-game
"""
   guessing-game
"""
from random import randint


def main():
        """
           guess.py  Ver 1.1
        """
        chances=5
        print "Guess a number from 0 to 10"
        num=randint(0,10)
        #print 'num=', num
        i=1
        while i<=chances:
                print
                print "Time {} of {}".format(i,chances)
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
                   if guess>num:
                           print "Too high..."
                   else:
                           print "Too low..."
                   #endif
                #endif
                i=i+1   
                if i>chances:
                        print "I won!" 
                        print "My number was:",num
                        print "Please try again!"
                #endif        
        #endwhile
#enddef main()
                   
if __name__=="__main__":
        main()
