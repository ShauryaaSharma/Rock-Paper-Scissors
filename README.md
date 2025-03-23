# 🪨📄✂️ Rock Paper Scissors Game - Python

This is a simple implementation of the classic Rock, Paper, Scissors game in Python. The player goes head-to-head with the computer, where both choose one of the three options (🪨, 📄, or ✂️), and the winner is determined based on the standard rules.

## How It Works

The player is prompted to choose between Rock (0 🪨), Paper (1 📄), or Scissors (2 ✂️). <br>
The computer randomly selects one of the three options.<br>
The game then compares the choices to determine the winner: <br>
🪨 beats ✂️. <br>
✂️ beats 📄. <br>
📄 beats 🪨. <br>
The result is printed, whether it's a win, loss, or draw. <br>

## Features

ASCII art used to represent 🪨, 📄, and ✂️. <br>
Randomness for the computer's choice. <br>
Clear display of both the player's and the computer's choices, followed by the result. <br>

## Code Breakdown

ASCII Art: Used multi-line strings to represent the visual art of 🪨, 📄, and ✂️.<br>
Random Module: random.randint(0, 2) is used to simulate the computer's random choice.<br>
User Input: The user is prompted to input their choice as an integer (0, 1, or 2).<br>
Conditional Logic: The outcome is determined by comparing the player's input and the computer’s random selection.<br>
