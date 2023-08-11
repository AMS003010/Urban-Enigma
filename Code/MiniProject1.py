#Here I have mentioned the libraries used
from playsound import playsound
import pyttsx3
import time
from subprocess import Popen


#Here I have created the text to speech engine for the player's and the narrator's voice.
engine=pyttsx3.init()
eng=pyttsx3.init()


#Here I have initialized some variables.
L=[]
L3=[]
fluro = 0
kilr1 = 0
kilr2 = 0
kilr3 = 0
hut='xix'


#This is the function for opening an image on ms print application and closing it according to the user's input.
def ima(fp,pn):
    p= Popen([pn,fp])
    fun=input("Enter \"q\" to close the image:")
    if fun=='q':
        p.terminate()


#This is the function for producing the narrator's voice.
def narrator_female(text):
    engine.setProperty("rate", 150)
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    

#This is the function for producing the player's voice.
def player_male(text):
    eng.setProperty("rate", 150)
    voices = eng.getProperty('voices')
    eng.setProperty('voice', voices[1].id)
    eng.say(text)
    eng.runAndWait()
    
    
#This is the function for displaying the general instructions of the Room 1.
def gen_ins():
    print("You can type \"move forward\" to move forward ")
    print("You can type \"move left\" to move left ")
    print("You can type \"move right\" to move right ")
    print("You can type \"use (itemname)\" to use one or more items like \"use key on door\"")
    print("You have a rope and a hose to use in your backpack (Hint:Use the items towards right)")
    print("PLEASE ENTER THE COMMANDS IN LOWERCASE ")
    print("PLEASE ENTER \"q\" TO CLOSE ANY IMAGE")
    print("PLEASE DO NOT CLOSE ANY IMAGE MANUALLY ON THE WINDOW JUST ENTER \"q\"")
    

#This is the function for displaying the general instructions of the Room 2.
def gen_ins2():
    print("You can type \"move forward\" to move forward ")
    print("You can type \"move left\" to move left ")
    print("You can type \"move right\" to move right ")
    print("PLEASE ENTER THE COMMANDS IN LOWERCASE ")
    print("PLEASE ENTER \"q\" TO CLOSE ANY IMAGE")
    print("PLEASE DO NOT CLOSE ANY IMAGE MANUALLY ON THE WINDOW JUST ENTER \"q\"")
    

#This is the function for displaying the general instructions of the Room 3.
def gen_ins3():
    print("You can type \"move forward\" to move forward ")
    print("You can type \"move left\" to move left ")
    print("You can type \"move right\" to move right ")
    print("PLEASE ENTER THE COMMANDS IN LOWERCASE ")
    print("PLEASE ENTER \"q\" TO CLOSE ANY IMAGE")
    print("PLEASE DO NOT CLOSE ANY IMAGE MANUALLY ON THE WINDOW JUST ENTER \"q\"")

    
#This is the function defined for Room 1 for moving in the forward direction.
def r1_f():
    narrator_female('There appears to be a old stuffy worn out sofa.Near the sofa there is a door with a 4 digit lock')
    decis=input("Do you wish to unlock the door(Y,N):")
    if decis=='Y':
        door_digit_code=input("Enter the code:")
        if door_digit_code=='1098':
            print("Congratulations, You have escaped room 1 ")
            narrator_female('Congratulations, You have escaped room 1')
            global kilr1
            kilr1=1
        else:
            print("The door is still locked")
            narrator_female('The door is still locked')
            
    else:
        pass
    

#This is the function defined for Room 1 for moving towards left.
def r1_r():
    hut='xix'
    narrator_female('There is a power supply connected to a gasoline generator. Next to it there is a old broken down bike with gasoline leaking.')
    while hut=='xix':
        decision=input("What do you want to to do with these items(use \"use\" with items) or enter \"look elsewhere\" to look in any other direction:")
        if decision=='use hose on bike':
            print("The generator is now filled.")
            decision1=input("What do you want to do next")
            if decision1=='use rope on generator':
                playsound('C:/Users/Saji M S/Downloads/startingpowerwasher-69423.mp3')
                print("Generator has started")
                playsound('C:/Users/Saji M S/Downloads/flickeringlight-90411.mp3')
                player_male('Looks like the power is back on')
                global fluro
                fluro = 1
                hut='ix'
        elif decision=='use rope on generator':
            print("The generator does not start")
            player_male('I think there is no gas in it. Maybe i can get some from the bike using the hose to siphon')
            
        elif decision=='look elsewhere':
            break
        elif decision=='help':
            gen_ins()
        else:
            print("Invalid output")


#This is the function defined for Room 1 for moving towards right.
def r1_l():
    narrator_female('There is a dark wooden shelf stocked with books.')
    playsound('C:/Users/Saji M S/Downloads/something-falling-on-a-desk-37719.mp3')
    narrator_female('Something has fallen.')
    narrator_female('It is a broken camera and few polaroid films.')
    ima(r"C:/Users/Saji M S/Downloads/Polaroid.jpg","C:\WINDOWS\system32\mspaint.exe")
    if fluro==1:
        ima(r"C:/Users/Saji M S/Downloads/PolaroidFinal.jpg","C:\WINDOWS\system32\mspaint.exe")
        player_male('Hey there is something on the film, i think it was because i switched on the bulb')
        player_male('It is the number 1 0 9 8 , maybe it is some code')
        player_male('Maybe i should look for something in other directions')
    else:
        player_male('There is nothing on the film')


#This is the function defined for Room 2 for moving in the forward direction.
def r2_f():
    narrator_female('There is a old stone coffin as an exhibit.')
    player_male('It is covered with cobwebs.')
    if (1 in L) and (2 in L) :
        player_male('Hey i see something on the coffin. It looks like morse code.')
        player_male('It looks like a number. Maybe it is the code to the lock on the coffin')
        ima(r"C:/Users/Saji M S/Downloads/stonecode.jpg","C:\WINDOWS\system32\mspaint.exe")
        d=input("Enter the the code:")
        if d=='1069':
            playsound('C:/Users/Saji M S/Downloads/rocks-sliding-101019.mp3')
            print("You have opened the coffin")
            player_male('Hey i see a key inside it.Maybe i can open the door with it.')
            L.append(3)
        


#This is the function defined for Room 2 for moving towards right.
def r2_r():
    narrator_female('There is an old morse code poster have a musty smell.')
    ima(r"C:/Users/Saji M S/Downloads/morsecode.jpg","C:\WINDOWS\system32\mspaint.exe")
    player_male('It seems to be a important piece of the museum')
    L.append(2)


#This is the function defined for Room 2 for moving towards left.
def r2_l():
    narrator_female('There is a door with a lock that can be opened only with a special key. There is also a paper nailed to the wall.')
    if 1 not in L:
        player_male('Hey there is something written on the paper')
        player_male('Its a riddle')
        ima(r"C:/Users/Saji M S/Downloads/riddle.jpg","C:\WINDOWS\system32\mspaint.exe")
        player_male('The person who built it sold it.')
        player_male('The person who bought it never used it')
        player_male('The person who used it never saw it. What is it.')
    ro=True
    if 3 in L:
        player_male('Let me see if the key fits in the doors lock ')
        player_male('YES it fits')
        print("Congratulations you have escaped room 2")
        narrator_female('Congratulations you have escaped room 2')
        global kilr2
        kilr2=1
        ro=False
    while ro!=False:
        ans=input("Enter the answer to the riddle or enter stop to exit:")
        if ans=='coffin':
            print("That is the right solution")
            L.append(1)
            ro=False
        elif ans=='stop':
            ro=False
        else:
            print("Wrong solution,Try again")
            

#This is the function defined for Room 3 for moving in the forward direction.
def r3_f():
    narrator_female('There is a table having hydrochloric acid and nitric acid')
    if (1 in L3) and (2 in L3):
        player_male('Maybe there is somomething inside the platinum chunk. I am have to melt it out.')
        player_male('I can melt it by immersing it in Royal Water.')
        ro=True
        while ro==True:
            wesq=input("Enter the HCl to HNO3 ratio to prepare Royal water as a:b :")
            if wesq=='3:1':
                print("Good job,Royal Water is prepared")
                player_male('Let me put the chunk in it.')
                playsound('C:/Users/Saji M S/Downloads/soda-fizzing-80464.mp3')
                player_male('All the platinum has melted and it left behind a ring')
                L3.append(3)
                ima(r"C:/Users/Saji M S/Downloads/IlluminatiDiamond.jpg","C:\WINDOWS\system32\mspaint.exe")
                player_male('Maybe i can open the door with this ring.')
                ro=False
                
            else:
                print("You weren't able to prepare Royal Water. Try again.")
                ro=True


#This is the function defined for Room 3 for moving towards left.
def r3_l():
    narrator_female('There is door having a special lock. There is also a book lying on the table near the door.')
    ro=True
    if 3 in L3:
        player_male('Let me use this key to open the door.')
        print("Congratulations, you have escaped room 3")
        narrator_female('Congratulations, you have escaped room 3.')
        global kilr3
        kilr3=1
        ro=False
    if 3 not in L3:
        player_male('Hey there is something written on the book.')
        player_male('It looks like a question.')
        ima(r"C:/Users/Saji M S/Downloads/question.jpg","C:\WINDOWS\system32\mspaint.exe")    
    while ro==True:
        quesans=input("Enter the answer to the question:")
        if quesans=='caffiene':
            print("It is the right answer to the question.")
            L3.append(1)
            ro=False
        else:
            print("Wrong answer. Try again.")
            ro=True
            
    
#This is the function defined for Room 3 for moving towards right.
def r3_r():
    narrator_female('There is a cryptic puzzle. There is a poster hanging on the wall which is about some chemical compounds.')
    player_male('Hey there are some interesting structures on the poster.')
    ima(r"C:/Users/Saji M S/Downloads/poster.jpg","C:\WINDOWS\system32\mspaint.exe")
    player_male('The cryptic puzzle seems to be hard.')
    ima(r"C:/Users/Saji M S/Downloads/cryptic.jpg","C:\WINDOWS\system32\mspaint.exe")
    if 1 in L3:
        player_male('The puzzle requires a 6 letter word but I only have a 8 letter word')
        player_male('Hey there is a clue as well.')
        ima(r"C:/Users/Saji M S/Downloads/note1.jpg","C:\WINDOWS\system32\mspaint.exe")
        ro=True
        while ro==True:
            quesanswer=input("Enter the word to solve the puzzle:")
            if quesanswer=='cafien':
                playsound('C:/Users/Saji M S/Downloads/opening-little-box-40878.mp3')
                player_male("Hey it opened. There seems to be note and a platinum chunk inside.")
                L3.append(2)
                ima(r"C:/Users/Saji M S/Downloads/platinum.jpg","C:\WINDOWS\system32\mspaint.exe")
                ima(r"C:/Users/Saji M S/Downloads/note2.jpg","C:\WINDOWS\system32\mspaint.exe")
                ro=False
            else:
                print("Wrong word. It did not open. Try again.")
                ro=True

                
        
#Here is the code for the beginning of Room 1.
narrator_female('Enter player name')  
player_name=input("Enter player name:")
time.sleep(1)
print("Hello",player_name)
narrator_female('Hello')
time.sleep(1)
print("There are three rooms to be escaped")
narrator_female('There are three rooms to be escaped')
time.sleep(2)
print("Entering Room 1...")
narrator_female('Entering Room 1')
time.sleep(2)
playsound('C:/Users/Saji M S/Downloads/door-open-and-close-with-a-creak-102380.mp3')
playsound('C:/Users/Saji M S/Downloads/double-door-lock-101210.mp3')
time.sleep(2)
player_male('That is scary. Lets start.')
gen_ins()
narrator_female('The room has a very dim lighting.It appears to be an old and dusty room.')
player_male('Nothing is clearly visible')



#This is the code for the functioning of Room 1.
while kilr1!=1:
    decision=input("Enter your move,Please enter help for commands:")
    if decision=='move forward':
        r1_f()
    elif decision=='move right':
        r1_r()
    elif decision=='move left':
        r1_l()    
    else:
        print("Invalid input,Try again")


#Here is the code for the beginning of Room 2.
time.sleep(2)
print("Entering Room 2...")
narrator_female('Entering Room 2')
time.sleep(2)
playsound('C:/Users/Saji M S/Downloads/door-opening-and-closing-18398.mp3')
time.sleep(2)
narrator_female('It is a museum. It has many artifacts,antiques,scluptures and many more historic items.')
player_male('This place looks abandoned. This place is filled with all kinds of old stuff.')
gen_ins2()


#This is the code for the functioning of Room 2.
while kilr2!=1:
    decision=input("Enter your move,Please enter help for commands:")
    if decision=='move forward':
        r2_f()
    elif decision=='move right':
        r2_r()
    elif decision=='move left':
        r2_l()    
    else:
        print("Invalid input,Try again")

        
#Here is the code for the beginning of Room 3.
time.sleep(2)
print("Entering Room 3...")
narrator_female('Entering Room 3')
time.sleep(2)
playsound('C:/Users/Saji M S/Downloads/door-opening-and-closing-18398.mp3')
time.sleep(2)
narrator_female('It is a laboratory. This is the last room. Good luck player')
player_male('This place is interesting. I may have to more scientific this time.')
gen_ins3()


#This is the code for the functioning of Room 3.
while kilr3!=1:
    decision=input("Enter your move,Please enter help for commands:")
    if decision=='move forward':
        r3_f()
    elif decision=='move right':
        r3_r()
    elif decision=='move left':
        r3_l()    
    else:
        print("Invalid input,Try again")


#This marks the end of the game.
print("Congratulations",player_name,"you have escaped all three rooms.")        
a=input("")

