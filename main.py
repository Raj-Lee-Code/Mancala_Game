# Author: Rajan Patel
# Date: 12/03/2022
# Description:  Creating a text based version of the game mancala that allows 2 players to play.
# CS 162
class Player:
    """A player class to create player objects"""

    def __init__(self, name):
        """An init method which takes in a name and sets the player object to a name"""
        self._player = name


class Mancala:
    """A mancala class"""

    def __init__(self):
        """The constructor for Mancala class.Takes no parameters. initializes the required data members.
    All data members are private"""
        self._player1_name = None  # initializes player1 and has initial parameter of None
        self._player2_name = None  # initializes player2 and has initial parameter of None
        self._winner = None  # sets the winner initially as None, but updates at the end of each play_game method
        self._board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]  # starting board

    def create_player(self, name):
        """Takes in a name parameter and creates a player object"""
        if self._player1_name is None:
            player1 = Player(name)
            self._player1_name = name
            return player1  # returns player 1 object
        player2 = Player(name)
        self._player2_name = name
        return player2  # returns the player 2 object

    def get_player(self, number):
        """returns the player name as a string, method takes in a integer representing player 1 or player 2"""
        if number == 1:  # if integer is player 1 returns player 1 name
            return self._player1_name
        elif number == 2:  # if integer is 2 returns player 2 name
            return self._player2_name
        else:  # if it's not a 1 or 2 returns nothing
            return

    def play_game(self, player_index, pit_index):
        """The method that will play the game, taking in the player_index which is if its player 1 or player 2 and
        the pit_index which is the pit that the player wants to move """
        if pit_index > 6 or pit_index <= 0:  # this checks if the pit_index inputted is within bounds
            return "Invalid number for pit index"

        if self._winner is not None:  # checks self._winners, if it does not have None as the value then game has ended
            return "Game is ended"

        if player_index == 1:  # this block of code works to make the player moves, in this case for player 1
            pit_index -= 1  # decreases the pit_index by 1 as the index starts at 0 in python while user inputs the
            # first pit as index 1 instead of 0
            initial_seed_count = self._board[
                pit_index]  # initial seeds are the amount of seeds at the start before moving
            self._board[pit_index] = 0  # sets the chosen pit seeds to 0 as they will all be moved
            while initial_seed_count != 0:  # moves the seeds by counting down the initial seeds that are moved,
                # decreases initial seed count by 1 for every seed added to another pit until seeds have run out
                pit_index += 1
                if pit_index == 13:  # for player 1 skips index 13 as that is player 2 store and resets the pit index
                    # back to 0
                    pit_index = 0
                self._board[pit_index] += 1  # adds a seed to the pit
                initial_seed_count -= 1  # decreases initial seed count
            if self._board[pit_index] == 1 and 5 >= pit_index >= 0:  # this is for special rule 2
                # checks if the last pit_index update has only 1 seed meaning it was empty before
                self._board[6] += (self._board[12 - pit_index] + self._board[pit_index])  # adds opposite pit + player1
                # seeds to player1 store
                self._board[pit_index] = 0  # sets both pits to empty (0)
                self._board[12 - pit_index] = 0
            if pit_index == 6:
                print("player 1 take another turn")  # this is to handle special rule 1

        elif player_index == 2:  # this block of code preforms the same as above but for player 2
            pit_index += 6
            initial_seed_count = self._board[pit_index]
            self._board[pit_index] = 0
            while initial_seed_count != 0:
                pit_index += 1
                if pit_index == 14:
                    pit_index = 0
                if pit_index == 6:
                    pit_index = 7
                self._board[pit_index] += 1
                initial_seed_count -= 1
            if self._board[pit_index] == 1 and 12 >= pit_index >= 7:
                self._board[13] += (self._board[12 - pit_index] + self._board[pit_index])
                self._board[pit_index] = 0
                self._board[12 - pit_index] = 0
            if pit_index == 12:
                print("player 2 take another turn")

        for empty in range(0, 6):  # checks the game state after moves have been made to see if either players pits
            # are all empty or not. If they are then updates self._winners.
            # This first for-statement checks pits for player 1
            if self._board[empty] != 0:
                player_1_board = 1  # assigns a dummy value to player_1_board if a pit in the board is not empty
                break  # ends for loop as not all pits are empty
            player_1_board = None  # if all pits are empty then player_1_board will have value None
        if player_1_board is None:  # if the value is None then this if-statement triggers
            for seeds in range(7, 13):  # looks at player 2's pits and adds them to player 2's store
                self._board[13] += self._board[seeds]
                self._board[seeds] = 0  # sets the pit to 0 after adding it to player 2's store
            if self._board[6] > self._board[13]:  # checks if player 1 has more seeds than player 2
                self._winner = 1  # if yes, then sets winner as "1" representing player 1
            elif self._board[6] < self._board[13]: # if player 2 store has more sets self._winners as "2"
                self._winner = 2
            else:
                self._winner = 3  # if it is a tie sets self._winners to "3"

        for empty in range(7, 13):  # this second for-statement checks if pits for player 2 are empty. logic is same as
            # above, but if player 2 pits are empty then adds the remaining seeds of player 1's pits to their store
            if self._board[empty] != 0:
                player_2_board = 1
                break
            player_2_board = None
        if player_2_board is None:  # same logic as above checking to see which player won or if it is a tie
            for seeds in range(0, 6):
                self._board[6] += self._board[seeds]
                self._board[seeds] = 0
            if self._board[6] > self._board[13]:
                self._winner = 1
            elif self._board[6] < self._board[13]:
                self._winner = 2
            else:
                self._winner = 3

        return self._board  # returns the list of current seeds

    def return_winner(self):
        """A method that takes in no input and returns if there is a winner, tie or game no ended"""
        if self._winner is None:  # checks self._winners which is updated in play game method
            return "Game has not ended"  # if self._winners is not updated that means game is not over
        elif self._winner == 3:  # if it's updated to a value of 3 that means it's a tie
            return "It's a tie"
        else:  # else there is a winner and self._winners will have a 1 or 2 depending on which player won
            return f"Winner is player {self._winner}: " + self.get_player(self._winner)

    def print_board(self):
        """This method prints the current game state of the game and takes in no inputs"""
        player_1_section = [0, 0, 0, 0, 0, 0]  # initializes player 1 section of the board
        player_2_section = [0, 0, 0, 0, 0, 0]  # initializes player 2 section of the board

        for index in range(0, 6):  # two for-loops add the values from the board to player 1 and player 2s section list
            index = index
            player_1_section[index] = self._board[index]
        for index in range(0, 6):
            player_2_section[index] = self._board[index + 7]

        print(  # prints the current board information
            f"player1: \nStore: {self._board[6]} \n{player_1_section} \nplayer2: \nStore: {self._board[13]} "
            f"\n{player_2_section}")