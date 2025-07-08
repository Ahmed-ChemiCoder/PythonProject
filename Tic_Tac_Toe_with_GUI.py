import tkinter as tk
from tkinter import messagebox

class Player:
    def __init__(self, name="", symbol=""):
        self.name = name
        self.symbol = symbol

class GameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.players = [Player(), Player()]
        self.current_player_index = 0
        self.board = [""] * 9
        self.buttons = []

        self.setup_frame = None
        self.game_frame = None

        self.create_setup_screen()

    def create_setup_screen(self):
        self.setup_frame = tk.Frame(self.root)
        self.setup_frame.pack(padx=20, pady=20)

        tk.Label(self.setup_frame, text="Player 1 Name:").grid(row=0, column=0)
        self.p1_name_entry = tk.Entry(self.setup_frame)
        self.p1_name_entry.grid(row=0, column=1)

        tk.Label(self.setup_frame, text="Player 1 Symbol (X or O):").grid(row=1, column=0)
        self.p1_symbol_entry = tk.Entry(self.setup_frame)
        self.p1_symbol_entry.grid(row=1, column=1)

        tk.Label(self.setup_frame, text="Player 2 Name:").grid(row=2, column=0)
        self.p2_name_entry = tk.Entry(self.setup_frame)
        self.p2_name_entry.grid(row=2, column=1)

        tk.Label(self.setup_frame, text="Player 2 Symbol (X or O):").grid(row=3, column=0)
        self.p2_symbol_entry = tk.Entry(self.setup_frame)
        self.p2_symbol_entry.grid(row=3, column=1)

        start_btn = tk.Button(self.setup_frame, text="Start Game", command=self.start_game)
        start_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def start_game(self):
        # Get names and symbols
        p1_name = self.p1_name_entry.get().strip()
        p1_symbol = self.p1_symbol_entry.get().strip().upper()
        p2_name = self.p2_name_entry.get().strip()
        p2_symbol = self.p2_symbol_entry.get().strip().upper()

        # Validate
        if not (p1_name and p2_name and p1_symbol and p2_symbol):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return
        if p1_symbol not in ['X', 'O'] or p2_symbol not in ['X', 'O']:
            messagebox.showerror("Symbol Error", "Symbols must be X or O.")
            return
        if p1_symbol == p2_symbol:
            messagebox.showerror("Symbol Conflict", "Players must choose different symbols.")
            return

        # Save players
        self.players[0] = Player(p1_name, p1_symbol)
        self.players[1] = Player(p2_name, p2_symbol)

        # Destroy setup and start game
        self.setup_frame.destroy()
        self.create_game_board()

    def create_game_board(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(padx=20, pady=20)

        for i in range(9):
            btn = tk.Button(self.game_frame, text="", font=('Arial', 24), width=5, height=2,
                            command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def make_move(self, index):
        if self.board[index] == "":
            player = self.players[self.current_player_index]
            self.board[index] = player.symbol
            self.buttons[index].config(text=player.symbol, state='disabled')

            if self.check_win():
                messagebox.showinfo("Game Over", f"{player.name} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        combos = [
            [0,1,2], [3,4,5], [6,7,8], # rows
            [0,3,6], [1,4,7], [2,5,8], # cols
            [0,4,8], [2,4,6]           # diags
        ]
        for c in combos:
            if self.board[c[0]] == self.board[c[1]] == self.board[c[2]] != "":
                return True
        return False

    def check_draw(self):
        return all(cell != "" for cell in self.board)

    def reset_game(self):
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state="normal")
        self.current_player_index = 0

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()
