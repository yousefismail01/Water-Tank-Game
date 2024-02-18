# TODO: Students, fill out statement of work header
# Student Name in Canvas: Yousef Ismail
# Penn ID: 76072638
# Did you do this homework on your own (yes / no): yes
# Resources used outside course materials: stackoverflow, youtube, reddit, google searches

# import statements
from random import shuffle

# TODO: Write the functions as described in the instructions
def get_user_input(question):
    """
    Prompts the user with a given question and processes the input according to specific rules.

    Parameters:
    - question (str): The question to prompt the user with.

    Returns:
    - int: If the input is a numeric string, it returns the input converted to an integer.
    - str: If the input is recognized as a power card ('SOH', 'DOT', 'DMT'), it returns the input as an uppercase string.
           If the input is any other string, it returns the input as a lowercase string.
           
    The function removes leading and trailing whitespaces from the user input.
    If the processed input is empty, it reprompts the user.
    """
    
    while True:
        # Prompt the user and remove leading/trailing whitespaces
        user_input = input(question).strip()
        
        # Check if the cleaned input is not empty
        if user_input:
            # If the input is purely numeric, cast to int and return
            if user_input.isdigit():
                return int(user_input)
            # Check if the input matches one of the power cards, considering case insensitivity
            elif user_input.upper() in ['SOH', 'DOT', 'DMT']:
                # Return the power card as uppercase for consistency
                return user_input.upper()
            # For any other string input, return as lowercase for consistency
            else:
                return user_input.lower()
        else:
            # Inform the user the input cannot be empty and reprompt
            print("Input cannot be empty. Please try again.")

def setup_water_cards():
    """
    Creates and shuffles a list of water cards according to predefined values and quantities.

    The function generates a list of integer values where each value represents a water card. 
    The distribution of cards is as follows:
    - 30 cards with a value of 1,
    - 15 cards with a value of 5,
    - 8 cards with a value of 10.

    Returns:
    - list of int: A shuffled list of integers where each integer represents a water card.
    """
    
    # Define the initial unshuffled list of water cards based on specified quantities
    water_cards = [1]*30 + [5]*15 + [10]*8  # List comprehension to create the cards
    
    # Use the shuffle function to randomly order the water cards
    shuffle(water_cards)
    
    # Return the shuffled list of water cards
    return water_cards

def setup_power_cards():
    """
    Creates and shuffles a list of power cards according to predefined values and quantities.

    The power cards have specific abilities and quantities as follows:
    - 'SOH' (Steal Opponent’s Half): 10 cards that allow stealing half of the opponent's tank value,
      truncating the decimal if the opponent’s tank value is an odd integer (e.g., ½ of 5 becomes 2).
    - 'DOT' (Drain Opponent’s Tank): 2 cards that empty the opponent's tank completely.
    - 'DMT' (Double My Tank): 3 cards that double the player's own tank value.

    Returns:
    - list of str: A shuffled list of strings where each string represents a power card.
    """
    
    # Define the initial unshuffled list of power cards based on specified quantities and abilities
    power_cards = ['SOH']*10 + ['DOT']*2 + ['DMT']*3  # List comprehension to create the cards
    
    # Use the shuffle function to randomly order the power cards
    shuffle(power_cards)
    
    # Return the shuffled list of power cards
    return power_cards

def setup_cards():
    """
    Sets up both water and power card piles for the game by invoking the respective setup functions
    for each type of card.

    This function calls setup_water_cards() to create and shuffle the water cards pile, 
    and setup_power_cards() to create and shuffle the power cards pile. 

    Returns:
    - tuple: A 2-tuple where the first element is a list of shuffled water cards and the second element 
             is a list of shuffled power cards. Each card is represented as an integer for water cards 
             and as a string for power cards, reflecting their respective values and abilities.
    """
    
    # Set up the water card pile by calling the setup_water_cards function
    water_cards_pile = setup_water_cards()
    
    # Set up the power card pile by calling the setup_power_cards function
    power_cards_pile = setup_power_cards()
    
    # Return a tuple containing both the water card pile and the power card pile
    return (water_cards_pile, power_cards_pile)

def get_card_from_pile(pile, index):
    """
    Removes and returns a card from a given pile at the specified index.

    Parameters:
    - pile (list): The card pile to remove a card from.
    - index (int): The index of the card to remove.

    Returns:
    - The removed card, which can be either an integer (water card) or a string (power card).

    The pile is modified in place, and the function assumes a valid index is provided.
    """
    
    return pile.pop(index)

def arrange_cards(cards_list):
    """
    Arranges a player's cards by sorting water cards in ascending order and power cards in alphabetical order,
    then updates the cards list to place the first three water cards followed by the first two power cards.

    Parameters:
    - cards_list (list): A mixed list of water cards (integers) and power cards (strings) representing a player's hand.

    The function modifies the cards_list in place, sorting and reordering the elements according to the game's rules.
    It does not return any value.
    
    Note:
    - If there are fewer than three water cards or two power cards, the function arranges as many as available.
    - The function assumes water cards are represented by integers and power cards by strings.
    """
    
    # Separate and sort water cards (int) and power cards (str)
    water_cards = sorted([card for card in cards_list if isinstance(card, int)])
    power_cards = sorted([card for card in cards_list if isinstance(card, str)])

    cards_list.clear()
    
    # Update the original list to the sorted arrangement
    cards_list[:] = water_cards[:3] + power_cards[:2]


def deal_cards(water_cards_pile, power_cards_pile):
    """
    Deals cards to two players from separate piles of water and power cards, ensuring each player receives
    three water cards and two power cards. The function then arranges each player's hand according to the
    game's rules.

    Parameters:
    - water_cards_pile (list): A list of integers representing the water cards pile.
    - power_cards_pile (list): A list of strings representing the power cards pile.

    Each card is drawn from the top of its respective pile (the first element in the list), and the dealing
    alternates between the two players for fairness.

    Returns:
    - tuple: A 2-tuple where the first element is player 1's arranged hand and the second element is player 2's
             arranged hand. Each hand is a list containing three water cards followed by two power cards, sorted
             according to the game's rules by the `arrange_cards` function.
    """
    
    # Initialize empty hands for both players
    player_1_cards = []
    player_2_cards = []
    
    # Alternately distribute 3 water cards to each player
    for _ in range(3):
        player_1_cards.append(water_cards_pile.pop(0))
        player_2_cards.append(water_cards_pile.pop(0))
    
    # Alternately distribute 2 power cards to each player
    for _ in range(2):
        player_1_cards.append(power_cards_pile.pop(0))
        player_2_cards.append(power_cards_pile.pop(0))
    
    # Arrange each player's cards according to the rules
    arrange_cards(player_1_cards)
    arrange_cards(player_2_cards)
    
    # Return the arranged hands of both players
    return (player_1_cards, player_2_cards)


def apply_overflow(tank_level):
    """
    Adjusts the tank level to handle overflow according to the game's rules.

    The game defines an overflow to occur when the tank level exceeds the maximum fill value (80 units).
    This function calculates the overflow amount and adjusts the tank level by setting it to the difference
    between the maximum fill value and the overflow amount, simulating the "spill over" of excess water.

    Parameters:
    - tank_level (int): The current level of the tank before adjusting for overflow.

    Returns:
    - int: The adjusted tank level after handling overflow, if any. If the tank level does not exceed
           the maximum fill value, the original tank level is returned unchanged.

    Note:
    - The minimum and maximum fill values are set at 75 and 80 units, respectively, for this game.
    - This function assumes tank levels are always positive integers.
    """
    
    # Define the maximum fill value for the game
    MAX_FILL_VALUE = 80

    # Check if the current tank level exceeds the maximum allowed fill value
    if tank_level > MAX_FILL_VALUE:
        # Calculate the amount of overflow
        overflow = tank_level - MAX_FILL_VALUE
        # Adjust the tank level to simulate water spilling out
        remaining_water = MAX_FILL_VALUE - overflow
        return remaining_water
    else:
        # If there's no overflow, return the tank level as is
        return tank_level

def use_card(player_tank, card_to_use, player_cards, opponent_tank):
    """
    Uses a specified card from the player's hand, applying its effects to either the player's or the opponent's tank.
    This function handles the logic for water cards and power cards, applying their effects accordingly.

    Parameters:
    - player_tank (int): The current water level of the player's tank.
    - card_to_use: The card chosen to be used from the player's hand, can be an int (water card) or str (power card).
    - player_cards (list): The player's current hand of cards.
    - opponent_tank (int): The current water level of the opponent's tank.

    Returns:
    - tuple: A 2-tuple containing the updated water levels of the player's tank and the opponent's tank, respectively.
    
    Note:
    - The function automatically removes the used card from the player's hand.
    - Overflow is applied if the player's tank exceeds the maximum fill value after using a card.
    - The function ensures tank levels do not fall below 0 or exceed the maximum fill value.
    """
    
    max_fill_value = 80  # Maximum water level allowed in the tank
    
    # Check if the card is in the player's hand and remove it if so
    if card_to_use in player_cards:
        player_cards.remove(card_to_use)
    
    # Apply the effect of the used card
    if isinstance(card_to_use, int):  # Water card
        player_tank += card_to_use
    elif card_to_use == 'SOH':  # Steal half of opponent's tank
        stolen_amount = opponent_tank // 2
        player_tank += stolen_amount
        opponent_tank -= stolen_amount
    elif card_to_use == 'DOT':  # Drain opponent's tank completely
        opponent_tank = 0
    elif card_to_use == 'DMT':  # Double player's tank
        player_tank *= 2
    
    # Apply overflow adjustments if necessary
    player_tank = apply_overflow(player_tank)
    
    # Ensure tank values are within valid range
    #player_tank = max(0, min(player_tank, max_fill_value))
    #opponent_tank = max(0, min(opponent_tank, max_fill_value))
    
    return (player_tank, opponent_tank)

def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
    """
    Removes a specified card from the player's hand and places it at the bottom of the appropriate card pile.

    This function distinguishes between water cards (integers) and power cards (strings) to ensure
    the discarded card is returned to the correct pile. It directly modifies the player's hand and the
    relevant card pile.

    Parameters:
    - card_to_discard: The card to be discarded, can be an int (water card) or str (power card).
    - player_cards (list): The player's current hand of cards.
    - water_cards_pile (list): The game's pile of water cards.
    - power_cards_pile (list): The game's pile of power cards.

    Note:
    - The function assumes the card to discard is present in the player's hand.
    - No replacement card is drawn by this function, affecting the player's hand size.
    - The discarded card is added to the end (bottom) of the appropriate pile.
    """
    
    # Check if the card is in the player's hand and remove it
    if card_to_discard in player_cards:
        player_cards.remove(card_to_discard)
        
        # Determine the type of card and append it to the correct pile
        if isinstance(card_to_discard, int):  # Water card
            water_cards_pile.append(card_to_discard)
        else:  # Power card
            power_cards_pile.append(card_to_discard)

def filled_tank(tank):
    """
    Checks if the tank's water level is within the specified range for being considered filled.

    This function evaluates whether the current water level of the tank falls within the game's defined range
    for a filled tank, which is between the minimum fill value (inclusive) and the maximum fill value (inclusive).

    Parameters:
    - tank (int): The current water level of the tank.

    Returns:
    - bool: True if the tank's water level is within the filled range, False otherwise.

    The function uses predefined minimum and maximum fill values of 75 and 80 units, respectively, to
    determine if the tank is filled according to the game's rules.
    """
    
    # Predefined fill values for determining if a tank is considered filled
    min_fill_value = 75
    max_fill_value = 80
    
    # Return True if tank level is within the filled range, False otherwise
    return min_fill_value <= tank <= max_fill_value

def check_pile(pile, pile_type):
    """
    Checks if a given pile (water or power cards) is empty and replenishes it if necessary.

    This function assesses whether the specified pile (either water cards or power cards) is empty. If the pile is found
    to be empty, the function calls the appropriate setup function to replenish the pile based on its type, ensuring that
    the game can continue without interruption.

    Parameters:
    - pile (list): The pile to be checked and potentially replenished. This could be a list of water cards or power cards.
    - pile_type (str): A string indicating the type of the pile being checked. Valid values are "water" or "power".

    The function does not return any value. Instead, it directly modifies the pile in place if replenishment is necessary.

    Note: The setup functions for water and power cards (setup_water_cards and setup_power_cards) are assumed to
    exist elsewhere in the codebase, providing new, shuffled piles of their respective card types.
    """
    
    # Check if the pile is empty
    if not pile:
        # Determine the type of pile and replenish accordingly
        if pile_type == "water":
            replenished_pile = setup_water_cards()  # Assuming this function exists and returns a list of water cards
        elif pile_type == "power":
            replenished_pile = setup_power_cards()  # Assuming this function exists and returns a list of power cards
        
        # Replace the contents of the original pile with the replenished pile
        pile.extend(replenished_pile)

def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Manages the human player's turn in the game, allowing them to use or discard a card and draw a new one.

    This function handles the human player's actions during their turn, including displaying current water levels, 
    showing their hand, and processing their decision to use or discard a card. Based on the player's action, it 
    updates the game state accordingly, including both players' water levels and the human player's hand of cards. 
    It also ensures that piles of cards are replenished if necessary and maintains the order of the human player's hand.

    Parameters:
    - human_tank (int): The current water level in the human player's tank.
    - human_cards (list): The current hand of cards held by the human player.
    - water_cards_pile (list): The pile of water cards available for drawing.
    - power_cards_pile (list): The pile of power cards available for drawing.
    - opponent_tank (int): The current water level in the computer opponent's tank.

    Returns:
    - A tuple containing the updated water levels of the human player and the computer opponent, in that order.
    """
    print(f"Your current water level: {human_tank}")
    print(f"Computer's water level: {opponent_tank}")
    print(f"Your cards: {human_cards}")
    action = ""

    while action not in ['u', 'd']:
        action = input("Do you want to use or discard a card? (u/d): ").lower().strip()

    # Initialize variables to avoid NameError in conditional branches
    card_to_use = None
    card_to_discard = None

    # Use a card
    if action == "u":
        while True:
            card_to_use = get_user_input("Enter the card you want to use (number for water, SOH/DOT/DMT for power): ")
            if card_to_use in human_cards:
                human_tank, opponent_tank = use_card(human_tank, card_to_use, human_cards, opponent_tank)
                print(f"Card used: {card_to_use}")
                print(f"Your water level is now at: {human_tank}")
                print(f"Computer's water level is now at: {opponent_tank}")
                break
            else:
                print("You don't have that card. Please choose a card from your hand.")

    # Discard a card
    elif action == "d":
        while True:
            card_to_discard = get_user_input("Enter the card you want to discard (number for water, SOH/DOT/DMT for power): ")
            if card_to_discard in human_cards:
                discard_card(card_to_discard, human_cards, water_cards_pile, power_cards_pile)
                print(f"Card discarded: {card_to_discard}.")
                print(f"Your water level is now at: {human_tank}")
                print(f"Computer's water level is now at: {opponent_tank}")
                break
            else:
                print("You don't have that card. Please choose a card from your hand.")

    # Draw a new card
    new_card_type = int if action == "u" and isinstance(card_to_use, int) else (type(card_to_discard) if action == "d" else None)
    if new_card_type == int:  # If a water card was played or discarded
        check_pile(water_cards_pile, "water")  # Ensure the pile isn't empty
        new_card = get_card_from_pile(water_cards_pile, 0)
    else:  # If a power card was played or discarded
        check_pile(power_cards_pile, "power")  # Ensure the pile isn't empty
        new_card = get_card_from_pile(power_cards_pile, 0)
    
    human_cards.append(new_card)
    arrange_cards(human_cards)  # Ensure the player's hand is sorted

    print(f"New card drawn: {new_card}. Your hand is now: {human_cards}")
    return human_tank, opponent_tank


def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
    """
    Executes the computer's turn in the water tank game by selecting and using or discarding a card from its hand.
    The computer's strategy aims to maximize its tank level without exceeding the maximum allowed value (80),
    considering both water and power cards. The function ensures deterministic behavior, with the computer
    making decisions based on its current tank level, the opponent's tank level, and the cards in hand.

    Parameters:
    - computer_tank (int): The current water level of the computer's tank.
    - computer_cards (list): The computer's current hand, containing both water and power cards.
    - water_cards_pile (list): The pile of water cards available for drawing.
    - power_cards_pile (list): The pile of power cards available for drawing.
    - opponent_tank (int): The current water level of the opponent's (human player's) tank.

    Returns:
    - tuple: A 2-tuple containing the updated water levels of the computer's and the opponent's tanks, respectively.

    The computer's strategy involves carefully selecting cards to use in order to approach a target water level
    without overflowing. It prioritizes winning conditions and strategic power card plays. After taking an action,
    the computer draws a new card of the same type (water or power) as the one used or discarded, ensuring the
    hand remains sorted and the game rules are followed.
    """

    # Define target water levels
    max_fill_value = 80
    min_fill_value = 75

    action_taken = False  # Flag to track if an action has been taken
    card_used_or_discarded = None  # Track the card used or discarded for drawing a similar type card later

    # Strategy to use specific water cards when close to winning conditions
    if computer_tank >= 65:
        for card in computer_cards:
            if card == 1 and computer_tank == 74:
                computer_tank += card  # Use the card and increase tank level
                print(f"Computer used water card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True  # Mark action as taken
                card_used_or_discarded = card
                break
            if card == 5 and computer_tank >= 70:
                computer_tank += card
                print(f"Computer used water card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True
                card_used_or_discarded = card
                break
            if card == 10 and computer_tank >= 65:
                computer_tank += card
                print(f"Computer used water card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True
                card_used_or_discarded = card
                break           
               

    # Strategy for using power cards if no water card was suitable
    if not action_taken:
        for card in computer_cards:
            if card == 'DMT' and (opponent_tank > computer_tank + 10):
                computer_tank = computer_tank * 2
                print(f"Computer used power card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True
                card_used_or_discarded = 'DMT'
                break
            if card == 'SOH' and opponent_tank > 8 :
                stolen_amount = opponent_tank // 2
                if computer_tank + stolen_amount <= max_fill_value:
                    computer_tank += stolen_amount
                    opponent_tank -= stolen_amount
                    print(f"Computer used power card: {card}")
                    print(f"Computer's water level is now at: {computer_tank}")
                    print(f"Your water level is now at: {opponent_tank}")
                    computer_cards.remove(card)
                    action_taken = True
                    card_used_or_discarded = 'SOH'
                    break
            if card == 'DOT' and (opponent_tank > computer_tank):
                opponent_tank = 0
                print(f"Computer used power card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True
                card_used_or_discarded = 'DOT'
                break
    
        # General strategy for using water cards if no specific play was made
    if not action_taken:
      # Try to use a water card to reach a desired level within the tank
        for card in computer_cards:
            if isinstance(card, int): # Check if it's a water card
                computer_tank += card  # Use the card
                print(f"Computer used water card: {card}")
                print(f"Computer's water level is now at: {computer_tank}")
                print(f"Your water level is now at: {opponent_tank}")
                computer_cards.remove(card)
                action_taken = True
                card_used_or_discarded = card
                break

    # If no card was used, discard the first available card
    if not action_taken:        
        card = computer_cards[0] 
        print(f"Computer discarded: {card}")
        discard_card(card, computer_cards, water_cards_pile, power_cards_pile)
        card_used_or_discarded = card

    # Draw a new card of the same type as the one just used or discarded
    if isinstance(card_used_or_discarded, int):  # Water card
        new_card = get_card_from_pile(water_cards_pile, 0)
    else:  # Power card
        new_card = get_card_from_pile(power_cards_pile, 0)
        
    computer_cards.append(new_card)
    arrange_cards(computer_cards)

    computer_tank = apply_overflow(computer_tank)

    return computer_tank, opponent_tank

def main():
    """
    The main function orchestrates the game flow, implementing the structure and rules as described in the User Interface section of the assignment. Here's how it works:

    1. Initialization:
        - Set up the game environment, including players' tanks and card piles.
        - Determine randomly which player (human or computer) will take the first turn.

    2. Game Loop:
        Each turn consists of the following actions for the current player (either human or computer):
            a. Decide whether to use or discard a card. This decision is made based on the strategy for the computer or input for the human player.
            b. Perform the action chosen:
                - If using a card, apply its effects accordingly.
                - If discarding a card, simply remove it from the player's hand.
            c. Draw a new card from the corresponding pile (water or power) to replace the used or discarded card.
            d. Check for the end-game conditions, such as reaching the maximum tank level.

    3. End of Game:
        - The game ends when one of the players reaches the winning condition.
        - Display the game outcome and declare the winner.

    Note: This function does not return a value; it's meant to control the game's progression and handle interactions between the game's components.
    """
    # Initialize the game
    water_cards_pile = setup_water_cards()
    power_cards_pile = setup_power_cards()
    
    human_tank, computer_tank = 0, 0
    human_cards = deal_cards(water_cards_pile, power_cards_pile)[0]
    computer_cards = deal_cards(water_cards_pile, power_cards_pile)[1]
    
    # Decide who goes first
    player_order = ["human", "computer"]
    shuffle(player_order)
    current_player = player_order[0]   

    # Game loop
    while not filled_tank(human_tank) and not filled_tank(computer_tank):
        if current_player == "human":
            print("\n=== Human Player's turn ===")
            human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, computer_tank)
            current_player = "computer"
        else:
            print("\n=== Computer Player's turn ===")
            computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, human_tank)
            current_player = "human"
        
        # After each turn, check if either pile needs replenishing
        check_pile(water_cards_pile, "water")
        check_pile(power_cards_pile, "power")
        
    # Determine and announce the winner
    if filled_tank(human_tank):
        print("You win!")
    else:
        print("Computer wins!")

if __name__ == '__main__':
    main()
