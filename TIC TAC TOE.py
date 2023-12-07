import tkinter as tk
from tkinter import messagebox

# Create a Tic Tac Toe class
class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Define the players and their symbols
        self.player1 = "X"
        self.player2 = "O"
        self.current_player = self.player1

        # Define the game board
        self.board = [["", "", ""],
                      ["", "", ""],
                      ["", "", ""]]

        # Create buttons for the game board
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=5,
                                   command=lambda r=row, c=col: self.handle_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

        # Create a reset button
        reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        reset_button.grid(row=3, columnspan=3, padx=5, pady=10)

    def handle_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            button = self.buttons[row][col]
            button.config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def check_winner(self, player):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset_game(self):
        self.current_player = self.player1
        for row in range(3):
            for col in range(3):
                self.board[row][col] = ""
                button = self.buttons[row][col]
                button.config(text="")


def main():
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
