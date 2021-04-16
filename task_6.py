class WrongNumberOfPlayersError(Exception):
   pass
       

class NoSuchStrategyError(Exception):
   pass


def rps_game_winner(array=None):
    if array is None:
        raise WrongNumberOfPlayersError()
    variants = ["S", "P", "R"]
    strategy = {"S": 2, "P": 1, "R": 0}
    if len(array) > 2 or len(array) < 2:
        raise WrongNumberOfPlayersError()
    if len(array[0]) < 2 or len(array[1]) < 2:
        raise NoSuchStrategyError()
    if array[0][1] not in variants or array[1][1] not in variants:
        raise NoSuchStrategyError()
    else:
        diff = strategy[array[0][1]] - strategy[array[1][1]]
        if diff == -1 or diff == 2:
            return f"{array[1][0]} {array[1][1]}"
        elif diff == 0:
            return f"{array[0][0]} {array[0][1]}"
        else:
            return f"{array[0][0]} {array[0][1]}"


"""
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])) #=> WrongNumberOfPlayersError
print(rps_game_winner([['player1', 'P'], ['player2', 'A']])) #=> NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) #=> 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'
"""
