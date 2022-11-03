import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def enablegroup():
    SeedNameEntry.configure(state="normal")
    Random_button.configure(state="normal")
    help_button.configure(state="normal")
    dropdown.configure(state="normal")
    DowngradePlants_c1.configure(state="normal")
    PlantHealth_c1.configure(state="normal")
    PlantDamage_c1.configure(state="normal")
    PlantAction_c1.configure(state="normal")
    AdventureModeSeedpackets_c1.configure(state="normal")
    AdventureModeSeedpackets_matchseedpackets_c1.configure(state="normal")
    AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1.configure(state="normal")

def disablegroup():
    SeedNameEntry.configure(state="disabled")
    Random_button.configure(state="disabled")
    help_button.configure(state="disabled")
    dropdown.configure(state="disabled")
    DowngradePlants_c1.configure(state="disabled")
    PlantHealth_c1.configure(state="disabled")
    PlantDamage_c1.configure(state="disabled")
    PlantAction_c1.configure(state="disabled")
    PlantAction_c1.configure(state="disabled")
    AdventureModeSeedpackets_c1.configure(state="disabled")
    AdventureModeSeedpackets_matchseedpackets_c1.configure(state="disabled")
    AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1.configure(state="disabled")
    SummonedZombieAdventure_c1.configure(state="disabled")
    ZombieAdventure_c1.configure(state="disabled")
    ZoboantyAdventure_c1.configure(state="disabled")
    GigaGargAdventure_c1.configure(state="disabled")
    Converyor_c1.configure(state="disabled")
    ConveryorAll_c1.configure(state="disabled")
    DowngradePlants_c1.configure(state="disabled")
    RandomizeBackground_c1.configure(state="disabled")
    RandomizeCustomBackground_c1.configure(state="disabled")
    Sunmeta_c1.configure(state="disabled")
    MinWavesEntry.configure(state="disabled")
    MaxWavesEntry.configure(state="disabled")
    FixedWavesEntry.configure(state="disabled")
    BalloonZombieCounterCheck_c1.configure(state="disabled")
    StorePlants_c1.configure(state="disabled")
def Randomize():
    clearConsole()
    print("Seed name:", SeedNameEntry.get())
    #
    minwaves = MinWavesEntry.get()
    maxwaves = MaxWavesEntry.get()
    SeedNum = SeedNameEntry.get()
    waveamount = FixedWavesEntry.get()
    ZombieAdventurecheck = ZombieAdventure.get()
    Sunmeta = Sunmeta50.get()
    DontChangeSeedpacketIconOrder = AdventureModeSeedpackets_matchseedpackets.get()
    RandomizeBackground = RandomizeBackgrounds.get()
    EnableCustombackgrounds = RandomizeCustomBackground.get()
    RandomizeUpgrades = DowngradePlants.get()
    ConveryorRandomize = Converyor.get()
    ConveryorRandomizeAll = ConveryorAll.get()
    ZombieLevel = ZombieAdventure.get()
    SummonedZombies = SummonedZombieAdventure.get()
    Zombotany = ZoboantyAdventure.get()
    Giga = GigaGargAdventure.get()
    mode = Wavemode.get()
    RandomizeActionRate = PlantAction.get()
    RandomizePlantDamage = PlantDamage.get()
    RandomizePlantHealth = PlantHealth.get()
    Randomize = AdventureModeSeedpackets.get()
    RandomizeStorePlants = StorePlants.get()
    PuffinNight1 = AdventureModeSeedpackets_DontRandomizedPuffSeedpacket.get()
    BalloonZombieCounter = BalloonZombieCounterCheck.get()
    InstalledviaGUI = True
    #
    disablegroup()
    exec(open("RandomizerInstaller.py").read())
    showinfo(
    title='Randomizer done',
    message= ("Successfully randomized the game. Press ok to exit"))
    exit()
def Help():
    clearConsole()
    print("Make sure you have the files from the windows phone version of Plants vs. Zombies")
    print("Put the game's Content folder into the same folder as the installer, don't replace the files that are already in the randomizer's Content folder")
    print("Put the game's LawnStrings .txt files (LawnStrings_XX.txt) and the .xml files into the randomizer's Content folder")
    print("Now click on the Randomize button.")
    print("Once it finishes randomizing, you can start setting up the game.")
    print("Open up the sln file with Visual Studio 2019")
    print("Build the PC port projects (Lawn_PCDX and Lawn_PCGL) (Android port is untested), build them again if a error occurs")
    print("and now you're ready to play the randomizer, choose one of the exe files you had compiled to play")


my_w = tk.Tk()
my_w.geometry("905x620") 
my_w.title("Plants Vs. Zombies Randomizer (PlantsVsZombies.net)")

#
SeedLabel = tk.Label(text="Seed Name")
SeedName = tk.Entry()
SeedNameEntry = tk.Entry(textvariable=SeedName)
SeedLabel.grid(row=4,column=2)
SeedNameEntry.grid(row=5,column=2)

#
Random_button = ttk.Button(
    my_w,
    text='Randomize',
    command=Randomize
)
Random_button.grid(row=6,column=2)

#
help_button = ttk.Button(
    my_w,
    text='Help',
    command=Help
)
help_button.grid(row=6,column=4)

#

ZombieLabel = tk.LabelFrame(my_w, text="Zombies")
ZombieLabel.grid(row=1,column=3, columnspan=5, pady=5)

#
WaveModes = ['vanilla', 'vanilla', 'randomized', 'randomized+', 'hard', 'fixed']
Wavemode = tk.StringVar()
Wavemode.set(WaveModes[0])
WaveModeLabel = tk.LabelFrame(ZombieLabel, text="Wave Mode:")
WaveModeLabel.grid(row=3,column=1)
dropdown = ttk.OptionMenu(
    WaveModeLabel,
    Wavemode,
    *WaveModes
)
dropdown.grid(row=3,column=1)
WaveModeRandomizedplusLabel = tk.LabelFrame(WaveModeLabel, text="Randomized+ Wave Options")
WaveModeRandomizedplusLabel.grid(row=4,column=1)
MinWavesLabel = tk.Label(WaveModeRandomizedplusLabel, text="Min waves")
MinWavesLabel.grid(row=2,column=1)
MinWaves = tk.Entry()
MinWavesEntry = tk.Entry(WaveModeRandomizedplusLabel, textvariable=MinWaves)
MinWavesEntry.grid(row=3,column=1)
MaxWavesLabel = tk.Label(WaveModeRandomizedplusLabel, text="Max waves")
MaxWavesLabel.grid(row=2,column=2)
MaxWaves = tk.Entry()
MaxWavesEntry = tk.Entry(WaveModeRandomizedplusLabel, textvariable=MaxWaves)
MaxWavesEntry.grid(row=3,column=2)

WaveModeFixedLabel = tk.LabelFrame(WaveModeLabel, text="Fixed waves")
WaveModeFixedLabel.grid(row=5,column=1)
FixedWaves = tk.Entry()
FixedWavesEntry = tk.Entry(WaveModeFixedLabel, textvariable=FixedWaves)
FixedWavesEntry.grid(row=4,column=2)


#
def switchButtonState():
    if (ZoboantyAdventure_c1['state'] == tk.NORMAL):
        ZoboantyAdventure_c1['state'] = tk.DISABLED
        ZoboantyAdventure.set('n')
        SummonedZombieAdventure_c1['state'] = tk.DISABLED
        SummonedZombieAdventure.set('n')
        GigaGargAdventure_c1['state'] = tk.DISABLED
        GigaGargAdventure.set('n')
        BalloonZombieCounterCheck_c1['state'] = tk.DISABLED
        BalloonZombieCounterCheck.set('n')
    else:
        SummonedZombieAdventure_c1['state'] = tk.NORMAL
        GigaGargAdventure_c1['state'] = tk.NORMAL
        ZoboantyAdventure_c1['state'] = tk.NORMAL
        BalloonZombieCounterCheck_c1['state'] = tk.NORMAL

def switchButtonStateT():
    if (AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1['state'] == tk.NORMAL):
        AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1['state'] = tk.DISABLED
        AdventureModeSeedpackets_matchseedpackets_c1['state'] = tk.DISABLED
        AdventureModeSeedpackets_DontRandomizedPuffSeedpacket.set('n')
        AdventureModeSeedpackets_matchseedpackets.set('n')
    else:
        AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1['state'] = tk.NORMAL
        AdventureModeSeedpackets_matchseedpackets_c1['state'] = tk.NORMAL

def switchButtonStateC():
    if (RandomizeCustomBackground_c1['state'] == tk.NORMAL):
        RandomizeCustomBackground_c1['state'] = tk.DISABLED
        RandomizeCustomBackground.set('n')
    else:
        RandomizeCustomBackground_c1['state'] = tk.NORMAL

def switchButtonStateB():
    if (ConveryorAll_c1['state'] == tk.NORMAL):
        ConveryorAll_c1['state'] = tk.DISABLED
        ConveryorAll.set('n')
    else:
        ConveryorAll_c1['state'] = tk.NORMAL

ZombieAdventure=tk.StringVar()
ZombieAdventure_c1 = tk.Checkbutton(ZombieLabel, text='Randomize zombie appearances in Adventure Mode', variable=ZombieAdventure,
	onvalue='y',offvalue='n', command = switchButtonState, state = tk.NORMAL)
ZombieAdventure_c1.grid(row=1,column=1) 
ZombieAdventure.set('n')

ZombieAdventureLabel = tk.LabelFrame(ZombieLabel, text="Zombie appearance Options")
ZombieAdventureLabel.grid(row=2,column=1, columnspan=4, pady=5)

ZoboantyAdventure=tk.StringVar()
ZoboantyAdventure_c1 = tk.Checkbutton(ZombieAdventureLabel, text='Include Zombotany zombies', variable=ZoboantyAdventure,
	onvalue='y',offvalue='n', state = tk.DISABLED)
ZoboantyAdventure_c1.grid(row=5,column=8) 
ZoboantyAdventure.set('n')

SummonedZombieAdventure=tk.StringVar()
SummonedZombieAdventure_c1 = tk.Checkbutton(ZombieAdventureLabel, text='Include Summoned zombies', variable=SummonedZombieAdventure,
	onvalue='y',offvalue='n', state = tk.DISABLED)
SummonedZombieAdventure_c1.grid(row=6,column=8) 
SummonedZombieAdventure.set('n')

GigaGargAdventure=tk.StringVar()
GigaGargAdventure_c1 = tk.Checkbutton(ZombieAdventureLabel, text='Include Giga Garguantuars', variable=GigaGargAdventure,
	onvalue='y',offvalue='n', state = tk.DISABLED)
GigaGargAdventure_c1.grid(row=7,column=8) 
GigaGargAdventure.set('n')

BalloonZombieCounterCheck=tk.StringVar()
BalloonZombieCounterCheck_c1 = tk.Checkbutton(ZombieAdventureLabel, text='Allow Balloon Zombie to spawn after his counter plant is unlocked.', variable=BalloonZombieCounterCheck,
	onvalue='y',offvalue='n', state = tk.DISABLED)
BalloonZombieCounterCheck_c1.grid(row=5,column=9) 
BalloonZombieCounterCheck.set('n')

CustomZombieAdventure=tk.StringVar()
CustomZombieAdventure_c1 = tk.Checkbutton(ZombieAdventureLabel, text='Include Custom Zombies', variable=CustomZombieAdventure,
	onvalue='y',offvalue='n', state = tk.DISABLED)
CustomZombieAdventure_c1.grid(row=6,column=9) 
CustomZombieAdventure.set('n')


PlantLabel = tk.LabelFrame(my_w, text="Plants")
PlantLabel.grid(row=1,column=1, columnspan=2, pady=5)

PlantSeedPacketLabel = tk.LabelFrame(PlantLabel, text="Randomize plant seedpackets")
PlantSeedPacketLabel.grid(row=1,column=1, columnspan=2, pady=5)

StorePlants=tk.StringVar()
StorePlants_c1 = tk.Checkbutton(PlantSeedPacketLabel, text='Shuffle the order of store plants', variable=StorePlants,
	onvalue='y',offvalue='n', state = tk.NORMAL)
StorePlants_c1.grid(row=5,column=1) 
StorePlants.set('n')

AdventureModeSeedpackets=tk.StringVar()
AdventureModeSeedpackets_c1 = tk.Checkbutton(PlantSeedPacketLabel, text='Randomize Adventure mode seedpacket awards', variable=AdventureModeSeedpackets,
	onvalue='y',offvalue='n', command = switchButtonStateT, state = tk.NORMAL)
AdventureModeSeedpackets_c1.grid(row=1,column=1) 
AdventureModeSeedpackets.set('n')

PlantAdventureSeedPacket = tk.LabelFrame(PlantSeedPacketLabel, text="Adventure mode seedpacket options")
PlantAdventureSeedPacket.grid(row=2,column=1, columnspan=2, pady=5)

AdventureModeSeedpackets_DontRandomizedPuffSeedpacket=tk.StringVar()
AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1 = tk.Checkbutton(PlantAdventureSeedPacket, text="Don't Randomize Puff-shroom's award seedpacket", variable=AdventureModeSeedpackets_DontRandomizedPuffSeedpacket,
	onvalue='y',offvalue='n', state = tk.DISABLED)
AdventureModeSeedpackets_DontRandomizedPuffSeedpacket_c1.grid(row=1,column=1) 
AdventureModeSeedpackets_DontRandomizedPuffSeedpacket.set('n')

AdventureModeSeedpackets_matchseedpackets=tk.StringVar()
AdventureModeSeedpackets_matchseedpackets_c1 = tk.Checkbutton(PlantAdventureSeedPacket, text="Don't change the seedpacket icons", variable=AdventureModeSeedpackets_matchseedpackets,
	onvalue='y',offvalue='n', state = tk.DISABLED)
AdventureModeSeedpackets_matchseedpackets_c1.grid(row=2,column=1) 
AdventureModeSeedpackets_matchseedpackets.set('n')

AdventureModeCustomSeedpackets=tk.StringVar()
AdventureModeCustomSeedpackets_cl = tk.Checkbutton(PlantAdventureSeedPacket, text="Include custom plants", variable=AdventureModeCustomSeedpackets,
	onvalue='y',offvalue='n', state = tk.DISABLED)
AdventureModeCustomSeedpackets_cl.grid(row=3,column=1) 
AdventureModeCustomSeedpackets.set('n')

Converyor=tk.StringVar()
Converyor_c1 = tk.Checkbutton(PlantSeedPacketLabel, text='Randomize seedpackets in conveyorbelt levels', variable=Converyor,
	onvalue='y',offvalue='n', command = switchButtonStateB, state = tk.NORMAL)
Converyor_c1.grid(row=3,column=1) 
Converyor.set('n')

ConveryorAll=tk.StringVar()
ConveryorAll_c1 = tk.Checkbutton(PlantSeedPacketLabel, text='Have almost all seedpackets in every conveyorbelt level', variable=ConveryorAll,
	onvalue='y',offvalue='n', state = tk.DISABLED)
ConveryorAll_c1.grid(row=4,column=1) 
ConveryorAll.set('n')

PlantStatsLabel = tk.LabelFrame(PlantLabel, text="Randomize Plant Stats")
PlantStatsLabel.grid(row=2,column=1, columnspan=2, pady=5)

DowngradePlants=tk.StringVar()
DowngradePlants_c1 = tk.Checkbutton(PlantStatsLabel, text='Randomize downgrade plants of upgrade plants', variable=DowngradePlants,
	onvalue='y',offvalue='n')
DowngradePlants_c1.grid(row=5,column=1) 
DowngradePlants.set('n')

PlantHealth=tk.StringVar()
PlantHealth_c1 = tk.Checkbutton(PlantStatsLabel, text='Randomize defensive plant health', variable=PlantHealth,
	onvalue='y',offvalue='n')
PlantHealth_c1.grid(row=6,column=1) 
PlantHealth.set('n')

PlantDamage=tk.StringVar()
PlantDamage_c1 = tk.Checkbutton(PlantStatsLabel, text='Randomize plant attack damage', variable=PlantDamage,
	onvalue='y',offvalue='n')
PlantDamage_c1.grid(row=7,column=1) 
PlantDamage.set('n')

PlantAction=tk.StringVar()
PlantAction_c1 = tk.Checkbutton(PlantStatsLabel, text='Randomize plant action rate', variable=PlantAction,
	onvalue='y',offvalue='n')
PlantAction_c1.grid(row=8,column=1) 
PlantAction.set('n')

#
MISCLabel = tk.LabelFrame(my_w, text="MISC")
MISCLabel.grid(row=2,column=1, columnspan=9, pady=4)

RandomizeBackgroundlabele = tk.LabelFrame(MISCLabel, text="Background randomizer (BETA)")
RandomizeBackgroundlabele.grid(row=2,column=1, columnspan=9, pady=4)

RandomizeBackgrounds=tk.StringVar()
RandomizeBackground_c1 = tk.Checkbutton(RandomizeBackgroundlabele, text='Randomize backgrounds per world in adventure mode', variable=RandomizeBackgrounds,
	onvalue='y',offvalue='n',  command = switchButtonStateC, state = tk.NORMAL)
RandomizeBackground_c1.grid(row=1,column=1) 
RandomizeBackgrounds.set('n')

Backgroundoptionslabel = tk.LabelFrame(RandomizeBackgroundlabele, text="Background randomizer Options")
Backgroundoptionslabel.grid(row=2,column=1, columnspan=2, pady=5)

RandomizeCustomBackground=tk.StringVar()
RandomizeCustomBackground_c1 = tk.Checkbutton(Backgroundoptionslabel, text='Include custom backgrounds', variable=RandomizeCustomBackground,
	onvalue='y',offvalue='n', state = tk.DISABLED)
RandomizeCustomBackground_c1.grid(row=2,column=1) 
RandomizeCustomBackground.set('n')

#
Sunmeta50=tk.StringVar()
Sunmeta_c1 = tk.Checkbutton(MISCLabel, text='50 sun meta', variable=Sunmeta50,
	onvalue='y',offvalue='n', state = tk.NORMAL)
Sunmeta_c1.grid(row=3,column=1) 
Sunmeta50.set('n')
#
my_w.mainloop() 
