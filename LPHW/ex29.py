#encoding=utf-8

from sys import exit


def gold_room():
    print "This room is full of gold.  How much do you take?"
    nxt = raw_input("> ")
    if "0" in nxt or "1" in nxt:
        how_much = int(nxt)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        nxt = raw_input("> ")

        if nxt == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif nxt == "taunt bear" and not bear_moved:
            print """The bear has moved from the door.
                    You can go through it now."""
            bear_moved = True
        elif nxt == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif nxt == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print "Or you want to following Cthulhu?"

    nxt = raw_input("> ")

    if "flee" in nxt:
        start()
    elif "head" in nxt:
        dead("Well that was tasty!")
    elif "follow" in nxt:
        hell_room()
    else:
        cthulhu_room()


def hell_room():
    print "Now you inda HELL!!! Ahhaahaaahaa!"
    print "All you base are belong to us!"


def dead(why):
    print why, "Good job!"
    exit('AAAAAAAAAAAAA')


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    nxt = raw_input("> ")

    if nxt == "left":
        bear_room()
    elif nxt == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
