import random
try:
    SeedNum
except NameError:
    SeedNum = input("seed num >")
random.seed(SeedNum)
##Store plants
Gatlingpeadowngradeplant = "Repeater"
Twinsunflowerdowngradeplant = "Sunflower"
Spikerockdowngradeplant = "Spikeweed"
Goldmagnetdowngradeplant = "Magnetshroom"
Gloomshroomdowngradeplant = "Fumeshroom"
Wintermelondowngradeplant = "Melonpult"
Cobcannondowngradeplant = "Kernelpult"
selecteddowngradeplant = ""
#Gatlingpea
GatlingpeaSuncost = 450
GatlingpeaFiringSpeed = 150
#Twinsunflower
TwinsunflowerSuncost = 200
#Spikerock and Gold Magnet
SpikerockSuncost = 225
SpikerockDamage = 20
SpikerockFiringSpeedA = 69
SpikerockFiringSpeedB = 33
GoldmagnetSuncost = 150
#GloomShroom
GloomshroomSuncost = 225
GloomShroomFiringSpeed = 200
GloomShroomDamage = 20
#Cattail
CattailSuncost = 225
CattailFiringSpeed = 150
#Cobcannon
CobcannonSuncost = 700
#Wintermelon
WintermelonSuncost = 500
WintermelonFiringSpeed = 300
Wintermelondamage = 80
##Adventure mode plants
#Cherry Bomb
CherryBombSuncost = 150
CherryBombDamage = 1800
#Wallnut
WallnutSuncost = 50
WallnutHealth = 4000
#PotatoMine
PotatoMineSuncost = 25
PotatoMineSurfacingtime = 1500
PotatoMineDamage = 1800
#Chomper
ChomperSuncost = 150
ChomperChewingTime = 4000
#Snowpea
SnowpeaSuncost = 175
SnowpeaFiringSpeed = 150
SnowpeaDamage = 20
#Repeater
RepeaterSuncost = 200
RepeaterFiringSpeed = 150
#Fumeshroom and Spikeweed
FumeShroomSuncost = 75
SpikeweedSuncost = 100
SpikeweedDamage = 20
FumeShroomDamage = 20
FumeShroomFiringSpeed = 150
SpikeweedFiringSpeed = 76
#Gravebuster
GraveBusterSuncost = 75
GraveBusterEatingtime = 400
#IceShroom
IceShroomSuncost = 75
IceShroomDamage = 20
#ScaredyShroom
ScaredyShroomSuncost = 25
ScaredyShroomFiringSpeed = 150
#Doomshroom
DoomshroomSuncost = 125
DoomshroomDamage = 1800
DoomshroomCratertime = 18000
#Squash
SquashSuncost = 50
SquashDamage = 1800
#Threepeater
ThreepeaterSuncost = 325
ThreepeaterFiringSpeed = 150
#Tallnut
TallnutSuncost = 125
TallnutHealth = 8000
#Cactus
CactusSuncost = 125
CactusFiringSpeed = 150
CactusDamage = 20
#Starfruit
StarfuitSuncost = 125
StarfruitFiringSpeed = 150
StarfruitDamage = 20
#Blover
BloverSuncost = 100
Bloverfogawaytime = 4000
#Pumpkin
PumpkinSuncost = 125
PumpkinHealth = 4000
#Splitpea
SplitpeaSuncost = 125
SplitpeaFiringSpeed = 150
#MagnetShroom
MagnetShroomSuncost = 100
MagnetShroomcooldown = 1500
#Cabbagepult
CabbagepultSuncost = 100
CabbagepultDamage = 40
CabbagepultFiringSpeed = 300
#Kernelpult
KernelpultSuncost = 100
KernelpultFiringSpeed = 300
KernelpultKerneldamage = 20
KernelpultButterdamage = 40
KernelpultButterStuntime = 400
#Garlic
GarlicSuncost = 50
GarlicHealth = 400
#Melonpult
MelonpultSuncost = 300
MelonpultFiringSpeed = 400
Melonpultdamage = 80

try:
    RandomizeActionRate
    RandomizePlantDamage
    RandomizeUpgrades
    RandomizePlantHealth
except NameError:
    RandomizeActionRate = None
    RandomizePlantDamage = None
    RandomizeUpgrades = None
    RandomizePlantHealth = None
    
while RandomizeActionRate != 'n' and RandomizeActionRate != 'y':
    print("Randomize the action rates of the plants? (y/n)>")
    RandomizeActionRate = input()
while RandomizePlantDamage != 'n' and RandomizePlantDamage != 'y':
    print("randomize the attack damage of the plants? (y/n)>")
    RandomizePlantDamage = input()
while RandomizeUpgrades != 'n' and RandomizeUpgrades != 'y':
    print("randomize downgrade plants of upgrade Plants? (y/n)>")
    RandomizeUpgrades = input()
while RandomizePlantHealth != 'n' and RandomizePlantHealth != 'y':
    print("randomize defensive Plant health? (y/n)>")
    RandomizePlantHealth = input()

if RandomizePlantHealth == 'y':
    DefensiveplantHealthList = [2000, 4000, 6000, 8000]
    GarlicHealthList = [200, 400, 600, 800]
    WallnutHealth = random.choice(DefensiveplantHealthList)
    TallnutHealth = random.choice(DefensiveplantHealthList)
    PumpkinHealth = random.choice(DefensiveplantHealthList)
    GarlicHealth = random.choice(GarlicHealthList)

    if WallnutHealth == DefensiveplantHealthList[0]:
        WallnutSuncost -= 25
    elif WallnutHealth == DefensiveplantHealthList[2]:
        WallnutSuncost += 25
    elif WallnutHealth == DefensiveplantHealthList[3]:
        WallnutSuncost += 50

    if TallnutHealth == DefensiveplantHealthList[0]:
        TallnutSuncost -= 75
    elif WallnutHealth == DefensiveplantHealthList[1]:
        TallnutSuncost -= 50
    elif TallnutHealth == DefensiveplantHealthList[2]:
        TallnutSuncost -= 25

    if PumpkinHealth == DefensiveplantHealthList[0]:
        PumpkinSuncost -= 75
    elif PumpkinHealth == DefensiveplantHealthList[1]:
        PumpkinSuncost -= 50
    elif PumpkinHealth == DefensiveplantHealthList[2]:
        PumpkinSuncost -= 25

    if GarlicHealth == GarlicHealthList[0]:
        GarlicSuncost -= 25
    elif GarlicHealth == GarlicHealthList[2]:
        GarlicSuncost += 25
    elif GarlicHealth == GarlicHealthList[3]:
        GarlicSuncost += 50

if RandomizeActionRate == 'y':
# 75 = 200 sun
#100 = 150 sun
#150 = 100 sun
#225 = 75 sun
#300 = 50 sun
    Firingspeedlist = [75, 100, 150, 225, 300]
    FiringspeedlistScaredy = [75, 100, 150]
    GloomshroomFiringspeedlist = [100, 150, 200, 300, 400]
#    SpikeweedFiringSpeedlist = [38, 50, 76, 152, 228]
    PotatoMineSurfacingtimelist =  [375, 750, 1500]
    ChomperChewingTimelist = [2000, 4000, 6000, 8000]
    GraveBusterEatingtimelist = [200, 300, 400, 600, 800]
    DoomshroomCratertimelist = [36000, 27000, 18000, 9000]
    Bloverfogawaytimelist = [2000, 4000, 6000, 8000]
    MagnetShroomcooldownlist = [3000, 1500, 1000, 750]
    KernelpultButterStuntimelist = [200, 400, 600, 800]

    GloomshroomFiringspeed = random.choice(GloomshroomFiringspeedlist)
#    SpikeweedFiringSpeed = random.choice(SpikeweedFiringSpeedlist)
    PotatoMineSurfacingtime =  random.choice(PotatoMineSurfacingtimelist)
    ChomperChewingTime = random.choice(ChomperChewingTimelist)
    GraveBusterEatingtime = random.choice(GraveBusterEatingtimelist)
    DoomshroomCratertime = random.choice(DoomshroomCratertimelist)
    Bloverfogawaytime = random.choice(Bloverfogawaytimelist)
    MagnetShroomcooldown = random.choice(MagnetShroomcooldownlist)
    KernelpultButterStuntime = random.choice(KernelpultButterStuntimelist)
    GatlingpeaFiringSpeed = random.choice(Firingspeedlist)
    CattailFiringSpeed = random.choice(Firingspeedlist)
    SnowpeaFiringSpeed = random.choice(Firingspeedlist)
    RepeaterFiringSpeed = random.choice(Firingspeedlist)
    FumeShroomFiringSpeed = random.choice(Firingspeedlist)
    ScaredyShroomFiringSpeed = random.choice(FiringspeedlistScaredy)
    ThreepeaterFiringSpeed = random.choice(Firingspeedlist)
    CactusFiringSpeed = random.choice(Firingspeedlist)
    StarfruitFiringSpeed = random.choice(Firingspeedlist)
    SplitpeaFiringSpeed = random.choice(Firingspeedlist)
    CabbagepultFiringSpeed = random.choice(Firingspeedlist)
    KernelpultFiringSpeed = random.choice(Firingspeedlist)
    MelonpultFiringSpeed = random.choice(Firingspeedlist)

    if GatlingpeaFiringSpeed == Firingspeedlist[0]:
        GatlingpeaSuncost = GatlingpeaSuncost + 450
    elif GatlingpeaFiringSpeed == Firingspeedlist[1]:
        GatlingpeaSuncost = GatlingpeaSuncost + 225
    elif GatlingpeaFiringSpeed == Firingspeedlist[3]:
        GatlingpeaSuncost = GatlingpeaSuncost - 150
    elif GatlingpeaFiringSpeed == Firingspeedlist[4]:
        GatlingpeaSuncost = GatlingpeaSuncost - 225

    if SnowpeaFiringSpeed == Firingspeedlist[0]:
        SnowpeaSuncost = SnowpeaSuncost + 100
    elif SnowpeaFiringSpeed == Firingspeedlist[1]:
        SnowpeaSuncost = SnowpeaSuncost + 50
    elif SnowpeaFiringSpeed == Firingspeedlist[3]:
        SnowpeaSuncost = SnowpeaSuncost - 25
    elif SnowpeaFiringSpeed == Firingspeedlist[4]:
        SnowpeaSuncost = SnowpeaSuncost - 50

    if RepeaterFiringSpeed == Firingspeedlist[0]:
        RepeaterSuncost = RepeaterSuncost + 200
    elif RepeaterFiringSpeed == Firingspeedlist[1]:
        RepeaterSuncost = RepeaterSuncost + 100
    elif RepeaterFiringSpeed == Firingspeedlist[3]:
        RepeaterSuncost = RepeaterSuncost - 50
    elif RepeaterFiringSpeed == Firingspeedlist[4]:
        RepeaterSuncost = RepeaterSuncost - 100

    if RepeaterSuncost < GatlingpeaSuncost and RandomizeUpgrades == 'n':
        RepeaterFiringSpeed = GatlingpeaFiringSpeed
        RepeaterSuncost = 200
        if RepeaterFiringSpeed == Firingspeedlist[0]:
            RepeaterSuncost = RepeaterSuncost + 200
        elif RepeaterFiringSpeed == Firingspeedlist[1]:
            RepeaterSuncost = RepeaterSuncost + 100
        elif RepeaterFiringSpeed == Firingspeedlist[3]:
            RepeaterSuncost = RepeaterSuncost - 50
        elif RepeaterFiringSpeed == Firingspeedlist[4]:
            RepeaterSuncost = RepeaterSuncost - 100

    if FumeShroomFiringSpeed == Firingspeedlist[0]:
        FumeShroomSuncost = FumeShroomSuncost + 75
    elif FumeShroomFiringSpeed == Firingspeedlist[1]:
        FumeShroomSuncost = FumeShroomSuncost + 25
    elif FumeShroomFiringSpeed == Firingspeedlist[3]:
        FumeShroomSuncost = FumeShroomSuncost - 25
    elif FumeShroomFiringSpeed == Firingspeedlist[4]:
        FumeShroomSuncost = FumeShroomSuncost - 50

    if ScaredyShroomFiringSpeed == Firingspeedlist[0]:
        ScaredyShroomSuncost = ScaredyShroomSuncost + 50
    elif ScaredyShroomFiringSpeed == Firingspeedlist[1]:
        ScaredyShroomSuncost = ScaredyShroomSuncost + 25

    if ThreepeaterFiringSpeed == Firingspeedlist[0]:
        ThreepeaterSuncost = ThreepeaterSuncost + 325
    elif ThreepeaterFiringSpeed == Firingspeedlist[1]:
        ThreepeaterSuncost = ThreepeaterSuncost + 175
    elif ThreepeaterFiringSpeed == Firingspeedlist[3]:
        ThreepeaterSuncost = ThreepeaterSuncost - 125
    elif ThreepeaterFiringSpeed == Firingspeedlist[4]:
        ThreepeaterSuncost = ThreepeaterSuncost - 175

    if CactusFiringSpeed == Firingspeedlist[0]:
        CactusSuncost = CactusSuncost + 125
    elif CactusFiringSpeed == Firingspeedlist[1]:
        CactusSuncost = CactusSuncost + 75
    elif CactusFiringSpeed == Firingspeedlist[3]:
        CactusSuncost = CactusSuncost - 50
    elif CactusFiringSpeed == Firingspeedlist[4]:
        CactusSuncost = CactusSuncost - 75

    if StarfruitFiringSpeed == Firingspeedlist[0]:
        StarfuitSuncost = StarfuitSuncost + 125
    elif StarfruitFiringSpeed == Firingspeedlist[1]:
        StarfuitSuncost = StarfuitSuncost + 75
    elif StarfruitFiringSpeed == Firingspeedlist[3]:
        StarfuitSuncost = StarfuitSuncost - 50
    elif StarfruitFiringSpeed == Firingspeedlist[4]:
        StarfuitSuncost = StarfuitSuncost - 75

    if SplitpeaFiringSpeed == Firingspeedlist[0]:
        SplitpeaSuncost = SplitpeaSuncost + 125
    elif SplitpeaFiringSpeed == Firingspeedlist[1]:
        SplitpeaSuncost = SplitpeaSuncost + 75
    elif SplitpeaFiringSpeed == Firingspeedlist[3]:
        SplitpeaSuncost = SplitpeaSuncost - 75
    elif SplitpeaFiringSpeed == Firingspeedlist[4]:
        SplitpeaSuncost = SplitpeaSuncost - 100

    if CabbagepultFiringSpeed == Firingspeedlist[0]:
        CabbagepultSuncost = CabbagepultSuncost + 100
    elif CabbagepultFiringSpeed == Firingspeedlist[1]:
        CabbagepultSuncost = CabbagepultSuncost + 50
    elif CabbagepultFiringSpeed == Firingspeedlist[3]:
        CabbagepultSuncost = CabbagepultSuncost - 25
    elif CabbagepultFiringSpeed == Firingspeedlist[4]:
        CabbagepultSuncost = CabbagepultSuncost - 50
    CabbagepultFiringSpeed = CabbagepultFiringSpeed * 2

    if KernelpultFiringSpeed == Firingspeedlist[0]:
        KernelpultSuncost = KernelpultSuncost + 100
    elif KernelpultFiringSpeed == Firingspeedlist[1]:
        KernelpultSuncost = KernelpultSuncost + 50
    elif KernelpultFiringSpeed == Firingspeedlist[3]:
        KernelpultSuncost = KernelpultSuncost - 25
    elif KernelpultFiringSpeed == Firingspeedlist[4]:
        KernelpultSuncost = KernelpultSuncost - 50
    KernelpultFiringSpeed = KernelpultFiringSpeed * 2

    if KernelpultButterStuntime == KernelpultButterStuntimelist[0]:
        KernelpultSuncost = KernelpultSuncost - 25
    elif KernelpultButterStuntime == KernelpultButterStuntimelist[2]:
        KernelpultSuncost = KernelpultSuncost + 50
    elif KernelpultButterStuntime == KernelpultButterStuntimelist[3]:
        KernelpultSuncost = KernelpultSuncost + 75

    if MelonpultFiringSpeed == Firingspeedlist[0]:
        MelonpultSuncost = MelonpultSuncost + 300
    elif MelonpultFiringSpeed == Firingspeedlist[1]:
        MelonpultSuncost = MelonpultSuncost + 150
    elif MelonpultFiringSpeed == Firingspeedlist[3]:
        MelonpultSuncost = MelonpultSuncost - 100
    elif MelonpultFiringSpeed == Firingspeedlist[4]:
        MelonpultSuncost = MelonpultSuncost - 150
    MelonpultFiringSpeed = MelonpultFiringSpeed * 2

    if WintermelonFiringSpeed == Firingspeedlist[0]:
        WintermelonSuncost = WintermelonSuncost + 300
    elif WintermelonFiringSpeed == Firingspeedlist[1]:
        WintermelonSuncost = WintermelonSuncost + 150
    elif WintermelonFiringSpeed == Firingspeedlist[3]:
        WintermelonSuncost = WintermelonSuncost - 100
    elif WintermelonFiringSpeed == Firingspeedlist[4]:
        WintermelonSuncost = WintermelonSuncost - 150
    WintermelonFiringSpeed = WintermelonFiringSpeed * 2

    if GloomshroomFiringspeed == GloomshroomFiringspeedlist[0]:
        GloomshroomSuncost = GloomshroomSuncost * 2
    elif GloomshroomFiringspeed == GloomshroomFiringspeedlist[1]:
        GloomshroomSuncost = GloomshroomSuncost + 125
    elif GloomshroomFiringspeed == GloomshroomFiringspeedlist[3]:
        GloomshroomSuncost = GloomshroomSuncost - 75
        if FumeShroomSuncost <= GloomshroomSuncost and RandomizeUpgrades == 'n':
            FumeShroomSuncost = 50
            FumeShroomFiringSpeed = 225
    elif GloomshroomFiringspeed == GloomshroomFiringspeedlist[4]:
        GloomshroomSuncost = GloomshroomSuncost - 125
        if FumeShroomSuncost < GloomshroomSuncost and RandomizeUpgrades == 'n':
            FumeShroomSuncost = 25
            FumeShroomFiringSpeed = 300


##    if SpikeweedFiringSpeed == SpikeweedFiringSpeedlist[0]:
##        SpikeweedSuncost = SpikeweedSuncost + 100
##    elif SpikeweedFiringSpeed == SpikeweedFiringSpeedlist[1]:
##        SpikeweedSuncost = SpikeweedSuncost + 50
##    elif SpikeweedFiringSpeed == SpikeweedFiringSpeedlist[3]:
##        SpikeweedSuncost = SpikeweedSuncost - 50
##    elif SpikeweedFiringSpeed == SpikeweedFiringSpeedlist[4]:
##        SpikeweedSuncost = SpikeweedSuncost - 75

    if PotatoMineSurfacingtime == PotatoMineSurfacingtimelist[0]:
        PotatoMineSuncost = PotatoMineSuncost + 50
    elif PotatoMineSurfacingtime == PotatoMineSurfacingtimelist[1]:
        PotatoMineSuncost = PotatoMineSuncost + 25

    if ChomperChewingTime == ChomperChewingTimelist[0]:
        ChomperSuncost = ChomperSuncost + 150
    elif ChomperChewingTime == ChomperChewingTimelist[1]:
        ChomperSuncost = ChomperSuncost + 75
    elif ChomperChewingTime == ChomperChewingTimelist[3]:
        ChomperSuncost = ChomperSuncost - 50

    if GraveBusterEatingtime == GraveBusterEatingtimelist[0]:
        GraveBusterSuncost = GraveBusterSuncost + 50
    elif GraveBusterEatingtime == GraveBusterEatingtimelist[1]:
        GraveBusterSuncost = GraveBusterSuncost + 25
    elif GraveBusterEatingtime == GraveBusterEatingtimelist[3]:
        GraveBusterSuncost = GraveBusterSuncost - 25
    elif GraveBusterEatingtime == GraveBusterEatingtimelist[4]:
        GraveBusterSuncost = GraveBusterSuncost - 50

    if DoomshroomCratertime == DoomshroomCratertimelist[0]:
        DoomshroomSuncost = DoomshroomSuncost - 50
    elif DoomshroomCratertime == DoomshroomCratertimelist[1]:
        DoomshroomSuncost = DoomshroomSuncost - 25
    elif DoomshroomCratertime == DoomshroomCratertimelist[3]:
        DoomshroomSuncost = DoomshroomSuncost + 25

    if Bloverfogawaytime == Bloverfogawaytimelist[0]:
        BloverSuncost = BloverSuncost - 25
    elif Bloverfogawaytime == Bloverfogawaytimelist[2]:
        BloverSuncost = BloverSuncost + 25
    elif Bloverfogawaytime == Bloverfogawaytimelist[3]:
        BloverSuncost = BloverSuncost + 50

    if MagnetShroomcooldown == MagnetShroomcooldownlist[0]:
        MagnetShroomSuncost = MagnetShroomSuncost - 50
    elif MagnetShroomcooldown == MagnetShroomcooldownlist[2]:
        MagnetShroomSuncost = MagnetShroomSuncost + 50
    elif MagnetShroomcooldown == MagnetShroomcooldownlist[3]:
        MagnetShroomSuncost = MagnetShroomSuncost + 100

    if CattailFiringSpeed == Firingspeedlist[0]:
        CattailSuncost = CattailSuncost + 225
    elif CattailFiringSpeed == Firingspeedlist[1]:
        CattailSuncost = CattailSuncost + 75
    elif CattailFiringSpeed == Firingspeedlist[3]:
        CattailSuncost = CattailSuncost - 75
    elif CattailFiringSpeed == Firingspeedlist[4]:
        CattailSuncost = CattailSuncost - 100

if RandomizePlantDamage == 'y':
#10 = 50- sun
#20 = 0+ sun
#30 = 50+ sun
#40 = 100+ sun
#50 = 150+ sun
#60 = 200+ sun
#70 = 250+ sun
#80 = 300+ sun
    ProjectileDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    if PotatoMineSuncost > 25:
        PotatoMineDamageList = [1800, 1200]
        if PotatoMineSuncost >= 50:
            PotatoMineDamageList.append(900)
        PotatoMineDamage = random.choice(PotatoMineDamageList)
        if PotatoMineDamage == PotatoMineDamageList[1]:
            PotatoMineSuncost = PotatoMineSuncost - 25
        elif PotatoMineDamage == PotatoMineDamageList[2]:
            PotatoMineSuncost = PotatoMineSuncost - 50
    SquashDamageList = [1800, 1200]
    SquashDamage = random.choice(SquashDamageList)
    if SquashDamage == SquashDamageList[1]:
        SquashSuncost = SquashSuncost - 25
#
    GloomshroomDamage = random.choice(ProjectileDamageList)
    if GloomshroomDamage == ProjectileDamageList[0]:
        GloomshroomSuncost = GloomshroomSuncost - 75
    elif GloomshroomDamage == ProjectileDamageList[2]:
        GloomshroomSuncost = GloomshroomSuncost + 75
    elif GloomshroomDamage == ProjectileDamageList[3]:
        GloomshroomSuncost = GloomshroomSuncost + 225
    elif GloomshroomDamage == ProjectileDamageList[4]:
        GloomshroomSuncost = GloomshroomSuncost + 300
    elif GloomshroomDamage == ProjectileDamageList[5]:
        GloomshroomSuncost = GloomshroomSuncost + 450
    elif GloomshroomDamage == ProjectileDamageList[6]:
        GloomshroomSuncost = GloomshroomSuncost + 600
    elif GloomshroomDamage == ProjectileDamageList[7]:
        GloomshroomSuncost = GloomshroomSuncost + 675

#
    SpikerockDamage = random.choice(ProjectileDamageList)
    if SpikerockDamage == ProjectileDamageList[0]:
        SpikerockSuncost = SpikerockSuncost - 75
    elif SpikerockDamage == ProjectileDamageList[2]:
        SpikerockSuncost = SpikerockSuncost + 25
    elif SpikerockDamage == ProjectileDamageList[3]:
        SpikerockSuncost = SpikerockSuncost + 75
    elif SpikerockDamage == ProjectileDamageList[4]:
        SpikerockSuncost = SpikerockSuncost + 125
    elif SpikerockDamage == ProjectileDamageList[5]:
        SpikerockSuncost = SpikerockSuncost + 175
    elif SpikerockDamage == ProjectileDamageList[6]:
        SpikerockSuncost = SpikerockSuncost + 225
    elif SpikerockDamage == ProjectileDamageList[7]:
        SpikerockSuncost = SpikerockSuncost + 275
#
    SnowpeaDamage = random.choice(ProjectileDamageList)
    if SnowpeaDamage == ProjectileDamageList[0]:
        SnowpeaSuncost = SnowpeaSuncost - 75
    elif SnowpeaDamage == ProjectileDamageList[2]:
        SnowpeaSuncost = SnowpeaSuncost + 25
    elif SnowpeaDamage == ProjectileDamageList[3]:
        SnowpeaSuncost = SnowpeaSuncost + 75
    elif SnowpeaDamage == ProjectileDamageList[4]:
        SnowpeaSuncost = SnowpeaSuncost + 125
    elif SnowpeaDamage == ProjectileDamageList[5]:
        SnowpeaSuncost = SnowpeaSuncost + 175
    elif SnowpeaDamage == ProjectileDamageList[6]:
        SnowpeaSuncost = SnowpeaSuncost + 225
    elif SnowpeaDamage == ProjectileDamageList[7]:
        SnowpeaSuncost = SnowpeaSuncost + 275
#
    FumeShroomDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    SpikeweedDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    if SpikeweedSuncost <= 50:
        SpikeweedDamageList.remove(10)
    if FumeShroomSuncost <= 50:
        FumeShroomDamageList.remove(10)
    if RandomizeUpgrades == 'n':            
        if SpikeweedSuncost <= 100:
            SpikeweedDamageList.remove(50)
        if SpikeweedSuncost <= 150:
            SpikeweedDamageList.remove(40)
        if SpikeweedSuncost <= 200:
            SpikeweedDamageList.remove(30)
        SpikeweedDamageList.remove(60)
        FumeShroomDamageList.remove(60)
        SpikeweedDamageList.remove(70)
        FumeShroomDamageList.remove(70)
        SpikeweedDamageList.remove(80)
        FumeShroomDamageList.remove(80)
    FumeShroomDamage = random.choice(FumeShroomDamageList)
    SpikeweedDamage = random.choice(SpikeweedDamageList)
    if SpikeweedDamage == 10:
        SpikeweedSuncost = SpikeweedSuncost - 75     
    elif SpikeweedDamage == 30:
        SpikeweedSuncost = SpikeweedSuncost + 50
    elif SpikeweedDamage == 40:
        SpikeweedSuncost = SpikeweedSuncost + 100
    elif SpikeweedDamage == 50:
        SpikeweedSuncost = SpikeweedSuncost + 150
    elif SpikeweedDamage == 60:
        SpikeweedSuncost = SpikeweedSuncost + 200 
    elif SpikeweedDamage == 70:
        SpikeweedSuncost = SpikeweedSuncost + 250
    elif SpikeweedDamage == 80:
        SpikeweedSuncost = SpikeweedSuncost + 300

    if FumeShroomDamage == 10:
        FumeShroomSuncost = FumeShroomSuncost - 50        
    elif FumeShroomDamage == 30:
        FumeShroomSuncost = FumeShroomSuncost + 25  
    elif FumeShroomDamage == 40:
        FumeShroomSuncost = FumeShroomSuncost + 75 
    elif FumeShroomDamage == 50:
        FumeShroomSuncost = FumeShroomSuncost + 100 
    elif FumeShroomDamage == 60:
        FumeShroomSuncost = FumeShroomSuncost + 150 
    elif FumeShroomDamage == 70:
        FumeShroomSuncost = FumeShroomSuncost + 175
    elif FumeShroomDamage == 80:
        FumeShroomSuncost = FumeShroomSuncost + 225

#
    CactusDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    if CactusSuncost == 50:
        CactusDamageList.remove(10)
    CactusDamage = random.choice(CactusDamageList)
    if CactusDamage == 10:
        CactusSuncost = CactusSuncost - 50
        CattailSuncost = CattailSuncost - 50
    elif CactusDamage == 30:
        CactusSuncost = CactusSuncost + 50
        CattailSuncost = CattailSuncost + 50
    elif CactusDamage == 40:
        CactusSuncost = CactusSuncost + 100
        CattailSuncost = CattailSuncost + 100
    elif CactusDamage == 50:
        CactusSuncost = CactusSuncost + 150
        CattailSuncost = CattailSuncost + 150
    elif CactusDamage == 60:
        CactusSuncost = CactusSuncost + 200
        CattailSuncost = CattailSuncost + 200
    elif CactusDamage == 70:
        CactusSuncost = CactusSuncost + 250
        CattailSuncost = CattailSuncost + 250
    elif CactusDamage == 80:
        CactusSuncost = CactusSuncost + 300
        CattailSuncost = CattailSuncost + 300
#
    StarfruitDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    if StarfuitSuncost == 50:
        StarfruitDamageList.remove(10)
    StarfruitDamage = random.choice(StarfruitDamageList)
    if StarfruitDamage == 10:
        StarfuitSuncost = StarfuitSuncost - 50
    elif StarfruitDamage == 30:
        StarfuitSuncost = StarfuitSuncost + 75
    elif StarfruitDamage == 40:
        StarfuitSuncost = StarfuitSuncost + 125
    elif StarfruitDamage == 50:
        StarfuitSuncost = StarfuitSuncost + 175
    elif StarfruitDamage == 60:
        StarfuitSuncost = StarfuitSuncost + 250
    elif StarfruitDamage == 70:
        StarfuitSuncost = StarfuitSuncost + 300
    elif StarfruitDamage == 80:
        StarfuitSuncost = StarfuitSuncost + 375
#
    CabbagepultDamage = random.choice(ProjectileDamageList)
    if CabbagepultDamage == ProjectileDamageList[0]:
        CabbagepultSuncost = CabbagepultSuncost - 50
    elif CabbagepultDamage == ProjectileDamageList[2]:
        CabbagepultSuncost = CabbagepultSuncost + 50
    elif CabbagepultDamage == ProjectileDamageList[3]:
        CabbagepultSuncost = CabbagepultSuncost + 100
    elif CabbagepultDamage == ProjectileDamageList[4]:
        CabbagepultSuncost = CabbagepultSuncost + 150
    elif CabbagepultDamage == ProjectileDamageList[5]:
        CabbagepultSuncost = CabbagepultSuncost + 200
    elif CabbagepultDamage == ProjectileDamageList[6]:
        CabbagepultSuncost = CabbagepultSuncost + 250
    elif CabbagepultDamage == ProjectileDamageList[7]:
        CabbagepultSuncost = CabbagepultSuncost + 300
    CabbagepultDamage = CabbagepultDamage * 2
#
    KernelpultKerneldamage = random.choice(ProjectileDamageList)
    if KernelpultKerneldamage == ProjectileDamageList[1]:
        KernelpultSuncost = KernelpultSuncost + 25
    elif KernelpultKerneldamage == ProjectileDamageList[2]:
        KernelpultSuncost = KernelpultSuncost + 50
    elif KernelpultKerneldamage == ProjectileDamageList[3]:
        KernelpultSuncost = KernelpultSuncost + 100
    elif KernelpultKerneldamage == ProjectileDamageList[4]:
        KernelpultSuncost = KernelpultSuncost + 150
    elif KernelpultKerneldamage == ProjectileDamageList[5]:
        KernelpultSuncost = KernelpultSuncost + 200
    elif KernelpultKerneldamage == ProjectileDamageList[6]:
        KernelpultSuncost = KernelpultSuncost + 250
    elif KernelpultKerneldamage == ProjectileDamageList[7]:
        KernelpultSuncost = KernelpultSuncost + 300
    KernelpultKerneldamage = KernelpultKerneldamage * 2
#
    KernelpultButterdamage = random.choice(ProjectileDamageList)
    if KernelpultButterdamage == ProjectileDamageList[0]:
        KernelpultSuncost = KernelpultSuncost - 25
    elif KernelpultButterdamage == ProjectileDamageList[2]:
        KernelpultSuncost = KernelpultSuncost + 25
    elif KernelpultButterdamage == ProjectileDamageList[3]:
        KernelpultSuncost = KernelpultSuncost + 75
    elif KernelpultButterdamage == ProjectileDamageList[4]:
        KernelpultSuncost = KernelpultSuncost + 125
    elif KernelpultButterdamage == ProjectileDamageList[5]:
        KernelpultSuncost = KernelpultSuncost + 175
    elif KernelpultButterdamage == ProjectileDamageList[6]:
        KernelpultSuncost = KernelpultSuncost + 225
    elif KernelpultButterdamage == ProjectileDamageList[7]:
        KernelpultSuncost = KernelpultSuncost + 275
    KernelpultButterdamage = KernelpultButterdamage * 2
#
    MelonpultDamageList = [10, 20, 30, 40, 50, 60, 70, 80]
    if MelonpultSuncost > 200:
        MelonpultDamageList.append(10)
    if MelonpultSuncost > 150:
        MelonpultDamageList.append(30)
    Melonpultdamage = random.choice(ProjectileDamageList)

    if Melonpultdamage == 10:
        MelonpultSuncost = MelonpultSuncost - 200
    elif Melonpultdamage == 20:
        MelonpultSuncost = MelonpultSuncost - 150
    elif Melonpultdamage == 30:
        MelonpultSuncost = MelonpultSuncost - 100
    elif Melonpultdamage == 50:
        MelonpultSuncost = MelonpultSuncost + 150
    elif Melonpultdamage == 60:
        MelonpultSuncost = MelonpultSuncost + 300
    elif Melonpultdamage == 70:
        MelonpultSuncost = MelonpultSuncost + 450
    elif Melonpultdamage == 80:
        MelonpultSuncost = MelonpultSuncost + 600
    Melonpultdamage = Melonpultdamage * 2

    Wintermelondamage = random.choice(ProjectileDamageList)
    if Wintermelondamage == ProjectileDamageList[0]:
        WintermelonSuncost = WintermelonSuncost - 200
    elif Wintermelondamage == ProjectileDamageList[1]:
        WintermelonSuncost = WintermelonSuncost - 150
    elif Wintermelondamage == ProjectileDamageList[2]:
        WintermelonSuncost = WintermelonSuncost - 100
    elif Wintermelondamage == ProjectileDamageList[4]:
        WintermelonSuncost = WintermelonSuncost + 150
    elif Wintermelondamage == ProjectileDamageList[5]:
        WintermelonSuncost = WintermelonSuncost + 300
    elif Wintermelondamage == ProjectileDamageList[6]:
        WintermelonSuncost = WintermelonSuncost + 450
    elif Wintermelondamage == ProjectileDamageList[7]:
        WintermelonSuncost = WintermelonSuncost + 600
    Wintermelondamage = Wintermelondamage * 2
    
    ExplodingPlantDamageList = [1800, 1200, 900]
    CherryBombDamage = random.choice(ExplodingPlantDamageList)
    if CherryBombDamage == ExplodingPlantDamageList[1]:
        CherryBombSuncost = CherryBombSuncost - 50
    elif CherryBombDamage == ExplodingPlantDamageList[2]:
        CherryBombSuncost = CherryBombSuncost - 75

    DoomshroomDamageList = [1800]
    if DoomshroomSuncost > 50:
        DoomshroomDamageList.append(900)
    if DoomshroomSuncost > 75:
        DoomshroomDamageList.append(1200)
    DoomshroomDamage = random.choice(DoomshroomDamageList)
    if DoomshroomDamage == 900:
        DoomshroomSuncost = DoomshroomSuncost - 50
    elif DoomshroomDamage == 1200:
        DoomshroomSuncost = DoomshroomSuncost - 75


if RandomizeUpgrades == 'y':
##NEW
    PeashooterSuncost = 100
    SunflowerSuncost = 50
    SunshroomSuncost = 25
    TorchwoodSuncost = 175
    UmberellaSuncost = 100

    GatlingpeaDowngradeSuncostPlantlist = []
    GatlingpeaDowngradePlantlist = []
    CobcannonDowngradeSuncostPlantlist = []
    CobcannonDowngradePlantlist = []
    WintermelonDowngradeSuncostPlantlist = []
    WintermelonDowngradePlantlist = []
    SpikerockDowngradeSuncostPlantlist = []
    SpikerockDowngradePlantlist = []
    TwinsunflowerDowngradeSuncostPlantlist = []
    TwinsunflowerDowngradePlantlist = []
    GoldmagnetDowngradeSuncostPlantlist = []
    GoldmagnetDowngradePlantlist = []
    GloomshroomDowngradeSuncostPlantlist = []
    GloomshroomDowngradePlantlist = []
    PlantListNum = 0



    PlantSuncostList = [PeashooterSuncost,
                        SunflowerSuncost,
                        SnowpeaSuncost,
                        ChomperSuncost,
                        RepeaterSuncost,
                        SunshroomSuncost,
                        FumeShroomSuncost,
                        ScaredyShroomSuncost,
                        ThreepeaterSuncost,
                        TorchwoodSuncost,
                        SpikeweedSuncost,
                        CactusSuncost,
                        SplitpeaSuncost,
                        StarfuitSuncost,
                        MagnetShroomSuncost,
                        CabbagepultSuncost,
                        KernelpultSuncost,
                        GarlicSuncost,
                        UmberellaSuncost,
                        MelonpultSuncost]
    Plantlist = ["Peashooter",
                 "Sunflower",
                 "Snowpea",
                 "Chomper",
                 "Repeater",
                 "Sunshroom",
                 "Fumeshroom",
                 "Scaredyshroom",
                 "Threepeater",
                 "Torchwood",
                 "Spikeweed",
                 "Cactus",
                 "Splitpea",
                 "Starfruit",
                 "Magnetshroom",
                 "Cabbagepult",
                 "Kernelpult",
                 "Garlic",
                 "Umbrella",
                 "Melonpult"]


    while PlantListNum != len(Plantlist):
        if PlantSuncostList[PlantListNum] < GatlingpeaSuncost:
            GatlingpeaDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            GatlingpeaDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < CobcannonSuncost:
            CobcannonDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            CobcannonDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < WintermelonSuncost:
            WintermelonDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            WintermelonDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < SpikerockSuncost:
            SpikerockDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            SpikerockDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < TwinsunflowerSuncost:
            TwinsunflowerDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            TwinsunflowerDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < GoldmagnetSuncost:
            GoldmagnetDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            GoldmagnetDowngradePlantlist.append(Plantlist[PlantListNum])
        if PlantSuncostList[PlantListNum] < GloomshroomSuncost:
            GloomshroomDowngradeSuncostPlantlist.append(PlantSuncostList[PlantListNum])
            GloomshroomDowngradePlantlist.append(Plantlist[PlantListNum])
        PlantListNum += 1


    GatlingpeaDowngradePlantNum = random.randint(0, len(GatlingpeaDowngradePlantlist) - 1)
    Gatlingpeadowngradeplant = GatlingpeaDowngradePlantlist[GatlingpeaDowngradePlantNum]
    GatlingpeaSuncost -= GatlingpeaDowngradeSuncostPlantlist[GatlingpeaDowngradePlantNum]

    CobcannonDowngradePlantNum = random.randint(0, len(CobcannonDowngradePlantlist) - 1)
    Cobcannondowngradeplant = CobcannonDowngradePlantlist[CobcannonDowngradePlantNum]
    CobcannonSuncost -= CobcannonDowngradeSuncostPlantlist[CobcannonDowngradePlantNum] * 2

    WintermelonDowngradePlantNum = random.randint(0, len(WintermelonDowngradePlantlist) - 1)
    Wintermelondowngradeplant = WintermelonDowngradePlantlist[WintermelonDowngradePlantNum]
    WintermelonSuncost -= WintermelonDowngradeSuncostPlantlist[WintermelonDowngradePlantNum]

    TwinsunflowerDowngradePlantNum = random.randint(0, len(TwinsunflowerDowngradePlantlist) - 1)
    Twinsunflowerdowngradeplant = TwinsunflowerDowngradePlantlist[TwinsunflowerDowngradePlantNum]
    TwinsunflowerSuncost -= TwinsunflowerDowngradeSuncostPlantlist[TwinsunflowerDowngradePlantNum]

    GoldmagnetDowngradePlantNum = random.randint(0, len(GoldmagnetDowngradePlantlist) - 1)
    Goldmagnetdowngradeplant = GoldmagnetDowngradePlantlist[GoldmagnetDowngradePlantNum]
    GoldmagnetSuncost -= GoldmagnetDowngradeSuncostPlantlist[GoldmagnetDowngradePlantNum]

    GloomshroomDowngradePlantNum = random.randint(0, len(GloomshroomDowngradePlantlist) - 1)
    Gloomshroomdowngradeplant = GloomshroomDowngradePlantlist[GloomshroomDowngradePlantNum]
    GloomshroomSuncost -= GloomshroomDowngradeSuncostPlantlist[GloomshroomDowngradePlantNum]

    SpikerockDowngradePlantNum = random.randint(0, len(SpikerockDowngradePlantlist) - 1)
    Spikerockdowngradeplant = SpikerockDowngradePlantlist[SpikerockDowngradePlantNum]
    SpikerockSuncost -= SpikerockDowngradeSuncostPlantlist[SpikerockDowngradePlantNum]
else:
    GatlingpeaSuncost = 250
    CobcannonSuncost = 500
    WintermelonSuncost = 200
    TwinsunflowerSuncost = 150
    GoldmagnetSuncost = 50
    GloomshroomSuncost = 150
    SpikerockSuncost = 125
##print("Wall-Nut")
##print("Sun Cost: ", WallnutSuncost)
##print("Health: ", WallnutHealth)
##print("")
##print("")
##print("Potato Mine")
##print("Sun Cost: ", PotatoMineSuncost)
##print("Surfacing time: ", PotatoMineSurfacingtime)
##print("Explosion Damage: ", PotatoMineDamage)
##print("")
##print("")
##print("Snow Pea")
##print("Sun Cost: ", SnowpeaSuncost)
##print("Attack Damage: ", SnowpeaDamage)
##print("Firing speed: ", SnowpeaFiringSpeed)
##print("")
##print("")
##print("Chomper")
##print("Sun Cost: ", ChomperSuncost)
##print("Chewing time: ", ChomperChewingTime)
##print("")
##print("")
##print("Repeater")
##print("Sun Cost: ", RepeaterSuncost)
##print("Attack Damage: ", 20)
##print("Firing speed: ", RepeaterFiringSpeed)
##print("")
##print("")
##print("Gatlingpea")
##print("Sun Cost: ", GatlingpeaSuncost)
##print("Attack Damage: ", 20)
##print("Firing speed: ", GatlingpeaFiringSpeed)
##print("Downgrade Plant: ", Gatlingpeadowngradeplant)
##print("")
##print("")
##print("Fume-shroom")
##print("Sun Cost: ", FumeShroomSuncost)
##print("Attack Damage: ", FumeShroomSpikeweedDamage)
##print("Firing speed: ", FumeShroomFiringSpeed)
##print("")
##print("")
##print("Gloomshroom")
##print("Sun Cost: ", GloomshroomSuncost)
##print("Attack Damage: ")
##print("Firing speed: ")
##print("Downgrade Plant: ", Gloomshroomdowngradeplant)
##print("")
##print("")
##print("Scaredy-shroom")
##print("Sun Cost: ", ScaredyShroomSuncost)
##print("Attack Damage: ", 20)
##print("Firing speed: ", ScaredyShroomFiringSpeed)
#print("")
#print("")
#print("Grave Buster")
#print("Sun Cost: ", GraveBusterSuncost)
#print("Eating Time: ", GraveBusterEatingtime)
#print("")
#print("")
##print("Ice-Shroom")
##print("Sun Cost: ", IceShroomSuncost)
##print("Attack Damage: ", IceShroomDamage)
##print("")
##print("")
##print("Doom-Shroom")
##print("Sun Cost: ", DoomshroomSuncost)
##print("Crater time: ", DoomshroomCratertime)
##print("")
##print("")
##print("Squash")
##print("Sun Cost: ", SquashSuncost)
##print("Attack Damage: ", SquashDamage)
##print("")
##print("")
##print("Spikeweed")
##print("Sun Cost: ", SpikeweedSuncost)
##print("Attack Damage: ", FumeShroomSpikeweedDamage)
##print("Firing speed: ", SpikeweedFiringSpeed)
##print("")
##print("")
##print("Threepeater")
##print("Sun Cost: ", ThreepeaterSuncost)
##print("Attack Damage: ", 20)
##print("Firing speed: ", ThreepeaterFiringSpeed)
##print("")
##print("")
##print("Tall-Nut")
##print("Sun Cost: ", TallnutSuncost)
##print("Health: ", TallnutHealth)
##print("")
##print("")
##print("Cactus")
##print("Sun Cost: ", CactusSuncost)
##print("Attack Damage: ", CactusDamage)
##print("Firing speed: ", CactusFiringSpeed)
##print("")
##print("")
##print("Split pea")
##print("Sun Cost: ", SplitpeaSuncost)
##print("Attack Damage: ", 20)
##print("Firing speed: ", SplitpeaFiringSpeed)
##print("")
##print("")
##print("Starfruit")
##print("Sun Cost: ", StarfuitSuncost)
##print("Attack Damage: ", StarfruitDamage)
##print("Firing speed: ", StarfruitFiringSpeed)
##print("")
##print("")
##print("Pumpkin")
##print("Sun Cost: ", PumpkinSuncost)
##print("Health: ", PumpkinHealth)
##print("")
##print("")
##print("Goldmagnet")
##print("Sun Cost: ", GoldmagnetSuncost)
##print("Downgrade Plant: ", Goldmagnetdowngradeplant)
##print("")
##print("")
##print("Spikerock")
##print("Sun Cost: ", SpikerockSuncost)
##print("Attack Damage: ")
##print("Firing speed: ")
##print("Downgrade Plant: ", Spikerockdowngradeplant)
##print("")
##print("")
##print("Winter melon")
##print("Sun Cost: ", WintermelonSuncost)
##print("Attack Damage: ")
##print("Firing speed: ")
##print("Downgrade Plant: ", Wintermelondowngradeplant)
##print("")
##print("")
##print("Cobcannon")
##print("Sun Cost: ", CobcannonSuncost)
##print("Attack Damage: ")
##print("Firing speed: ")
##print("Downgrade Plant: ", Cobcannondowngradeplant)
##print("")
##print("")
##print("Garlic")
##print("Sun Cost: ", GarlicSuncost)
##print("Health: ", GarlicHealth)
##print("")
##print("")

print("Setting up plant stats")

from xml.etree import ElementTree as et
datafile = "RandomizerSettings.xml";
tree = et.parse(datafile)

#Gatlingpea
tree.find(".//GatlingPeaFiringSpeed").text = str(GatlingpeaFiringSpeed)
tree.find(".//GatlingPeaSuncost").text = str(GatlingpeaSuncost)
tree.find(".//Gatlingpeadowngradeplant").text = str(Gatlingpeadowngradeplant)
#Twinsunflower
tree.find(".//TwinsunflowerSuncost").text = str(TwinsunflowerSuncost)
tree.find(".//Twinsunflowerdowngradeplant").text = str(Twinsunflowerdowngradeplant)
#Gloomshroom
tree.find(".//Gloomshroomdowngradeplant").text = str(Gloomshroomdowngradeplant)
tree.find(".//GloomshroomSuncost").text = str(GloomshroomSuncost)
tree.find(".//GloomshroomFiringSpeed").text = str(GloomShroomFiringSpeed)
tree.find(".//GloomShroomDamage").text = str(GloomShroomDamage)
#Cattail
tree.find(".//CattailSuncost").text = str(CattailSuncost)
tree.find(".//CattailFiringSpeed").text = str(CattailFiringSpeed)
#Cobcannon
tree.find(".//CobcannonSuncost").text = str(CobcannonSuncost)
tree.find(".//Cobcannondowngradeplant").text = str(Cobcannondowngradeplant)
#Wintermelon
tree.find(".//Wintermelondowngradeplant").text = str(Wintermelondowngradeplant)
tree.find(".//WintermelonSuncost").text = str(WintermelonSuncost)
tree.find(".//WintermelonFiringSpeed").text = str(WintermelonFiringSpeed)
tree.find(".//Wintermelondamage").text = str(Wintermelondamage)
#Goldmagnet
tree.find(".//Goldmagnetdowngradeplant").text = str(Goldmagnetdowngradeplant)
tree.find(".//GoldmagnetSuncost").text = str(GoldmagnetSuncost)
#Spikerock
tree.find(".//Spikerockdowngradeplant").text = str(Spikerockdowngradeplant)
tree.find(".//SpikerockSuncost").text = str(SpikerockSuncost)
tree.find(".//SpikerockFiringSpeedA").text = str(SpikerockFiringSpeedA)
tree.find(".//SpikerockFiringSpeedB").text = str(SpikerockFiringSpeedB)
tree.find(".//SpikerockDamage").text = str(SpikerockDamage)

#Wallnut
tree.find(".//WallnutSuncost").text = str(WallnutSuncost)
tree.find(".//WallnutHealth").text = str(WallnutHealth)



#PotatoMine
tree.find(".//PotatoMineSuncost").text = str(PotatoMineSuncost)
tree.find(".//PotatoMineSurfacingtime").text = str(PotatoMineSurfacingtime)
tree.find(".//PotatoMineDamage").text = str(PotatoMineDamage)
#Chomper
tree.find(".//ChomperSuncost").text = str(ChomperSuncost)
tree.find(".//ChomperChewingTime").text = str(ChomperChewingTime)

#Snowpea
tree.find(".//SnowpeaSuncost").text = str(SnowpeaSuncost)
tree.find(".//SnowpeaFiringSpeed").text = str(SnowpeaFiringSpeed)
tree.find(".//SnowpeaDamage").text = str(SnowpeaDamage)
#Repeater
tree.find(".//RepeaterSuncost").text = str(RepeaterSuncost)
tree.find(".//RepeaterFiringSpeed").text = str(RepeaterFiringSpeed)
#Fumeshroom and Spikeweed
tree.find(".//FumeShroomSuncost").text = str(FumeShroomSuncost)
tree.find(".//FumeShroomDamage").text = str(FumeShroomDamage)
tree.find(".//FumeShroomFiringSpeed").text = str(FumeShroomFiringSpeed)

tree.find(".//SpikeweedSuncost").text = str(SpikeweedSuncost)
tree.find(".//SpikeweedFiringSpeed").text = str(SpikeweedFiringSpeed)
tree.find(".//SpikeweedDamage").text = str(SpikeweedDamage)

#Gravebuster
tree.find(".//GraveBusterSuncost").text = str(GraveBusterSuncost)
tree.find(".//GraveBusterEatingtime").text = str(GraveBusterEatingtime)
#IceShroom
tree.find(".//IceShroomSuncost").text = str(IceShroomSuncost)
tree.find(".//IceShroomDamage").text = str(IceShroomDamage)
#ScaredyShroom
tree.find(".//ScaredyShroomSuncost").text = str(ScaredyShroomSuncost)
tree.find(".//ScaredyShroomFiringSpeed").text = str(ScaredyShroomFiringSpeed)
#Doomshroom
tree.find(".//DoomshroomSuncost").text = str(DoomshroomSuncost)
tree.find(".//DoomshroomCratertime").text = str(DoomshroomCratertime)
tree.find(".//DoomshroomDamage").text = str(DoomshroomDamage)
#Squash
tree.find(".//SquashSuncost").text = str(SquashSuncost)
tree.find(".//SquashDamage").text = str(SquashDamage)
#Threepeater
tree.find(".//ThreepeaterSuncost").text = str(ThreepeaterSuncost)
tree.find(".//ThreepeaterFiringSpeed").text = str(ThreepeaterFiringSpeed)
#Tallnut
tree.find(".//TallnutSuncost").text = str(TallnutSuncost)
tree.find(".//TallnutHealth").text = str(TallnutHealth)
#Cactus
tree.find(".//CactusSuncost").text = str(CactusSuncost)
tree.find(".//CactusFiringSpeed").text = str(CactusFiringSpeed)
tree.find(".//CactusDamage").text = str(CactusDamage)
#Starfruit
tree.find(".//StarfuitSuncost").text = str(StarfuitSuncost)
tree.find(".//StarfruitFiringSpeed").text = str(StarfruitFiringSpeed)
tree.find(".//StarfruitDamage").text = str(StarfruitDamage)
#Blover
tree.find(".//BloverSuncost").text = str(BloverSuncost)
tree.find(".//Bloverfogawaytime").text = str(Bloverfogawaytime)
#Pumpkin
tree.find(".//PumpkinSuncost").text = str(PumpkinSuncost)
tree.find(".//PumpkinHealth").text = str(PumpkinHealth)
#Splitpea
tree.find(".//SplitpeaSuncost").text = str(SplitpeaSuncost)
tree.find(".//SplitpeaFiringSpeed").text = str(SplitpeaFiringSpeed)
#MagnetShroom
tree.find(".//MagnetShroomSuncost").text = str(MagnetShroomSuncost)
tree.find(".//MagnetShroomcooldown").text = str(MagnetShroomcooldown)
#Cabbagepult
tree.find(".//CabbagepultSuncost").text = str(CabbagepultSuncost)
tree.find(".//CabbagepultFiringSpeed").text = str(CabbagepultFiringSpeed)
tree.find(".//CabbagepultDamage").text = str(CabbagepultDamage)
#Kernelpult
tree.find(".//KernelpultSuncost").text = str(KernelpultSuncost)
tree.find(".//KernelpultFiringSpeed").text = str(KernelpultFiringSpeed)
tree.find(".//KernelpultKerneldamage").text = str(KernelpultKerneldamage)
tree.find(".//KernelpultButterdamage").text = str(KernelpultButterdamage)
tree.find(".//KernelpultButterStuntime").text = str(KernelpultButterStuntime)
#Garlic
tree.find(".//GarlicSuncost").text = str(GarlicSuncost)
tree.find(".//GarlicHealth").text = str(GarlicHealth)
#Melonpult
tree.find(".//MelonpultSuncost").text = str(MelonpultSuncost)
tree.find(".//MelonpultFiringSpeed").text = str(MelonpultFiringSpeed)
tree.find(".//Melonpultdamage").text = str(Melonpultdamage)
#CherryBomb
tree.find(".//CherryBombSuncost").text = str(CherryBombSuncost)
tree.find(".//CherryBombDamage").text = str(CherryBombDamage)

tree.write(datafile)

print("Done")
