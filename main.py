print('''
*******************************************************************************
                           
                                                    
88           88                                 88  
""           88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  
                                                    
                                                    
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

river_action = input(
    "You're in front of a river.Do you want to go along the river or swim across it?\nType 'Along' or 'Swim' "
).lower()

if river_action != "swim":
    print(
        "While you are walking along the river you notice that there's a lion some meters away from you"
    )

    lion_action = input(
        "You have two options. You have to climb a tree and hope the lion didn't see you or get a knife inside your bag so you can protect yourself.\n Type 'Climb' or 'Knife': "
    ).lower()

    if lion_action != "knife":
        print(
            "You're so lucky! The lion hasn't seen you so it went to another direction."
        )
        maze_action = input(
            "You get down the tree and walk north. There are 3 paths you can take. Each path has a color to it.\n Choose 'Yellow', 'Blue' or 'Red'"
        ).lower()

        if maze_action == "yellow":
            print(
                "You are facing a giant gorilla which is very protective. You are beaten till death"
            )

        elif maze_action == "blue":
            print(
                "You found a big chest and inside of it there are golden coins.\n You made till the end of this amazing journey"
            )
        else:
            print(
                "There is nothing for you to do now. This path went back home and all the effort to find the treasure was trown away.\n Try again next time."
            )
    else:
        print(
            "You fought bravely against the lion and you won, but now you're bleeding and there is no one to help you.\n You died."
        )
else:
    print(
        "You were swimming the river, but you encountered a crocodile. You are dead now"
    )

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
