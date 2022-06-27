import random

Randomize = None

while Randomize != 'n' and Randomize != 'y':
    print("Do you want to randomize the plants? (y/n)>")
    Randomize = input()

if Randomize == 'y':
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

    PuffinNight1 = None

    while PuffinNight1 != 'n' and PuffinNight1 != 'y':
        print("Do you want to have Puff-shroom to be obtained in 1-10? (y/n)>")
        PuffinNight1 = input()

    if PuffinNight1 == 'y':
        NocturnalPlantidName = "Puffshroom"
        NocturnalPlantidNum = 8
    else:
        NocturnalPlantidName = random.choice(nocturnalPlantlist)
        NocturnalPlantidNum = random.choice(NocturnalPlantidNumList)

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

    CoffeeBeanidNumList = DayWorldplantidlist + PoolWorldplantidlist + RoofWorldplantidlist
    CoffeebeanidMinNum = 0

    while CoffeebeanidMinNum != NocturnalPlantidNum:
     CoffeebeanidMinNum = CoffeebeanidMinNum + 1
     if CoffeebeanidMinNum in CoffeeBeanidNumList:
        CoffeeBeanidNumList.remove(CoffeebeanidMinNum)

     if NocturnalPlantidNum in CoffeeBeanidNumList:
      CoffeeBeanidNumList.remove(NocturnalPlantidNum)

    if len(CoffeeBeanidNumList) != 0:
     CoffeebeanidNum = random.choice(CoffeeBeanidNumList)
    elif NocturnalPlantidNum == 39:
     CoffeebeanidNum = NocturnalPlantidNum - 1
    else:
     CoffeebeanidNum = NocturnalPlantidNum + 1

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
    plantcodenum = 6
    filename = "Lawn_Shared/Lawn/SeedPacket/SeedType.cs"
    print("Shuffling plants")
    while plantnum != 40:
     plantname = randomizedplantlist[plantnum]
     a_file = open(filename, "r")
     list_of_lines = a_file.readlines()
     list_of_lines[plantcodenum] = (plantname + ",\n")

     a_file = open(filename, "w")
     a_file.writelines(list_of_lines)
     a_file.close()
     plantnum = plantnum + 1
     plantcodenum = plantcodenum + 1

    randomizedGameConstantsPlantlist = randomizedplantlist
    for i in range(len(randomizedGameConstantsPlantlist)):
        if randomizedGameConstantsPlantlist[i] == "Peashooter":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Peashooter,    null, ReanimationType.Peashooter,   0,  100,750, PlantSubClass.Shooter, 150, \"PEASHOOTER\"),"
        if randomizedGameConstantsPlantlist[i] == "Sunflower":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Sunflower,     null, ReanimationType.Sunflower,    1,  50, 750, PlantSubClass.Normal,  2500, \"SUNFLOWER\"),"
        if randomizedGameConstantsPlantlist[i] == "Lilypad":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Lilypad,       null, ReanimationType.Lilypad,      19, 25, 750, PlantSubClass.Normal,  0, \"LILY_PAD\"),"
        if randomizedGameConstantsPlantlist[i] == "Cherrybomb":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Cherrybomb,    null, ReanimationType.Cherrybomb,   3,  150,5000,PlantSubClass.Normal,  0, \"CHERRY_BOMB\"),"
        if randomizedGameConstantsPlantlist[i] == "Wallnut":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Wallnut,       null, ReanimationType.Wallnut,      2,  50, 3000,PlantSubClass.Normal,  0, \"WALL_NUT\"),"
        if randomizedGameConstantsPlantlist[i] == "Potatomine":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Potatomine,    null, ReanimationType.Potatomine,   37, 25, 3000,PlantSubClass.Normal,  0, \"POTATO_MINE\"),"
        if randomizedGameConstantsPlantlist[i] == "Snowpea":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Snowpea,       null, ReanimationType.Snowpea,      4,  175,750, PlantSubClass.Shooter, 150, \"SNOW_PEA\"),"
        if randomizedGameConstantsPlantlist[i] == "Chomper":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Chomper,       null, ReanimationType.Chomper,      31, 150,750, PlantSubClass.Normal,  0, \"CHOMPER\"),"
        if randomizedGameConstantsPlantlist[i] == "Repeater":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Repeater,      null, ReanimationType.Repeater,     5,  200,750, PlantSubClass.Shooter, 150, \"REPEATER\"),"
        if randomizedGameConstantsPlantlist[i] == "Puffshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Puffshroom,    null, ReanimationType.Puffshroom,   6,  0,  750, PlantSubClass.Shooter, 150, \"PUFF_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Sunshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Sunshroom,     null, ReanimationType.Sunshroom,    7,  25, 750, PlantSubClass.Normal,  2500, \"SUN_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Fumeshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Fumeshroom,    null, ReanimationType.Fumeshroom,   9,  75, 750, PlantSubClass.Shooter, 150, \"FUME_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Hypnoshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Hypnoshroom,   null, ReanimationType.Hypnoshroom,  10, 75, 3000,PlantSubClass.Normal,  0, \"HYPNO_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Scaredyshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Scaredyshroom, null, ReanimationType.Scrareyshroom,33, 25, 750, PlantSubClass.Shooter, 150, \"SCAREDY_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Iceshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Iceshroom,     null, ReanimationType.Iceshroom,    36, 75, 5000,PlantSubClass.Normal,  0, \"ICE_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Doomshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Doomshroom,    null, ReanimationType.Doomshroom,   20, 125,5000,PlantSubClass.Normal,  0, \"DOOM_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Squash":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Squash,        null, ReanimationType.Squash,       21, 50, 3000,PlantSubClass.Normal,  0, \"SQUASH\"),"
        if randomizedGameConstantsPlantlist[i] == "Threepeater":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Threepeater,   null, ReanimationType.Threepeater,  12, 325,750, PlantSubClass.Shooter, 150, \"THREEPEATER\"),"
        if randomizedGameConstantsPlantlist[i] == "Jalapeno":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Jalapeno,      null, ReanimationType.Jalapeno,     11, 125,5000,PlantSubClass.Normal,  0, \"JALAPENO\"),"
        if randomizedGameConstantsPlantlist[i] == "Torchwood":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Torchwood,     null, ReanimationType.Torchwood,    29, 175,750, PlantSubClass.Normal,  0, \"TORCHWOOD\"),"
        if randomizedGameConstantsPlantlist[i] == "Tallnut":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Tallnut,       null, ReanimationType.Tallnut,      28, 125,3000,PlantSubClass.Normal,  0, \"TALL_NUT\"),"
        if randomizedGameConstantsPlantlist[i] == "Plantern":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Plantern,      null, ReanimationType.Plantern,     38, 25, 3000,PlantSubClass.Normal,  2500, \"PLANTERN\"),"
        if randomizedGameConstantsPlantlist[i] == "Cactus":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Cactus,        null, ReanimationType.Cactus,       15, 125,750, PlantSubClass.Shooter, 150, \"CACTUS\"),"
        if randomizedGameConstantsPlantlist[i] == "Blover":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Blover,        null, ReanimationType.Blover,       18, 100,750, PlantSubClass.Normal,  0, \"BLOVER\"),"
        if randomizedGameConstantsPlantlist[i] == "Splitpea":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Splitpea,      null, ReanimationType.Splitpea,     32, 125,750, PlantSubClass.Shooter, 150, \"SPLIT_PEA\"),"
        if randomizedGameConstantsPlantlist[i] == "Starfruit":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Starfruit,     null, ReanimationType.Starfruit,    30, 125,750, PlantSubClass.Shooter, 150, \"STARFRUIT\"),"
        if randomizedGameConstantsPlantlist[i] == "Pumpkinshell":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Pumpkinshell,  null, ReanimationType.Pumpkin,      25, 125,3000,PlantSubClass.Normal,  0, \"PUMPKIN\"),"
        if randomizedGameConstantsPlantlist[i] == "Magnetshroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Magnetshroom,  null, ReanimationType.Magnetshroom, 35, 100,750, PlantSubClass.Normal,  0, \"MAGNET_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Cabbagepult":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Cabbagepult,   null, ReanimationType.Cabbagepult,  13, 100,750, PlantSubClass.Shooter, 300, \"CABBAGE_PULT\"),"
        if randomizedGameConstantsPlantlist[i] == "Kernelpult":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Kernelpult,    null, ReanimationType.Kernelpult,   13, 100,750, PlantSubClass.Shooter, 300, \"KERNEL_PULT\"),"
        if randomizedGameConstantsPlantlist[i] == "Garlic":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Garlic,        null, ReanimationType.Garlic,       8,  50, 750, PlantSubClass.Normal,  0, \"GARLIC\"),"
        if randomizedGameConstantsPlantlist[i] == "Umbrella":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Umbrella,      null, ReanimationType.Umbrellaleaf, 23, 100,750, PlantSubClass.Normal,  0, \"UMBRELLA_LEAF\"),"
        if randomizedGameConstantsPlantlist[i] == "Marigold":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Marigold,      null, ReanimationType.Marigold,     24, 50, 6000,PlantSubClass.Normal,  2500, \"MARIGOLD\"),"
        if randomizedGameConstantsPlantlist[i] == "Melonpult":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Melonpult,     null, ReanimationType.Melonpult,    14, 300,750, PlantSubClass.Shooter, 300, \"MELON_PULT\"),"
        if randomizedGameConstantsPlantlist[i] == "Gravebuster":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Gravebuster,   null, ReanimationType.GraveBuster,  40, 75, 750, PlantSubClass.Normal,  0, \"GRAVE_BUSTER\"),"
        if randomizedGameConstantsPlantlist[i] == "Tanglekelp":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Tanglekelp,    null, ReanimationType.Tanglekelp,   17, 25, 3000,PlantSubClass.Normal,  0, \"TANGLE_KELP\"),"
        if randomizedGameConstantsPlantlist[i] == "Spikeweed":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Spikeweed,     null, ReanimationType.Spikeweed,    22, 100,750, PlantSubClass.Normal,  0, \"SPIKEWEED\"),"
        if randomizedGameConstantsPlantlist[i] == "Seashroom":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Seashroom,     null, ReanimationType.Seashroom,    39, 0,  3000,PlantSubClass.Shooter, 150, \"SEA_SHROOM\"),"
        if randomizedGameConstantsPlantlist[i] == "Flowerpot":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.Flowerpot,     null, ReanimationType.FlowerPot,    33, 25, 750, PlantSubClass.Normal,  0, \"FLOWER_POT\"),"
        if randomizedGameConstantsPlantlist[i] == "InstantCoffee":
         randomizedGameConstantsPlantlist[i] = "new PlantDefinition(SeedType.InstantCoffee, null, ReanimationType.Coffeebean,   33, 75, 750, PlantSubClass.Normal,  0, \"COFFEE_BEAN\"),"

    plantnum = 0
    plantcodenum = 563
    filename = "Lawn_Shared/Lawn/System/GameConstants.cs"
    while plantnum != 40:
     plantname = randomizedGameConstantsPlantlist[plantnum]
     a_file = open(filename, "r", encoding="utf-8")
     list_of_lines = a_file.readlines()
     list_of_lines[plantcodenum] = (plantname + "\n")

     a_file = open(filename, "w", encoding="utf-8")
     a_file.writelines(list_of_lines)
     a_file.close()
     plantnum = plantnum + 1
     plantcodenum = plantcodenum + 1


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
