#Greet the user and provide instructions
print(f"Hi, there! Welcome to the short story called The Fierce Dragon and the Brave Prince and Princess. I can't wait to tell it. ")
print(f"Before the story begins, I have a few questions I need you to answer.")
print(f"After typing your answer, be sure to press the enter key.")
input(f"\nPress the enter key to continue...")


keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    #1 Prince Name
    princeName = input(f"\nWhat is the name of the prince?:  ")
    while len(princeName) == 0:
        princeName = input(f"Please enter a name:")

    #2 Princess Name
    princessName = input(f"What is the name of the princess?:  ")
    while len(princessName) == 0:
        princessName = input(f"Please enter the name of the princess:  ")


         #3 Dragon Name
    dragonName = input(f"What is the name of the dragon?:  ")
    while len(dragonName) == 0:
        dragonName = input(f"Please enter the name of the dragon:  ")


         #4 Dragon Color
    dragonColor = input(f"What color is the dragon?:  ")
    while len(dragonColor) == 0:
        dragonColor = input(f"Please pick a color for the dragon:  ")


         #5 Kingdom Name
    kingdomName = input(f"What is the kingdom name?:  ")
    while len(kingdomName) == 0:
        kingdomName = input(f"Please enter a name for the kingdom:  ")


        #Story Starts
    print(f"\nADVENTURE AWAITS!!!")


    print(f"\nOnce upon a time in the kingdom of {kingdomName},  there lived a brave prince named {princeName}. ")

    print(f"{princeName} had been searching for his true love, the beautiful princess {princessName}, for many years. ")

    print(f"One day, while exploring a nearby forest, the prince stumbled upon a fierce dragon named {dragonName}. ")

    print(f"The dragon was {dragonColor} and breathing fire! The prince knew he had to act fast to save his kingdom and his princess. ")

   #Decision 1
    decision1 = input(f"\nShould {princeName} fight the dragon?  Type yes or no:  ")
    while decision1.lower() != "yes" and decision1.lower() != "no":
        decision1 = input("Please type yes or no:  ")

    if decision1.lower() == "yes":
        print(f"\n {princeName} drew his sword and charged at the great and powerful {dragonName}. ")

        print(f"{dragonName} breathed fire and narrowly missed the prince, but the prince was quick and managed to slice off one of {dragonName}’s claws! ")

        print(f"and starts jumping on customer tables knocking everything over in it's path. ")

        print(f"The dragon howled in pain and flew away, vowing to never return into {kingdomName} again. ")

        print(f"{princeName} returned to the kingdom a hero, and princess {princessName} was so impressed with his bravery that she immediately wanted to marry prince {princeName} . ")

        print(f"And they all lived happily ever after! . ")


    else:
        print(f"\n Prince {princeName} knew he was no match for the fierce dragon and decided to retreat... ")
        print(f"He returned to the kingdom and gathered all of the knights to help him defeat {dragonName}!")
        print(f"Prince {princeName} was hailed as a hero and princess {princessName} was so grateful for his bravery and she immediately wanted to marry the prince. ")

    #Decision 2
    Decision2 = input(f"\nShould the prince and princess get married in a grand ceremony? Type yes or no:  ")
    while Decision2.lower() != "yes" and Decision2.lower() != "no":
         Decision2 = input(f"Please type yes or no:  ")

    if Decision2 == "yes":
        print(f"\nThe prince and princess got married in a grand ceremony, attended by all of the people in the kingdom. ")
        print(f"They lived happily ever after and ruled the kingdom with wisdom and kindness. ")

    else:
        print(f"\nThe prince and princess decided to have a small, intimate wedding with just their closest friends and family. ")
        print(f"They lived happily ever after and ruled the kingdom with wisdom and kindness.")

#Alternate Endings
    if decision1 == "no" and Decision2 == "no":
        print(f"\nAfter {princeName} rejected the marriage, {kingdomName} became a normal and peaceful kingdom. ")
        print(f"After the dragon has been slayed, there were no more threats to the kingdom. ")
        print(f"{princeName} became the well known hero of kingdom of {kingdomName}. ")
        print(f"While princess {princessName} married to another prince in another kingdom.  ")
    elif decision1 == "yes" and Decision2 == "no":
        print(f"\nAfter the dragon has been slayed, there were no more threats to the kingdom. ")
        print(f"{princeName} became the well known hero of kingdom of {kingdomName}. ") 
        print(f"{princessName} was bored and wanted to have excitement in the kingdom. ")
        print(f"She went to the nearby wizard and brought a potion to bring {dragonName} back to life. ")
        print(f"Princess{princessName} gets kidnapped from the dragon and {princeName} was prepared to save the princess again . ")
    else:
        print(f"\nAfter the dragon has been slayed, there were no more threats to the kingdom. ")
        print(f"Kingdom was saved and everyone lived peacefully. ")

    
    keepPlaying = input(f"\nDo you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")