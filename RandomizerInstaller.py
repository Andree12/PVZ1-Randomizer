print("PlantsVsZombies.net Randomizer Installer")
print("Please note that there may be bugs and issues with this randomizer.")
print("")
print("Instructions 1/2:")
print("Make sure you have the files from the windows phone version of Plants vs. Zombies")
print("Put the game's Content folder into the same folder as the installer, don't replace the files that are already in the randomizer's Content folder")
print("Put the game's LawnStrings .txt files (LawnStrings_XX.txt) and the .xml files into the randomizer's Content folder")
print("")
SeedNum = input("Type in your seed name >")
print("")
exec(open("plants.py").read())
print("")
exec(open("Upgradeplants.py").read())
print("")
exec(open("ZombieWaveAmount.py").read())
print("")
exec(open("LawnstringENPatcher.py").read())
print("")
print("Instructions 2/2:")
print("Now you can start setting up the game.")
print("Open up the sln file with Visual Studio 2019 first")
print("Build the PC port projects (Lawn_PCDX and Lawn_PCGL) (Android port is untested)")
print("and now you're ready to play the randomizer!")
input("press enter to leave >")
