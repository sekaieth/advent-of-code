import os # operating system interface
import re # regular expression

# Get input from txt file
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + "/data.txt", "r")
input = file.read().splitlines()

# Part 1 - Example Game data
exampleGameData: list[str] = [
    'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
    'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
    'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
    'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
    'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
]

# Find if games would be possible with 12 red cubes, 13 green cubes, 14 blue cubes
def isGamePossible(gameData: str) -> bool:
    red = re.findall(r'(\d+) red', gameData)
    green = re.findall(r'(\d+) green', gameData)
    blue = re.findall(r'(\d+) blue', gameData)

    # Loop through each color and check if the number of cubes is greater than the max
    if len(red) > 0 and len(green) > 0 and len(blue) > 0:
        for i in range(len(red)):
            if int(red[i]) > 12:
                return False
        for i in range(len(green)):
            if int(green[i]) > 13:
                return False
        for i in range(len(blue)):
            if int(blue[i]) > 14:
                return False
    return True 

# Find all possible games, their associated game number, and sum up all of the game numbers
def findPossibleGames(gameData: list[str]) -> int:
    possibleGames: list[str] = []
    for game in gameData:
        if isGamePossible(game):
            possibleGames.append(game)
    gameNumbers: list[int] = []
    for game in possibleGames:
        gameNumbers.append(int(re.findall(r'(\d+):', game)[0]))
    return sum(gameNumbers)

# Find the fewest number of cubes of each color for each game
def findFewestCubes(gameData: list[str]) -> int:
    fewestCubes: dict[str, dict[str, int]] = {}
    for game in gameData:
        gameNumber: str = re.findall(r'(\d+):', game)[0]
        red: list[str] = [int(num) for num in re.findall(r'(\d+) red', game)]
        green: list[str] = [int(num) for num in re.findall(r'(\d+) green', game)]
        blue: list[str] = [int(num) for num in re.findall(r'(\d+) blue', game)]

        # Add the game number and the fewest number of cubes of each color to the fewestCubes dictionary
        fewestCubes[gameNumber] = {
            'red': max(red),
            'green': max(green),
            'blue': max(blue)
        }

    # Multiply the values of each game's red, green, and blue cubes together
    gamePowers: list[int] = []
    for game in fewestCubes:
        gamePowers.append(int(fewestCubes[game]['red']) * int(fewestCubes[game]['green']) * int(fewestCubes[game]['blue']))

    # Return the sum of all of the game powers
    return sum(gamePowers) 




print(findPossibleGames(input))
print(findFewestCubes(input))

