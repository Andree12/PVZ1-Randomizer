import random
mode = ""
while mode != "hard" and mode != "random" and mode != "vanilla":
 print("Select your zombie wave amount mode in adventure mode")
 print("")
 print("vanilla: retain the amount of waves in each adventure mode level the same")
 print("hard: the amount of waves in each adventure mode level are all 30")
 print("random: the amount of waves in each adventure mode level are all randomized")
 print("")
 print("Please note that this doesn't apply to the first three levels (as they are tutorial levels) and 1-5 to make sure the player passes through it")
 mode = input()

hardwaves = [ 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
vanillawaves = [ 10, 10, 20, 10, 20, 20,
            10, 20, 10, 20, 10, 10, 20, 10, 20, 20,
            10, 20, 20, 30, 20, 20, 30, 20, 30, 30,
            10, 20, 10, 20, 20, 10, 20, 10, 20, 20,
            10, 20, 20, 30, 20, 20, 30, 20, 30, 30]

randomwaves = [10, 8, 20, 30]

if mode == "hard":
 selectedwaves = hardwaves

if mode == "vanilla":
 selectedwaves = vanillawaves

if mode == "random":
 random.seed(SeedNum)
 selectedwaves = []
 while len(selectedwaves) != 46:
  waveamount = random.choice(randomwaves)
  selectedwaves.append(waveamount)
##print(selectedwaves)
##print(len(selectedwaves))
listid = 0
print("Setting up zombie waves")
while listid != len(selectedwaves):
 wavenumber = selectedwaves[listid]
 a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf-8")
 word = a_file.read()
 stringwavenumber = str(wavenumber)
 a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
 replace_string = word.replace('randomwavenum', stringwavenumber, 1)
 a_file.write(replace_string)
 a_file.close()
 listid = listid + 1
print("Done")
