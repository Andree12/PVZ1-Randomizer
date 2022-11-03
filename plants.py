import random
from xml.etree import ElementTree as et
datafile = "RandomizerSettings.xml";
tree = et.parse(datafile)

try:
    Randomize
except NameError:
    Randomize = None

while Randomize != 'n' and Randomize != 'y':
    print("Do you want to randomize the plants? (y/n)>")
    Randomize = input()

if Randomize == 'y':
    World1 = tree.find(".//Background1").text
    World2 = tree.find(".//Background2").text
    World3 = tree.find(".//Background3").text
    World4 = tree.find(".//Background4").text
    World5 = tree.find(".//Background5").text
    try:
        SeedNum
    except NameError:
        SeedNum = input("Seed num >")
    random.seed(SeedNum)
    randomizedplantlist = [
        "Peashooter",
            "Sunflower",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "Lilypad",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            ""]

    DayWorldplantidlist = [2, 3, 4, 5, 6, 7]
    NightWorldplantidlist = [8, 9, 10, 11, 12, 13, 14, 15]
    PoolWorldplantidlist = [17, 18, 19, 20, 21, 22, 23]
    FogWorldplantidlist = [24, 25, 26, 27, 28, 29, 30, 31]
    RoofWorldplantidlist = [32, 33, 34, 35, 36, 37, 38, 39]

    plantlist = [
            "Cherrybomb",
            "Wallnut",
            "Potatomine",
            "Snowpea",
            "Chomper",
            "Repeater",
            "Puffshroom",
            "Sunshroom",
            "Fumeshroom",
            "Hypnoshroom",
            "Scaredyshroom",
            "Iceshroom",
            "Doomshroom",
            "Squash",
            "Threepeater",
            "Jalapeno",
            "Torchwood",
            "Tallnut",
            "Plantern",
            "Cactus",
            "Blover",
            "Splitpea",
            "Starfruit",
            "Pumpkinshell",
            "Magnetshroom",
            "Cabbagepult",
            "Kernelpult",
            "Garlic",
            "Umbrella",
            "Marigold",
            "Melonpult"]



    #Gravebuster
    GravebusteridNumList = NightWorldplantidlist
    GravebusteridNum = random.choice(GravebusteridNumList)

    if GravebusteridNum in NightWorldplantidlist:
        NightWorldplantidlist.remove(GravebusteridNum)
    randomizedplantlist[GravebusteridNum] = "Gravebuster"

    #Tangle Kelp
    PoolPlantidRandomNumList = PoolWorldplantidlist + FogWorldplantidlist

    TanglekelpidNum = random.choice(PoolPlantidRandomNumList)
    PoolPlantidRandomNumList.remove(TanglekelpidNum)

    if TanglekelpidNum in PoolWorldplantidlist:
        PoolWorldplantidlist.remove(TanglekelpidNum)
    elif TanglekelpidNum in FogWorldplantidlist:
        FogWorldplantidlist.remove(TanglekelpidNum)
    randomizedplantlist[TanglekelpidNum] = "Tanglekelp"


    #Spikeweed
    SpikeweedidNumList = DayWorldplantidlist + NightWorldplantidlist + PoolWorldplantidlist + FogWorldplantidlist

    SpikeweedidNum = random.choice(SpikeweedidNumList)
    if SpikeweedidNum in DayWorldplantidlist:
     DayWorldplantidlist.remove(SpikeweedidNum)
    elif SpikeweedidNum in NightWorldplantidlist:
     NightWorldplantidlist.remove(SpikeweedidNum)
    elif SpikeweedidNum in PoolWorldplantidlist:
     PoolWorldplantidlist.remove(SpikeweedidNum)
    elif SpikeweedidNum in FogWorldplantidlist:
     FogWorldplantidlist.remove(SpikeweedidNum)
    randomizedplantlist[SpikeweedidNum] = "Spikeweed"


    #Seashroom
    SeashroomidNumList = FogWorldplantidlist
    Seashroomidnum = random.choice(SeashroomidNumList)

    if Seashroomidnum in FogWorldplantidlist:
        FogWorldplantidlist.remove(Seashroomidnum)
    randomizedplantlist[Seashroomidnum] = "Seashroom"

    #Flowerpot
    
    if World2 == "Num9JTTW2" or World1 == "Num7GreatWall":
        FlowerpotidNumList = DayWorldplantidlist
    else:
        FlowerpotidNumList = DayWorldplantidlist + NightWorldplantidlist + PoolWorldplantidlist + FogWorldplantidlist + RoofWorldplantidlist
        rooflevelnum = 32
        while rooflevelnum != 39:
         if  rooflevelnum in RoofWorldplantidlist:
          FlowerpotidNumList.remove(rooflevelnum)
         rooflevelnum = rooflevelnum + 1

    Flowerpotidnum = random.choice(FlowerpotidNumList)

    if Flowerpotidnum in DayWorldplantidlist:
     DayWorldplantidlist.remove(Flowerpotidnum)
    elif Flowerpotidnum in NightWorldplantidlist:
     NightWorldplantidlist.remove(Flowerpotidnum)
    elif Flowerpotidnum in PoolWorldplantidlist:
     PoolWorldplantidlist.remove(Flowerpotidnum)
    elif Flowerpotidnum in FogWorldplantidlist:
     FogWorldplantidlist.remove(Flowerpotidnum)
    elif Flowerpotidnum in RoofWorldplantidlist:
     RoofWorldplantidlist.remove(Flowerpotidnum)
    randomizedplantlist[Flowerpotidnum] = "Flowerpot"

    #Coffee Bean
    nocturnalPlantlist = ["Puffshroom", "Sunshroom", "Fumeshroom", "Hypnoshroom", "Scaredyshroom", "Iceshroom", "Doomshroom", "Magnetshroom"]
    NocturnalPlantidNumList = DayWorldplantidlist + NightWorldplantidlist + PoolWorldplantidlist + FogWorldplantidlist + RoofWorldplantidlist

    try:
        PuffinNight1
    except NameError:
        PuffinNight1 = None

    while PuffinNight1 != 'n' and PuffinNight1 != 'y':
        print("Do you want to have Puff-shroom to be obtained in 1-10? (y/n)>")
        PuffinNight1 = input()

    if PuffinNight1 == 'y':
        NocturnalPlantidNum = 8
        NocturnalPlantidName = "Puffshroom"
        CoffeeBeanidNumList = PoolWorldplantidlist + RoofWorldplantidlist
        CoffeebeanidNum = random.choice(CoffeeBeanidNumList)
    else:
        CoffeeBeanidNumList = DayWorldplantidlist + PoolWorldplantidlist + RoofWorldplantidlist
        CoffeebeanidNum = random.choice(CoffeeBeanidNumList)
        NocturnalPlantidName = random.choice(nocturnalPlantlist)
        if CoffeebeanidNum <= 3:
            CoffeebeanidNum = 4
            NocturnalPlantidNum = 3
        else:
            NocturnalPlantidNum = random.randrange(3, (CoffeebeanidNum - 1))

    plantlist.remove(NocturnalPlantidName)
    randomizedplantlist[NocturnalPlantidNum] = NocturnalPlantidName

    if NocturnalPlantidNum in DayWorldplantidlist:
     DayWorldplantidlist.remove(NocturnalPlantidNum)
    elif NocturnalPlantidNum in NightWorldplantidlist:
     NightWorldplantidlist.remove(NocturnalPlantidNum)
    elif NocturnalPlantidNum in PoolWorldplantidlist:
     PoolWorldplantidlist.remove(NocturnalPlantidNum)
    elif NocturnalPlantidNum in FogWorldplantidlist:
     FogWorldplantidlist.remove(NocturnalPlantidNum)
    elif NocturnalPlantidNum in RoofWorldplantidlist:
     RoofWorldplantidlist.remove(NocturnalPlantidNum)

    if CoffeebeanidNum in DayWorldplantidlist:
     DayWorldplantidlist.remove(CoffeebeanidNum)
    elif CoffeebeanidNum in PoolWorldplantidlist:
     PoolWorldplantidlist.remove(CoffeebeanidNum)
    elif CoffeebeanidNum in RoofWorldplantidlist:
     RoofWorldplantidlist.remove(CoffeebeanidNum)

    randomizedplantlist[CoffeebeanidNum] = "InstantCoffee"


    #randomizeer start
    plantidNumList = DayWorldplantidlist + NightWorldplantidlist + PoolWorldplantidlist + FogWorldplantidlist + RoofWorldplantidlist


    while len(plantlist) != 0:
     Plantidnum = random.choice(plantidNumList)
     if Plantidnum in plantidNumList:
      plantidNumList.remove(Plantidnum)
     plantname = random.choice(plantlist)
     randomizedplantlist[Plantidnum] = plantname 
     plantlist.remove(plantname)
    plantname = None
    plantnum = 0
    print("Shuffling plants")
    i = 0
    while i < len(randomizedplantlist):
        if "Cherrybomb" == randomizedplantlist[i]:
            tree.find(".//Cherrybomb").text = str(i)
        if "Wallnut" == randomizedplantlist[i]:
            tree.find(".//Wallnut").text = str(i)
        if "Potatomine" == randomizedplantlist[i]:
            tree.find(".//Potatomine").text = str(i)
        if "Snowpea" == randomizedplantlist[i]:
            tree.find(".//Snowpea").text = str(i)
        if "Chomper" == randomizedplantlist[i]:
            tree.find(".//Chomper").text = str(i)
        if "Repeater" == randomizedplantlist[i]:
            tree.find(".//Repeater").text = str(i)
            
        if "Puffshroom" == randomizedplantlist[i]:
            tree.find(".//Puffshroom").text = str(i)
        if "Sunshroom" == randomizedplantlist[i]:
            tree.find(".//Sunshroom").text = str(i)
        if "Fumeshroom" == randomizedplantlist[i]:
            tree.find(".//Fumeshroom").text = str(i)
        if "Gravebuster" == randomizedplantlist[i]:
            tree.find(".//Gravebuster").text = str(i)
        if "Hypnoshroom" == randomizedplantlist[i]:
            tree.find(".//Hypnoshroom").text = str(i)
        if "Scaredyshroom" == randomizedplantlist[i]:
            tree.find(".//Scaredyshroom").text = str(i)
        if "Iceshroom" == randomizedplantlist[i]:
            tree.find(".//Iceshroom").text = str(i)
        if "Doomshroom" == randomizedplantlist[i]:
            tree.find(".//Doomshroom").text = str(i)
            
        if "Squash" == randomizedplantlist[i]:
            tree.find(".//Squash").text = str(i)
        if "Threepeater" == randomizedplantlist[i]:
            tree.find(".//Threepeater").text = str(i)
        if "Tanglekelp" == randomizedplantlist[i]:
            tree.find(".//Tanglekelp").text = str(i)
        if "Jalapeno" == randomizedplantlist[i]:
            tree.find(".//Jalapeno").text = str(i)
        if "Spikeweed" == randomizedplantlist[i]:
            tree.find(".//Spikeweed").text = str(i)
        if "Torchwood" == randomizedplantlist[i]:
            tree.find(".//Torchwood").text = str(i)
        if "Tallnut" == randomizedplantlist[i]:
            tree.find(".//Tallnut").text = str(i)

        if "Seashroom" == randomizedplantlist[i]:
            tree.find(".//Seashroom").text = str(i)
        if "Plantern" == randomizedplantlist[i]:
            tree.find(".//Plantern").text = str(i)
        if "Cactus" == randomizedplantlist[i]:
            tree.find(".//Cactus").text = str(i)
        if "Blover" == randomizedplantlist[i]:
            tree.find(".//Blover").text = str(i)
        if "Splitpea" == randomizedplantlist[i]:
            tree.find(".//Splitpea").text = str(i)
        if "Starfruit" == randomizedplantlist[i]:
            tree.find(".//Starfruit").text = str(i)
        if "Pumpkinshell" == randomizedplantlist[i]:
            tree.find(".//Pumpkinshell").text = str(i)
        if "Magnetshroom" == randomizedplantlist[i]:
            tree.find(".//Magnetshroom").text = str(i)

        if "Cabbagepult" == randomizedplantlist[i]:
            tree.find(".//Cabbagepult").text = str(i)
        if "Flowerpot" == randomizedplantlist[i]:
            tree.find(".//Flowerpot").text = str(i)
        if "Kernelpult" == randomizedplantlist[i]:
            tree.find(".//Kernelpult").text = str(i)
        if "InstantCoffee" == randomizedplantlist[i]:
            tree.find(".//InstantCoffee").text = str(i)
        if "Garlic" == randomizedplantlist[i]:
            tree.find(".//Garlic").text = str(i)
        if "Umbrella" == randomizedplantlist[i]:
            tree.find(".//Umbrella").text = str(i)
        if "Marigold" == randomizedplantlist[i]:
            tree.find(".//Marigold").text = str(i)
        if "Melonpult" == randomizedplantlist[i]:
            tree.find(".//Melonpult").text = str(i)
        i+= 1
else:
    tree.find(".//Cherrybomb").text = "2"
    tree.find(".//Wallnut").text = "3"
    tree.find(".//Potatomine").text = "4"
    tree.find(".//Snowpea").text = "5"
    tree.find(".//Chomper").text = "6"
    tree.find(".//Repeater").text = "7"
    tree.find(".//Puffshroom").text = "8"
    tree.find(".//Sunshroom").text = "9"
    tree.find(".//Fumeshroom").text = "10"
    tree.find(".//Gravebuster").text = "11"
    tree.find(".//Hypnoshroom").text = "12"
    tree.find(".//Scaredyshroom").text = "13"
    tree.find(".//Iceshroom").text = "14"
    tree.find(".//Doomshroom").text = "15"
    tree.find(".//Squash").text = "17"
    tree.find(".//Threepeater").text = "18"
    tree.find(".//Tanglekelp").text = "19"
    tree.find(".//Jalapeno").text = "20"
    tree.find(".//Spikeweed").text = "21"
    tree.find(".//Torchwood").text = "22"
    tree.find(".//Tallnut").text = "23"
    tree.find(".//Seashroom").text = "24"
    tree.find(".//Plantern").text = "25"
    tree.find(".//Cactus").text = "26"
    tree.find(".//Blover").text = "27"
    tree.find(".//Splitpea").text = "28"
    tree.find(".//Starfruit").text = "29"
    tree.find(".//Pumpkinshell").text = "30"
    tree.find(".//Magnetshroom").text = "31"
    tree.find(".//Cabbagepult").text = "32"
    tree.find(".//Flowerpot").text = "33"
    tree.find(".//Kernelpult").text = "34"
    tree.find(".//InstantCoffee").text = "35"
    tree.find(".//Garlic").text = "36"
    tree.find(".//Umbrella").text = "37"
    tree.find(".//Marigold").text = "38"
    tree.find(".//Melonpult").text = "39"
    
tree.write(datafile)
print("Plant shuffling complete")



plantlistoriginal = [
        "Peashooter",
        "Sunflower",
        "Cherrybomb",
        "Wallnut",
        "Potatomine",
        "Snowpea",
        "Chomper",
        "Repeater",
        "Puffshroom",
        "Sunshroom",
        "Fumeshroom",
        "Gravebuster",
        "Hypnoshroom",
        "Scaredyshroom",
        "Iceshroom",
        "Doomshroom",
        "Lilypad",
        "Squash",
        "Threepeater",
        "Tanglekelp",
        "Jalapeno",
        "Spikeweed",
        "Torchwood",
        "Tallnut",
        "Seashroom",
        "Plantern",
        "Cactus",
        "Blover",
        "Splitpea",
        "Starfruit",
        "Pumpkinshell",
        "Magnetshroom",
        "Cabbagepult",
        "Flowerpot",
        "Kernelpult",
        "InstantCoffee",
        "Garlic",
        "Umbrella",
        "Marigold",
        "Melonpult",
        "Gatlingpea",
        "Twinsunflower",
        "Gloomshroom",
        "Cattail",
        "Wintermelon",
        "GoldMagnet",
        "Spikerock",
        "Cobcannon",
        "Imitater"]
