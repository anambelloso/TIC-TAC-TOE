# TIC-TAC-TOE
A fun and interactive Tic Tac Toe game built with Python and Tkinter. This project showcases a simple yet effective implementation of the classic game, complete with a graphical user interface, player interaction, and game logic.

## Features
- Customizable board size (default 3x3).
- Interactive gameplay with alternating turns for "X" and "O".
- Automatic winner and tie detection.
- Game resets automatically after a round.

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```
Ensure Python 3.x is installed.
Run the game:
```
python tic_tac_toe.py
```
## How to Play
1. Launch the game using the steps above.
2. Players take turns clicking on cells to mark "X" or "O".
3. The game announces the winner or a tie and resets automatically.

## Creating the Board
This function sets up the grid of buttons for the game interface.
``` python
def create_board(self):
    """Create the grid of buttons for the game."""
    for i in range(self.size):
        for j in range(self.size):
            self.buttons[i][j] = tk.Button(
                self.root, text=" ", font=("Arial", 20), width=4, height=2,
                command=lambda i=i, j=j: self.make_move(i, j)
            )
            self.buttons[i][j].grid(row=i, column=j)
```
## Making a Move
This function manages the player's move and updates the board.
``` python
def make_move(self, i, j):
    """Handle the player's move."""
    if self.board[i][j] != "*":
        return  # Ignore clicks on already-filled cells

    self.board[i][j] = self.current_player
    self.buttons[i][j].config(text=self.current_player)

    if self.check_winner(self.current_player):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.reset_game()
    elif self.is_tie():
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_game()
    else:
        self.current_player = "O" if self.current_player == "X" else "X"
```
## Checking for a Winner
This function determines if a player has won.
``` python
def check_winner(self, player):
    """Check for a winner."""
    # Check rows and columns
    for i in range(self.size):
        if all(self.board[i][j] == player for j in range(self.size)) or \
           all(self.board[j][i] == player for j in range(self.size)):
            return True
    
    # Check diagonals
    if all(self.board[i][i] == player for i in range(self.size)) or \
       all(self.board[i][self.size - 1 - i] == player for i in range(self.size)):
        return True

    return False
```
## Resetting the Game
Resets the board for a new game.
``` python
def reset_game(self):
    """Reset the game for a new round."""
    self.board = [["*" for _ in range(self.size)] for _ in range(self.size)]
    self.current_player = "X"
    for i in range(self.size):
        for j in range(self.size):
            self.buttons[i][j].config(text=" ")
```
## Main Function
The game is launched using the ```main()``` function.
``` python
def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game = TicTacToeGUI(root, size=3)  # Default size is 3x3
    root.mainloop()

if __name__ == "__main__":
    main()
```

## Contributions
Contributions are welcome! Feel free to fork this repository, submit pull requests, or raise issues. Suggestions for additional features or improvements are highly encouraged.

## Future Enhancements
- AI opponent for single-player mode.
- Online multiplayer functionality.
- Customizable themes and board designs.

## License
This project is released under the MIT License.
```
Feel free to adjust or expand upon this as needed! 😊
```
