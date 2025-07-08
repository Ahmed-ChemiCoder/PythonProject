class Player: 
   
    def __init__(self):
        self.name = " " 
        self.symbol = " " 

    def choose_name(self):
        while True:
          name = input("Enter your name(only letters): ")
          if name.isalpha():
             self.name =name
             break
          print("Please enter a valid name using only letters.")
    
    def choose_symbol(self):
        while True:
          symbol = input(f"{self.name},Choose a symbol between 'X' and 'O'; ")
          if symbol.isalpha() and len(symbol) ==1: 
              self.symbol =symbol.upper() 
              break
          print("Please enter a valid single symbol.")

class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
       
    def display_board(self):
        for i in range(0,9,3): 
            print("|".join(self.board[i:i+3]))
            if i < 6:
                print("-"*5)

    def update_board(self ,choice ,symbol):
        if self.is_valed_move(choice):
            self.board[choice-1] = symbol
            return True
        return False

    def is_valed_move(self, choice ):
        return self.board[choice-1].isdigit() 

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Menu:
    def display_main_menu(self):
        print("Welcome to Tic Tac Toe")
        print('1. Start Game')
        print('2. End Game')
        choice = input("Enter your choice 1 or 2: ")
        return choice
    def display_endgame_menu(self):
        menu_text = """
        Game Over!
        1. Restart Game
        2. End Game
        Enter your choice 1 or 2: """
        choice = input(menu_text)
        return choice

class Game:
    
    def __init__(self):

        self.players = [Player(), Player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice =self.menu.display_main_menu()
        if choice == "1":
            self.setup_players() 
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, Player in enumerate(self.players ,start=1):
            print(f"player {number}, Enter your details!")
            Player.choose_name()
            Player.choose_symbol()

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


    def play_turn(self):
       player = self.players[self.current_player_index]
       self.board.display_board()
       print(f"{player.name}'s turn {player.symbol}")
       while True:
        try:
            cell_choice = int(input("Choose a cell (1-9): "))
            if 1<= cell_choice <=9 and self.board.update_board(cell_choice ,player.symbol):
               break
            else:
                print("Please enter a valid move.")
        except ValueError:
           print("Please enter a valid move between 1-9.")
       self.switch_player()

    def switch_player(self):
        self.current_player_index = 1- self.current_player_index


    def check_win(self):
        win_combination = [
            [0 ,1 ,2] ,[3 ,4, 5] ,[6, 7, 8],
            [0 ,3 ,6] ,[2 ,4 ,7] ,[1 ,5 ,8],
            [0 ,4 ,8] ,[2 ,4 ,6]
        ]

        for comb in win_combination:
            if (self.board.board[comb[0]] == self.board.board[comb[1]] == self.board.board[comb[2]]):
                return True
            
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) 

    def quit_game(self):
        
        print("Thank you for playing!")

game = Game()
game.start_game()
