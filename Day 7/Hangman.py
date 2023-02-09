import random
hangman=['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''

,'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',                                                   # ASCII art for the hangman game
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
,'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = [
'abruptly',
'absurd',
'abyss',
'affix',
'askew',
'avenue',
'awkward',
'axiom',
'azure',
'bagpipes',
'bandwagon',
'banjo',
'bayou',
'beekeeper',
'bikini',
'blitz',
'blizzard',
'boggle',
'bookworm',
'boxcar',
'boxful',
'buckaroo',
'buffalo',
'buffoon',
'buxom',
'buzzard',
'buzzing',
'buzzwords',
'caliph',
'cobweb',
'cockiness',
'croquet',
'crypt',
'curacao',
'cycle',
'daiquiri',
'dirndl',
'disavow',
'dizzying',
'duplex',
'dwarves',
'embezzle',
'equip',
'espionage',
'euouae',
'exodus',
'faking',
'fishhook',
'fixable',
'fjord',
'flapjack',
'flopping',
'fluffiness',
'flyby',
'foxglove',
'frazzled',
'frizzled',
'fuchsia',
'funny',
'gabby',
'galaxy',
'galvanize',
'gazebo',
'giaour',
'gizmo',
'glowworm',
'glyph',
'gnarly',
'gnostic',
'gossip',
'grogginess',
'haiku',
'haphazard',
'hyphen',
'iatrogenic',
'icebox',
'injury',
'ivory',
'ivy',
'jackpot',
'jaundice',
'jawbreaker',
'jaywalk',
'jazziest',
'jazzy',
'jelly',
'jigsaw',
'jinx',
'jiujitsu',
'jockey',
'jogging',
'joking',
'jovial',
'joyful',
'juicy',
'jukebox',
'jumbo',
'kayak',
'kazoo',
'keyhole',
'khaki',
'kilobyte',
'kiosk',
'kitsch',
'kiwifruit',
'klutz',
'knapsack',
'larynx',
'lengths',
'lucky',
'luxury',
'lymph',
'marquis',
'matrix',
'megahertz',
'microwave',
'mnemonic',
'mystify',
'naphtha',
'nightclub',
'nowadays',
'numbskull',
'nymph',
'onyx',
'ovary',
'oxidize',
'oxygen',
'pajama',
'peekaboo',
'phlegm',
'pixel',
'pizazz',
'pneumonia',
'polka',
'pshaw',
'psyche',
'puppy',
'puzzling',
'quartz',
'queue',
'quips',
'quixotic',
'quiz',
'quizzes',
'quorum',
'razzmatazz',
'rhubarb',
'rhythm',
'rickshaw',
'schnapps',
'scratch',
'shiv',
'snazzy',
'sphinx',
'spritz',
'squawk',
'staff',
'strength',
'strengths',
'stretch',
'stronghold',
'stymied',
'subway',
'swivel',
'syndrome',
'thriftless',
'thumbscrew',
'topaz',
'transcript',
'transgress',
'transplant',
'triphthong',
'twelfth',
'twelfths',
'unknown',
'unworthy',
'unzip',
'uptown',
'vaporize',
'vixen',
'vodka',
'voodoo',
'vortex',
'voyeurism',
'walkway',
'waltz',
'wave',
'wavy',
'waxy',
'wellspring',
'wheezy',
'whiskey',
'whizzing',
'whomever',
'wimpy',
'witchcraft',
'wizard',
'woozy',
'wristwatch',
'wyvern',
'xylophone',
'yachtsman',
'yippee',
'yoked',
'youthful',
'yummy',
'zephyr',
'zigzag',
'zigzagging',
'zilch',
'zipper',
'zodiac',
'zombie',
]                                            # a list of a lot of words

secret_word=[i for i in random.choice(word_list)]            # a list of the letters from the random word chosen
guess_word=["_" for j in range(len(secret_word))]            # a list of blank spaces for each letter in the secret word
letters_not_in=[]                                            # an empty list that will be filled as we guess wrong letters

lives=7                                                     # start lives

while guess_word!=secret_word:                              # a loop so the game continues until the word is guessed

    guess = input("Guess a letter -----> ").lower()         # input letter from the player .lower() in case it is typed in capital letters
    if guess not in guess_word:                             # if statement in order to not repeating the letter
        for i in range(len(secret_word)):                       # we compare the letter guessed with each letter of the secret word list
            if secret_word[i]==guess:
                guess_word[i]=guess
                print("Nice, this letter is in the word!!!!\n")
                print(f"These letters are not in the word: {letters_not_in}")
                print(f"This is your guessed word: {guess_word}\n")
    else:
        print("This letter is already in the list of the guessed word, try again.")
    if guess not in secret_word:                            # in case the letter is wrong

        if guess not in letters_not_in:                     # if statement in order to not repeating the letter
            lives = lives - 1
            print(hangman[lives])
            letters_not_in.append(guess)
            print(f"These letters are not in the word: {letters_not_in}")
            print(f"This is your guessed word: {guess_word}\n")
        else:
            print("This letter is already in the list of mistakes, try again.")

    if lives==0:                                            # lost condition and the break of the loop instantly
        print("You lost :(")
        print("The word is","".join(secret_word))
        break

if guess_word==secret_word:                                 # winning condition
    print("You've guessed the word!!!!")

