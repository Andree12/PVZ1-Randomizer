import random
from xml.etree import ElementTree as et
datafile = "RandomizerSettings.xml";
tree = et.parse(datafile)
try:
    ConveryorRandomize
    ConveryorRandomizeAll
except NameError:
    ConveryorRandomize = None
    ConveryorRandomizeAll = None
while ConveryorRandomize != 'n' and ConveryorRandomize != 'y':
    print("randomize Plants in Conveyorbelt levels? (y/n)>")
    ConveryorRandomize = input()
random.seed(SeedNum)
World3 = tree.find(".//Background3").text
if ConveryorRandomize == 'y':
    while ConveryorRandomizeAll != 'n' and ConveryorRandomizeAll != 'y':
        print("Include every plant in every Conveyorbelt levels? (y/n)>")
        ConveryorRandomizeAll = input()
    if ConveryorRandomizeAll == 'n':
        DayPlantsList = ["Peashooter",
                "Cherrybomb",
                "Wallnut",
                "Potatomine",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Squash",
                "Threepeater",
                "Jalapeno",
                "Spikeweed",
                "Tallnut",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Pumpkinshell",
                "Cabbagepult",
                "Kernelpult",
                "Garlic",
                "Melonpult"]

        NightPlantsList = ["Peashooter",
                "Cherrybomb",
                "Wallnut",
                "Potatomine",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Puffshroom",
                "Fumeshroom",
                "Hypnoshroom",
                "Scaredyshroom",
                "Iceshroom",
                "Doomshroom",
                "Squash",
                "Threepeater",
                "Jalapeno",
                "Spikeweed",
                "Tallnut",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Pumpkinshell",
                "Magnetshroom",
                "Cabbagepult",
                "Kernelpult",
                "Garlic",
                "Melonpult"]
        if World3 == 'Num15CustomFlood':
                        PoolPlantsList = ["Peashooter",
                        "Cherrybomb",
                        "Wallnut",
                        "Snowpea",
                        "Chomper",
                        "Repeater",
                        "Squash",
                        "Threepeater",
                        "Jalapeno",
                        "Tallnut",
                        "Cactus",
                        "Splitpea",
                        "Starfruit",
                        "Pumpkinshell",
                        "Cabbagepult",
                        "Kernelpult",
                        "Garlic",
                        "Melonpult",
                        "Tanglekelp"]
        else:
                        PoolPlantsList = ["Peashooter",
                        "Cherrybomb",
                        "Wallnut",
                        "Potatomine",
                        "Snowpea",
                        "Chomper",
                        "Repeater",
                        "Squash",
                        "Threepeater",
                        "Jalapeno",
                        "Spikeweed",
                        "Tallnut",
                        "Cactus",
                        "Splitpea",
                        "Starfruit",
                        "Pumpkinshell",
                        "Cabbagepult",
                        "Kernelpult",
                        "Garlic",
                        "Melonpult",
                        "Tanglekelp"]
        FogPlantsList = ["Peashooter",
                "Cherrybomb",
                "Wallnut",
                "Potatomine",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Puffshroom",
                "Fumeshroom",
                "Hypnoshroom",
                "Scaredyshroom",
                "Iceshroom",
                "Doomshroom",
                "Squash",
                "Threepeater",
                "Jalapeno",
                "Spikeweed",
                "Tallnut",
                "Seashroom",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Pumpkinshell",
                "Magnetshroom",
                "Cabbagepult",
                "Kernelpult",
                "Garlic",
                "Melonpult",
                "Tanglekelp"]

        DayAttackingPlantsList = ["Peashooter",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Threepeater",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Cabbagepult",
                "Kernelpult",
                "Melonpult"]

        NightAttackingPlantsList = [
                "Puffshroom",
                "Fumeshroom",
                "Scaredyshroom",
                "Peashooter",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Threepeater",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Cabbagepult",
                "Kernelpult",
                "Melonpult"]

        Roof5DefendingPlantsList = [
                "Wallnut",
                "Tallnut",
                "Pumpkinshell"]

        Roof5AttackingPlantsList = ["Peashooter",
                "Snowpea",
                "Chomper",
                "Repeater",
                "Threepeater",
                "Cactus",
                "Splitpea",
                "Starfruit",
                "Cabbagepult",
                "Kernelpult",
                "Melonpult"]

        Roof10AttackingPlantsList = [
                "Fumeshroom",
                "Cabbagepult",
                "Kernelpult",
                "Melonpult"]

        #1-10
        Day10PlantsList = []
        Day10PlantsList.extend(DayPlantsList)

        Day10Seed1 = random.choice(DayAttackingPlantsList)
        Day10PlantsList.remove(Day10Seed1)

        Day10Seed2 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed2)

        Day10Seed3 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed3)

        Day10Seed4 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed4)

        Day10Seed5 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed5)

        Day10Seed6 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed6)

        Day10Seed7 = random.choice(Day10PlantsList)
        Day10PlantsList.remove(Day10Seed7)

        tree.find(".//DayFinallevelSeed1").text = str(Day10Seed1)
        tree.find(".//DayFinallevelSeed2").text = str(Day10Seed2)
        tree.find(".//DayFinallevelSeed3").text = str(Day10Seed3)
        tree.find(".//DayFinallevelSeed4").text = str(Day10Seed4)
        tree.find(".//DayFinallevelSeed5").text = str(Day10Seed5)
        tree.find(".//DayFinallevelSeed6").text = str(Day10Seed6)
        tree.find(".//DayFinallevelSeed7").text = str(Day10Seed7)

        #2-10
        Night10PlantsList = []
        Night10PlantsList.extend(NightPlantsList)

        Night10Seed1 = random.choice(NightAttackingPlantsList)
        Night10PlantsList.remove(Night10Seed1)

        Night10Seed2 = random.choice(Night10PlantsList)
        Night10PlantsList.remove(Night10Seed2)

        Night10Seed3 = random.choice(Night10PlantsList)
        Night10PlantsList.remove(Night10Seed3)

        Night10Seed4 = random.choice(Night10PlantsList)
        Night10PlantsList.remove(Night10Seed4)

        Night10Seed5 = random.choice(Night10PlantsList)
        Night10PlantsList.remove(Night10Seed5)

        Night10Seed6 = random.choice(Night10PlantsList)
        Night10PlantsList.remove(Night10Seed6)

        tree.find(".//NightFinallevelSeed1").text = str(Night10Seed1)
        tree.find(".//NightFinallevelSeed2").text = str(Night10Seed2)
        tree.find(".//NightFinallevelSeed3").text = str(Night10Seed3)
        tree.find(".//NightFinallevelSeed4").text = str(Night10Seed4)
        tree.find(".//NightFinallevelSeed5").text = str(Night10Seed5)
        tree.find(".//NightFinallevelSeed6").text = str(Night10Seed6)

        #3-5


        Pool5PlantsList = []
        Pool5PlantsList.extend(PoolPlantsList)

        Pool5Seed1 = random.choice(DayAttackingPlantsList)
        Pool5PlantsList.remove(Pool5Seed1)

        Pool5Seed2 = random.choice(Pool5PlantsList)
        Pool5PlantsList.remove(Pool5Seed2)

        Pool5Seed3 = random.choice(Pool5PlantsList)
        Pool5PlantsList.remove(Pool5Seed3)

        tree.find(".//PoolMinigamelevelSeed1").text = str(Pool5Seed1)
        tree.find(".//PoolMinigamelevelSeed2").text = str(Pool5Seed2)
        tree.find(".//PoolMinigamelevelSeed3").text = str(Pool5Seed3)


        print();
        #3-10

        Pool10PlantsList = []

        Pool10PlantsList.extend(PoolPlantsList)

        Pool10Seed1 = random.choice(DayAttackingPlantsList)
        Pool10PlantsList.remove(Pool10Seed1)

        Pool10Seed2 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed2)

        Pool10Seed3 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed3)

        Pool10Seed4 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed4)

        Pool10Seed5 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed5)

        Pool10Seed6 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed6)

        Pool10Seed7 = random.choice(Pool10PlantsList)
        Pool10PlantsList.remove(Pool10Seed7)

        tree.find(".//PoolFinallevelSeed1").text = str(Pool10Seed1)
        tree.find(".//PoolFinallevelSeed2").text = str(Pool10Seed2)
        tree.find(".//PoolFinallevelSeed3").text = str(Pool10Seed3)
        tree.find(".//PoolFinallevelSeed4").text = str(Pool10Seed4)
        tree.find(".//PoolFinallevelSeed5").text = str(Pool10Seed5)
        tree.find(".//PoolFinallevelSeed6").text = str(Pool10Seed6)
        tree.find(".//PoolFinallevelSeed7").text = str(Pool10Seed7)

        #4-10
        Fog10PlantsList = []
        Fog10PlantsList.extend(FogPlantsList)

        Fog10Seed1 = random.choice(NightAttackingPlantsList)
        Fog10PlantsList.remove(Fog10Seed1)

        Fog10Seed2 = random.choice(Fog10PlantsList)
        Fog10PlantsList.remove(Fog10Seed2)

        Fog10Seed4 = random.choice(Fog10PlantsList)
        Fog10PlantsList.remove(Fog10Seed4)

        Fog10Seed5 = random.choice(Fog10PlantsList)
        Fog10PlantsList.remove(Fog10Seed5)

        Fog10Seed6 = random.choice(Fog10PlantsList)
        Fog10PlantsList.remove(Fog10Seed6)

        Fog10Seed7 = random.choice(Fog10PlantsList)
        Fog10PlantsList.remove(Fog10Seed7)

        tree.find(".//FogFinallevelSeed1").text = str(Fog10Seed1)
        tree.find(".//FogFinallevelSeed2").text = str(Fog10Seed2)
        tree.find(".//FogFinallevelSeed4").text = str(Fog10Seed4)
        tree.find(".//FogFinallevelSeed5").text = str(Fog10Seed5)
        tree.find(".//FogFinallevelSeed6").text = str(Fog10Seed6)
        tree.find(".//FogFinallevelSeed7").text = str(Fog10Seed7)

        #5-5
        Roof5PlantsList = []
        Roof5PlantsList.extend(DayPlantsList)

        Roof5Seed1 = random.choice(Roof5AttackingPlantsList)
        Roof5PlantsList.remove(Roof5Seed1)

        Roof5Seed2 = random.choice(Roof5DefendingPlantsList)
        Roof5PlantsList.remove(Roof5Seed2)

        Roof5Seed3 = random.choice(Roof5PlantsList)
        Roof5PlantsList.remove(Roof5Seed3)

        tree.find(".//RoofMinigamelevelSeed1").text = str(Roof5Seed1)
        tree.find(".//RoofMinigamelevelSeed2").text = str(Roof5Seed2)
        tree.find(".//RoofMinigamelevelSeed3").text = str(Roof5Seed3)

        #5-10
        Roof10PlantsList = []
        Roof10PlantsList.extend(NightPlantsList)

        Roof10Seed1 = random.choice(Roof10AttackingPlantsList)
        Roof10PlantsList.remove(Roof10Seed1)

        Roof10Seed2 = random.choice(Roof10PlantsList)
        Roof10PlantsList.remove(Roof10Seed2)

        Roof10Seed3 = random.choice(Roof10PlantsList)
        Roof10PlantsList.remove(Roof10Seed3)

        tree.find(".//RoofFinallevelSeed1").text = str(Roof10Seed1)
        tree.find(".//RoofFinallevelSeed2").text = str(Roof10Seed2)
        tree.find(".//RoofFinallevelSeed3").text = str(Roof10Seed3)

        tree.find(".//CompletelyRandomizedSeedPacketsInConveyorBeltLevels").text = str("False")
    else:
        tree.find(".//CompletelyRandomizedSeedPacketsInConveyorBeltLevels").text = str("True")

else:
    tree.find(".//DayFinallevelSeed1").text = "Peashooter"
    tree.find(".//DayFinallevelSeed2").text = "Cherrybomb"
    tree.find(".//DayFinallevelSeed3").text = "Wallnut"
    tree.find(".//DayFinallevelSeed4").text = "Potatomine"
    tree.find(".//DayFinallevelSeed5").text = "Snowpea"
    tree.find(".//DayFinallevelSeed6").text = "Chomper"
    tree.find(".//DayFinallevelSeed7").text = "Repeater"

    tree.find(".//NightFinallevelSeed1").text = "Puffshroom"
    tree.find(".//NightFinallevelSeed2").text = "Fumeshroom"
    tree.find(".//NightFinallevelSeed3").text = "Hypnoshroom"
    tree.find(".//NightFinallevelSeed4").text = "Scaredyshroom"
    tree.find(".//NightFinallevelSeed5").text = "Iceshroom"
    tree.find(".//NightFinallevelSeed6").text = "Doomshroom"

    tree.find(".//PoolMinigamelevelSeed1").text = "Peashooter"
    tree.find(".//PoolMinigamelevelSeed2").text = "Cherrybomb"
    tree.find(".//PoolMinigamelevelSeed3").text = "Wallnut"

    tree.find(".//PoolFinallevelSeed1").text = "Squash"
    tree.find(".//PoolFinallevelSeed2").text = "Threepeater"
    tree.find(".//PoolFinallevelSeed3").text = "Tanglekelp"
    tree.find(".//PoolFinallevelSeed4").text = "Jalapeno"
    tree.find(".//PoolFinallevelSeed5").text = "Spikeweed"
    tree.find(".//PoolFinallevelSeed6").text = "Torchwood"
    tree.find(".//PoolFinallevelSeed7").text = "Tallnut"
        
    tree.find(".//FogFinallevelSeed1").text = "Seashroom"
    tree.find(".//FogFinallevelSeed2").text = "Cactus"
    tree.find(".//FogFinallevelSeed4").text = "Splitpea"
    tree.find(".//FogFinallevelSeed5").text = "Starfruit"
    tree.find(".//FogFinallevelSeed6").text = "Pumpkinshell"
    tree.find(".//FogFinallevelSeed7").text = "Magnetshroom"
    
    tree.find(".//RoofMinigamelevelSeed1").text = "Chomper"
    tree.find(".//RoofMinigamelevelSeed2").text = "Pumpkinshell"
    tree.find(".//RoofMinigamelevelSeed3").text = "Cherrybomb"
    
    tree.find(".//RoofFinallevelSeed1").text = "Cabbagepult"
    tree.find(".//RoofFinallevelSeed2").text = "Kernelpult"
    tree.find(".//RoofFinallevelSeed3").text = "Melonpult"

    tree.find(".//CompletelyRandomizedSeedPacketsInConveyorBeltLevels").text = str("False")

print("Done")
tree.write(datafile)
