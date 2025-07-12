"""Quentin "Blake" Conaway Text Based Game"""
import time



castle_map = {
    # Map of castle rooms and what rooms they connect to
    "Dining Hall": {"N": "Kitchen", "S": "Parlour", "E": "Library", "W": "Master Bedroom"},
    "Kitchen": {"S": "Dining Hall", "N": "Servant Quarters"},
    "Servant Quarters": {"S": "Kitchen"},
    "Library": {"W": "Dining Hall"},
    "Master Bedroom": {"E": "Dining Hall", "S": "Cellar"},
    "Parlour": {"N": "Dining Hall", "S": "Courtyard", "W": "Cellar"},
    "Cellar": {"N": "Master Bedroom", "E": "Parlour"},
    "Courtyard": {"N": "Parlour"}  # Dragon is here
}

room_items = {
    # Map of each room and the item in the room
    "Kitchen": "shield",
    "Library": "scroll of anti-fire",
    "Servant Quarters": "helm",
    "Cellar": "health potion",
    "Master Bedroom": "staff of frost",
    "Parlour": "robes of the eternal"
}
def play_intro():
    """Decided to make intro into a function to avoid having to play it every time you play the game"""
    print("""You play as Kaos, a young adventurer set on proving himself to the king and establishing himself as a member of the royal guard.\nYou are sent on a mission to “retrieve a valuable artifact” for the king.""")
    time.sleep(6)
    print("""After a long and tiring journey, you cross a bridge and realize that you have made it to the castle.\nAs you look around for a way in, you hear someone shout. As you turn around, you are met with a club to the head.\n""")
    time.sleep(4.5)
    print("""You wake up in a mysterious banquet hall in the middle of the castle.""")
    time.sleep(3)
    print("""You are without your gear and can hear a tremendous roar...""")
    time.sleep(2)
    print("""which you can only assume is the dragon guarding this “valuable artifact” your king sent you to retrieve.\n""")
    time.sleep(3)
    print("""Will you be able to find all of your items, defeat the dragon, and earn your place among the royal guard?""")
    time.sleep(3)
    print("""\nWill you be like the many before you and fall victim to the fierce beast waiting for you?""")
    time.sleep(3)
    print("""\nTHE CHOICE IS YOURS.\n""")
    time.sleep(2)
    print(f"You wake up in the Dining Hall after being knocked out outside.")
    time.sleep(1.5)
    print("Where are you?")
    time.sleep(1.5)
    print("Where is your gear?")
    time.sleep(1.5)
    print("How are you going to get out of here? ")
    time.sleep(2)
    print("""\n--------You must travel through the castle and collect all six items you are missing
            before you come across the fierce dragon waiting for you. Be careful where you decide to go.
            You never know where he could be hiding----------\n""")

def move_room(current_room, direction):
    try:
        # using try / except block to handle if user tries to move to a room not connected
        return castle_map[current_room][direction.upper()]
    except KeyError:
        print(f"You cannot go {direction} from here. Try another way.")
        return current_room


def main():
    play_again = True
    # used while loop to run again if user wants to play again
    while play_again:
        current_room = "Dining Hall"
        player_inventory = []
        # Added try/ except blocks to help validate input
        try:
            play = input("Would you like to play the intro? (y/n): ").lower()
            if play == "y":
                    play_intro()
        except ValueError:
            print("Please enter a valid selection (y/n): ")


        while current_room != "Courtyard":
            print(f"\nYou are in the {current_room}")


            if current_room in room_items and room_items[current_room] not in player_inventory:
                print(f"You see a {room_items[current_room]} here.")
                print(f"You have {len(player_inventory)} items so far.")
                try:
                    take = input("Would you like to take it? (y/n): ").lower()
                    if take == 'y':
                        player_inventory.append(room_items[current_room])
                        print(f"You picked up the {room_items[current_room]}.")
                except ValueError:
                    print("Please enter y or n.")


            direction = input("Which direction would you like to go? (N, S, E, W): ")
            current_room = move_room(current_room, direction)



        # End of loop: player reached Courtyard
        print("\nYou have entered the Courtyard. A dragon awaits!")
        if len(player_inventory) < 6:
            print("The dragon incinerates you. You weren't prepared.")
        else:
            print("With all the magical items, you defeat the dragon and win!")
            print("You search the dragon for the artifact...")
            time.sleep(4)
            print("You rummage through what is left of the dragon...\n")
            time.sleep(5)
            print("Woot! Woot! Fighting a dragon must have been hard work!\nThe 'valuable artifact' was a can of Dr. Pepper.")
            time.sleep(5)
            print("\nSorry it wasn't something cooler.")
            time.sleep(2)
            print("I mean, you do have a Staff of Frost and Robes of the Eternal.")
            time.sleep(3)
            print("What else could you want?")
            time.sleep(1)
            try:
                again = input("Would you like to play again? (y/n): ").lower()
                play_again = again == 'y'
            except ValueError:
                print("Please enter y or n.")
if __name__ == "__main__":
    main()
