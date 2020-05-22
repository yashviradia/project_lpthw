print("""This is the game of Space and changing the history of the humanity.
The Space race has begun.
What is your choice:
'Mars' or 'Moon'?""")

place = input("> ")

if place == 'Mars':
    print("""You're sharing the vision with Elon Musk.
    His vision is to create the human colony on the mars.
    Do you agree with his idea?
    'Yes' or 'No'?""")


    answer = input("> ")
    if answer == 'Yes':
        print("""You could join the SpaceX team. Make your dream come true.
        You'll need certain amount skill sets, american citizenship, which you might easily get if you're german citizen.
        You can create your own idea and work with it. Find the problems in the society and get the solution.
        You can also collaberate with SpaceX or buy its equity.""")
    elif answer == 'No':
        print("""There are other two giants in this race. You can join them. Or you can create your own idea.""")
    else:
        print("""Always try to solve other people's problem. They will reward you.
        Develop the high income skills and develop the financial confidence.""")


elif place == 'Moon':
    print("""You're the sharing the vision with Jeff Bezos, who's net worth is 150 Billion dollars.
    His vision is: the people will be living in a capsule in the space. The capsule will be floating in the space.
    Do you agree with his vision?
    'Yes' or 'No'?""")

    answer = input("> ")
    if answer == 'Yes':
        print("""You're with Jeff Bezos and want to go to Moon.
        But, the moon has no atmosphere. But, the capsule concept may come true.
        Anyways, it's your choice.
        Develop the high income skills and gain the confidence.""")
    elif answer == 'No':
        print("""You can still join any of the other giants: Elon Musk or Richard Brandson.""")
    else:
        print("""Develop the financial confidence and it comes by developing the high income skills.
        You can still join the space race by joining Elon Musk or Richard Brandson.""")

else:
    print("""You can always go for a space travel. The Virgin Galactic is doing it.
    Even SpaceX and Blue origin are doing that.
    So there are three giants: Elon Musk, Jeff Bezos and Richard Brandson.
    Would like to join the space race and mine the asteroids?
    'Yes' or 'No'?""")

    answer = input("> ")
    if answer == 'Yes':
        print("""Space travel is possible and many people can get benefit with this.
        You can go from New York to HongKong in just 40Minutes.
        That's the possibility of this outcome.""")
    elif answer == 'No':
        print("""So you don't want to go with Galactic Virgin.
        Are you with 'Elon Musk' or 'Jeff Bezos'""")

        person = input("> ")
        if person == 'Elon Musk':
            print("Great choice.")
        elif person == 'Jeff Bezos':
            print("""He's the richest man.
            But everything has its limit and sky is the limit. Is it?
            I don't think so. There are no limits.
            When there are limits just push them.""")
        else:
            print("You can create your own company. First develop the financial confidence.")
    else:
        print("Kind of sounds like you don't like space. You can still do asteroid mining.")
