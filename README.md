# Go Fish!

## Diploma in Full Stack Software Development - Portfolio Project 

<!-- Mockup Image -->


[Click here to view the live project.](https://pp3-go-fish.herokuapp.com/)

Go Fish! is a terminal-based card game which is aimed at children aged 6+.

## UX
My aim was to create a game which is fun to play, yet simple to manipulate using text inputs only.

### Ideal Clients

* Children aged 6+
* English speakers
* Children who enjoy playing games which involve pattern-matching

### The application helps clients to:
* Easily navigate the terminal
* Test and improve short-term memory skills
* have fun

### Owner Stories
* I want to a game which is simple, yet fun to play
* I'd like to encourage players to come back for more
* I want to demonstrate my newly acquired Python skills

### User Stories
* As a visitor, I want a game that is simple to navigate and play
* As a visitor I enjoy the challenge of trying to beat the computer

## Scope
The application featuers are as follows:

### Features

1. A section explaining the rules for playing the game, scoring, etc
2. Instructions on how to enter card requests
3. A help command to remind the player of the rules & instructions
4. An exit command for terminating the game mid-play, if desired
5. Notifications on which cards have been requested, drawn from the stockpile, etc
6. A scoreboard displaying whose turn it is to play, the user's hand and books won by both the user and computer

### Features to implement in future
1. The ability to allow multiple players against each other or the computer
2. Adding graphical representations of the cards, as opposed to just text

## Skeleton
The game uses a single terminal window as the interface, run on Python.

* I visited the [Bicycle Cards](https://bicyclecards.com/how-to-play/go-fish/) website, to look for possible card games which one would be able to play, using text-only input and output.
* Eventually, I settled on Go Fish! as it fitted the bill.
Below is the initial flowchart I created in order to work out which basic functions to use as a starting point:

![](docs/images/readme/go-fish-flowchart.webp)

## Technologies Used
* [Gitpod](https://gitpod.io/workspaces) - IDE for writing code and version control
* [Github](https://github.com/) - Where the repository is hosted
* [Heroku](https://id.heroku.com/login) - Hosting for the live app
* [pylint](https://pypi.org/project/pylint/) - Code validation and error-checking
* [LucidChart](https://lucid.app/lucidchart) - Flowchart application
* [Cloudconvert.com](https://cloudconvert.com/) - Converting README images to .webp format
* [Tinypng.com](https://tinypng.com/) - README image compression & optimisation

# Testing 
## Testing against client stories from UX section of this document

1. **As a visitor, I want a game that is simple to navigate and play**
* Inputs are as simple as pressing <ENTER>, typing numbers (2 to 10), and letters (J, Q, K, A, H, E)
* The player receive notifications when cards are dealt, the cards in their hand, whose turn it is and books won

![](docs/images/readme/scoreboard.webp)

2. **As a visitor I enjoy the challenge of trying to beat the computer**
* 