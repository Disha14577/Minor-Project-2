# Minor-Project-2
# Racing Beast
Racing Beast is a car racing game which is a fun and engaging genre of video game where players control a car and compete to win a race, avoid obstacles, or beat a timer.
## Table of contents

- [About](#About)
- [Technologies used](#Technologiesused)
- [Project Structure](#ProjectStructure)
- [Features](#features)
- [Getting started](#GettingStarted)
- [Steps To Create Car Racing Game](#StepsToCreateCarRacingGame)
- [Setup & Installation](#Setup&Installation)
- [Future Enhancement](#FutureEnhancement)
- [Live Demo](#LiveDemo)
- [License](#-license)
---
## About
The Car Racing Game is a 2D endless runner-style game built using Python and Pygame. In this game, the player controls a car driving on a busy road with the goal of avoiding oncoming enemy cars for as long as possible. The background road scrolls continuously to simulate motion, and the speed gradually increases to make the game more challenging over time. The game features intuitive controls, basic sound effects, and a scoring system that tracks the player's survival time. This project demonstrates core concepts of game development such as sprite handling, collision detection, user input, and modular code structure, making it a great learning experience and a fun, playable game.

## Technologies used
- python
- pygame
- Assets (Graphics & Audio)
- Editor / IDE
- VS Code (with Python extension)
- PyCharm
  
## Project Structure
```bash
car-racing-game/
│
├── assets/                   # Game assets
│   ├── car.png               # Player's car image
│   ├── enemy_car.png         # Enemy car image
│   ├── road.png              # Road background image
│   └── crash.wav             # Crash sound effect
│
├── main.py                   # Main game loop and setup
├── LICENSE                   # Project MIT license
├── highscore.txt             # show highscore
└── README.md                 # Project documentation
```
### Key Features:
- Smooth car control using arrow keys
- Continuously scrolling road animation
- Randomly appearing enemy cars
- Collision detection with game over sound
- Score tracking for how long you survive
- Organized codebase with separate modules for game logic and utilities

## Why I consider building a car racing game?
- I chose to build a car racing game because it's a classic and exciting genre that allows me to apply and showcase fundamental game development concepts such as movement, collision detection, event handling, scoring systems, and animation.
- It's simple enough to be achievable within a limited timeframe, yet flexible enough to allow for creative additions like sound effects, increasing difficulty, and visual enhancements.
- Working on this project helped me strengthen my Python and Pygame skills, improve my problem-solving ability, and gain hands-on experience in structuring a real-world game application.
-	it is a easy to start with, but offers room for advanced features like speed scaling, collision detection, and power-ups.
-	It is a perfect project to explore the capabilities of the Pygame library in a fun and visual way.
-	It Allow creative expression through designing cars, road styles, enemy behavior, and sound effects.

## Steps To Create Car Racing Game
### To create racing beast using pygame, follow these step-by-step instructions:
- Set up environment – Install Python & Pygame, create project folder.
- Initialize game – Set up window, FPS, and game loop.
- Load assets – Import car, enemy, road images, and sounds.
- Draw elements – Display player car and enemies on screen.
- Add controls – Move car using arrow keys, limit movement.
- Scroll background – Simulate road movement with a looping image.
- Enemy logic – Randomly generate enemy cars and move them down.
- Collision detection – Detect crashes and trigger game over.
- Score system – Increase score over time and display it.
- Test & enhance – Add sound, polish visuals, and fix bugs.

## Setup & Installation
You can easily set up this weather app locally by following these steps:
### Prerequisites 

- Python 3.x
- Pygame library

Install Pygame with:

```bash
pip install pygame
```

## Future Enhancement
- Add power-ups and boosters
- Include different car models to choose from
- Implement a main menu and pause/resume feature
- Save and display high scores
- Add levels or difficulty progression
   
## live Demo

![SS1](output1.png)
![SS1](output2.png)
![SS1](output3.png)   

## 📜 License
This project is [MIT](./LICENSE) licensed. 


