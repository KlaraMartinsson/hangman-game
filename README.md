# Hangman game
![Image of website](documentation/screenshots/hangman_firstpage.JPG)
[Link to live site]

The Hangman game is a Python terminal game deployed to Heroku. The goal of this game is to guess the secret word with one letter at a time. If the player guess it's wrong to many times the man hangs. If the player guess the word the man survives.

## User Experience

### User Goals
As a user I want:
* First of all to have a simple fun game and be challenged. (The user get's challenged with diffrent levels of difficulty and randomised words at every round.)
* Secondly, to learn how to play and understand the game. (The user get's to understand the game if they read the rules.)
* To play the game without any issues. (If an invalid input occurs the player get's to know what is wrong with an error message.)
* To easily navigate through available options and have clear feedback on my inputs. (The user get's direct feedback when guessing a letter correct or wrong.)
* To know if I won the game or not and what the secret word was. (The user get's feedback if the won or lose when the game is over. They also get's to know what the secret word was.)

### Project Goals
As a programmer of the game, I want the user to meet their goals (above). I also want the game to run smoothly with no bugs.

## Flowchart
I was using a Flowchart to plan out how the code should work. My thoughts while doing this was:
- How should the game start?
- Where should it be inputs from the user?
- How do I deal with incorrect input?
![Design FlowChart](documentation/screenshots/hangman_flowchart.JPG)

## Headings
I used graphics from [Fancy text pro](https://www.fancytextpro.com/) to make the welcome, game rules, win and lose headings.

## Features
### Existing features
* Start of the game
    * Welcomes the player.
    * Ask's to enter the player's name.
    * Ask's if the player want's to read the rules.

![Image of the start](documentation/screenshots/read_rules.JPG)

* Game rules
    * Explains how to play the game.
    * Explains the rules of the game.
    * When scrolling down in the terminal, the player get's asked to choose level of difficulty. From 1-3, "1" is easy, "2" is medium and "3" is hard.

![Image of the game rules](documentation/screenshots/game_rules.JPG)

* The game starts
    * The hangman is displayed.
    * The word is hidden by "_" for every secret letter.
    * Under the hidden word the letters guessed shows up. 
    * The user get's to guess letters until they finish the word or until they or out of their 6 chances of guessing wrong and the hangman is hangd. 

![Image of the game](documentation/screenshots/the_game.JPG)

* The player wins/loses
    * The player get's to know the secret word. 
    * The player get's asked if they want to play again.
    * If they want to play again it takes them to the beginning of the game.
    * If they dont want to play again a "Thank your for playing!" message shows up.

![Image of winning](documentation/screenshots/win.JPG) ![Image of losing](documentation/screenshots/fail.JPG)

### Future Features
 * Ability to guess whole words if player thinks they know the answer.
 * A highscore board.

## Testing
### Manual testing
I been testing the code many times by my own in the local terminal and in the mock terminal on the deployed site Heroku.
- Tried to put invalid input.
- Navigated through the whole game while trying out diffrent of options.
My family and my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) have also been testing it.
### Automated testing
I used my school Code Institutes own validator https://pep8ci.herokuapp.com/ to check the code automated. I tested run.py, words.py, word_art.py and hangman_stages.py and the code had no errors or warnings in it.

## Technologies Used
* Languages: 
    * Python.
* Libraries:
    * random 
        - Used to select a random word.
    * os
        - Used for its `clear` tool, to clear the terminal window.
* Others:
    * Github
        - To store the repository for submission.
    * Heroku
        - To deploy a live version of the terminal.
    * Lucid 
        - To make a flowchart for preparation to project.
    * Fancy text pro
        - To make word art. 
## Bugs
### Fixed bugs
* On error that I had was when guessing a letter in lowercase, I got an error message saing it is invalid input. I fixed this by using the .upper() method on the input for guessing a letter. So if I guess with lowercase my guess becomes uppercase and that resulted in no error message.
![Error letter image](documentation/bugs/error_letter.JPG)
* Another bug I had was that my data who where a string needed to become an integrer. So I solved this by changing the code to int(data).
![Error lvl image](documentation/bugs/error_lvl.JPG)

## Deployment
 The app was deployed through Heroku. The steps are as following:

1. Log into Github and locate [Github Repository](https://github.com/KlaraMartinsson/hangman-game).
2. After creating a Heroku account, click "New" to create a new app from the dashboard.
3. Create a unique name for the app and select your region: press "Create app".
4. Go to settings and add the necessary Config_vars and buildpacks. Ensure that the buildpacks are set to `Python` and `NodeJS`.
5. Click the `Deploy Branch`.
6. Scroll Down to Deployment Method and select GitHub.
7. Select the name of the repository from Github to be deployed and connect to Heroku.
8. Scroll down to deploy: 
The first option is selecting Automatic deploys (Will Update Automatically with every "git push"). This was chosen for this project.

## Credits
### Code
I learned how to use word art from [Patthoeges](https://github.com/patthoege/hangmangame-pp3-python) gihub. 
I used wordart from [Fancy text pro](https://www.fancytextpro.com/BigTextGenerator?fbclid=IwAR0TsTKLRY91w8ggGxdgfZp6Cu-R4HP2SjAemqdaCRtT86b_tIwp-WeF3u8).
I learned about how to clear the terminal window from Stack Overflows [thread](https://stackoverflow.com/questions/2084508/clear-terminal-in-python).

### Acknowledgements
Thanks to my mentor [Oluwaseun Owonikoko](https://github.com/seunkoko) for advising me.
Thank to my family for trying out the game.