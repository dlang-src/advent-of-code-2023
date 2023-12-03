import re

def sum_valid_games(input_file, max_cubes):
    with open(input_file) as f:
        lines = f.readlines()

    # Each line in the input file consists of a GameID and the results.
    # Format: Game DD: N Color 1, M Color 2, O Color 3; P Color 2, Q Color 3, R Color 1; ...
    # Only the maximum value for each color type is needed.
    # Read the line, tokenize and create a dictionary entry for each game
    # The dictionary format will be: ID: Max R, Max B, max G
    games = {}
    sum_ids = 0
    for line in lines:
        # A sample line to work with 
        # Game 8: 8 green, 4 blue; 17 green, 4 red; 10 blue, 5 green, 9 red; 9 green, 8 red, 3 blue; 9 green, 5 red, 2 blue
        game_id = int(re.search(r"\d+", line).group(0))
        # Iterate through the game "results" to find the maximum value for each color
        # The results are not in a color order, and not all colors are in each result
        # 1 green, 1 blue, 6 red; 1 green, 4 red, 1 blue; 6 red, 1 blue
        red_max = max(list(map(int, re.findall(r"\d+(?= red)", line))))
        blue_max = max(list(map(int, re.findall(r"\d+(?= blue)", line))))
        green_max =max(list(map(int, re.findall(r"\d+(?= green)", line))))
        
        # With the max values for each result, compare to the values in
        # max_cube to determine if this is a valid game. 
        if red_max <= max_colors["red"] and blue_max <= max_colors["blue"] and green_max <= max_colors["green"]:
            # This is a valid game! 
            sum_ids+=game_id

    return sum_ids

max_colors = {"red": 12, "green": 13, "blue": 14}
result = sum_valid_games("input.txt", max_colors)
print(f'The sum of valid games is {result}')
