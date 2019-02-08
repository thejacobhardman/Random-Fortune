# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 1/30/19
# Python Version 3.7.2

# Importing the 'random' pkg
import random

# Creating an array to store the different fortunes in
FortuneList = ["0", "1", "2", "3", "4", "5", "6", "7", "8,", "9"]

# Defining the different Fortune variables
FortuneList[0] = "You will accomplish great things!"
FortuneList[1] = "You should try harder to accomplish your dreams!"
FortuneList[2] = "Run!!!"
FortuneList[3] = "You will meet a fowl end..."
FortuneList[4] = "This is a filler fortune, try again."
FortuneList[5] = "The ghost of Robin Williams will visit you."
FortuneList[6] = "Honestly I'm out of ideas for fortunes..."
FortuneList[7] = "Maybe go try the slot machine down the aisle."
FortuneList[8] = "I'm not even a real genie. I'm just a computer program."
FortuneList[9] = "Yo Rugman! Let's blow this digital popsicle stand!"

# Generating a random number which will determine which fortune is printed
RandNum = random.randint(0, 9)

# Sudden Genie
print("""
                          .
       .:::.....:::::::..  :.
    .::::::::::::::::::::::.::.
   :       `::::::::::::::::::::.
               `::::::::::::::::::.
                       `::::::::::::
                         `::::::::::
                           `:::::::
           %%,   .::::.      `:::'      .::::.        ,%%%%
           `%%%, :::::::.    oOOOo    .:::::::.     ,%%;%%%
            `%%%,::%%%%::%%%%%%%%%%%%%::%%%%%::%   %%%;%%%
             `%%,%%%%%%%:%%%%%%%%%%%%%%%%%%%%:'%%,%%%;%%%
              %%,%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%,%%;%%%;
              %%,%;a@@@a;%%%%%%%%%;a@@@@@@a;%%%%%%%%%;%%%
        .oOOOo%,%;@@@@@@@a;%%%%%%;@@@@@@@@@a;%%%%%%,%%;%%
        OOO' .,%;a@@@@@@@@a;%%%%;@@@@@@@@@@@;%%%%%%%%,%;%,
        `OO.%%%%;@@@@@@@@@@;%%%;@@@@@@@@@@@@;%;%%%%%%%,%%%
          ;%%%%;%;@@@@@@@@@;%%%;@@@@@@@@@@@;;%%%%%%%%%,%%%
          `%%%%%%;;@@@@@@@@;%%%;@@@@@@@@@;%%%%%%%%%%%,%%%'
           `%%%%%%%;;@@' .;%%%%%, `@@@@;%%%%%%%;%%%%,%%%'
            `%;%;%%%%%%%%`%%%%%%%%%%%%%%%%;%;%;%%%%%,""
            :%%%;,%;%%`%%%%%%%%%%%%%%%%%%%%;;%%%::%%;
          ::%%%%;O;%%`%%%%%%%%%%%%%%%%%%%%;O;%%%%::%;
        ::%%%%%%;OO;%`%%%%%%%%%%%'%%%%%%%;OO;;%%%%::%
       ::%%%%%%;OOOOOO`%%%%%%%%'%%%%;OOOOOOOO;%%%%%::%
     ::%%%%%%%;OOOOOOOOOO`%%%%'OOOOOOOOOOOOOOO;%%%%%::.
   ::%%%%%%%%;                                ;%%%%%%::.
  ::%%%%%%%%;           ,;;;;;;;;;,;;;;;;;;;, ,;%%%%%%::.
 ::%%%%%%%;           .;;;;;;;;;;,;;;;;;;;;;;oO;%%%%%%%::
::%%%%%;OOo,.         ;;;;;;;;;;;;;;;;;;ooOOOOOO;%%%%%%::
::%%%%%;OOOOOOoOOOOOOOOoOOOOOOOOoOOOOOOOOOOOOOO;%%%%%%%::
::%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%::
 ::%%%%%%%%%;OOOOOOOOOOOOOOOOOOOOOOOOOOOO;%%%%%%%%%%%%::'
  `::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::'
    `:::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%::::'
      `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%:::::'
         `:::::%%%%%%%%%%%%%%%%%%%%%%%%%%%::::::'
            `:::::::::::::::::::::::::::::::'
               `:::::::::::::::::::::::::'
                  `::::::::::::::::::'
                     `:::::::::::'
                       `:::::::'
                       .::::'
                      .:::'
                     :::'
                    ::'   .::::.
                    ::.   ::  `::
                     ::.   `  .::
                      `::::::::'
""")

# Welcomes the user
print("Welcome to GENIE!!!")
input("Press 'Enter' to learn your fortune...\n")

# Printing the upper border of the fortune
i = -4 # Counter set to -4 to account for the offest of the fortune
while i < len(FortuneList[RandNum]):
    print ("~", end="")
    i += 1
    if i == len(FortuneList[RandNum]):
        print("")

# Printing the random fortune      
print("~ " + FortuneList[RandNum] + " ~")

# Printing the bottom border of the fortune
i = -4 # Counter set to -4 to account for the offest of the fortune
while i < len(FortuneList[RandNum]):
    print ("~", end="")
    i += 1
    if i == len(FortuneList[RandNum]):
        print("\n")

# Closes the program
input("Press 'Enter' to carry on with your life wayward traveler...")
