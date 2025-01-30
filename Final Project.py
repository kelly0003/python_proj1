import random

#word list
def word_list():
    #category list
    categories = {
        "Animals": {
            "Common Animals": ["dog", "cat", "horse", "hamster", "rabbit", "mouse"],
            "Birds": ["eagle", "parrot", "hummingbird", "penguin", "flamingo", "ostrich"],
            "Marine Animals": ["dolphin", "whale", "octopus", "shark", "jellyfish", "seahorse"],
            "Jungle Animals": ["jaguar", "monkey", "sloth", "elephant", "cobra", "frog"]
        },
        "Movies": {
            "Disney Movies": ["the lion king", "aladdin", "beauty and the beast", "cinderella", "frozen", "moana"],
            "Genres": ["horror", "comedy", "action", "romance", "sci fi", "superhero"],
            "Modern Blockbusters": ["avatar", "titanic", "star wars", "jurassic park", "the avengers", "gladiator"],
            "Famous Actors": ["Tom Hanks", "Morgan Freeman", "Leonardo DiCaprio", "Robert Downey Jr", "Will Smith", "Meryl Streep"]
        },
        "Geography": {
            "Countries": ["Australia", "Canada", "Brazil", "India", "Japan", "Italy"],
            "Capitals": ["Paris", "Tokyo", "London", "Berlin", "Rome", "Madrid"],
            "Famous Landmarks": ["Eiffel Tower", "Taj Mahal", "Statue of Liberty", "Mount Everest", "Great Wall of China", "Machu Picchu"],
            "Natural Features": ["Amazon River", "Sahara Desert", "Nile River", "Grand Canyon", "Mount Kilimanjaro", "Alps"]
        },
        "Sports": {
            "Common Sports": ["soccer", "basketball", "baseball", "volleyball", "ice hockey", "tennis"],
            "Olympic Sports": ["gymnastics", "fencing", "rowing", "archery", "cycling", "boxing"],
            "Sports Terms": ["touchdown", "penalty", "referee", "home run", "sprint", "slam dunk"],
            "Sports Gear": ["helmet", "glove", "whistle", "bat", "goggles", "cleats"]
        }
    }
    return categories


#get random word from word list
def get_random_word(category, level, categories):
    return random.choice(categories[category][level])

#display state of word
def display_word(word, guessed_letters):
    display = ''
    for letter in word.lower():
        if letter == ' ':
            display += ' '  # Preserve space for multi-word phrases
        elif letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

#display remaining letters
def display_wordbank(guessed_letters):
    remaining_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    return ''.join([letter + ' ' if letter not in guessed_letters else '' for letter in remaining_letters]).strip()

#if letter guessed or not
def is_word_guessed(word, guessed_letters):
    # Convert word to lowercase and check if all letters are in guessed_letters
    for letter in word.lower():
        if letter != ' ' and letter not in guessed_letters:  # Ignore spaces
            return False
    return True

#display hangman
def display_hangman(wrong_guesses):
    stages = [
        """
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """
    ]
    return stages[wrong_guesses]

#play the game
def play_hangman(score):
    categories = word_list()

    while True:  # Loop for multiple rounds of the game
        print("\nCategories: 1) Animals  2) Movies  3) Geography  4) Sports")
        category_choice = int(input("Enter category number: "))
        category_names = list(categories.keys())
        category = category_names[category_choice - 1]

        # Show named levels for the selected category
        print(f"\nAvailable Levels for {category}:")
        level_names = list(categories[category].keys())
        for i, level in enumerate(level_names, 1):
            print(f"{i}) {level}")

        level_choice = int(input("Enter difficulty level number: "))
        level_name = level_names[level_choice - 1]

        word = get_random_word(category, level_name, categories)
        guessed_letters = set()
        wrong_guesses = 0
        max_wrong_guesses = 6  # Maximum number of wrong guesses before losing

        print(f"\nYou chose {category} at '{level_name}' level. Let's play!")
        print(display_word(word, guessed_letters))

        while wrong_guesses < max_wrong_guesses:
            print(f"Remaining Letters: {display_wordbank(guessed_letters)}")

            guess = input(f"\nGuess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                wrong_guesses += 1
                print(f"Oops! '{guess}' is not in the word.")
                print(display_hangman(wrong_guesses))

            # Display the word state
            print(display_word(word, guessed_letters))

            # Check if the word is fully guessed
            if is_word_guessed(word, guessed_letters):
                print("\nCongratulations! You've guessed the word!")
                score['wins'] += 1
                break

        if wrong_guesses == max_wrong_guesses:
            print(f"\nSorry, you lost! The word was '{word}'.")
            score['losses'] += 1

        # Display the current score
        print(f"\nYour current score: Wins: {score['wins']}, Losses: {score['losses']}")

        # Ask the player if they want to play again or return to the main menu
        play_again = input(
            "\nWould you like to play again, go to the main menu, or quit? (p = play again, m = main menu, q = quit): ").lower()

        if play_again == 'p':
            continue  # Start a new round
        elif play_again == 'm':
            return  # Return to the main menu
        elif play_again == 'q':
            print("\nThanks for playing Hangman!")
            break  # Exit the game completely

#main menu
def main_menu():
    score = {'wins': 0, 'losses': 0}

    # Display welcome message and instructions
    print("Welcome to the Hangman Game! \nHangman Instructions: \n")
    print("Guess the hidden word by typing one letter at a time.")
    print("If the letter is in the word, it will be revealed.")
    print("You have until the hangman is completed to guess the word.")

    while True:
        print("\n==== Main Menu ====")
        print("1) Start New Game")
        print("2) View Score")
        print("3) Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            play_hangman(score)  # Start a new game
        elif choice == 2:
            print(f"\nCurrent Score: Wins: {score['wins']}, Losses: {score['losses']}")
        elif choice == 3:
            print("\nThanks for playing! Goodbye!")
            break  # Exit the game
        else:
            print("\nInvalid choice. Please choose again.")
main_menu()