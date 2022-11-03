import shutil
try:
    SeedNum
except NameError:
        print("PlantsVsZombies.net Randomizer")
        print("Make sure you have the files from the windows phone version of Plants vs. Zombies")
        print("Put the game's Content folder into the same folder as the installer.")
        print("Put the game's LawnStrings .txt files (LawnStrings_XX.txt) and the .xml files into the randomizer's Content folder")
        print("Please note that there may be bugs and issues with this randomizer.")
        print("")
        SeedNum = input("Type in your seed name >")
print("")
exec(open("Misc.py").read())
print("")
exec(open("plants.py").read())
print("")
exec(open("ZombieWaveAmount.py").read())
print("")
exec(open("SpawnedZombies.py").read())
print("")
exec(open("Conveyor.py").read())
print("")
exec(open("Plantstats.py").read())
print("")
exec(open("LawnstringENPatcher.py").read())
print("")
shutil.copy('RandomizerSettings.xml', 'Lawn_PCGL/RandomizerSettings.xml')
shutil.copy('RandomizerSettings.xml', 'Lawn_PCDX/RandomizerSettings.xml')
try:
    InstalledviaGUI
except NameError:
    print("Now you can start setting up the game.")
    print("Open up the sln file with Visual Studio 2019")
    print("Build the PC port projects (Lawn_PCDX and Lawn_PCGL) (Android port is untested), build them again if a error occurs")
    print("and now you're ready to play the randomizer, choose one of the exe files you had compiled to play")
