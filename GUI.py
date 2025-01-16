import tkinter as tk
from tkinter import messagebox

# Initialize board size
size = 3  # You can change the grid size here

class TicTacToeGUI:
    def __init__(self, root, size):
        self.root = root
        self.size = size
        self.board = [["*" for _ in range(size)] for _ in range(size)]
        self.current_player = "X"
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.create_board()
    
    def create_board(self):
        """Create the grid of buttons for the game."""
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j] = tk.Button(
                    self.root, text=" ", font=("Arial", 20), width=4, height=2,
                    command=lambda i=i, j=j: self.make_move(i, j)
                )
                self.buttons[i][j].grid(row=i, column=j)

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

    def is_tie(self):
        """Check if the game is a tie."""
        return all(cell != "*" for row in self.board for cell in row)

    def reset_game(self):
        """Reset the game for a new round."""
        self.board = [["*" for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = "X"
        for i in range(self.size):
            for j in range(self.size):
                self.buttons[i][j].config(text=" ")

# Main function to start the game
def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    game = TicTacToeGUI(root, size)
    root.mainloop()

if __name__ == "__main__":
    main()
