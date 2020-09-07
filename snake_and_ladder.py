from random import randint

class Snake:
    def __init__(self , start_point = None , end_point = None):
        self.start_point = start_point
        self.end_point = end_point
        self.message = f"SNAKE BITE -> GO TO {self.end_point}"

    #Getters , Setters
    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point

    def set_start_point(self , start_point):
        self.start_point = start_point

    def set_end_point(self, end_point):
        self.end_point = end_point


class Ladder:
    def __init__(self , start_point = None , end_point = None):
        self.start_point = start_point
        self.end_point = end_point
        self.message = f"LADDER -> CLIMB TO {self.end_point}"

    #Getters , Setters
    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point

    def set_start_point(self , start_point):
        self.start_point = start_point

    def set_end_point(self, end_point):
        self.end_point = end_point

class Player:
    def __init__(self , name = None , position = None):
        self.name = name
        self.position = position
        self.is_winner = False

    def move(self , dice_value , encounter = None):
        '''
        moving a player from one position to another 
        checks for index out of bounds
        moves according to encounters if any
        '''
        
        if not encounter:
            print(f"Player {self.name} has rolled a {dice_value}")
            new_position = self.position + dice_value
        
        else:
            new_position = dice_value

        if new_position > 100:
            print(f'Player {self.name} has not been moved from {self.position} to {new_position} <OUT OF BOUNDS>')
            return

        elif new_position == 100:
            self.is_winner = True

        print(f'Player {self.name} has been moved from {self.position} to {new_position}')
        self.position = new_position



    #Getters , Setters
    def get_name (self):
        return self.name

    def get_position(self):
        return self.position

    def set_name (self , name):
        return self.name
    
    def set_position (self , position):
        return self.position



    
class Dice:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = randint(1,6)
        return self.value


class Board:
    def __init__(self):
        self.board = [None for x in range(101)]

    def populate(self, snake_positions , ladder_positions ):

        #placing snakes
        for start_point , end_point in snake_positions:
            snake = Snake(start_point , end_point)
            self.board[start_point] = snake
            
        #placing ladders
        for start_point , end_point in ladder_positions:
            ladder = Ladder(start_point , end_point)
            self.board[start_point] = ladder

        return self.board

        
class Game:
    def __init__(self):
        self.winner = None
    
    def play(self):
        # hard coded snake and ladder positions
        snake_positions = [(7,3) , (37,13) , (80,60)]
        ladder_positions = [(1,27) , (33,60) , (70,79)]

        # hard coded details for 2 players
        players = [ Player("A" , 1), Player("B" , 1)]
        turns = 0

        #initializing board and Dice
        board = Board().populate(snake_positions , ladder_positions)
        dice = Dice()
        
        # looping till we get a winner
        while self.winner == None:
            turns += 1

            print(f"\n--------------Turn : {turns}--------------")

            for player in players:

                dice_value = dice.roll()
                player.move(dice_value)
                
                #encounter event for snake / ladder
                encounter = board[player.position]
                if encounter:
                    end_point = encounter.end_point
                    print(f"--ENCOUNTER : {encounter.message}--")
                    player.move(end_point , encounter = True)

                #checking if player won
                if player.is_winner:
                    self.winner = player
                    break



        print("\n--------------GAME OVER--------------")
        print(f"Player {self.winner.name} Has won the game after {turns} turns")
        print("--------------GAME OVER--------------\n")


if __name__ == "__main__":
    game = Game()
    game.play()