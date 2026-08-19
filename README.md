# Scrabble in Python


A two-stage implementation of a **Scrabble-inspired game in Python**, developed progressively from a basic terminal-based version into a more advanced version with modular abstractions, vocabulary management and automated players.


## Repository Structure


```text
Scrabble-Game/
├── scrabble-v1/
│   └── scrabble.py
├── scrabble-v2/
│   └── scrabble2.py
└── README.md
Overview

This repository contains two versions of the same Scrabble project.

The first version focuses on implementing the core mechanics of the game.

The second version builds on those concepts and introduces a more modular architecture, vocabulary management and AI-controlled players.

Version 1 — Basic Scrabble

The first version implements the fundamental mechanics of a terminal-based Scrabble game.

Main Features
15×15 Scrabble board
support for multiple human players
player racks with up to 7 letters
configurable letter distribution
configurable letter scoring
custom pseudo-random letter shuffling
horizontal and vertical word placement
move validation
letter exchange
passing
score tracking
complete game loop
Main Concepts
Python
Procedural Programming
Dictionaries
Lists and Tuples
Matrix Representation
Input Validation
Game State Management
Pseudo-Random Number Generation
Bitwise Operations
Turn-Based Game Logic
Version 2 — Scrabble with AI Players

The second version extends the original project into a more advanced implementation.

It introduces:

Abstract Data Types
dedicated abstractions for cells, players, vocabulary and board
external vocabulary loading
word scoring and filtering
board-pattern generation
automated word search
human and AI players
multiple AI difficulty levels
more modular game architecture

The game supports between 2 and 4 players, including both human players and computer-controlled agents.

AI Difficulty Levels

The automated players can operate at three different levels:

FACIL
MEDIO
DIFICIL

The difficulty affects how much of the possible move space the agent evaluates before selecting a move.

FACIL    -> smaller search space
MEDIO    -> larger search space
DIFICIL  -> more candidate moves evaluated
Project Evolution

The progression between the two versions can be summarized as:

Version 1
Core Scrabble mechanics
        │
        ▼
Board, Players and Scoring
        │
        ▼
Move Validation
        │
        ▼
Complete Human Game
        │
        ▼
Version 2
Abstract Data Types
        │
        ▼
Vocabulary Management
        │
        ▼
Pattern-Based Word Search
        │
        ▼
AI Players
        │
        ▼
Multiple Difficulty Levels
Board

Both versions use a:

15 × 15

board.

Empty cells are represented by:

.

Words can be placed horizontally or vertically.

The first move must cross the center of the board:

(8, 8)

Later moves must connect to letters already present on the board.

Letter Bag

The projects implement a letter bag containing different quantities of each letter.

The bag is shuffled using a custom pseudo-random number generator based on bitwise transformations.

Using the same seed produces the same letter order, making the shuffle deterministic and reproducible.

Word Validation

Before a word is placed, the game verifies that:

it fits inside the board
it respects the chosen direction
overlapping letters match
the player owns the required letters
repeated letters do not exceed the available quantity

Version 2 additionally checks candidate words against an external vocabulary.

Vocabulary System

Version 2 loads words from an external file.

Words are organized internally according to:

Word Length
    │
    └── First Letter
            │
            └── Candidate Words

This helps reduce the search space when looking for playable words.

Automated Word Search

Version 2 can analyse the current board and generate possible word patterns.

For example:

C . S A

represents a pattern where one position must be completed using a letter from the player's rack.

The system searches the vocabulary for valid words that:

match existing letters
fit the available spaces
can be formed using the player's letters
satisfy scoring constraints

The best valid candidate can then be selected by an AI player.

Player Actions

Players can perform three main actions.

Play
J <row> <column> <direction> <word>

Example:

J 8 6 H CASA
Exchange Letters
T <letters>
Pass
P
Game Flow
Initialize Game
      │
      ▼
Create Board
      │
      ▼
Shuffle Letter Bag
      │
      ▼
Create Players
      │
      ▼
Give 7 Letters
      │
      ▼
Game Loop
      │
      ▼
Human / AI Move
      │
      ▼
Validate Move
      │
      ▼
Update Board
      │
      ▼
Update Score
      │
      ▼
Refill Player
      │
      ▼
End Condition
End Conditions

The game ends when:

all players pass consecutively

or

a player has no letters left and the letter bag is empty

The final scores are returned at the end of the game.

Technologies & Concepts
Python
Procedural Programming
Abstract Data Types
Dictionaries
Lists and Tuples
File I/O
String Processing
Search Algorithms
Pattern Matching
Game State Management
Input Validation
Pseudo-Random Number Generation
AI Agents
Turn-Based Game Logic
Key Technical Highlights

This repository demonstrates:

implementation of a complete board game
progression from procedural to more modular design
custom pseudo-random shuffling
board-state management
move validation
word-overlap handling
external vocabulary processing
automated word search
AI-controlled players
multiple difficulty levels
Academic Context

Developed as two consecutive projects for Programming Fundamentals at Instituto Superior Técnico (IST).
