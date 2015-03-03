# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#characters
image dog = "dog.png"
image teacher = "teacher.png"
image dad = "dad.png"

#backgrounds
image home = "home.jpg"
image classroom = "classroom.jpg"
image won = "classroom_won.jpg"
image lost = "classroom_lost.jpg"

# Declare characters used by this game.
define you = Character("[yourname]") #the player/user
define dog = Character("Sparky")
define teacher= Character("Teacher") #character named Nana
define dad= Character("Dad") #character named Nana

# The game starts here.
label start:
    
    $ game_score = 0 #score here is either -1 or 1
    
    scene home
    #play music "SleepAway.mp3"
    
    #What follows a $ sign is Python code
    $ yourname = renpy.input("Hi! My name is ...") #user input
    $ yourname = yourname.strip() #remove spaces
    
    you "I'm a high school student and today is Monday."
    you "Also, I have homework due today."
    you "Let's see, let's see, where is it..."
    you "..."
    you "OMG, WHERE'S MY HOMEWORK?"
    "You frantically go through all your papers and possessions in search of your homework, but it is to no avail."
    you "NOOOO! WHERE IS IT?"
    
    show dog
    "Your dog comes into the room."
    you "Oh, hi, Sparky. Do you know where my homework is?"
    dog "*pant pant* WOOF!"
    you "Aww, so cute."
    you "Wait... wait a minute..."
    "You look at your dog's mouth and notice there are some pieces of paper stuck to his teeth."
    you "Oh no... is that... did you... DID YOU EAT MY HOMEWORK?"
    dog "... ARF!"
    "You die a little inside."
    you "This has to be a nightmare..."
    "You close your eyes and start to count."
    $ count = 10
    while count > 0:
            you "[count]..."
            $ count -= 1
    "You open your eyes and look around you."
    you "...Darn it, it's real."
    
    scene classroom with Dissolve(.5)
    
    "You arrive at school."
    "You attempt to redo your homework, but you do not have enough time."
    you "Oh no... I don't have anything to turn in! What am I going to do... this isn't fair!"
    you "I'm hosed!"
    
    show teacher with Dissolve(.5)
    
    teacher "Hello class. Your homework is due today. Time to turn it in."
    "Students turn in their homework, one by one."
    "Soon enough, you realize that you are the only one that did not get up to turn in the homework."
    "The teacher comes up to you."
    teacher "Where's your homework, [yourname]?"
    you "Um... um... well..."
    you "*On no... what should I do?*"
    
    menu:
        "Lie.":
            jump lie
        "Tell the truth.":
            jump truth
            
    label lie:
        
        "I will blame some other student for not having my homework. Who should I blame it on..."
        you "Fred Weezie took my homework, erased my name, and put his name on it."
        teacher "Is this true, Fred Weezie?"
        "Before Fred can defend himself, a knock on the door is heard."
        "Someone opens the door and comes into the classroom."
        show teacher at left with move
        show dad at right with moveinright
        dad "Hello!"
        you "What the? Dad, what are you doing here?"
        dad "Well, you see..."
        "Your father takes out an unsanitary, crumpled up piece of paper."
        dad "Sparky puked out your homework. It's kind of gross, but... maybe your teacher will accept it?"
        "Your father looks at your teacher in a questioning manner."
        teacher "Hmmm..."
        "Your teacher tries to pick up the homework but is too disgusted by it."
        teacher "Well, if you had told me your dog ate your homework, I might have shown mercy."
        teacher "However, because you lied, I am going to punish you. I sentence you to seven days of detention!"
        "Your father looks back at you."
        dad "Did you lie about not doing your homework, [yourname]?"
        you "I was going to fess up and..."
        "Before you can finish your sentence, your father interrupts you."
        dad "When you get home tonight, I'm making you wash your mouth out with soap!"
        "You hear your classmates begin to laugh."
        you "Wait, I..."
        dad "I'll see you at home, [yourname]."
        hide dad with moveoutright
        show teacher at center with move
        "Your teacher looks at you, with a scowl."
        teacher "Come with me, [yourname], it's time for detention to start..."
        hide teacher with Dissolve(.5)
        $ game_score -= 1
        jump finish
        
    label truth:
        
        you "The truth is... my dog ate my homework..."
        teacher "...Seriously?"
        teacher "That's the oldest excuse in the book! Do you expect me to believe that? I was not born yesterday!"
        "The teacher is noticeably angry"
        you "But... but... it's the truth!"
        teacher "The mature thing to do is to fess up to your mistakes. You should know better--"
        "The teacher's lecture gets cut short by a knock on the door."
        "Someone opens the door and comes into the classroom."
        show teacher at left with move
        show dad at right with moveinright
        dad "Hello!"
        you "What the? Dad, what are you doing here?"
        dad "Well, you see..."
        "Your father takes out an unsanitary, crumpled up piece of paper."
        dad "Sparky puked out your homework. It's kind of gross, but... maybe your teacher will accept it?"
        "Your father looks at your teacher in a questioning manner."
        teacher "Oh, um... okay."
        "Your teacher tries to pick up the homework but is too disgusted by it."
        teacher "How about [yourname] just redoes the homework and turns it in by Friday? You can toss away that paper..."
        "Your father looks back at you."
        dad "Works for you, kiddo?"
        you "Yes! Thank you Dad, you've saved my life!"
        dad "Well, see you at home, [yourname]!"
        hide dad with moveoutright
        show teacher at center with move
        "Your teacher looks at you, embarrassed."
        teacher "... I'm sorry I accused you of lying, [yourname] ..."
        hide teacher with Dissolve(.5)
        $ game_score += 1
        
    label finish:
        if (game_score < 0):
            scene lost with Dissolve(.5)
            "Sad Ending..."
            "Today's lesson is... do your homework on the computer, and save it constantly, of course."
        else:   #it's > or = 0, but only logically 1
            scene won with Dissolve(.5)
            "Happy Ending!"
            "Today's lesson is... telling the truth is the way to go!"

    return #end the game
