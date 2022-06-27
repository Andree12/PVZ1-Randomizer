import random
random.seed(SeedNum)
Randomize = ""
Wintermelondowngradeplant = "Melonpult"
Gatlingpeadowngradeplant = "Repeater"
Spikerockdowngradeplant = "Spikeweed"
Twinsunflowerdowngradeplant = "Sunflower"
Goldmagnetdowngradeplant = "Magnetshroom"
Gloomshroomdowngradeplant = "Fumeshroom"
Cobcannondowngradeplant = "Kernelpult"
CobcannonSuncost = 500
WintermelonSuncost = 200
GatlingpeaSuncost = 250
SpikerockSuncost = 125
TwinsunflowerSuncost = 150
GoldmagnetSuncost = 50
GloomshroomSuncost = 150


while Randomize != 'n' and Randomize != 'y':
    print("randomize Plant upgrades? (y/n)>")
    Randomize = input()


if Randomize == 'y':
    CobcannonSuncost = 700
    WintermelonSuncost = 500
    GatlingpeaSuncost = 450
    SpikerockSuncost = 225
    TwinsunflowerSuncost = 200
    GoldmagnetSuncost = 150
    GloomshroomSuncost = 225
    selecteddowngradeplant = ""

    sun25costplantlist = ["Sunshroom", "Scaredyshroom"]
    sun50costplantlist = ["Sunflower", "Garlic"]
    sun100costplantlist = ["Peashooter", "Spikeweed", "Magnetshroom", "Cabbagepult", "Kernelpult", "Umbrella"]
    sun125costplantlist = ["Cactus", "Splitpea", "Starfruit"]
    sun175costplantlist = ["Snowpea", "Torchwood"]
    othersuncostplantlist = ["Fumeshroom", "Chomper", "Repeater", "Melonpult", "Threepeater"]
    downgradeplantlist = othersuncostplantlist + sun25costplantlist + sun50costplantlist + sun100costplantlist + sun125costplantlist + sun175costplantlist

    othersuncostplantlist = ["Fumeshroom", "Chomper"]
    twinsunflowerdowngradeplantlist = othersuncostplantlist + sun25costplantlist + sun50costplantlist + sun100costplantlist + sun125costplantlist + sun175costplantlist

    othersuncostplantlist = ["Fumeshroom", "Chomper", "Repeater"]
    spikerockdowngradeplantlist = othersuncostplantlist + sun25costplantlist + sun50costplantlist + sun100costplantlist + sun125costplantlist + sun175costplantlist

    othersuncostplantlist = ["Fumeshroom"]
    goldmagnetdowngradeplantlist = othersuncostplantlist + sun25costplantlist + sun50costplantlist + sun100costplantlist + sun125costplantlist


    #Cobcannon
    selecteddowngradeplant = random.choice(downgradeplantlist)
    if selecteddowngradeplant in sun25costplantlist:
     CobcannonSuncost = CobcannonSuncost - 50
    if selecteddowngradeplant in sun50costplantlist:
     CobcannonSuncost = CobcannonSuncost - 100
    if selecteddowngradeplant == "Fumeshroom":
     CobcannonSuncost = CobcannonSuncost - 150
    if selecteddowngradeplant in sun100costplantlist:
     CobcannonSuncost = CobcannonSuncost - 200
    if selecteddowngradeplant in sun125costplantlist:
     CobcannonSuncost = CobcannonSuncost - 250
    if selecteddowngradeplant == "Chomper":
     CobcannonSuncost = CobcannonSuncost - 300
    if selecteddowngradeplant in sun175costplantlist:
     CobcannonSuncost = CobcannonSuncost - 350
    if selecteddowngradeplant == "Repeater":
     CobcannonSuncost = CobcannonSuncost - 400
    if selecteddowngradeplant == "Melonpult":
     CobcannonSuncost = CobcannonSuncost - 600
    if selecteddowngradeplant == "Threepeater":
     CobcannonSuncost = CobcannonSuncost - 650

    Cobcannondowngradeplant = selecteddowngradeplant


    #
    UpgradeplantNum = 0
    UpgradeplantSuncost = 0
    while UpgradeplantNum != 6:
        if UpgradeplantNum <= 1:
         selecteddowngradeplant = random.choice(downgradeplantlist)
        elif UpgradeplantNum == 2:
         selecteddowngradeplant = random.choice(spikerockdowngradeplantlist)
        elif UpgradeplantNum == 3:
         selecteddowngradeplant = random.choice(twinsunflowerdowngradeplantlist)
        elif UpgradeplantNum == 4:
         selecteddowngradeplant = random.choice(goldmagnetdowngradeplantlist)
        elif UpgradeplantNum == 5:
         selecteddowngradeplant = random.choice(spikerockdowngradeplantlist)

        if selecteddowngradeplant in sun25costplantlist:
         UpgradeplantSuncost = 25
        if selecteddowngradeplant in sun50costplantlist:
         UpgradeplantSuncost = 50
        if selecteddowngradeplant == "Fumeshroom":
         UpgradeplantSuncost = 75
        if selecteddowngradeplant in sun100costplantlist:
         UpgradeplantSuncost = 100
        if selecteddowngradeplant in sun125costplantlist:
         UpgradeplantSuncost = 125
        if selecteddowngradeplant == "Chomper":
         UpgradeplantSuncost = 150
        if selecteddowngradeplant in sun175costplantlist:
         UpgradeplantSuncost = 175
        if selecteddowngradeplant == "Repeater":
         UpgradeplantSuncost = 200
        if selecteddowngradeplant == "Melonpult":
         UpgradeplantSuncost = 300
        if selecteddowngradeplant == "Threepeater":
         UpgradeplantSuncost = 325

        if UpgradeplantNum == 0:
         WintermelonSuncost = WintermelonSuncost - UpgradeplantSuncost
         Wintermelondowngradeplant = selecteddowngradeplant
        elif UpgradeplantNum == 1:
         GatlingpeaSuncost = GatlingpeaSuncost - UpgradeplantSuncost
         Gatlingpeadowngradeplant = selecteddowngradeplant
        elif UpgradeplantNum == 2:
         SpikerockSuncost = SpikerockSuncost - UpgradeplantSuncost
         Spikerockdowngradeplant = selecteddowngradeplant
        elif UpgradeplantNum == 3:
         TwinsunflowerSuncost = TwinsunflowerSuncost - UpgradeplantSuncost
         Twinsunflowerdowngradeplant = selecteddowngradeplant
        elif UpgradeplantNum == 4:
         GoldmagnetSuncost = GoldmagnetSuncost - UpgradeplantSuncost
         Goldmagnetdowngradeplant = selecteddowngradeplant
        elif UpgradeplantNum == 5:
         GloomshroomSuncost = GloomshroomSuncost - UpgradeplantSuncost
         Gloomshroomdowngradeplant = selecteddowngradeplant
        UpgradeplantNum = UpgradeplantNum + 1

##print("Gatlingpea")
##print("Sun Cost: ", GatlingpeaSuncost)
##print("Downgrade Plant: ", Gatlingpeadowngradeplant)
##print("")
##print("")
##print("Twinsunflower")
##print("Sun Cost: ", TwinsunflowerSuncost)
##print("Downgrade Plant: ", Twinsunflowerdowngradeplant)
##print("")
##print("")
##print("Gloomshroom")
##print("Sun Cost: ", GloomshroomSuncost)
##print("Downgrade Plant: ", Gloomshroomdowngradeplant)
##print("")
##print("")
##print("Wintermelon")
##print("Sun Cost: ", WintermelonSuncost)
##print("Downgrade Plant: ", Wintermelondowngradeplant)
##print("")
##print("")
##print("Goldmagnet")
##print("Sun Cost: ", GoldmagnetSuncost)
##print("Downgrade Plant: ", Goldmagnetdowngradeplant)
##print("")
##print("")
##print("Spikerock")
##print("Sun Cost: ", SpikerockSuncost)
##print("Downgrade Plant: ", Spikerockdowngradeplant)
##print("")
##print("")
##print("Cobcannon")
##print("Sun Cost: ", CobcannonSuncost)
##print("Downgrade Plant: ", Cobcannondowngradeplant)

##"GatlingpeaSuncost"
##"TwinSunflowerSuncost"
##"GloomshroomSuncost"
##"WinterMelonSuncost"
##"GoldMagnetSuncost"
##"SpikerockSuncost"
##"CobcannonSuncost"

GatlingpeaSuncost = str(GatlingpeaSuncost)
TwinsunflowerSuncost = str(TwinsunflowerSuncost)
GloomshroomSuncost = str(GloomshroomSuncost)
WintermelonSuncost = str(WintermelonSuncost)
GoldmagnetSuncost = str(GoldmagnetSuncost)
SpikerockSuncost = str(SpikerockSuncost)
CobcannonSuncost = str(CobcannonSuncost)

print("Setting up upgrade plants")

#GameConstants.cs
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost1 = word.replace('GatlingpeaSuncost', GatlingpeaSuncost)
a_file.write(replace_suncost1)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost2 = word.replace('TwinSunflowerSuncost', TwinsunflowerSuncost)
a_file.write(replace_suncost2)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost3 = word.replace('GloomshroomSuncost', GloomshroomSuncost)
a_file.write(replace_suncost3)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost4 = word.replace('WinterMelonSuncost', WintermelonSuncost)
a_file.write(replace_suncost4)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost5 = word.replace('GoldMagnetSuncost', GoldmagnetSuncost)
a_file.write(replace_suncost5)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost6 = word.replace('SpikerockSuncost', SpikerockSuncost)
a_file.write(replace_suncost6)
a_file.close()

a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf8")
word = a_file.read()
a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
replace_suncost7 = word.replace('CobcannonSuncost', CobcannonSuncost)
a_file.write(replace_suncost7)
a_file.close()

#SeedChooserScreen.cs
filenum = 0
while filenum != 2:
    if filenum == 0:
     filename = "Lawn_Shared/Lawn/Widget/SeedChooser/SeedChooserScreen.cs"
    if filenum == 1:
     filename = "Lawn_Shared/Lawn/Plant/Plant.cs"

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name1 = word.replace('GatlingpeaDowngradePlant', Gatlingpeadowngradeplant)
    a_file.write(replace_name1)

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name2 = word.replace('TwinsunflowerDowngradePlant', Twinsunflowerdowngradeplant)
    a_file.write(replace_name2)
    a_file.close()

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name3 = word.replace('GloomshroomDowngradePlant', Gloomshroomdowngradeplant)
    a_file.write(replace_name3)
    a_file.close()

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name4 = word.replace('WintermelonDowngradePlant', Wintermelondowngradeplant)
    a_file.write(replace_name4)
    a_file.close()

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name5 = word.replace('GoldMagnetDowngradePlant', Goldmagnetdowngradeplant)
    a_file.write(replace_name5)
    a_file.close()

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name6 = word.replace('SpikerockDowngradePlant', Spikerockdowngradeplant)
    a_file.write(replace_name6)
    a_file.close()

    a_file = open(filename, "r", encoding="utf-8")
    word = a_file.read()
    a_file = open(filename, "w", encoding="utf-8")
    replace_name7 = word.replace('CobcannonDowngradePlant', Cobcannondowngradeplant)
    a_file.write(replace_name7)
    a_file.close()

    filenum = filenum + 1

print("Done")
