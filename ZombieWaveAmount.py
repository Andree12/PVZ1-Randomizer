import random
try:
    mode
except NameError:
    mode = None
while mode != "hard" and mode != "randomized" and mode != "vanilla" and mode != "fixed" and mode != "randomized+":
 print("Select your zombie wave amount mode in adventure mode")
 print("")
 print("vanilla: retain the amount of waves in each adventure mode level the same")
 print("hard: the amount of waves in each adventure mode level are all 30")
 print("randomized: the amount of waves in each adventure mode level are all randomized")
 print("randomized+: Set the min amount and max amount of waves for each randomized level in adventure mode")
 print("fixed: Set a fixed amount of waves for every level in adventure mode")
 print("")
 print("Please note that this doesn't apply to the first three levels (as they are tutorial levels) and 1-5 to make sure the player passes through it")
 mode = input()

hardwaves = [ 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 30, 30, 30]
vanillawaves = [
            10, 10, 20, 10, 20, 20,
            10, 20, 10, 20, 10, 10, 20, 10, 20, 20,
            10, 20, 20, 30, 20, 20, 30, 20, 30, 30,
            10, 20, 10, 20, 10, 20, 10, 20, 20,
            10, 20, 20, 30, 20, 20, 30, 20, 30]

randomwaves = [10, 8, 20, 30]

if mode == "hard":
 selectedwaves = hardwaves

if mode == "vanilla":
 selectedwaves = vanillawaves

if mode == "fixed":
 selectedwaves = []
 try:
     amountofwaves
 except NameError:
    amountofwaves = input("Set a fixed wave amount to be applied to every adventure mode level >")
 i = 0
 while i <= 44:
   selectedwaves.append(amountofwaves)
   i+= 1
if mode == "randomized" or mode == "randomized+":
 random.seed(SeedNum)
 selectedwaves = []
 if mode == "randomized+":
     try:
         minwaves
         maxwaves
     except NameError:
         minwaves = int(input("Set the min amount of waves >"))
         maxwaves = int(input("Set the max amount of waves >"))
 while len(selectedwaves) != 44:
  if mode == "randomized+":
   waveamount = random.randint(minwaves, maxwaves)
  else:
   waveamount = random.choice(randomwaves)
  selectedwaves.append(waveamount)

##print(selectedwaves)
##print(len(selectedwaves))
listid = 0
print("Setting up zombie waves")
##while listid != len(selectedwaves):
## wavenumber = selectedwaves[listid]
## a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "r", encoding="utf-8")
## word = a_file.read()
## stringwavenumber = str(wavenumber)
## a_file = open("Lawn_Shared/Lawn/System/GameConstants.cs", "w", encoding="utf-8")
## replace_string = word.replace('randomwavenum', stringwavenumber, 1)
## a_file.write(replace_string)
## a_file.close()
## listid = listid + 1
from xml.etree import ElementTree as et
datafile = "RandomizerSettings.xml";
tree = et.parse(datafile)

tree.find(".//Level1_4_wavenum").text = str(selectedwaves[0])
tree.find(".//Level1_6_wavenum").text = str(selectedwaves[1])
tree.find(".//Level1_7_wavenum").text = str(selectedwaves[2])
tree.find(".//Level1_8_wavenum").text = str(selectedwaves[3])
tree.find(".//Level1_9_wavenum").text = str(selectedwaves[4])
tree.find(".//Level1_10_wavenum").text = str(selectedwaves[5])
tree.find(".//Level2_1_wavenum").text = str(selectedwaves[6])
tree.find(".//Level2_2_wavenum").text = str(selectedwaves[7])
tree.find(".//Level2_3_wavenum").text = str(selectedwaves[8])
tree.find(".//Level2_4_wavenum").text = str(selectedwaves[9])
tree.find(".//Level2_5_wavenum").text = str(selectedwaves[10])
tree.find(".//Level2_6_wavenum").text = str(selectedwaves[11])
tree.find(".//Level2_7_wavenum").text = str(selectedwaves[12])
tree.find(".//Level2_8_wavenum").text = str(selectedwaves[13])
tree.find(".//Level2_9_wavenum").text = str(selectedwaves[14])
tree.find(".//Level2_10_wavenum").text = str(selectedwaves[15])
tree.find(".//Level3_1_wavenum").text = str(selectedwaves[16])
tree.find(".//Level3_2_wavenum").text = str(selectedwaves[17])
tree.find(".//Level3_3_wavenum").text = str(selectedwaves[18])
tree.find(".//Level3_4_wavenum").text = str(selectedwaves[19])
tree.find(".//Level3_5_wavenum").text = str(selectedwaves[20])
tree.find(".//Level3_6_wavenum").text = str(selectedwaves[21])
tree.find(".//Level3_7_wavenum").text = str(selectedwaves[22])
tree.find(".//Level3_8_wavenum").text = str(selectedwaves[23])
tree.find(".//Level3_9_wavenum").text = str(selectedwaves[24])
tree.find(".//Level3_10_wavenum").text = str(selectedwaves[25])
tree.find(".//Level4_1_wavenum").text = str(selectedwaves[26])
tree.find(".//Level4_2_wavenum").text = str(selectedwaves[27])
tree.find(".//Level4_3_wavenum").text = str(selectedwaves[28])
tree.find(".//Level4_4_wavenum").text = str(selectedwaves[29])
tree.find(".//Level4_6_wavenum").text = str(selectedwaves[30])
tree.find(".//Level4_7_wavenum").text = str(selectedwaves[31])
tree.find(".//Level4_8_wavenum").text = str(selectedwaves[32])
tree.find(".//Level4_9_wavenum").text = str(selectedwaves[33])
tree.find(".//Level4_10_wavenum").text = str(selectedwaves[34])
tree.find(".//Level5_1_wavenum").text = str(selectedwaves[35])
tree.find(".//Level5_2_wavenum").text = str(selectedwaves[36])
tree.find(".//Level5_3_wavenum").text = str(selectedwaves[37])
tree.find(".//Level5_4_wavenum").text = str(selectedwaves[38])
tree.find(".//Level5_5_wavenum").text = str(selectedwaves[39])
tree.find(".//Level5_6_wavenum").text = str(selectedwaves[40])
tree.find(".//Level5_7_wavenum").text = str(selectedwaves[41])
tree.find(".//Level5_8_wavenum").text = str(selectedwaves[42])
tree.find(".//Level5_9_wavenum").text = str(selectedwaves[43])

tree.write(datafile)
print("Done")
