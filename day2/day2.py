sum = 0
redLimit, greenLimit, blueLimit = 12, 13, 14

with open("input.txt") as input:
    # TODO: For each set of cubes, sum the gameID for all games that are possible.
    for line in input:
        game, sets = line.strip().split(": ")
        gameID = int(game.split(" ")[-1])
        flag = True
        for set in sets.split("; "):    # set = 9 green, 3 blue;
            colorDict = {}
            pairs = set.split(", ")
            for pair in pairs:          # pair = 9 green
                count, color = pair.split(" ")
                colorDict[color] = int(count)
            if not(colorDict.get("red", 0) <= redLimit and colorDict.get("green", 0) <= greenLimit and colorDict.get("blue", 0) <= blueLimit):
                flag = False        
        if flag:
            print(f"adding {gameID}")
            sum += gameID

print(sum)

