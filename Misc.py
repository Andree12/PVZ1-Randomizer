import random
random.seed(SeedNum)
from xml.etree import ElementTree as et
datafile = "RandomizerSettings.xml";
tree = et.parse(datafile)

StorePlants = ["STORE_ITEM_PLANT_GATLINGPEA",
               "STORE_ITEM_PLANT_TWINSUNFLOWER",
               "STORE_ITEM_PLANT_SPIKEROCK",
               "STORE_ITEM_PLANT_GLOOMSHROOM",
               "STORE_ITEM_PLANT_CATTAIL",
               "STORE_ITEM_PLANT_GOLD_MAGNET",
               "STORE_ITEM_PLANT_COBCANNON",
               "STORE_ITEM_PLANT_WINTERMELON"]

try:
    Sunmeta
    DontChangeSeedpacketIconOrder
    RandomizeBackground
    EnableCustombackgrounds
    RandomizeStorePlants
except NameError:
    Sunmeta = None
    DontChangeSeedpacketIconOrder = None
    RandomizeBackground = None
    EnableCustombackgrounds = None
    RandomizeStorePlants = None

while Sunmeta != 'n' and Sunmeta != 'y':
    print("Enable 50 Sun meta? (y/n)>")
    Sunmeta = input()

while DontChangeSeedpacketIconOrder != 'n' and DontChangeSeedpacketIconOrder != 'y':
    print("Don't change the order of the seed packets? (y/n)>")
    DontChangeSeedpacketIconOrder = input()

while RandomizeBackground != 'n' and RandomizeBackground != 'y':
    print("Randomize backgrounds? (y/n)>")
    RandomizeBackground = input()

while RandomizeStorePlants != 'n' and RandomizeStorePlants != 'y':
    print("Shuffle the order of Store Plants? (y/n)>")
    RandomizeStorePlants = input()
    
if RandomizeBackground == 'y':
    while EnableCustombackgrounds != 'n' and EnableCustombackgrounds != 'y':
        print("Include custom backgrounds in the background randomizer? y/n)>")
        EnableCustombackgrounds = input()

    World1BackgroundList = ["Num1Day", "Num7GreatWall"]

    World2BackgroundList = ["Num2Night", "Num9JTTW2"]

    World3BackgroundList = ["Num3Pool"]

    World4BackgroundList = ["Num4Fog"]

    World5BackgroundList = ["Num5Roof"]

    if EnableCustombackgrounds == 'y':
        World1BackgroundList.append("Num18CustomMars")
        #World2BackgroundList.append()
        World3BackgroundList.append("Num15CustomFlood")
        World4BackgroundList.append("Num16CustomWaterFallNight")
        World5BackgroundList.append("Num17CustomEveningRoof")
    tree.find(".//Background1").text = random.choice(World1BackgroundList)
    tree.find(".//Background2").text = random.choice(World2BackgroundList)
    tree.find(".//Background3").text = random.choice(World3BackgroundList)
    tree.find(".//Background4").text = random.choice(World4BackgroundList)
    tree.find(".//Background5").text = random.choice(World5BackgroundList)
else:
    tree.find(".//Background1").text = "Num1Day"
    tree.find(".//Background2").text = "Num2Night"
    tree.find(".//Background3").text = "Num3Pool"
    tree.find(".//Background4").text = "Num4Fog"
    tree.find(".//Background5").text = "Num5Roof"
if Sunmeta == 'y':
    tree.find(".//Sunmeta").text = str("True")
else:
    tree.find(".//Sunmeta").text = str("False")

if DontChangeSeedpacketIconOrder == 'y':
    tree.find(".//DontChangeSeedpacketIconOrder").text = str("True")
else:
    tree.find(".//DontChangeSeedpacketIconOrder").text = str("False")
if RandomizeStorePlants == "y":
    random.shuffle(StorePlants)
    tree.find(".//StorePlantSlot1").text = StorePlants[0]
    tree.find(".//StorePlantSlot2").text = StorePlants[1]
    tree.find(".//StorePlantSlot3").text = StorePlants[2]
    tree.find(".//StorePlantSlot4").text = StorePlants[3]
    tree.find(".//StorePlantSlot5").text = StorePlants[4]
    tree.find(".//StorePlantSlot6").text = StorePlants[5]
    tree.find(".//StorePlantSlot7").text = StorePlants[6]
    tree.find(".//StorePlantSlot8").text = StorePlants[7]
else:
    tree.find(".//StorePlantSlot1").text = "STORE_ITEM_PLANT_GATLINGPEA"
    tree.find(".//StorePlantSlot2").text = "STORE_ITEM_PLANT_TWINSUNFLOWER"
    tree.find(".//StorePlantSlot3").text = "STORE_ITEM_PLANT_SPIKEROCK"
    tree.find(".//StorePlantSlot4").text = "STORE_ITEM_PLANT_GLOOMSHROOM"
    tree.find(".//StorePlantSlot5").text = "STORE_ITEM_PLANT_CATTAIL"
    tree.find(".//StorePlantSlot6").text = "STORE_ITEM_PLANT_GOLD_MAGNET"
    tree.find(".//StorePlantSlot7").text = "STORE_ITEM_PLANT_COBCANNON"
    tree.find(".//StorePlantSlot8").text = "STORE_ITEM_PLANT_WINTERMELON"

tree.find(".//Seedname").text = SeedNum

tree.write(datafile)
