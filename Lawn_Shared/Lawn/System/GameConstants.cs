using System;
using Sexy;
using Sexy.TodLib;

namespace Lawn
{
    public/*internal*/ class GameConstants
    {
        public static void Init()
        {
            GameConstants.AchievementInfo = new Achievement[]
            {
                new Achievement(10223, "[ACHIEVEMENT_HOME_SECURITY_TITLE]", "[ACHIEVEMENT_HOME_SECURITY_DESCRIPTION]"),
                new Achievement(10224, "[ACHIEVEMENT_SPUDOW_TITLE]", "[ACHIEVEMENT_SPUDOW_DESCRIPTION]"),
                new Achievement(10225, "[ACHIEVEMENT_EXPLODONATOR_TITLE]", "[ACHIEVEMENT_EXPLODONATOR_DESCRIPTION]"),
                new Achievement(10226, "[ACHIEVEMENT_MORTICULTURALIST_TITLE]", "[ACHIEVEMENT_MORTICULTURALIST_DESCRIPTION]"),
                new Achievement(10227, "[ACHIEVEMENT_DONT_PEA_IN_POOL_TITLE]", "[ACHIEVEMENT_DONT_PEA_IN_POOL_DESCRIPTION]"),
                new Achievement(10228, "[ACHIEVEMENT_ROLL_SOME_HEADS_TITLE]", "[ACHIEVEMENT_ROLL_SOME_HEADS_DESCRIPTION]"),
                new Achievement(10229, "[ACHIEVEMENT_GROUNDED_TITLE]", "[ACHIEVEMENT_GROUNDED_DESCRIPTION]"),
                new Achievement(10230, "[ACHIEVEMENT_ZOMBOLOGIST_TITLE]", "[ACHIEVEMENT_ZOMBOLOGIST_DESCRIPTION]"),
                new Achievement(10231, "[ACHIEVEMENT_PENNY_PINCHER_TITLE]", "[ACHIEVEMENT_PENNY_PINCHER_DESCRIPTION]"),
                new Achievement(10232, "[ACHIEVEMENT_SUNNY_DAYS_TITLE]", "[ACHIEVEMENT_SUNNY_DAYS_DESCRIPTION]"),
                new Achievement(10233, "[ACHIEVEMENT_POPCORN_PARTY_TITLE]", "[ACHIEVEMENT_POPCORN_PARTY_DESCRIPTION]"),
                new Achievement(10234, "[ACHIEVEMENT_GOOD_MORNING_TITLE]", "[ACHIEVEMENT_GOOD_MORNING_DESCRIPTION]"),
                new Achievement(10235, "[ACHIEVEMENT_NO_FUNGUS_AMONG_US_TITLE]", "[ACHIEVEMENT_NO_FUNGUS_AMONG_US_DESCRIPTION]")
            };
            GameConstants.gLawnDialogColors = new int[,]
            {
                { 255,255,255 },
                { 255,255,0   },
                { 255,255,255 },
                { 255,255,255 },
                { 255,255,255 },
                { 80, 80, 80  },
                { 255,255,255 }
            };
            GameConstants.gLawnParticleArray = new ParticleParams[]
            {
                new ParticleParams(ParticleEffect.Melonsplash, "particles/melonimpact"),
                new ParticleParams(ParticleEffect.Wintermelon, "particles/WinterMelonImpact"),
                new ParticleParams(ParticleEffect.Fumecloud, "particles/FumeCloud"),
                new ParticleParams(ParticleEffect.Popcornsplash, "particles/PopcornSplash"),
                new ParticleParams(ParticleEffect.Powie, "particles/Powie"),
                new ParticleParams(ParticleEffect.Jackexplode, "particles/JackExplode"),
                new ParticleParams(ParticleEffect.ZombieHead, "particles/ZombieHead"),
                new ParticleParams(ParticleEffect.ZombieArm, "particles/ZombieArm"),
                new ParticleParams(ParticleEffect.ZombieTrafficCone, "particles/ZombieTrafficCone"),
                new ParticleParams(ParticleEffect.ZombiePail, "particles/ZombiePail"),
                new ParticleParams(ParticleEffect.ZombieHelmet, "particles/ZombieHelmet"),
                new ParticleParams(ParticleEffect.ZombieFlag, "particles/ZombieFlag"),
                new ParticleParams(ParticleEffect.ZombieDoor, "particles/ZombieDoor"),
                new ParticleParams(ParticleEffect.ZombieNewspaper, "particles/ZombieNewspaper"),
                new ParticleParams(ParticleEffect.ZombieHeadlight, "particles/ZombieHeadLight"),
                new ParticleParams(ParticleEffect.Pow, "particles/Pow"),
                new ParticleParams(ParticleEffect.ZombiePogo, "particles/ZombiePogo"),
                new ParticleParams(ParticleEffect.ZombieNewspaperHead, "particles/ZombieNewspaperHead"),
                new ParticleParams(ParticleEffect.ZombieBalloonHead, "particles/ZombieBalloonHead"),
                new ParticleParams(ParticleEffect.SodRoll, "particles/SodRoll"),
                new ParticleParams(ParticleEffect.GraveStoneRise, "particles/GraveStoneRise"),
                new ParticleParams(ParticleEffect.Planting, "particles/Planting"),
                new ParticleParams(ParticleEffect.PlantingPool, "particles/PlantingPool"),
                new ParticleParams(ParticleEffect.ZombieRise, "particles/ZombieRise"),
                new ParticleParams(ParticleEffect.GraveBuster, "particles/GraveBuster"),
                new ParticleParams(ParticleEffect.GraveBusterDie, "particles/GraveBusterDie"),
                new ParticleParams(ParticleEffect.PoolSplash, "particles/PoolSplash"),
                new ParticleParams(ParticleEffect.IceSparkle, "particles/IceSparkle"),
                new ParticleParams(ParticleEffect.SeedPacket, "particles/SeedPacket"),
                new ParticleParams(ParticleEffect.TallNutBlock, "particles/TallNutBlock"),
                new ParticleParams(ParticleEffect.Doom, "particles/Doom"),
                new ParticleParams(ParticleEffect.DiggerRise, "particles/DiggerRise"),
                new ParticleParams(ParticleEffect.DiggerTunnel, "particles/DiggerTunnel"),
                new ParticleParams(ParticleEffect.DancerRise, "particles/DancerRise"),
                new ParticleParams(ParticleEffect.PoolSparkly, "particles/PoolSparkly"),
                new ParticleParams(ParticleEffect.WallnutEatSmall, "particles/WallnutEatSmall"),
                new ParticleParams(ParticleEffect.WallnutEatLarge, "particles/WallnutEatLarge"),
                new ParticleParams(ParticleEffect.PeaSplat, "particles/PeaSplat"),
                new ParticleParams(ParticleEffect.ButterSplat, "particles/ButterSplat"),
                new ParticleParams(ParticleEffect.CabbageSplat, "particles/CabbageSplat"),
                new ParticleParams(ParticleEffect.PuffSplat, "particles/PuffSplat"),
                new ParticleParams(ParticleEffect.StarSplat, "particles/StarSplat"),
                new ParticleParams(ParticleEffect.IceTrap, "particles/IceTrap"),
                new ParticleParams(ParticleEffect.SnowpeaSplat, "particles/SnowPeaSplat"),
                new ParticleParams(ParticleEffect.SnowpeaPuff, "particles/SnowPeaPuff"),
                new ParticleParams(ParticleEffect.SnowpeaTrail, "particles/SnowPeaTrail"),
                new ParticleParams(ParticleEffect.LanternShine, "particles/LanternShine"),
                new ParticleParams(ParticleEffect.SeedPacketPickup, "particles/Award"),
                new ParticleParams(ParticleEffect.PotatoMine, "particles/PotatoMine"),
                new ParticleParams(ParticleEffect.PotatoMineRise, "particles/PotatoMineRise"),
                new ParticleParams(ParticleEffect.PuffshroomTrail, "particles/PuffShroomTrail"),
                new ParticleParams(ParticleEffect.PuffshroomMuzzle, "particles/PuffShroomMuzzle"),
                new ParticleParams(ParticleEffect.SeedPacketFlash, "particles/SeedPacketFlash"),
                new ParticleParams(ParticleEffect.WhackAZombieRise, "particles/WhackAZombieRise"),
                new ParticleParams(ParticleEffect.ZombieLadder, "particles/ZombieLadder"),
                new ParticleParams(ParticleEffect.UmbrellaReflect, "particles/UmbrellaReflect"),
                new ParticleParams(ParticleEffect.SeedPacketPick, "particles/SeedPacketPick"),
                new ParticleParams(ParticleEffect.IceTrapZombie, "particles/IceTrapZombie"),
                new ParticleParams(ParticleEffect.IceTrapRelease, "particles/IceTrapRelease"),
                new ParticleParams(ParticleEffect.ZamboniSmoke, "particles/ZamboniSmoke"),
                new ParticleParams(ParticleEffect.Gloomcloud, "particles/GloomCloud"),
                new ParticleParams(ParticleEffect.ZombiePogoHead, "particles/ZombiePogoHead"),
                new ParticleParams(ParticleEffect.ZamboniTire, "particles/ZamboniTire"),
                new ParticleParams(ParticleEffect.ZamboniExplosion, "particles/ZamboniExplosion"),
                new ParticleParams(ParticleEffect.ZamboniExplosion2, "particles/ZamboniExplosion2"),
                new ParticleParams(ParticleEffect.CatapultExplosion, "particles/CatapultExplosion"),
                new ParticleParams(ParticleEffect.MowerCloud, "particles/MowerCloud"),
                new ParticleParams(ParticleEffect.BossIceBall, "particles/BossIceBallTrail"),
                new ParticleParams(ParticleEffect.Blastmark, "particles/BlastMark"),
                new ParticleParams(ParticleEffect.CoinPickupArrow, "particles/CoinPickupArrow"),
                new ParticleParams(ParticleEffect.PresentPickup, "particles/PresentPickup"),
                new ParticleParams(ParticleEffect.ImitaterMorph, "particles/ImitaterMorph"),
                new ParticleParams(ParticleEffect.MoweredZombieHead, "particles/MoweredZombieHead"),
                new ParticleParams(ParticleEffect.MoweredZombieArm, "particles/MoweredZombieArm"),
                new ParticleParams(ParticleEffect.ZombieHeadPool, "particles/ZombieHeadPool"),
                new ParticleParams(ParticleEffect.ZombieBossFireball, "particles/Zombie_boss_fireball"),
                new ParticleParams(ParticleEffect.FireballDeath, "particles/FireBallDeath"),
                new ParticleParams(ParticleEffect.IceballDeath, "particles/IceBallDeath"),
                new ParticleParams(ParticleEffect.IceballTrail, "particles/Iceball_Trail"),
                new ParticleParams(ParticleEffect.FireballTrail, "particles/Fireball_Trail"),
                new ParticleParams(ParticleEffect.BossExplosion, "particles/BossExplosion"),
                new ParticleParams(ParticleEffect.ScreenFlash, "particles/ScreenFlash"),
                new ParticleParams(ParticleEffect.TrophySparkle, "particles/TrophySparkle"),
                new ParticleParams(ParticleEffect.PortalCircle, "particles/PortalCircle"),
                new ParticleParams(ParticleEffect.PortalSquare, "particles/PortalSquare"),
                new ParticleParams(ParticleEffect.PottedPlantGlow, "particles/PottedPlantGlow"),
                new ParticleParams(ParticleEffect.PottedWaterPlantGlow, "particles/PottedWaterPlantGlow"),
                new ParticleParams(ParticleEffect.PottedZenGlow, "particles/PottedZenGlow"),
                new ParticleParams(ParticleEffect.MindControl, "particles/MindControl"),
                new ParticleParams(ParticleEffect.VaseShatter, "particles/VaseShatter"),
                new ParticleParams(ParticleEffect.VaseShatterLeaf, "particles/VaseShatterLeaf"),
                new ParticleParams(ParticleEffect.VaseShatterZombie, "particles/VaseShatterZombie"),
                new ParticleParams(ParticleEffect.AwardPickupArrow, "particles/AwardPickupArrow"),
                new ParticleParams(ParticleEffect.ZombieSeaweed, "particles/Zombie_seaweed"),
                new ParticleParams(ParticleEffect.ZombieMustache, "particles/ZombieMustache"),
                new ParticleParams(ParticleEffect.ZombieFutureGlasses, "particles/ZombieFutureGlasses"),
                new ParticleParams(ParticleEffect.Pinata, "particles/Pinata"),
                new ParticleParams(ParticleEffect.DustSquash, "particles/Dust_Squash"),
                new ParticleParams(ParticleEffect.DustFoot, "particles/Dust_Foot"),
                new ParticleParams(ParticleEffect.Daisy, "particles/Daisy"),
                new ParticleParams(ParticleEffect.Starburst, "particles/Starburst"),
                new ParticleParams(ParticleEffect.UpsellArrow, "particles/UpsellArrow")
            };
            GameConstants.gLawnReanimationArray = new ReanimationParams[]
            {
                new ReanimationParams(ReanimationType.LoadbarSprout, "reanim/LoadBar_sprout", 1),
                new ReanimationParams(ReanimationType.LoadbarZombiehead, "reanim/LoadBar_Zombiehead", 1),
                new ReanimationParams(ReanimationType.Sodroll, "reanim/SodRoll", 0),
                new ReanimationParams(ReanimationType.FinalWave, "reanim/FinalWave", 1),
                new ReanimationParams(ReanimationType.Peashooter, "reanim/PeaShooterSingle", 0),
                new ReanimationParams(ReanimationType.Wallnut, "reanim/Wallnut", 0),
                new ReanimationParams(ReanimationType.Lilypad, "reanim/LilyPad", 0),
                new ReanimationParams(ReanimationType.Sunflower, "reanim/SunFlower", 0),
                new ReanimationParams(ReanimationType.Lawnmower, "reanim/LawnMower", 0),
                new ReanimationParams(ReanimationType.Readysetplant, "reanim/StartReadySetPlant", 1),
                new ReanimationParams(ReanimationType.Cherrybomb, "reanim/CherryBomb", 0),
                new ReanimationParams(ReanimationType.Squash, "reanim/Squash", 0),
                new ReanimationParams(ReanimationType.Doomshroom, "reanim/DoomShroom", 0),
                new ReanimationParams(ReanimationType.Snowpea, "reanim/SnowPea", 0),
                new ReanimationParams(ReanimationType.Repeater, "reanim/PeaShooter", 0),
                new ReanimationParams(ReanimationType.Sunshroom, "reanim/SunShroom", 0),
                new ReanimationParams(ReanimationType.Tallnut, "reanim/Tallnut", 0),
                new ReanimationParams(ReanimationType.Fumeshroom, "reanim/FumeShroom", 0),
                new ReanimationParams(ReanimationType.Puffshroom, "reanim/PuffShroom", 0),
                new ReanimationParams(ReanimationType.Hypnoshroom, "reanim/HypnoShroom", 0),
                new ReanimationParams(ReanimationType.Chomper, "reanim/Chomper", 0),
                new ReanimationParams(ReanimationType.Zombie, "reanim/Zombie", 0),
                new ReanimationParams(ReanimationType.Sun, "reanim/Sun", 0),
                new ReanimationParams(ReanimationType.Potatomine, "reanim/PotatoMine", 0),
                new ReanimationParams(ReanimationType.Spikeweed, "reanim/Caltrop", 0),
                new ReanimationParams(ReanimationType.Spikerock, "reanim/SpikeRock", 0),
                new ReanimationParams(ReanimationType.Threepeater, "reanim/ThreePeater", 0),
                new ReanimationParams(ReanimationType.Marigold, "reanim/Marigold", 0),
                new ReanimationParams(ReanimationType.Iceshroom, "reanim/IceShroom", 0),
                new ReanimationParams(ReanimationType.ZombieFootball, "reanim/Zombie_football", 0),
                new ReanimationParams(ReanimationType.ZombieNewspaper, "reanim/Zombie_paper", 0),
                new ReanimationParams(ReanimationType.ZombieZamboni, "reanim/Zombie_zamboni", 0),
                new ReanimationParams(ReanimationType.Splash, "reanim/splash", 0),
                new ReanimationParams(ReanimationType.Jalapeno, "reanim/Jalapeno", 0),
                new ReanimationParams(ReanimationType.JalapenoFire, "reanim/fire", 0),
                new ReanimationParams(ReanimationType.CoinSilver, "reanim/Coin_silver", 0),
                new ReanimationParams(ReanimationType.ZombieCharred, "reanim/Zombie_charred", 0),
                new ReanimationParams(ReanimationType.ZombieCharredImp, "reanim/Zombie_charred_imp", 0),
                new ReanimationParams(ReanimationType.ZombieCharredDigger, "reanim/Zombie_charred_digger", 0),
                new ReanimationParams(ReanimationType.ZombieCharredZamboni, "reanim/Zombie_charred_zamboni", 0),
                new ReanimationParams(ReanimationType.ZombieCharredCatapult, "reanim/Zombie_charred_catapult", 0),
                new ReanimationParams(ReanimationType.ZombieCharredGargantuar, "reanim/Zombie_charred_gargantuar", 0),
                new ReanimationParams(ReanimationType.Scrareyshroom, "reanim/ScaredyShroom", 0),
                new ReanimationParams(ReanimationType.Pumpkin, "reanim/Pumpkin", 0),
                new ReanimationParams(ReanimationType.Plantern, "reanim/Plantern", 0),
                new ReanimationParams(ReanimationType.Torchwood, "reanim/Torchwood", 0),
                new ReanimationParams(ReanimationType.Splitpea, "reanim/SplitPea", 0),
                new ReanimationParams(ReanimationType.Seashroom, "reanim/SeaShroom", 0),
                new ReanimationParams(ReanimationType.Blover, "reanim/Blover", 0),
                new ReanimationParams(ReanimationType.FlowerPot, "reanim/Pot", 0),
                new ReanimationParams(ReanimationType.Cactus, "reanim/Cactus", 0),
                new ReanimationParams(ReanimationType.Disco, "reanim/Zombie_disco", 0),
                new ReanimationParams(ReanimationType.Tanglekelp, "reanim/Tanglekelp", 0),
                new ReanimationParams(ReanimationType.Starfruit, "reanim/Starfruit", 0),
                new ReanimationParams(ReanimationType.Polevaulter, "reanim/Zombie_polevaulter", 0),
                new ReanimationParams(ReanimationType.Balloon, "reanim/Zombie_balloon", 0),
                new ReanimationParams(ReanimationType.Gargantuar, "reanim/Zombie_gargantuar", 0),
                new ReanimationParams(ReanimationType.Imp, "reanim/Zombie_imp", 0),
                new ReanimationParams(ReanimationType.Digger, "reanim/Zombie_digger", 0),
                new ReanimationParams(ReanimationType.DiggerDirt, "reanim/Digger_rising_dirt", 0),
                new ReanimationParams(ReanimationType.ZombieDolphinrider, "reanim/Zombie_dolphinrider", 0),
                new ReanimationParams(ReanimationType.Pogo, "reanim/Zombie_pogo", 0),
                new ReanimationParams(ReanimationType.BackupDancer, "reanim/Zombie_backup", 0),
                new ReanimationParams(ReanimationType.Bobsled, "reanim/Zombie_bobsled", 0),
                new ReanimationParams(ReanimationType.Jackinthebox, "reanim/Zombie_jackbox", 0),
                new ReanimationParams(ReanimationType.Snorkel, "reanim/Zombie_snorkle", 0),
                new ReanimationParams(ReanimationType.Bungee, "reanim/Zombie_bungi", 0),
                new ReanimationParams(ReanimationType.Catapult, "reanim/Zombie_catapult", 0),
                new ReanimationParams(ReanimationType.Ladder, "reanim/Zombie_ladder", 0),
                new ReanimationParams(ReanimationType.Puff, "reanim/Puff", 0),
                new ReanimationParams(ReanimationType.Sleeping, "reanim/Z", 0),
                new ReanimationParams(ReanimationType.GraveBuster, "reanim/Gravebuster", 0),
                new ReanimationParams(ReanimationType.ZombiesWon, "reanim/ZombiesWon", 1),
                new ReanimationParams(ReanimationType.Magnetshroom, "reanim/Magnetshroom", 0),
                new ReanimationParams(ReanimationType.Boss, "reanim/Zombie_boss", 1),
                new ReanimationParams(ReanimationType.Cabbagepult, "reanim/Cabbagepult", 0),
                new ReanimationParams(ReanimationType.Kernelpult, "reanim/Cornpult", 0),
                new ReanimationParams(ReanimationType.Melonpult, "reanim/Melonpult", 0),
                new ReanimationParams(ReanimationType.Coffeebean, "reanim/Coffeebean", 1),
                new ReanimationParams(ReanimationType.Umbrellaleaf, "reanim/Umbrellaleaf", 0),
                new ReanimationParams(ReanimationType.Gatlingpea, "reanim/GatlingPea", 0),
                new ReanimationParams(ReanimationType.Cattail, "reanim/Cattail", 0),
                new ReanimationParams(ReanimationType.Gloomshroom, "reanim/GloomShroom", 0),
                new ReanimationParams(ReanimationType.BossIceball, "reanim/Zombie_boss_iceball", 1),
                new ReanimationParams(ReanimationType.BossFireball, "reanim/Zombie_boss_fireball", 1),
                new ReanimationParams(ReanimationType.Cobcannon, "reanim/CobCannon", 0),
                new ReanimationParams(ReanimationType.Garlic, "reanim/Garlic", 0),
                new ReanimationParams(ReanimationType.GoldMagnet, "reanim/GoldMagnet", 0),
                new ReanimationParams(ReanimationType.WinterMelon, "reanim/WinterMelon", 0),
                new ReanimationParams(ReanimationType.TwinSunflower, "reanim/TwinSunflower", 0),
                new ReanimationParams(ReanimationType.PoolCleaner, "reanim/PoolCleaner", 0),
                new ReanimationParams(ReanimationType.RoofCleaner, "reanim/RoofCleaner", 0),
                new ReanimationParams(ReanimationType.FirePea, "reanim/FirePea", 0),
                new ReanimationParams(ReanimationType.Imitater, "reanim/Imitater", 0),
                new ReanimationParams(ReanimationType.Yeti, "reanim/Zombie_yeti", 0),
                new ReanimationParams(ReanimationType.BossDriver, "reanim/Zombie_Boss_driver", 0),
                new ReanimationParams(ReanimationType.LawnMoweredZombie, "reanim/LawnMoweredZombie", 0),
                new ReanimationParams(ReanimationType.CrazyDave, "reanim/CrazyDave", 1),
                new ReanimationParams(ReanimationType.TextFadeOn, "reanim/TextFadeOn", 0),
                new ReanimationParams(ReanimationType.Hammer, "reanim/Hammer", 0),
                new ReanimationParams(ReanimationType.SlotMachineHandle, "reanim/SlotMachine", 0),
                new ReanimationParams(ReanimationType.SelectorScreen, "reanim/SelectorScreen", 3),
                new ReanimationParams(ReanimationType.PortalCircle, "reanim/Portal_Circle", 0),
                new ReanimationParams(ReanimationType.PortalSquare, "reanim/Portal_Square", 0),
                new ReanimationParams(ReanimationType.ZengardenSprout, "reanim/ZenGarden_sprout", 0),
                new ReanimationParams(ReanimationType.ZengardenWateringcan, "reanim/ZenGarden_wateringcan", 1),
                new ReanimationParams(ReanimationType.ZengardenFertilizer, "reanim/ZenGarden_fertilizer", 1),
                new ReanimationParams(ReanimationType.ZengardenBugspray, "reanim/ZenGarden_bugspray", 1),
                new ReanimationParams(ReanimationType.ZengardenPhonograph, "reanim/ZenGarden_phonograph", 1),
                new ReanimationParams(ReanimationType.Diamond, "reanim/Diamond", 0),
                new ReanimationParams(ReanimationType.Stinky, "reanim/Stinky", 0),
                new ReanimationParams(ReanimationType.Rake, "reanim/Rake", 0),
                new ReanimationParams(ReanimationType.RainCircle, "reanim/Rain_circle", 0),
                new ReanimationParams(ReanimationType.RainSplash, "reanim/Rain_splash", 0),
                new ReanimationParams(ReanimationType.ZombieSurprise, "reanim/Zombie_surprise", 0),
                new ReanimationParams(ReanimationType.CoinGold, "reanim/Coin_gold", 0),
                new ReanimationParams(ReanimationType.ZombieFlagpole, "reanim/Zombie_flagpole"),
                new ReanimationParams(ReanimationType.Woodsign, "reanim/woodsign"),
                new ReanimationParams(ReanimationType.Astronaut, "reanim/astronaut"),
            };
            GameConstants.gLawnTrailArray = new TrailParams[]
            {
                new TrailParams(TrailType.Ice, "particles/IceTrail")
            };
            GameConstants.gLawnStringFormats = new TodStringListFormat[]
            {
                new TodStringListFormat("NORMAL", null, new SexyColor(40, 50, 90), 0, 0U),
                new TodStringListFormat("FLAVOR", null, new SexyColor(143, 67, 27), 0, 1U),
                new TodStringListFormat("KEYWORD", null, new SexyColor(143, 67, 27), 0, 0U),
                new TodStringListFormat("NOCTURNAL", null, new SexyColor(136, 50, 170), 0, 0U),
                new TodStringListFormat("AQUATIC", null, new SexyColor(10, 151, 216), 0, 0U),
                new TodStringListFormat("STAT", null, new SexyColor(204, 36, 29), 0, 0U),
                new TodStringListFormat("METAL", null, new SexyColor(204, 36, 29), 0, 2U),
                new TodStringListFormat("KEYMETAL", null, new SexyColor(143, 67, 27), 0, 2U),
                new TodStringListFormat("SHORTLINE", null, new SexyColor(0, 0, 0, 0), 0, 0U),
                new TodStringListFormat("EXTRASHORTLINE", null, new SexyColor(0, 0, 0, 0), -14, 0U),
                new TodStringListFormat("CREDITS1", null, new SexyColor(0, 0, 0, 0), 3, 0U),
                new TodStringListFormat("CREDITS2", null, new SexyColor(0, 0, 0, 0), 2, 0U)
            };
            GameConstants.gLawnStringFormatCount = GameConstants.gLawnStringFormats.Length;
        }

        public static int GetRectOverlap(TRect rect1, TRect rect2)
        {
            int num;
            int aX2;
            int num2;
            if (rect1.mX < rect2.mX)
            {
                int aX = rect1.mX;
                num = rect1.mX + rect1.mWidth;
                aX2 = rect2.mX;
                num2 = rect2.mX + rect2.mWidth;
            }
            else
            {
                int aX3 = rect2.mX;
                num = rect2.mX + rect2.mWidth;
                aX2 = rect1.mX;
                num2 = rect1.mX + rect1.mWidth;
            }
            if (num <= aX2)
            {
                return num - aX2;
            }
            if (num <= num2)
            {
                return num - aX2;
            }
            return num2 - aX2;
        }

        public static bool GetCircleRectOverlap(int theCircleX, int theCircleY, int theRadius, TRect theRect)
        {
            bool flag = false;
            bool flag2 = false;
            int num = 0;
            int num2 = 0;
            if (theCircleX < theRect.mX)
            {
                flag = true;
                num = theRect.mX - theCircleX;
            }
            else if (theCircleX > theRect.mX + theRect.mWidth)
            {
                flag = true;
                num = theCircleX - theRect.mX - theRect.mWidth;
            }
            if (theCircleY < theRect.mY)
            {
                flag2 = true;
                num2 = theRect.mY - theCircleY;
            }
            else if (theCircleY > theRect.mY + theRect.mHeight)
            {
                flag2 = true;
                num2 = theCircleY - theRect.mY - theRect.mHeight;
            }
            if (!flag2 && !flag)
            {
                return true;
            }
            if (flag && flag2)
            {
                int num3 = num * num + num2 * num2;
                return num3 <= theRadius * theRadius;
            }
            if (flag)
            {
                return num <= theRadius;
            }
            return num2 <= theRadius;
        }

        // Note: this type is marked as 'beforefieldinit'.
        static GameConstants()
        {
            // 冒险关卡出怪
            GameConstants.gZombieAllowedLevels = new ZombieAllowedLevels[(int)ZombieType.ZombieTypesCount]
            {
                /*                    | ZombieType 枚举值 | 允许的关卡(1为允许、0为不允许) | */
                new ZombieAllowedLevels(ZombieType.Normal, new int[NUM_LEVELS]
                {
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                }),
                new ZombieAllowedLevels(ZombieType.Flag, new int[NUM_LEVELS]
                {
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                }),
                new ZombieAllowedLevels(ZombieType.TrafficCone, new int[NUM_LEVELS]
                {
                    0, 0, 1, XmlReader.Conehead_Level1_4, XmlReader.Conehead_Level1_5, XmlReader.Conehead_Level1_6, XmlReader.Conehead_Level1_7, XmlReader.Conehead_Level1_8, XmlReader.Conehead_Level1_9, XmlReader.Conehead_Level1_10,
                    XmlReader.Conehead_Level2_1, XmlReader.Conehead_Level2_2, XmlReader.Conehead_Level2_3, XmlReader.Conehead_Level2_4, XmlReader.Conehead_Level2_5, XmlReader.Conehead_Level2_6, XmlReader.Conehead_Level2_7, XmlReader.Conehead_Level2_8, XmlReader.Conehead_Level2_9, XmlReader.Conehead_Level2_10,
                    XmlReader.Conehead_Level3_1, XmlReader.Conehead_Level3_2, XmlReader.Conehead_Level3_3, XmlReader.Conehead_Level3_4, XmlReader.Conehead_Level3_5, XmlReader.Conehead_Level3_6, XmlReader.Conehead_Level3_7, XmlReader.Conehead_Level3_8, XmlReader.Conehead_Level3_9, XmlReader.Conehead_Level3_10,
                    XmlReader.Conehead_Level4_1, XmlReader.Conehead_Level4_2, XmlReader.Conehead_Level4_3, XmlReader.Conehead_Level4_4, 0, XmlReader.Conehead_Level4_6, XmlReader.Conehead_Level4_7, XmlReader.Conehead_Level4_8, XmlReader.Conehead_Level4_9, XmlReader.Conehead_Level4_10,
                    XmlReader.Conehead_Level5_1, XmlReader.Conehead_Level5_2, XmlReader.Conehead_Level5_3, XmlReader.Conehead_Level5_4, XmlReader.Conehead_Level5_5, XmlReader.Conehead_Level5_6, XmlReader.Conehead_Level5_7, XmlReader.Conehead_Level5_8, XmlReader.Conehead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Polevaulter, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Polevaulter_Level1_4, XmlReader.Polevaulter_Level1_5, XmlReader.Polevaulter_Level1_6, XmlReader.Polevaulter_Level1_7, XmlReader.Polevaulter_Level1_8, XmlReader.Polevaulter_Level1_9, XmlReader.Polevaulter_Level1_10,
                    XmlReader.Polevaulter_Level2_1, XmlReader.Polevaulter_Level2_2, XmlReader.Polevaulter_Level2_3, XmlReader.Polevaulter_Level2_4, XmlReader.Polevaulter_Level2_5, XmlReader.Polevaulter_Level2_6, XmlReader.Polevaulter_Level2_7, XmlReader.Polevaulter_Level2_8, XmlReader.Polevaulter_Level2_9, XmlReader.Polevaulter_Level2_10,
                    XmlReader.Polevaulter_Level3_1, XmlReader.Polevaulter_Level3_2, XmlReader.Polevaulter_Level3_3, XmlReader.Polevaulter_Level3_4, XmlReader.Polevaulter_Level3_5, XmlReader.Polevaulter_Level3_6, XmlReader.Polevaulter_Level3_7, XmlReader.Polevaulter_Level3_8, XmlReader.Polevaulter_Level3_9, XmlReader.Polevaulter_Level3_10,
                    XmlReader.Polevaulter_Level4_1, XmlReader.Polevaulter_Level4_2, XmlReader.Polevaulter_Level4_3, XmlReader.Polevaulter_Level4_4, 0, XmlReader.Polevaulter_Level4_6, XmlReader.Polevaulter_Level4_7, XmlReader.Polevaulter_Level4_8, XmlReader.Polevaulter_Level4_9, XmlReader.Polevaulter_Level4_10,
                    XmlReader.Polevaulter_Level5_1, XmlReader.Polevaulter_Level5_2, XmlReader.Polevaulter_Level5_3, XmlReader.Polevaulter_Level5_4, XmlReader.Polevaulter_Level5_5, XmlReader.Polevaulter_Level5_6, XmlReader.Polevaulter_Level5_7, XmlReader.Polevaulter_Level5_8, XmlReader.Polevaulter_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Pail, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Pail_Level1_4, XmlReader.Pail_Level1_5, XmlReader.Pail_Level1_6, XmlReader.Pail_Level1_7, XmlReader.Pail_Level1_8, XmlReader.Pail_Level1_9, XmlReader.Pail_Level1_10,
                    XmlReader.Pail_Level2_1, XmlReader.Pail_Level2_2, XmlReader.Pail_Level2_3, XmlReader.Pail_Level2_4, XmlReader.Pail_Level2_5, XmlReader.Pail_Level2_6, XmlReader.Pail_Level2_7, XmlReader.Pail_Level2_8, XmlReader.Pail_Level2_9, XmlReader.Pail_Level2_10,
                    XmlReader.Pail_Level3_1, XmlReader.Pail_Level3_2, XmlReader.Pail_Level3_3, XmlReader.Pail_Level3_4, XmlReader.Pail_Level3_5, XmlReader.Pail_Level3_6, XmlReader.Pail_Level3_7, XmlReader.Pail_Level3_8, XmlReader.Pail_Level3_9, XmlReader.Pail_Level3_10,
                    XmlReader.Pail_Level4_1, XmlReader.Pail_Level4_2, XmlReader.Pail_Level4_3, XmlReader.Pail_Level4_4, 0, XmlReader.Pail_Level4_6, XmlReader.Pail_Level4_7, XmlReader.Pail_Level4_8, XmlReader.Pail_Level4_9, XmlReader.Pail_Level4_10,
                    XmlReader.Pail_Level5_1, XmlReader.Pail_Level5_2, XmlReader.Pail_Level5_3, XmlReader.Pail_Level5_4, XmlReader.Pail_Level5_5, XmlReader.Pail_Level5_6, XmlReader.Pail_Level5_7, XmlReader.Pail_Level5_8, XmlReader.Pail_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Newspaper, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Newspaper_Level1_4, XmlReader.Newspaper_Level1_5, XmlReader.Newspaper_Level1_6, XmlReader.Newspaper_Level1_7, XmlReader.Newspaper_Level1_8, XmlReader.Newspaper_Level1_9, XmlReader.Newspaper_Level1_10,
                    XmlReader.Newspaper_Level2_1, XmlReader.Newspaper_Level2_2, XmlReader.Newspaper_Level2_3, XmlReader.Newspaper_Level2_4, XmlReader.Newspaper_Level2_5, XmlReader.Newspaper_Level2_6, XmlReader.Newspaper_Level2_7, XmlReader.Newspaper_Level2_8, XmlReader.Newspaper_Level2_9, XmlReader.Newspaper_Level2_10,
                    XmlReader.Newspaper_Level3_1, XmlReader.Newspaper_Level3_2, XmlReader.Newspaper_Level3_3, XmlReader.Newspaper_Level3_4, XmlReader.Newspaper_Level3_5, XmlReader.Newspaper_Level3_6, XmlReader.Newspaper_Level3_7, XmlReader.Newspaper_Level3_8, XmlReader.Newspaper_Level3_9, XmlReader.Newspaper_Level3_10,
                    XmlReader.Newspaper_Level4_1, XmlReader.Newspaper_Level4_2, XmlReader.Newspaper_Level4_3, XmlReader.Newspaper_Level4_4, 0, XmlReader.Newspaper_Level4_6, XmlReader.Newspaper_Level4_7, XmlReader.Newspaper_Level4_8, XmlReader.Newspaper_Level4_9, XmlReader.Newspaper_Level4_10,
                    XmlReader.Newspaper_Level5_1, XmlReader.Newspaper_Level5_2, XmlReader.Newspaper_Level5_3, XmlReader.Newspaper_Level5_4, XmlReader.Newspaper_Level5_5, XmlReader.Newspaper_Level5_6, XmlReader.Newspaper_Level5_7, XmlReader.Newspaper_Level5_8, XmlReader.Newspaper_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Door, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Door_Level1_4, XmlReader.Door_Level1_5, XmlReader.Door_Level1_6, XmlReader.Door_Level1_7, XmlReader.Door_Level1_8, XmlReader.Door_Level1_9, XmlReader.Door_Level1_10,
                    XmlReader.Door_Level2_1, XmlReader.Door_Level2_2, XmlReader.Door_Level2_3, XmlReader.Door_Level2_4, XmlReader.Door_Level2_5, XmlReader.Door_Level2_6, XmlReader.Door_Level2_7, XmlReader.Door_Level2_8, XmlReader.Door_Level2_9, XmlReader.Door_Level2_10,
                    XmlReader.Door_Level3_1, XmlReader.Door_Level3_2, XmlReader.Door_Level3_3, XmlReader.Door_Level3_4, XmlReader.Door_Level3_5, XmlReader.Door_Level3_6, XmlReader.Door_Level3_7, XmlReader.Door_Level3_8, XmlReader.Door_Level3_9, XmlReader.Door_Level3_10,
                    XmlReader.Door_Level4_1, XmlReader.Door_Level4_2, XmlReader.Door_Level4_3, XmlReader.Door_Level4_4, 0, XmlReader.Door_Level4_6, XmlReader.Door_Level4_7, XmlReader.Door_Level4_8, XmlReader.Door_Level4_9, XmlReader.Door_Level4_10,
                    XmlReader.Door_Level5_1, XmlReader.Door_Level5_2, XmlReader.Door_Level5_3, XmlReader.Door_Level5_4, XmlReader.Door_Level5_5, XmlReader.Door_Level5_6, XmlReader.Door_Level5_7, XmlReader.Door_Level5_8, XmlReader.Door_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Football, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Football_Level1_4, XmlReader.Football_Level1_5, XmlReader.Football_Level1_6, XmlReader.Football_Level1_7, XmlReader.Football_Level1_8, XmlReader.Football_Level1_9, XmlReader.Football_Level1_10,
                    XmlReader.Football_Level2_1, XmlReader.Football_Level2_2, XmlReader.Football_Level2_3, XmlReader.Football_Level2_4, XmlReader.Football_Level2_5, XmlReader.Football_Level2_6, XmlReader.Football_Level2_7, XmlReader.Football_Level2_8, XmlReader.Football_Level2_9, XmlReader.Football_Level2_10,
                    XmlReader.Football_Level3_1, XmlReader.Football_Level3_2, XmlReader.Football_Level3_3, XmlReader.Football_Level3_4, XmlReader.Football_Level3_5, XmlReader.Football_Level3_6, XmlReader.Football_Level3_7, XmlReader.Football_Level3_8, XmlReader.Football_Level3_9, XmlReader.Football_Level3_10,
                    XmlReader.Football_Level4_1, XmlReader.Football_Level4_2, XmlReader.Football_Level4_3, XmlReader.Football_Level4_4, 0, XmlReader.Football_Level4_6, XmlReader.Football_Level4_7, XmlReader.Football_Level4_8, XmlReader.Football_Level4_9, XmlReader.Football_Level4_10,
                    XmlReader.Football_Level5_1, XmlReader.Football_Level5_2, XmlReader.Football_Level5_3, XmlReader.Football_Level5_4, XmlReader.Football_Level5_5, XmlReader.Football_Level5_6, XmlReader.Football_Level5_7, XmlReader.Football_Level5_8, XmlReader.Football_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Dancer, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Dancer_Level1_4, XmlReader.Dancer_Level1_5, XmlReader.Dancer_Level1_6, XmlReader.Dancer_Level1_7, XmlReader.Dancer_Level1_8, XmlReader.Dancer_Level1_9, XmlReader.Dancer_Level1_10,
                    XmlReader.Dancer_Level2_1, XmlReader.Dancer_Level2_2, XmlReader.Dancer_Level2_3, XmlReader.Dancer_Level2_4, XmlReader.Dancer_Level2_5, XmlReader.Dancer_Level2_6, XmlReader.Dancer_Level2_7, XmlReader.Dancer_Level2_8, XmlReader.Dancer_Level2_9, XmlReader.Dancer_Level2_10,
                    XmlReader.Dancer_Level3_1, XmlReader.Dancer_Level3_2, XmlReader.Dancer_Level3_3, XmlReader.Dancer_Level3_4, XmlReader.Dancer_Level3_5, XmlReader.Dancer_Level3_6, XmlReader.Dancer_Level3_7, XmlReader.Dancer_Level3_8, XmlReader.Dancer_Level3_9, XmlReader.Dancer_Level3_10,
                    XmlReader.Dancer_Level4_1, XmlReader.Dancer_Level4_2, XmlReader.Dancer_Level4_3, XmlReader.Dancer_Level4_4, 0, XmlReader.Dancer_Level4_6, XmlReader.Dancer_Level4_7, XmlReader.Dancer_Level4_8, XmlReader.Dancer_Level4_9, XmlReader.Dancer_Level4_10,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                }),
                new ZombieAllowedLevels(ZombieType.BackupDancer, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.BackupDancer_Level1_4, XmlReader.BackupDancer_Level1_5, XmlReader.BackupDancer_Level1_6, XmlReader.BackupDancer_Level1_7, XmlReader.BackupDancer_Level1_8, XmlReader.BackupDancer_Level1_9, XmlReader.BackupDancer_Level1_10,
                    XmlReader.BackupDancer_Level2_1, XmlReader.BackupDancer_Level2_2, XmlReader.BackupDancer_Level2_3, XmlReader.BackupDancer_Level2_4, XmlReader.BackupDancer_Level2_5, XmlReader.BackupDancer_Level2_6, XmlReader.BackupDancer_Level2_7, XmlReader.BackupDancer_Level2_8, XmlReader.BackupDancer_Level2_9, XmlReader.BackupDancer_Level2_10,
                    XmlReader.BackupDancer_Level3_1, XmlReader.BackupDancer_Level3_2, XmlReader.BackupDancer_Level3_3, XmlReader.BackupDancer_Level3_4, XmlReader.BackupDancer_Level3_5, XmlReader.BackupDancer_Level3_6, XmlReader.BackupDancer_Level3_7, XmlReader.BackupDancer_Level3_8, XmlReader.BackupDancer_Level3_9, XmlReader.BackupDancer_Level3_10,
                    XmlReader.BackupDancer_Level4_1, XmlReader.BackupDancer_Level4_2, XmlReader.BackupDancer_Level4_3, XmlReader.BackupDancer_Level4_4, 0, XmlReader.BackupDancer_Level4_6, XmlReader.BackupDancer_Level4_7, XmlReader.BackupDancer_Level4_8, XmlReader.BackupDancer_Level4_9, XmlReader.BackupDancer_Level4_10,
                    XmlReader.BackupDancer_Level5_1, XmlReader.BackupDancer_Level5_2, XmlReader.BackupDancer_Level5_3, XmlReader.BackupDancer_Level5_4, XmlReader.BackupDancer_Level5_5, XmlReader.BackupDancer_Level5_6, XmlReader.BackupDancer_Level5_7, XmlReader.BackupDancer_Level5_8, XmlReader.BackupDancer_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.DuckyTube, new int[NUM_LEVELS]),
                new ZombieAllowedLevels(ZombieType.Snorkel, new int[NUM_LEVELS]
                {
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    XmlReader.Snorkel_Level3_1, XmlReader.Snorkel_Level3_2, XmlReader.Snorkel_Level3_3, XmlReader.Snorkel_Level3_4, XmlReader.Snorkel_Level3_5, XmlReader.Snorkel_Level3_6, XmlReader.Snorkel_Level3_7, XmlReader.Snorkel_Level3_8, XmlReader.Snorkel_Level3_9, XmlReader.Snorkel_Level3_10,
                    XmlReader.Snorkel_Level4_1, XmlReader.Snorkel_Level4_2, XmlReader.Snorkel_Level4_3, XmlReader.Snorkel_Level4_4, 0, XmlReader.Snorkel_Level4_6, XmlReader.Snorkel_Level4_7, XmlReader.Snorkel_Level4_8, XmlReader.Snorkel_Level4_9, XmlReader.Snorkel_Level4_10,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Zamboni, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Zamboni_Level1_4, XmlReader.Zamboni_Level1_5, XmlReader.Zamboni_Level1_6, XmlReader.Zamboni_Level1_7, XmlReader.Zamboni_Level1_8, XmlReader.Zamboni_Level1_9, XmlReader.Zamboni_Level1_10,
                    XmlReader.Zamboni_Level2_1, XmlReader.Zamboni_Level2_2, XmlReader.Zamboni_Level2_3, XmlReader.Zamboni_Level2_4, XmlReader.Zamboni_Level2_5, XmlReader.Zamboni_Level2_6, XmlReader.Zamboni_Level2_7, XmlReader.Zamboni_Level2_8, XmlReader.Zamboni_Level2_9, XmlReader.Zamboni_Level2_10,
                    XmlReader.Zamboni_Level3_1, XmlReader.Zamboni_Level3_2, XmlReader.Zamboni_Level3_3, XmlReader.Zamboni_Level3_4, XmlReader.Zamboni_Level3_5, XmlReader.Zamboni_Level3_6, XmlReader.Zamboni_Level3_7, XmlReader.Zamboni_Level3_8, XmlReader.Zamboni_Level3_9, XmlReader.Zamboni_Level3_10,
                    XmlReader.Zamboni_Level4_1, XmlReader.Zamboni_Level4_2, XmlReader.Zamboni_Level4_3, XmlReader.Zamboni_Level4_4, 0, XmlReader.Zamboni_Level4_6, XmlReader.Zamboni_Level4_7, XmlReader.Zamboni_Level4_8, XmlReader.Zamboni_Level4_9, XmlReader.Zamboni_Level4_10,
                    XmlReader.Zamboni_Level5_1, XmlReader.Zamboni_Level5_2, XmlReader.Zamboni_Level5_3, XmlReader.Zamboni_Level5_4, 0, XmlReader.Zamboni_Level5_6, XmlReader.Zamboni_Level5_7, XmlReader.Zamboni_Level5_8, XmlReader.Zamboni_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Bobsled, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Zamboni_Level1_4, XmlReader.Zamboni_Level1_5, XmlReader.Zamboni_Level1_6, XmlReader.Zamboni_Level1_7, XmlReader.Zamboni_Level1_8, XmlReader.Zamboni_Level1_9, XmlReader.Zamboni_Level1_10,
                    XmlReader.Zamboni_Level2_1, XmlReader.Zamboni_Level2_2, XmlReader.Zamboni_Level2_3, XmlReader.Zamboni_Level2_4, XmlReader.Zamboni_Level2_5, XmlReader.Zamboni_Level2_6, XmlReader.Zamboni_Level2_7, XmlReader.Zamboni_Level2_8, XmlReader.Zamboni_Level2_9, XmlReader.Zamboni_Level2_10,
                    XmlReader.Zamboni_Level3_1, XmlReader.Zamboni_Level3_2, XmlReader.Zamboni_Level3_3, XmlReader.Zamboni_Level3_4, XmlReader.Zamboni_Level3_5, XmlReader.Zamboni_Level3_6, XmlReader.Zamboni_Level3_7, XmlReader.Zamboni_Level3_8, XmlReader.Zamboni_Level3_9, XmlReader.Zamboni_Level3_10,
                    XmlReader.Zamboni_Level4_1, XmlReader.Zamboni_Level4_2, XmlReader.Zamboni_Level4_3, XmlReader.Zamboni_Level4_4, 0, XmlReader.Zamboni_Level4_6, XmlReader.Zamboni_Level4_7, XmlReader.Zamboni_Level4_8, XmlReader.Zamboni_Level4_9, XmlReader.Zamboni_Level4_10,
                    XmlReader.Zamboni_Level5_1, XmlReader.Zamboni_Level5_2, XmlReader.Zamboni_Level5_3, XmlReader.Zamboni_Level5_4, 0, XmlReader.Zamboni_Level5_6, XmlReader.Zamboni_Level5_7, XmlReader.Zamboni_Level5_8, XmlReader.Zamboni_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.DolphinRider, new int[NUM_LEVELS]
                {
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    XmlReader.DolphinRider_Level3_1, XmlReader.DolphinRider_Level3_2, XmlReader.DolphinRider_Level3_3, XmlReader.DolphinRider_Level3_4, XmlReader.DolphinRider_Level3_5, XmlReader.DolphinRider_Level3_6, XmlReader.DolphinRider_Level3_7, XmlReader.DolphinRider_Level3_8, XmlReader.DolphinRider_Level3_9, XmlReader.DolphinRider_Level3_10,
                    XmlReader.DolphinRider_Level4_1, XmlReader.DolphinRider_Level4_2, XmlReader.DolphinRider_Level4_3, XmlReader.DolphinRider_Level4_4, 0, XmlReader.DolphinRider_Level4_6, XmlReader.DolphinRider_Level4_7, XmlReader.DolphinRider_Level4_8, XmlReader.DolphinRider_Level4_9, XmlReader.DolphinRider_Level4_10,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                }),
                new ZombieAllowedLevels(ZombieType.JackInTheBox, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.JackInTheBox_Level1_4, XmlReader.JackInTheBox_Level1_5, XmlReader.JackInTheBox_Level1_6, XmlReader.JackInTheBox_Level1_7, XmlReader.JackInTheBox_Level1_8, XmlReader.JackInTheBox_Level1_9, XmlReader.JackInTheBox_Level1_10,
                    XmlReader.JackInTheBox_Level2_1, XmlReader.JackInTheBox_Level2_2, XmlReader.JackInTheBox_Level2_3, XmlReader.JackInTheBox_Level2_4, XmlReader.JackInTheBox_Level2_5, XmlReader.JackInTheBox_Level2_6, XmlReader.JackInTheBox_Level2_7, XmlReader.JackInTheBox_Level2_8, XmlReader.JackInTheBox_Level2_9, XmlReader.JackInTheBox_Level2_10,
                    XmlReader.JackInTheBox_Level3_1, XmlReader.JackInTheBox_Level3_2, XmlReader.JackInTheBox_Level3_3, XmlReader.JackInTheBox_Level3_4, XmlReader.JackInTheBox_Level3_5, XmlReader.JackInTheBox_Level3_6, XmlReader.JackInTheBox_Level3_7, XmlReader.JackInTheBox_Level3_8, XmlReader.JackInTheBox_Level3_9, XmlReader.JackInTheBox_Level3_10,
                    XmlReader.JackInTheBox_Level4_1, XmlReader.JackInTheBox_Level4_2, XmlReader.JackInTheBox_Level4_3, XmlReader.JackInTheBox_Level4_4, 0, XmlReader.JackInTheBox_Level4_6, XmlReader.JackInTheBox_Level4_7, XmlReader.JackInTheBox_Level4_8, XmlReader.JackInTheBox_Level4_9, XmlReader.JackInTheBox_Level4_10,
                    XmlReader.JackInTheBox_Level5_1, XmlReader.JackInTheBox_Level5_2, XmlReader.JackInTheBox_Level5_3, XmlReader.JackInTheBox_Level5_4, XmlReader.JackInTheBox_Level5_5, XmlReader.JackInTheBox_Level5_6, XmlReader.JackInTheBox_Level5_7, XmlReader.JackInTheBox_Level5_8, XmlReader.JackInTheBox_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Balloon, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Balloon_Level1_4, XmlReader.Balloon_Level1_5, XmlReader.Balloon_Level1_6, XmlReader.Balloon_Level1_7, XmlReader.Balloon_Level1_8, XmlReader.Balloon_Level1_9, XmlReader.Balloon_Level1_10,
                    XmlReader.Balloon_Level2_1, XmlReader.Balloon_Level2_2, XmlReader.Balloon_Level2_3, XmlReader.Balloon_Level2_4, XmlReader.Balloon_Level2_5, XmlReader.Balloon_Level2_6, XmlReader.Balloon_Level2_7, XmlReader.Balloon_Level2_8, XmlReader.Balloon_Level2_9, XmlReader.Balloon_Level2_10,
                    XmlReader.Balloon_Level3_1, XmlReader.Balloon_Level3_2, XmlReader.Balloon_Level3_3, XmlReader.Balloon_Level3_4, XmlReader.Balloon_Level3_5, XmlReader.Balloon_Level3_6, XmlReader.Balloon_Level3_7, XmlReader.Balloon_Level3_8, XmlReader.Balloon_Level3_9, XmlReader.Balloon_Level3_10,
                    XmlReader.Balloon_Level4_1, XmlReader.Balloon_Level4_2, XmlReader.Balloon_Level4_3, XmlReader.Balloon_Level4_4, 0, XmlReader.Balloon_Level4_6, XmlReader.Balloon_Level4_7, XmlReader.Balloon_Level4_8, XmlReader.Balloon_Level4_9, XmlReader.Balloon_Level4_10,
                    XmlReader.Balloon_Level5_1, XmlReader.Balloon_Level5_2, XmlReader.Balloon_Level5_3, XmlReader.Balloon_Level5_4, XmlReader.Balloon_Level5_5, XmlReader.Balloon_Level5_6, XmlReader.Balloon_Level5_7, XmlReader.Balloon_Level5_8, XmlReader.Balloon_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Digger, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Digger_Level1_4, XmlReader.Digger_Level1_5, XmlReader.Digger_Level1_6, XmlReader.Digger_Level1_7, XmlReader.Digger_Level1_8, XmlReader.Digger_Level1_9, XmlReader.Digger_Level1_10,
                    XmlReader.Digger_Level2_1, XmlReader.Digger_Level2_2, XmlReader.Digger_Level2_3, XmlReader.Digger_Level2_4, XmlReader.Digger_Level2_5, XmlReader.Digger_Level2_6, XmlReader.Digger_Level2_7, XmlReader.Digger_Level2_8, XmlReader.Digger_Level2_9, XmlReader.Digger_Level2_10,
                    XmlReader.Digger_Level3_1, XmlReader.Digger_Level3_2, XmlReader.Digger_Level3_3, XmlReader.Digger_Level3_4, XmlReader.Digger_Level3_5, XmlReader.Digger_Level3_6, XmlReader.Digger_Level3_7, XmlReader.Digger_Level3_8, XmlReader.Digger_Level3_9, XmlReader.Digger_Level3_10,
                    XmlReader.Digger_Level4_1, XmlReader.Digger_Level4_2, XmlReader.Digger_Level4_3, XmlReader.Digger_Level4_4, 0, XmlReader.Digger_Level4_6, XmlReader.Digger_Level4_7, XmlReader.Digger_Level4_8, XmlReader.Digger_Level4_9, XmlReader.Digger_Level4_10,
                                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0,

                }),
                new ZombieAllowedLevels(ZombieType.Pogo, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Pogo_Level1_4, XmlReader.Pogo_Level1_5, XmlReader.Pogo_Level1_6, XmlReader.Pogo_Level1_7, XmlReader.Pogo_Level1_8, XmlReader.Pogo_Level1_9, XmlReader.Pogo_Level1_10,
                    XmlReader.Pogo_Level2_1, XmlReader.Pogo_Level2_2, XmlReader.Pogo_Level2_3, XmlReader.Pogo_Level2_4, XmlReader.Pogo_Level2_5, XmlReader.Pogo_Level2_6, XmlReader.Pogo_Level2_7, XmlReader.Pogo_Level2_8, XmlReader.Pogo_Level2_9, XmlReader.Pogo_Level2_10,
                    XmlReader.Pogo_Level3_1, XmlReader.Pogo_Level3_2, XmlReader.Pogo_Level3_3, XmlReader.Pogo_Level3_4, XmlReader.Pogo_Level3_5, XmlReader.Pogo_Level3_6, XmlReader.Pogo_Level3_7, XmlReader.Pogo_Level3_8, XmlReader.Pogo_Level3_9, XmlReader.Pogo_Level3_10,
                    XmlReader.Pogo_Level4_1, XmlReader.Pogo_Level4_2, XmlReader.Pogo_Level4_3, XmlReader.Pogo_Level4_4, 0, XmlReader.Pogo_Level4_6, XmlReader.Pogo_Level4_7, XmlReader.Pogo_Level4_8, XmlReader.Pogo_Level4_9, XmlReader.Pogo_Level4_10,
                    XmlReader.Pogo_Level5_1, XmlReader.Pogo_Level5_2, XmlReader.Pogo_Level5_3, XmlReader.Pogo_Level5_4, 0, XmlReader.Pogo_Level5_6, XmlReader.Pogo_Level5_7, XmlReader.Pogo_Level5_8, XmlReader.Pogo_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Yeti, new int[NUM_LEVELS]),
                new ZombieAllowedLevels(ZombieType.Bungee, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Bungee_Level1_4, XmlReader.Bungee_Level1_5, XmlReader.Bungee_Level1_6, XmlReader.Bungee_Level1_7, XmlReader.Bungee_Level1_8, XmlReader.Bungee_Level1_9, XmlReader.Bungee_Level1_10,
                    XmlReader.Bungee_Level2_1, XmlReader.Bungee_Level2_2, XmlReader.Bungee_Level2_3, XmlReader.Bungee_Level2_4, XmlReader.Bungee_Level2_5, XmlReader.Bungee_Level2_6, XmlReader.Bungee_Level2_7, XmlReader.Bungee_Level2_8, XmlReader.Bungee_Level2_9, XmlReader.Bungee_Level2_10,
                    XmlReader.Bungee_Level3_1, XmlReader.Bungee_Level3_2, XmlReader.Bungee_Level3_3, XmlReader.Bungee_Level3_4, XmlReader.Bungee_Level3_5, XmlReader.Bungee_Level3_6, XmlReader.Bungee_Level3_7, XmlReader.Bungee_Level3_8, XmlReader.Bungee_Level3_9, XmlReader.Bungee_Level3_10,
                    XmlReader.Bungee_Level4_1, XmlReader.Bungee_Level4_2, XmlReader.Bungee_Level4_3, XmlReader.Bungee_Level4_4, 0, XmlReader.Bungee_Level4_6, XmlReader.Bungee_Level4_7, XmlReader.Bungee_Level4_8, XmlReader.Bungee_Level4_9, XmlReader.Bungee_Level4_10,
                    XmlReader.Bungee_Level5_1, XmlReader.Bungee_Level5_2, XmlReader.Bungee_Level5_3, XmlReader.Bungee_Level5_4, 1, XmlReader.Bungee_Level5_6, XmlReader.Bungee_Level5_7, XmlReader.Bungee_Level5_8, XmlReader.Bungee_Level5_9, 0,                }),
                new ZombieAllowedLevels(ZombieType.Ladder, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Ladder_Level1_4, XmlReader.Ladder_Level1_5, XmlReader.Ladder_Level1_6, XmlReader.Ladder_Level1_7, XmlReader.Ladder_Level1_8, XmlReader.Ladder_Level1_9, XmlReader.Ladder_Level1_10,
                    XmlReader.Ladder_Level2_1, XmlReader.Ladder_Level2_2, XmlReader.Ladder_Level2_3, XmlReader.Ladder_Level2_4, XmlReader.Ladder_Level2_5, XmlReader.Ladder_Level2_6, XmlReader.Ladder_Level2_7, XmlReader.Ladder_Level2_8, XmlReader.Ladder_Level2_9, XmlReader.Ladder_Level2_10,
                    XmlReader.Ladder_Level3_1, XmlReader.Ladder_Level3_2, XmlReader.Ladder_Level3_3, XmlReader.Ladder_Level3_4, XmlReader.Ladder_Level3_5, XmlReader.Ladder_Level3_6, XmlReader.Ladder_Level3_7, XmlReader.Ladder_Level3_8, XmlReader.Ladder_Level3_9, XmlReader.Ladder_Level3_10,
                    XmlReader.Ladder_Level4_1, XmlReader.Ladder_Level4_2, XmlReader.Ladder_Level4_3, XmlReader.Ladder_Level4_4, 0, XmlReader.Ladder_Level4_6, XmlReader.Ladder_Level4_7, XmlReader.Ladder_Level4_8, XmlReader.Ladder_Level4_9, XmlReader.Ladder_Level4_10,
                    XmlReader.Ladder_Level5_1, XmlReader.Ladder_Level5_2, XmlReader.Ladder_Level5_3, XmlReader.Ladder_Level5_4, XmlReader.Ladder_Level5_5, XmlReader.Ladder_Level5_6, XmlReader.Ladder_Level5_7, XmlReader.Ladder_Level5_8, XmlReader.Ladder_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Catapult, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Catapult_Level1_4, XmlReader.Catapult_Level1_5, XmlReader.Catapult_Level1_6, XmlReader.Catapult_Level1_7, XmlReader.Catapult_Level1_8, XmlReader.Catapult_Level1_9, XmlReader.Catapult_Level1_10,
                    XmlReader.Catapult_Level2_1, XmlReader.Catapult_Level2_2, XmlReader.Catapult_Level2_3, XmlReader.Catapult_Level2_4, XmlReader.Catapult_Level2_5, XmlReader.Catapult_Level2_6, XmlReader.Catapult_Level2_7, XmlReader.Catapult_Level2_8, XmlReader.Catapult_Level2_9, XmlReader.Catapult_Level2_10,
                    XmlReader.Catapult_Level3_1, XmlReader.Catapult_Level3_2, XmlReader.Catapult_Level3_3, XmlReader.Catapult_Level3_4, XmlReader.Catapult_Level3_5, XmlReader.Catapult_Level3_6, XmlReader.Catapult_Level3_7, XmlReader.Catapult_Level3_8, XmlReader.Catapult_Level3_9, XmlReader.Catapult_Level3_10,
                    XmlReader.Catapult_Level4_1, XmlReader.Catapult_Level4_2, XmlReader.Catapult_Level4_3, XmlReader.Catapult_Level4_4, 0, XmlReader.Catapult_Level4_6, XmlReader.Catapult_Level4_7, XmlReader.Catapult_Level4_8, XmlReader.Catapult_Level4_9, XmlReader.Catapult_Level4_10,
                    XmlReader.Catapult_Level5_1, XmlReader.Catapult_Level5_2, XmlReader.Catapult_Level5_3, XmlReader.Catapult_Level5_4, XmlReader.Catapult_Level5_5, XmlReader.Catapult_Level5_6, XmlReader.Catapult_Level5_7, XmlReader.Catapult_Level5_8, XmlReader.Catapult_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Gargantuar, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.Gargantuar_Level1_4, XmlReader.Gargantuar_Level1_5, XmlReader.Gargantuar_Level1_6, XmlReader.Gargantuar_Level1_7, XmlReader.Gargantuar_Level1_8, XmlReader.Gargantuar_Level1_9, XmlReader.Gargantuar_Level1_10,
                    XmlReader.Gargantuar_Level2_1, XmlReader.Gargantuar_Level2_2, XmlReader.Gargantuar_Level2_3, XmlReader.Gargantuar_Level2_4, XmlReader.Gargantuar_Level2_5, XmlReader.Gargantuar_Level2_6, XmlReader.Gargantuar_Level2_7, XmlReader.Gargantuar_Level2_8, XmlReader.Gargantuar_Level2_9, XmlReader.Gargantuar_Level2_10,
                    XmlReader.Gargantuar_Level3_1, XmlReader.Gargantuar_Level3_2, XmlReader.Gargantuar_Level3_3, XmlReader.Gargantuar_Level3_4, XmlReader.Gargantuar_Level3_5, XmlReader.Gargantuar_Level3_6, XmlReader.Gargantuar_Level3_7, XmlReader.Gargantuar_Level3_8, XmlReader.Gargantuar_Level3_9, XmlReader.Gargantuar_Level3_10,
                    XmlReader.Gargantuar_Level4_1, XmlReader.Gargantuar_Level4_2, XmlReader.Gargantuar_Level4_3, XmlReader.Gargantuar_Level4_4, 0, XmlReader.Gargantuar_Level4_6, XmlReader.Gargantuar_Level4_7, XmlReader.Gargantuar_Level4_8, XmlReader.Gargantuar_Level4_9, XmlReader.Gargantuar_Level4_10,
                    XmlReader.Gargantuar_Level5_1, XmlReader.Gargantuar_Level5_2, XmlReader.Gargantuar_Level5_3, XmlReader.Gargantuar_Level5_4, 0, XmlReader.Gargantuar_Level5_6, XmlReader.Gargantuar_Level5_7, XmlReader.Gargantuar_Level5_8, XmlReader.Gargantuar_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Imp, new int[NUM_LEVELS]
                {
                      0, 0, 0, XmlReader.Imp_Level1_4, XmlReader.Imp_Level1_5, XmlReader.Imp_Level1_6, XmlReader.Imp_Level1_7, XmlReader.Imp_Level1_8, XmlReader.Imp_Level1_9, XmlReader.Imp_Level1_10,
                    XmlReader.Imp_Level2_1, XmlReader.Imp_Level2_2, XmlReader.Imp_Level2_3, XmlReader.Imp_Level2_4, XmlReader.Imp_Level2_5, XmlReader.Imp_Level2_6, XmlReader.Imp_Level2_7, XmlReader.Imp_Level2_8, XmlReader.Imp_Level2_9, XmlReader.Imp_Level2_10,
                    XmlReader.Imp_Level3_1, XmlReader.Imp_Level3_2, XmlReader.Imp_Level3_3, XmlReader.Imp_Level3_4, XmlReader.Imp_Level3_5, XmlReader.Imp_Level3_6, XmlReader.Imp_Level3_7, XmlReader.Imp_Level3_8, XmlReader.Imp_Level3_9, XmlReader.Imp_Level3_10,
                    XmlReader.Imp_Level4_1, XmlReader.Imp_Level4_2, XmlReader.Imp_Level4_3, XmlReader.Imp_Level4_4, 0, XmlReader.Imp_Level4_6, XmlReader.Imp_Level4_7, XmlReader.Imp_Level4_8, XmlReader.Imp_Level4_9, XmlReader.Imp_Level4_10,
                    XmlReader.Imp_Level5_1, XmlReader.Imp_Level5_2, XmlReader.Imp_Level5_3, XmlReader.Imp_Level5_4, XmlReader.Imp_Level5_5, XmlReader.Imp_Level5_6, XmlReader.Imp_Level5_7, XmlReader.Imp_Level5_8, XmlReader.Imp_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.Boss, new int[NUM_LEVELS]),
                new ZombieAllowedLevels(ZombieType.PeaHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.PeaHead_Level1_4, XmlReader.PeaHead_Level1_5, XmlReader.PeaHead_Level1_6, XmlReader.PeaHead_Level1_7, XmlReader.PeaHead_Level1_8, XmlReader.PeaHead_Level1_9, XmlReader.PeaHead_Level1_10,
                    XmlReader.PeaHead_Level2_1, XmlReader.PeaHead_Level2_2, XmlReader.PeaHead_Level2_3, XmlReader.PeaHead_Level2_4, XmlReader.PeaHead_Level2_5, XmlReader.PeaHead_Level2_6, XmlReader.PeaHead_Level2_7, XmlReader.PeaHead_Level2_8, XmlReader.PeaHead_Level2_9, XmlReader.PeaHead_Level2_10,
                    XmlReader.PeaHead_Level3_1, XmlReader.PeaHead_Level3_2, XmlReader.PeaHead_Level3_3, XmlReader.PeaHead_Level3_4, XmlReader.PeaHead_Level3_5, XmlReader.PeaHead_Level3_6, XmlReader.PeaHead_Level3_7, XmlReader.PeaHead_Level3_8, XmlReader.PeaHead_Level3_9, XmlReader.PeaHead_Level3_10,
                    XmlReader.PeaHead_Level4_1, XmlReader.PeaHead_Level4_2, XmlReader.PeaHead_Level4_3, XmlReader.PeaHead_Level4_4, 0, XmlReader.PeaHead_Level4_6, XmlReader.PeaHead_Level4_7, XmlReader.PeaHead_Level4_8, XmlReader.PeaHead_Level4_9, XmlReader.PeaHead_Level4_10,
                    XmlReader.PeaHead_Level5_1, XmlReader.PeaHead_Level5_2, XmlReader.PeaHead_Level5_3, XmlReader.PeaHead_Level5_4, XmlReader.PeaHead_Level5_5, XmlReader.PeaHead_Level5_6, XmlReader.PeaHead_Level5_7, XmlReader.PeaHead_Level5_8, XmlReader.PeaHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.WallnutHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.WallnutHead_Level1_4, XmlReader.WallnutHead_Level1_5, XmlReader.WallnutHead_Level1_6, XmlReader.WallnutHead_Level1_7, XmlReader.WallnutHead_Level1_8, XmlReader.WallnutHead_Level1_9, XmlReader.WallnutHead_Level1_10,
                    XmlReader.WallnutHead_Level2_1, XmlReader.WallnutHead_Level2_2, XmlReader.WallnutHead_Level2_3, XmlReader.WallnutHead_Level2_4, XmlReader.WallnutHead_Level2_5, XmlReader.WallnutHead_Level2_6, XmlReader.WallnutHead_Level2_7, XmlReader.WallnutHead_Level2_8, XmlReader.WallnutHead_Level2_9, XmlReader.WallnutHead_Level2_10,
                    XmlReader.WallnutHead_Level3_1, XmlReader.WallnutHead_Level3_2, XmlReader.WallnutHead_Level3_3, XmlReader.WallnutHead_Level3_4, XmlReader.WallnutHead_Level3_5, XmlReader.WallnutHead_Level3_6, XmlReader.WallnutHead_Level3_7, XmlReader.WallnutHead_Level3_8, XmlReader.WallnutHead_Level3_9, XmlReader.WallnutHead_Level3_10,
                    XmlReader.WallnutHead_Level4_1, XmlReader.WallnutHead_Level4_2, XmlReader.WallnutHead_Level4_3, XmlReader.WallnutHead_Level4_4, 0, XmlReader.WallnutHead_Level4_6, XmlReader.WallnutHead_Level4_7, XmlReader.WallnutHead_Level4_8, XmlReader.WallnutHead_Level4_9, XmlReader.WallnutHead_Level4_10,
                    XmlReader.WallnutHead_Level5_1, XmlReader.WallnutHead_Level5_2, XmlReader.WallnutHead_Level5_3, XmlReader.WallnutHead_Level5_4, XmlReader.WallnutHead_Level5_5, XmlReader.WallnutHead_Level5_6, XmlReader.WallnutHead_Level5_7, XmlReader.WallnutHead_Level5_8, XmlReader.WallnutHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.JalapenoHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.JalapenoHead_Level1_4, XmlReader.JalapenoHead_Level1_5, XmlReader.JalapenoHead_Level1_6, XmlReader.JalapenoHead_Level1_7, XmlReader.JalapenoHead_Level1_8, XmlReader.JalapenoHead_Level1_9, XmlReader.JalapenoHead_Level1_10,
                    XmlReader.JalapenoHead_Level2_1, XmlReader.JalapenoHead_Level2_2, XmlReader.JalapenoHead_Level2_3, XmlReader.JalapenoHead_Level2_4, XmlReader.JalapenoHead_Level2_5, XmlReader.JalapenoHead_Level2_6, XmlReader.JalapenoHead_Level2_7, XmlReader.JalapenoHead_Level2_8, XmlReader.JalapenoHead_Level2_9, XmlReader.JalapenoHead_Level2_10,
                    XmlReader.JalapenoHead_Level3_1, XmlReader.JalapenoHead_Level3_2, XmlReader.JalapenoHead_Level3_3, XmlReader.JalapenoHead_Level3_4, XmlReader.JalapenoHead_Level3_5, XmlReader.JalapenoHead_Level3_6, XmlReader.JalapenoHead_Level3_7, XmlReader.JalapenoHead_Level3_8, XmlReader.JalapenoHead_Level3_9, XmlReader.JalapenoHead_Level3_10,
                    XmlReader.JalapenoHead_Level4_1, XmlReader.JalapenoHead_Level4_2, XmlReader.JalapenoHead_Level4_3, XmlReader.JalapenoHead_Level4_4, 0, XmlReader.JalapenoHead_Level4_6, XmlReader.JalapenoHead_Level4_7, XmlReader.JalapenoHead_Level4_8, XmlReader.JalapenoHead_Level4_9, XmlReader.JalapenoHead_Level4_10,
                    XmlReader.JalapenoHead_Level5_1, XmlReader.JalapenoHead_Level5_2, XmlReader.JalapenoHead_Level5_3, XmlReader.JalapenoHead_Level5_4, XmlReader.JalapenoHead_Level5_5, XmlReader.JalapenoHead_Level5_6, XmlReader.JalapenoHead_Level5_7, XmlReader.JalapenoHead_Level5_8, XmlReader.JalapenoHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.GatlingHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.GatlingHead_Level1_4, XmlReader.GatlingHead_Level1_5, XmlReader.GatlingHead_Level1_6, XmlReader.GatlingHead_Level1_7, XmlReader.GatlingHead_Level1_8, XmlReader.GatlingHead_Level1_9, XmlReader.GatlingHead_Level1_10,
                    XmlReader.GatlingHead_Level2_1, XmlReader.GatlingHead_Level2_2, XmlReader.GatlingHead_Level2_3, XmlReader.GatlingHead_Level2_4, XmlReader.GatlingHead_Level2_5, XmlReader.GatlingHead_Level2_6, XmlReader.GatlingHead_Level2_7, XmlReader.GatlingHead_Level2_8, XmlReader.GatlingHead_Level2_9, XmlReader.GatlingHead_Level2_10,
                    XmlReader.GatlingHead_Level3_1, XmlReader.GatlingHead_Level3_2, XmlReader.GatlingHead_Level3_3, XmlReader.GatlingHead_Level3_4, XmlReader.GatlingHead_Level3_5, XmlReader.GatlingHead_Level3_6, XmlReader.GatlingHead_Level3_7, XmlReader.GatlingHead_Level3_8, XmlReader.GatlingHead_Level3_9, XmlReader.GatlingHead_Level3_10,
                    XmlReader.GatlingHead_Level4_1, XmlReader.GatlingHead_Level4_2, XmlReader.GatlingHead_Level4_3, XmlReader.GatlingHead_Level4_4, 0, XmlReader.GatlingHead_Level4_6, XmlReader.GatlingHead_Level4_7, XmlReader.GatlingHead_Level4_8, XmlReader.GatlingHead_Level4_9, XmlReader.GatlingHead_Level4_10,
                    XmlReader.GatlingHead_Level5_1, XmlReader.GatlingHead_Level5_2, XmlReader.GatlingHead_Level5_3, XmlReader.GatlingHead_Level5_4, XmlReader.GatlingHead_Level5_5, XmlReader.GatlingHead_Level5_6, XmlReader.GatlingHead_Level5_7, XmlReader.GatlingHead_Level5_8, XmlReader.GatlingHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.SquashHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.SquashHead_Level1_4, XmlReader.SquashHead_Level1_5, XmlReader.SquashHead_Level1_6, XmlReader.SquashHead_Level1_7, XmlReader.SquashHead_Level1_8, XmlReader.SquashHead_Level1_9, XmlReader.SquashHead_Level1_10,
                    XmlReader.SquashHead_Level2_1, XmlReader.SquashHead_Level2_2, XmlReader.SquashHead_Level2_3, XmlReader.SquashHead_Level2_4, XmlReader.SquashHead_Level2_5, XmlReader.SquashHead_Level2_6, XmlReader.SquashHead_Level2_7, XmlReader.SquashHead_Level2_8, XmlReader.SquashHead_Level2_9, XmlReader.SquashHead_Level2_10,
                    XmlReader.SquashHead_Level3_1, XmlReader.SquashHead_Level3_2, XmlReader.SquashHead_Level3_3, XmlReader.SquashHead_Level3_4, XmlReader.SquashHead_Level3_5, XmlReader.SquashHead_Level3_6, XmlReader.SquashHead_Level3_7, XmlReader.SquashHead_Level3_8, XmlReader.SquashHead_Level3_9, XmlReader.SquashHead_Level3_10,
                    XmlReader.SquashHead_Level4_1, XmlReader.SquashHead_Level4_2, XmlReader.SquashHead_Level4_3, XmlReader.SquashHead_Level4_4, 0, XmlReader.SquashHead_Level4_6, XmlReader.SquashHead_Level4_7, XmlReader.SquashHead_Level4_8, XmlReader.SquashHead_Level4_9, XmlReader.SquashHead_Level4_10,
                    XmlReader.SquashHead_Level5_1, XmlReader.SquashHead_Level5_2, XmlReader.SquashHead_Level5_3, XmlReader.SquashHead_Level5_4, XmlReader.SquashHead_Level5_5, XmlReader.SquashHead_Level5_6, XmlReader.SquashHead_Level5_7, XmlReader.SquashHead_Level5_8, XmlReader.SquashHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.TallnutHead, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.TallnutHead_Level1_4, XmlReader.TallnutHead_Level1_5, XmlReader.TallnutHead_Level1_6, XmlReader.TallnutHead_Level1_7, XmlReader.TallnutHead_Level1_8, XmlReader.TallnutHead_Level1_9, XmlReader.TallnutHead_Level1_10,
                    XmlReader.TallnutHead_Level2_1, XmlReader.TallnutHead_Level2_2, XmlReader.TallnutHead_Level2_3, XmlReader.TallnutHead_Level2_4, XmlReader.TallnutHead_Level2_5, XmlReader.TallnutHead_Level2_6, XmlReader.TallnutHead_Level2_7, XmlReader.TallnutHead_Level2_8, XmlReader.TallnutHead_Level2_9, XmlReader.TallnutHead_Level2_10,
                    XmlReader.TallnutHead_Level3_1, XmlReader.TallnutHead_Level3_2, XmlReader.TallnutHead_Level3_3, XmlReader.TallnutHead_Level3_4, XmlReader.TallnutHead_Level3_5, XmlReader.TallnutHead_Level3_6, XmlReader.TallnutHead_Level3_7, XmlReader.TallnutHead_Level3_8, XmlReader.TallnutHead_Level3_9, XmlReader.TallnutHead_Level3_10,
                    XmlReader.TallnutHead_Level4_1, XmlReader.TallnutHead_Level4_2, XmlReader.TallnutHead_Level4_3, XmlReader.TallnutHead_Level4_4, 0, XmlReader.TallnutHead_Level4_6, XmlReader.TallnutHead_Level4_7, XmlReader.TallnutHead_Level4_8, XmlReader.TallnutHead_Level4_9, XmlReader.TallnutHead_Level4_10,
                    XmlReader.TallnutHead_Level5_1, XmlReader.TallnutHead_Level5_2, XmlReader.TallnutHead_Level5_3, XmlReader.TallnutHead_Level5_4, XmlReader.TallnutHead_Level5_5, XmlReader.TallnutHead_Level5_6, XmlReader.TallnutHead_Level5_7, XmlReader.TallnutHead_Level5_8, XmlReader.TallnutHead_Level5_9, 0,
                }),
                new ZombieAllowedLevels(ZombieType.RedeyeGargantuar, new int[NUM_LEVELS]
                {
                    0, 0, 0, XmlReader.RedeyeGargantuar_Level1_4, XmlReader.RedeyeGargantuar_Level1_5, XmlReader.RedeyeGargantuar_Level1_6, XmlReader.RedeyeGargantuar_Level1_7, XmlReader.RedeyeGargantuar_Level1_8, XmlReader.RedeyeGargantuar_Level1_9, XmlReader.RedeyeGargantuar_Level1_10,
                    XmlReader.RedeyeGargantuar_Level2_1, XmlReader.RedeyeGargantuar_Level2_2, XmlReader.RedeyeGargantuar_Level2_3, XmlReader.RedeyeGargantuar_Level2_4, XmlReader.RedeyeGargantuar_Level2_5, XmlReader.RedeyeGargantuar_Level2_6, XmlReader.RedeyeGargantuar_Level2_7, XmlReader.RedeyeGargantuar_Level2_8, XmlReader.RedeyeGargantuar_Level2_9, XmlReader.RedeyeGargantuar_Level2_10,
                    XmlReader.RedeyeGargantuar_Level3_1, XmlReader.RedeyeGargantuar_Level3_2, XmlReader.RedeyeGargantuar_Level3_3, XmlReader.RedeyeGargantuar_Level3_4, XmlReader.RedeyeGargantuar_Level3_5, XmlReader.RedeyeGargantuar_Level3_6, XmlReader.RedeyeGargantuar_Level3_7, XmlReader.RedeyeGargantuar_Level3_8, XmlReader.RedeyeGargantuar_Level3_9, XmlReader.RedeyeGargantuar_Level3_10,
                    XmlReader.RedeyeGargantuar_Level4_1, XmlReader.RedeyeGargantuar_Level4_2, XmlReader.RedeyeGargantuar_Level4_3, XmlReader.RedeyeGargantuar_Level4_4, 0, XmlReader.RedeyeGargantuar_Level4_6, XmlReader.RedeyeGargantuar_Level4_7, XmlReader.RedeyeGargantuar_Level4_8, XmlReader.RedeyeGargantuar_Level4_9, XmlReader.RedeyeGargantuar_Level4_10,
                    XmlReader.RedeyeGargantuar_Level5_1, XmlReader.RedeyeGargantuar_Level5_2, XmlReader.RedeyeGargantuar_Level5_3, XmlReader.RedeyeGargantuar_Level5_4, 0, XmlReader.RedeyeGargantuar_Level5_6, XmlReader.RedeyeGargantuar_Level5_7, XmlReader.RedeyeGargantuar_Level5_8, XmlReader.RedeyeGargantuar_Level5_9, 0,
                }),
            };
            // 植物常量定义
            GameConstants.gPlantDefs = new PlantDefinition[2]
            {
                /*                | SeedType 枚举值   | 植物图像 |动画轨道类型           |选卡序号|价格|冷却|子类                  |发射速率|名称| */
new PlantDefinition(SeedType.Peashooter,    null, ReanimationType.Peashooter,   0,  100,750, PlantSubClass.Shooter, 150, "PEASHOOTER"),
new PlantDefinition(SeedType.Sunflower,     null, ReanimationType.Sunflower,    1,  50, 750, PlantSubClass.Normal,  2500, "SUNFLOWER"),
};
            for (int i = 2; i < 53; i = i + 1)
            {
                Array.Resize(ref gPlantDefs, gPlantDefs.Length + 1);
                if (i == (int)SeedType.Cherrybomb)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Cherrybomb, null, ReanimationType.Cherrybomb, 3, 150, 5000, PlantSubClass.Normal, 0, "CHERRY_BOMB");

                };
                if (i == (int)SeedType.Wallnut)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Wallnut, null, ReanimationType.Wallnut, 2, XmlReader.WallnutSuncost, 3000, PlantSubClass.Normal, 0, "WALL_NUT");
                };
                if (i == (int)SeedType.Potatomine)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Potatomine, null, ReanimationType.Potatomine, 37, XmlReader.PotatoMineSuncost, 3000, PlantSubClass.Normal, 0, "POTATO_MINE");
                };
                if (i == (int)SeedType.Snowpea)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Snowpea, null, ReanimationType.Snowpea, 4, XmlReader.SnowpeaSuncost, 750, PlantSubClass.Shooter, XmlReader.SnowpeaFiringSpeed, "SNOW_PEA");
                };
                if (i == (int)SeedType.Chomper)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Chomper, null, ReanimationType.Chomper, 31, XmlReader.ChomperSuncost, 750, PlantSubClass.Normal, 0, "CHOMPER");
                };
                if (i == (int)SeedType.Repeater)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Repeater, null, ReanimationType.Repeater, 5, XmlReader.RepeaterSuncost, 750, PlantSubClass.Shooter, XmlReader.RepeaterFiringSpeed, "REPEATER");
                };
                if (i == (int)SeedType.Puffshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Puffshroom, null, ReanimationType.Puffshroom, 6, 0, 750, PlantSubClass.Shooter, 150, "PUFF_SHROOM");
                };
                if (i == (int)SeedType.Sunshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Sunshroom, null, ReanimationType.Sunshroom, 7, 25, 750, PlantSubClass.Normal, 2500, "SUN_SHROOM");
                };
                if (i == (int)SeedType.Fumeshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Fumeshroom, null, ReanimationType.Fumeshroom, 9, XmlReader.FumeShroomSuncost, 750, PlantSubClass.Shooter, XmlReader.FumeShroomFiringSpeed, "FUME_SHROOM");
                };
                if (i == (int)SeedType.Gravebuster)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Gravebuster, null, ReanimationType.GraveBuster, 40, XmlReader.GraveBusterSuncost, 750, PlantSubClass.Normal, 0, "GRAVE_BUSTER");
                };
                if (i == (int)SeedType.Hypnoshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Hypnoshroom, null, ReanimationType.Hypnoshroom, 10, 75, 3000, PlantSubClass.Normal, 0, "HYPNO_SHROOM");
                };
                if (i == (int)SeedType.Scaredyshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Scaredyshroom, null, ReanimationType.Scrareyshroom, 33, XmlReader.ScaredyShroomSuncost, 750, PlantSubClass.Shooter, XmlReader.ScaredyShroomFiringSpeed, "SCAREDY_SHROOM");
                };
                if (i == (int)SeedType.Iceshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Iceshroom, null, ReanimationType.Iceshroom, 36, XmlReader.IceShroomSuncost, 5000, PlantSubClass.Normal, 0, "ICE_SHROOM");
                };
                if (i == (int)SeedType.Doomshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Doomshroom, null, ReanimationType.Doomshroom, 20, XmlReader.DoomshroomSuncost, 5000, PlantSubClass.Normal, 0, "DOOM_SHROOM");
                };
                if (i == (int)SeedType.Lilypad)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Lilypad, null, ReanimationType.Lilypad, 19, 25, 750, PlantSubClass.Normal, 0, "LILY_PAD");
                };
                if (i == (int)SeedType.Squash)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Squash, null, ReanimationType.Squash, 21, XmlReader.SquashSuncost, 3000, PlantSubClass.Normal, 0, "SQUASH");
                };
                if (i == (int)SeedType.Threepeater)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Threepeater, null, ReanimationType.Threepeater, 12, XmlReader.ThreepeaterSuncost, 750, PlantSubClass.Shooter, XmlReader.ThreepeaterFiringSpeed, "THREEPEATER");
                };
                if (i == (int)SeedType.Tanglekelp)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Tanglekelp, null, ReanimationType.Tanglekelp, 17, 25, 3000, PlantSubClass.Normal, 0, "TANGLE_KELP");
                };
                if (i == (int)SeedType.Jalapeno)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Jalapeno, null, ReanimationType.Jalapeno, 11, 125, 5000, PlantSubClass.Normal, 0, "JALAPENO");
                };
                if (i == (int)SeedType.Spikeweed)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Spikeweed, null, ReanimationType.Spikeweed, 22, XmlReader.SpikeweedSuncost, 750, PlantSubClass.Normal, 0, "SPIKEWEED");
                };
                if (i == (int)SeedType.Torchwood)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Torchwood, null, ReanimationType.Torchwood, 29, 175, 750, PlantSubClass.Normal, 0, "TORCHWOOD");
                };
                if (i == (int)SeedType.Tallnut)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Tallnut, null, ReanimationType.Tallnut, 28, XmlReader.TallnutSuncost, 3000, PlantSubClass.Normal, 0, "TALL_NUT");
                };
                if (i == (int)SeedType.Seashroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Seashroom, null, ReanimationType.Seashroom, 39, 0, 3000, PlantSubClass.Shooter, 150, "SEA_SHROOM");
                };
                if (i == (int)SeedType.Plantern)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Plantern, null, ReanimationType.Plantern, 38, 25, 3000, PlantSubClass.Normal, 2500, "PLANTERN");
                };
                if (i == (int)SeedType.Cactus)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Cactus, null, ReanimationType.Cactus, 15, XmlReader.CactusSuncost, 750, PlantSubClass.Shooter, XmlReader.CactusFiringSpeed, "CACTUS");
                };
                if (i == (int)SeedType.Blover)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Blover, null, ReanimationType.Blover, 18, XmlReader.BloverSuncost, 750, PlantSubClass.Normal, 0, "BLOVER");
                };
                if (i == (int)SeedType.Splitpea)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Splitpea, null, ReanimationType.Splitpea, 32, XmlReader.SplitpeaSuncost, 750, PlantSubClass.Shooter, XmlReader.SplitpeaFiringSpeed, "SPLIT_PEA");
                };
                if (i == (int)SeedType.Starfruit)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Starfruit, null, ReanimationType.Starfruit, 30, XmlReader.StarfuitSuncost, 750, PlantSubClass.Shooter, XmlReader.StarfruitFiringSpeed, "STARFRUIT");
                };
                if (i == (int)SeedType.Pumpkinshell)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Pumpkinshell, null, ReanimationType.Pumpkin, 25, XmlReader.PumpkinSuncost, 3000, PlantSubClass.Normal, 0, "PUMPKIN");
                };
                if (i == (int)SeedType.Magnetshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Magnetshroom, null, ReanimationType.Magnetshroom, 35, XmlReader.MagnetShroomSuncost, 750, PlantSubClass.Normal, 0, "MAGNET_SHROOM");
                };
                if (i == (int)SeedType.Cabbagepult)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Cabbagepult, null, ReanimationType.Cabbagepult, 13, XmlReader.CabbagepultSuncost, 750, PlantSubClass.Shooter, XmlReader.CabbagepultFiringSpeed, "CABBAGE_PULT");
                };
                if (i == (int)SeedType.Flowerpot)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Flowerpot, null, ReanimationType.FlowerPot, 33, 25, 750, PlantSubClass.Normal, 0, "FLOWER_POT");
                };
                if (i == (int)SeedType.Kernelpult)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Kernelpult, null, ReanimationType.Kernelpult, 13, XmlReader.KernelpultSuncost, 750, PlantSubClass.Shooter, XmlReader.KernelpultFiringSpeed, "KERNEL_PULT");
                };
                if (i == (int)SeedType.InstantCoffee)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.InstantCoffee, null, ReanimationType.Coffeebean, 33, 75, 750, PlantSubClass.Normal, 0, "COFFEE_BEAN");
                };
                if (i == (int)SeedType.Garlic)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Garlic, null, ReanimationType.Garlic, 8, XmlReader.GarlicSuncost, 750, PlantSubClass.Normal, 0, "GARLIC");
                };
                if (i == (int)SeedType.Umbrella)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Umbrella, null, ReanimationType.Umbrellaleaf, 23, 100, 750, PlantSubClass.Normal, 0, "UMBRELLA_LEAF");
                };
                if (i == (int)SeedType.Marigold)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Marigold, null, ReanimationType.Marigold, 24, 50, 6000, PlantSubClass.Normal, 2500, "MARIGOLD");
                };
                if (i == (int)SeedType.Melonpult)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Melonpult, null, ReanimationType.Melonpult, 14, XmlReader.MelonpultSuncost, 750, PlantSubClass.Shooter, XmlReader.MelonpultFiringSpeed, "MELON_PULT");
                };
                if (i == (int)SeedType.Gatlingpea)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Gatlingpea, null, ReanimationType.Gatlingpea, 5, XmlReader.GatlingPeasuncost, 5000, PlantSubClass.Shooter, XmlReader.GatlingPeaFiringSpeed, "GATLING_PEA");
                };
                if (i == (int)SeedType.Twinsunflower)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Twinsunflower, null, ReanimationType.TwinSunflower, 1, XmlReader.TwinSunflowersuncost, 5000, PlantSubClass.Normal, 2500, "TWIN_SUNFLOWER");
                };
                if (i == (int)SeedType.Gloomshroom)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Gloomshroom, null, ReanimationType.Gloomshroom, 27, XmlReader.Gloomshroomsuncost, 5000, PlantSubClass.Shooter, XmlReader.GloomshroomFiringSpeed, "GLOOM_SHROOM");
                };
                if (i == (int)SeedType.Cattail)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Cattail, null, ReanimationType.Cattail, 27, XmlReader.CattailSuncost, 5000, PlantSubClass.Shooter, XmlReader.CattailFiringSpeed, "CATTAIL");
                };
                if (i == (int)SeedType.Wintermelon)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Wintermelon, null, ReanimationType.WinterMelon, 27, XmlReader.WinterMelonsuncost, 5000, PlantSubClass.Shooter, XmlReader.WintermelonFiringSpeed, "WINTER_MELON");
                };
                if (i == (int)SeedType.GoldMagnet)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.GoldMagnet, null, ReanimationType.GoldMagnet, 27, XmlReader.GoldMagnetsuncost, 5000, PlantSubClass.Normal, 0, "GOLD_MAGNET");
                };
                if (i == (int)SeedType.Spikerock)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Spikerock, null, ReanimationType.Spikerock, 27, XmlReader.Spikerocksuncost, 5000, PlantSubClass.Normal, 0, "SPIKEROCK");
                };
                if (i == (int)SeedType.Cobcannon)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Cobcannon, null, ReanimationType.Cobcannon, 16, XmlReader.Cobcannonsuncost, 5000, PlantSubClass.Normal, 600, "COB_CANNON");
                };
                if (i == (int)SeedType.Imitater)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Imitater, null, ReanimationType.Imitater, 33, 0, 750, PlantSubClass.Normal, 0, "IMITATER");
                };
                if (i == (int)SeedType.ExplodeONut)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.ExplodeONut, null, ReanimationType.Wallnut, 2, 0, 3000, PlantSubClass.Normal, 0, "EXPLODE_O_NUT");
                };
                if (i == (int)SeedType.GiantWallnut)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.GiantWallnut, null, ReanimationType.Wallnut, 2, 0, 3000, PlantSubClass.Normal, 0, "GIANT_WALLNUT");
                };
                if (i == (int)SeedType.Sprout)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Sprout, null, ReanimationType.None, 33, 0, 3000, PlantSubClass.Normal, 0, "SPROUT");
                };
                if (i == (int)SeedType.Leftpeater)
                {
                    gPlantDefs[gPlantDefs.Length - 1] = new PlantDefinition(SeedType.Leftpeater, null, ReanimationType.Repeater, 5, 200, 750, PlantSubClass.Shooter, 150, "REPEATER");
                };
            };
            GameConstants.NUM_BACKUP_DANCERS = 4;
            GameConstants.MAX_ZOMBIE_FOLLOWERS = 4;
            GameConstants.ZOMBIE_WAVE_DEBUG = -1;
            GameConstants.ZOMBIE_WAVE_CUTSCENE = -2;
            GameConstants.ZOMBIE_WAVE_UI = -3;
            GameConstants.ZOMBIE_WAVE_WINNER = -4;
            GameConstants.RENDER_GROUP_SHIELD = 1;
            GameConstants.RENDER_GROUP_ARMS = 2;
            GameConstants.RENDER_GROUP_OVER_SHIELD = 3;
            GameConstants.RENDER_GROUP_BOSS_BACK_LEG = 4;
            GameConstants.RENDER_GROUP_BOSS_FRONT_LEG = 5;
            GameConstants.RENDER_GROUP_BOSS_BACK_ARM = 6;
            GameConstants.RENDER_GROUP_BOSS_FIREBALL_ADDITIVE = 7;
            GameConstants.RENDER_GROUP_BOSS_FIREBALL_TOP = 8;
            GameConstants.CHILLED_SPEED_FACTOR = 0.4f;
            GameConstants.ZOMBIE_LIMP_SPEED_FACTOR = 2;
            GameConstants.BUNGEE_ZOMBIE_HEIGHT = 3000;
            GameConstants.DOG_WALKING_DISTANCE = 31;
            GameConstants.POGO_BOUNCE_TIME = 80;
            GameConstants.DOLPHIN_JUMP_TIME = 120;
            GameConstants.THOWN_ZOMBIE_GRAVITY = 0.05f;
            GameConstants.TICKS_BETWEEN_EATS = 4;
            GameConstants.CLIP_HEIGHT_OFF = -200f;
            GameConstants.CLIP_HEIGHT_LIMIT = -100f;
            GameConstants.ZOMBIE_MINDCONTROLLED_COLOR = new SexyColor(128, 64, 192);
            GameConstants.ZOMBIE_BLINK_RATE = 400;
            GameConstants.BOSS_FLASH_HEALTH_FRACTION = 10;
            GameConstants.ZOMBIE_WALK_IN_FRONT_DOOR_Y = 290f;
            GameConstants.BOBSLED_CRASH_TIME = 150;
            GameConstants.YUCKI_PAUSE_TIME = 69;
            GameConstants.YUCKI_SHORT_PAUSE_TIME = 21;
            GameConstants.YUCKI_HOLD_TIME = GameConstants.YUCKI_PAUSE_TIME + 99;
            GameConstants.YUCKI_WALK_TIME = GameConstants.YUCKI_HOLD_TIME + 99;
            GameConstants.BOSS_BALL_OFFSET_Y = -90f;
            // 僵尸常量定义
            GameConstants.gZombieDefs = new ZombieDefinition[(int)ZombieType.ZombieTypesCount]
            {
                /*                 | ZombieType 枚举值        | 动画轨道类型               |价值|首现关|首现波|权重|名称| */
                new ZombieDefinition(ZombieType.Normal,         ReanimationType.Zombie,         1,  1,  1,  4000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.Flag,           ReanimationType.Zombie,         1,  1,  1,  0, "FLAG_ZOMBIE"),
                new ZombieDefinition(ZombieType.TrafficCone,    ReanimationType.Zombie,         2,  1,  1,  4000, "CONEHEAD_ZOMBIE"),
                new ZombieDefinition(ZombieType.Polevaulter,    ReanimationType.Polevaulter,    2,  1,  5,  2000, "POLE_VAULTING_ZOMBIE"),
                new ZombieDefinition(ZombieType.Pail,           ReanimationType.Zombie,         4,  1,  1,  3000, "BUCKETHEAD_ZOMBIE"),
                new ZombieDefinition(ZombieType.Newspaper,      ReanimationType.ZombieNewspaper,2,  1, 1,  1000, "NEWSPAPER_ZOMBIE"),
                new ZombieDefinition(ZombieType.Door,           ReanimationType.Zombie,         4,  1, 5,  3500, "SCREEN_DOOR_ZOMBIE"),
                new ZombieDefinition(ZombieType.Football,       ReanimationType.ZombieFootball, 7,  1, 5,  2000, "FOOTBALL_ZOMBIE"),
                new ZombieDefinition(ZombieType.Dancer,         ReanimationType.Disco,          5,  1, 5,  1000, "DANCING_ZOMBIE"),
                new ZombieDefinition(ZombieType.BackupDancer,   ReanimationType.BackupDancer,   1,  1, 1,  XmlReader.BackupDancerWeight, "BACKUP_DANCER"),
                new ZombieDefinition(ZombieType.DuckyTube,      ReanimationType.Zombie,         1,  1, 5,  0, "DUCKY_TUBE_ZOMBIE"),
                new ZombieDefinition(ZombieType.Snorkel,        ReanimationType.Snorkel,        3,  1, 10, 2000, "SNORKEL_ZOMBIE"),
                new ZombieDefinition(ZombieType.Zamboni,        ReanimationType.ZombieZamboni,  7,  1, 10, 2000, "ZOMBONI"),
                new ZombieDefinition(ZombieType.Bobsled,        ReanimationType.Bobsled,        3,  1, 10, 2000, "ZOMBIE_BOBSLED_TEAM"),
                new ZombieDefinition(ZombieType.DolphinRider, ReanimationType.ZombieDolphinrider,3, 1, 10, 1500, "DOLPHIN_RIDER_ZOMBIE"),
                new ZombieDefinition(ZombieType.JackInTheBox,   ReanimationType.Jackinthebox,   3,  1, 10, 1000, "JACK_IN_THE_BOX_ZOMBIE"),
                new ZombieDefinition(ZombieType.Balloon,        ReanimationType.Balloon,        2,  1, 10, 2000, "BALLOON_ZOMBIE"),
                new ZombieDefinition(ZombieType.Digger,         ReanimationType.Digger,         4,  1, 10, 1000, "DIGGER_ZOMBIE"),
                new ZombieDefinition(ZombieType.Pogo,           ReanimationType.Pogo,           4,  1, 10, 1000, "POGO_ZOMBIE"),
                new ZombieDefinition(ZombieType.Yeti,           ReanimationType.Yeti,           4,  1, 1,  1, "ZOMBIE_YETI"),
                new ZombieDefinition(ZombieType.Bungee,         ReanimationType.Bungee,         3,  1, 10, 1000, "BUNGEE_ZOMBIE"),
                new ZombieDefinition(ZombieType.Ladder,         ReanimationType.Ladder,         4,  1, 10, 1000, "LADDER_ZOMBIE"),
                new ZombieDefinition(ZombieType.Catapult,       ReanimationType.Catapult,       5,  1, 10, 1500, "CATAPULT_ZOMBIE"),
                new ZombieDefinition(ZombieType.Gargantuar,     ReanimationType.Gargantuar,     10, 1, 15, 1500, "GARGANTUAR"),
                new ZombieDefinition(ZombieType.Imp,            ReanimationType.Imp,            10, 1, 1,  XmlReader.ImpWeight, "IMP"),
                new ZombieDefinition(ZombieType.Boss,           ReanimationType.Boss,           10, 1, 1,  0, "BOSS"),
                new ZombieDefinition(ZombieType.PeaHead,        ReanimationType.Zombie,         1,  1, 1,  4000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.WallnutHead,    ReanimationType.Zombie,         4,  1, 1,  3000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.JalapenoHead,   ReanimationType.Zombie,         3,  1, 10, 1000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.GatlingHead,    ReanimationType.Zombie,         3,  1, 10, 2000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.SquashHead,     ReanimationType.Zombie,         3,  1, 10, 2000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.TallnutHead,    ReanimationType.Zombie,         4,  1, 10, 2000, "ZOMBIE"),
                new ZombieDefinition(ZombieType.RedeyeGargantuar,ReanimationType.Gargantuar,    10, 1, 15, 6000, "REDEYED_GARGANTUAR")
            };
            // 僵王召唤的僵尸类型
            GameConstants.gBossZombieList = new ZombieType[]
            {
                /*                 | ZombieType 枚举值        | 动画轨道类型               |价值|首现关|首现波|权重|名称| */
                ZombieType.TrafficCone,
                ZombieType.Pail,
                ZombieType.Football,
                ZombieType.Polevaulter,
                ZombieType.JackInTheBox,
                ZombieType.Ladder,
                ZombieType.Zamboni,
                ZombieType.Catapult,
                ZombieType.Pogo,
                ZombieType.Newspaper,
                ZombieType.Door,
                ZombieType.Gargantuar
            };
            GameConstants.TESTING_LOAD_BAR = false;
            GameConstants.BAR_FADE_TIME = 8;
            GameConstants.NUM_ALMANAC_REANIMS = 4;
            GameConstants.NUM_ALMANAC_SEEDS = 49;
            GameConstants.NUM_ALMANAC_ZOMBIES = 26;
            GameConstants.NUM_ALMANAC_ZOMBIES_PERF_TEST = 400;
            GameConstants.BUTTON_SIZE = 40;
            GameConstants.BUTTONS_PER_ROW = 10;
            GameConstants.gFlowerCenter = new LawnFPoint[]
            {
                new LawnFPoint(765f, 483f),
                new LawnFPoint(663f, 455f),
                new LawnFPoint(701f, 439f)
            };
            GameConstants.MUSIC_SLIDER_THRESHOLD = 0.01;
            GameConstants.gUserVersionTilJuly07 = 2;
            GameConstants.gUserVersionTilFeb08 = 3;
            GameConstants.gUserVersionTilApril08 = 4;
            GameConstants.gUserVersionTilMay08 = 5;
            GameConstants.gUserVersionTilSep08 = 8;
            GameConstants.gUserVersionTilNov08 = 9;
            GameConstants.gUserVersionTilJan09 = 10;
            GameConstants.gUserVersionTilApr09 = 11;
            GameConstants.gUserVersion = 13;
            // 子弹定义
            GameConstants.gProjectileDefinition = new ProjectileDefinition[(int)ProjectileType.ProjectilesCount]
            {
                /*                     | ProjectileType 枚举值 | ImageRow | 伤害值 |*/
                new ProjectileDefinition(ProjectileType.Pea,            0,  20  ),
                new ProjectileDefinition(ProjectileType.Snowpea,        0,  XmlReader.SnowpeaDamage  ),
                new ProjectileDefinition(ProjectileType.Cabbage,        0,  XmlReader.CabbagepultDamage  ),
                new ProjectileDefinition(ProjectileType.Melon,          0,  XmlReader.Melonpultdamage  ),
                new ProjectileDefinition(ProjectileType.Puff,           0,  20  ),
                new ProjectileDefinition(ProjectileType.Wintermelon,    0,  XmlReader.Wintermelondamage  ),
                new ProjectileDefinition(ProjectileType.Fireball,       0,  40  ),
                new ProjectileDefinition(ProjectileType.Star,           0,  XmlReader.StarfruitDamage  ),
                new ProjectileDefinition(ProjectileType.Spike,          0,  XmlReader.CactusDamage  ),
                new ProjectileDefinition(ProjectileType.Basketball,     0,  75  ),
                new ProjectileDefinition(ProjectileType.Kernel,         0,  XmlReader.KernelpultKerneldamage  ),
                new ProjectileDefinition(ProjectileType.Cobbig,         0,  300 ),
                new ProjectileDefinition(ProjectileType.Butter,         0,  XmlReader.KernelpultButterdamage  ),
                new ProjectileDefinition(ProjectileType.ZombiePea,      0,  20  ),
                new ProjectileDefinition(ProjectileType.ZombiePeaMindControl, 0, 20),
            };
            GameConstants.SEED_BANK_OFFSET_X = 0;
            GameConstants.SEED_BANK_OFFSET_X_END = 0;
        }

        public const int SURVIVAL_NORMAL_FLAGS = 5;

        public const int SURVIVAL_HARD_FLAGS = 10;

        public const int LAST_STAND_FLAGS = 5;

        public const int FINAL_LEVEL = 50;

        public const int LEVELS_PER_AREA = 10;

        public const float SOUND_EFFECT_VOLUME_FACTOR = 0.65f;

        public const int NUM_CHALLENGE_MODES = 122;

        public const int PRICE_MULTIPLIER = 10;

        public const int MINI_GAME_COUNT = 19;

        public const int I_ZOMBIE_LEVEL_COUNT = 10;

        public const int VASEBREAKER_LEVEL_COUNT = 10;

        public const int VASEBREAKER_ACHIEVEMENT = 15;

        public const int IZOMBIE_ACHIEVEMENT = 10;

        public const int LAWN_IMAGE_AVE_MS_TO_LOAD = 9;

        public const int LAWN_SOUND_AVE_MS_TO_LOAD = 54;

        public const int LAWN_FONT_AVE_MS_TO_LOAD = 54;

        public const int LAWN_PARTICLE_AVE_MS_TO_LOAD = 6;

        public const int LAWN_REANIM_AVE_MS_TO_LOAD = 68;

        public const int CRAVE_DAVE_BLINK_RATE = 400;

        public const int MAX_ZOMBIE_WAVES = 100;

        public const int MAX_ZOMBIES_IN_WAVE = 50;

        public const int MAX_ZOMBIE_TYPES = 100;

        public const int FOG_BLOW_RETURN_TIME = 2000;

        public const int FOG_CUTSCENE_TIME = 200;

        public const int NUM_FLAMES_IN_FWOOSH = 12;

        public const int NUM_FOG_ROWS = 7;

        public const int PROGRESS_METER_COUNTER = 150;

        public const int NUM_LEVELS = 50;

        public const int BOARD_SHAKE_TIME = 12;

        public const int FLAG_RAISE_TIME = 100;

        public const int ZOMBIE_COUNTDOWN_FIRST_WAVE = 1800;

        public const int ZOMBIE_COUNTDOWN = 2500;

        public const int ZOMBIE_COUNTDOWN_RANGE = 600;

        public const int ZOMBIE_COUNTDOWN_BEFORE_FLAG = 4500;

        public const int ZOMBIE_COUNTDOWN_BEFORE_REPICK = 5499;

        public const int ZOMBIE_COUNTDOWN_MIN = 400;

        public const int SUN_COUNTDOWN = 425;

        public const int SUN_COUNTDOWN_RANGE = 275;

        public const int SUN_COUNTDOWN_MAX = 950;

        public const int LAWN_MOWER_COIN_START = 200;//?

        public const int LAWN_MOWER_COIN_DELAY = 40;//?

        public const int LAWN_MOWER_COIN_END = 150;//?

        public const int MAX_RENDER_ITEMS = 2048;

        public const int ROOF_SLOPE_PER_ROW = 20;//?

        public const int ROOF_SLOPE_PER_ROW_OFF = 10;//?

        public const int BLINK_RATE = 400;

        public const int BLINK_RATE_WALLNUT = 1000;

        public const int GRAVE_BUSTER_EAT_TIME = XmlReader.GraveBusterEatingtime;

        public const int CRATER_TIME = XmlReader.DoomshroomCratertime;

        public const int MAX_MAGNET_ITEMS = 5;

        public const int RENDER_GROUP_PUMPKIN_BACK = 1;//?

        public const int WAKE_UP_TIME = 100;

        public const int SEEDBANK_MAX = 9;

        public const int SLOT_MACHINE_TIME = 400;

        public const int CONVEYOR_SPEED = 4;

        public const int CONVEYOR_PACKET_OFFSET_Y = 35;//?

        public const int CONVEYOR_PACKET_MIN_OFFSET = 40;//?

        public const int TICKS_PER_SECOND = 100;//?

        public const int REANIMATOR_LOAD_TASK_FACTOR = 0;//?

        public const int TAP_TAP_TO_PLANT = 1;//?

        public const int PARTNER_PREVIEW_MAX_DRIFT = 300;//?

        public const int NO_IMAGE_ID = 999999;//?

        public const int PRESENT_OFFSET_Y = 60;//?

        public const int MAX_CREDIT_SECTIONS = 57;//?

        public const int NUM_CLOUDS = 6;//?

        public const int NUM_FLOWERS = 3;//?

        public const int CLOUD_MOVE_TIME = 6000;//?

        public const int CLOUD_WAIT_TIME = 2000;//?

        public const int LEAF_WAIT_TIME = 200;//?

        public const int QUICKPLAY_SLIDE_COUNT = 30;//?

        public const int SLIDE_COUNT = 75;//?

        public const int MORE_GAMES_LIST_OFFSET = 52;//?

        public const int NUM_MOTION_TRAIL_FRAMES = 12;//?

        public const int CHOMP_TIME = 50;//?

        public const int MAX_MESSAGE_LENGTH = 128;//?

        public const int SLIDE_OFF_TIME = 100;//?

        public const int MIN_MESSAGE_TIME = 100;//?

        public const int MUSIC_ROW_FACTOR = 4;//?

        public const int BURST_FADE_IN_TIME = 400;//?

        public const int BURST_TIME_AFTER_START_TO_QUEUE_DRUMS = 300;//?

        public const int BURST_MIN_TIME = 800;//?

        public const int BURST_FADE_OUT_TIME = 800;//?

        public const int BURST_FOG_FADE_OUT_DELAY = 300;//?

        public const int DRUMS_FOG_FADE_OUT_TIME = 800;//?

        public const int DRUMS_FADE_OUT_TIME = 50;//?

        public const int LAWN_SONG_AVE_MS_TO_LOAD = 3500;//?

        public const int MAX_CHALLENGE_MODES = 200;

        public const int MAX_PURCHASES = 80;

        public const int NUM_PLACEHOLDER_INTS = 1;

        public const int MAX_POTTED_PLANTS = 200;

        public const int ITEM_GAP = 10;//?

        public const int MENU_BUTTON_TOP_OFFSET = 2;//?

        public const int STREET_GRID_SIZE_X = 5;//?

        public const int STREET_GRID_SIZE_Y = 5;//?

        public const int BEGHOULED_WINNING_SCORE = 75;

        public const int NUM_SQUIRRELS = 7;

        public const int SLOT_MACHINE_WINNING_SCORE = 2000;

        public const int ZOMBIQUARIUM_WINNING_SCORE = 1000;

        public const int IZOMBIE_WINNING_SCORE = 5;

        public const int NUM_TREE_CLOUDS = 6;//?

        public const int SLOT_MACHINE_COST = 25;

        public const int ART_CHALLEGE_SIZE_X = 9;

        public const int ART_CHALLEGE_SIZE_Y = 6;

        public const int STORM_FLASH_TIME = 150;

        public const int ICE_CHALLANGE_DELAY = 3000;

        public const int BEGHOULED_DELAY_BEFORE_HINT_FLASH = 1500;

        public const int BEGHOULED_DELAY_BEFORE_HINT_FLASH_AGAIN = 1500;

        public const int MAX_SCARY_POTS = 54;

        public const int RENDER_GROUP_TREE_BACKGROUND = 1;//?

        public const int RENDER_GROUP_TREE_TRUNK = 2;//?

        public const int RENDER_GROUP_TREE_GRASS = 3;//?

        public const int RENDER_GROUP_TREE_TOP = 4;//?

        public const int TREE_CLOUD_MOVE_TIME = 6000;//?

        public const int TREE_CLOUD_WAIT_TIME = 2000;//?

        public const int ZEN_GARDEN_FADE_DELAY = 3000;//?

        public const int STINKY_RENDER_ORDER_OFFSET = 30;//?

        public const float STINKY_COIN_OFFSET_Y = 30f;//?

        public static Achievement[] AchievementInfo;

        internal static int[,] gLawnDialogColors;

        public static SexyColor[] gGameButtonColors = new SexyColor[]
        {
            new SexyColor(0, 0, 0),
            new SexyColor(0, 0, 0),
            new SexyColor(0, 0, 0),
            new SexyColor(255, 255, 255),
            new SexyColor(132, 132, 132),
            new SexyColor(212, 212, 212)
        };

        public static ParticleParams[] gLawnParticleArray;

        public static ReanimationParams[] gLawnReanimationArray;

        public static TrailParams[] gLawnTrailArray;

        public static int gLawnStringFormatCount;

        public static TodStringListFormat[] gLawnStringFormats;

        // 冒险模式中每关的僵尸波数
        public static int[] gZombieWaves = new int[]
        {
                        4,  6,  8,  XmlReader.Level1_4_wavenum, 8,  XmlReader.Level1_6_wavenum, XmlReader.Level1_7_wavenum, XmlReader.Level1_8_wavenum, XmlReader.Level1_9_wavenum, XmlReader.Level1_10_wavenum,
            XmlReader.Level2_1_wavenum, XmlReader.Level2_2_wavenum, XmlReader.Level2_3_wavenum, XmlReader.Level2_4_wavenum, XmlReader.Level2_5_wavenum, XmlReader.Level2_6_wavenum, XmlReader.Level2_7_wavenum, XmlReader.Level2_8_wavenum, XmlReader.Level2_9_wavenum, XmlReader.Level2_10_wavenum,
            XmlReader.Level3_1_wavenum, XmlReader.Level3_2_wavenum, XmlReader.Level3_3_wavenum, XmlReader.Level3_4_wavenum, XmlReader.Level3_5_wavenum, XmlReader.Level3_6_wavenum, XmlReader.Level3_7_wavenum, XmlReader.Level3_8_wavenum, XmlReader.Level3_9_wavenum, XmlReader.Level3_10_wavenum,
            XmlReader.Level4_1_wavenum, XmlReader.Level4_2_wavenum, XmlReader.Level4_3_wavenum, XmlReader.Level4_4_wavenum, 1, XmlReader.Level4_6_wavenum, XmlReader.Level4_7_wavenum, XmlReader.Level4_8_wavenum, XmlReader.Level4_9_wavenum, XmlReader.Level4_10_wavenum,
            XmlReader.Level5_1_wavenum, XmlReader.Level5_2_wavenum, XmlReader.Level5_3_wavenum, XmlReader.Level5_4_wavenum, XmlReader.Level5_5_wavenum, XmlReader.Level5_6_wavenum, XmlReader.Level5_7_wavenum, XmlReader.Level5_8_wavenum, XmlReader.Level5_9_wavenum, 1,
        };

        public static ZombieAllowedLevels[] gZombieAllowedLevels;

        public static PlantDefinition[] gPlantDefs;

        public static int NUM_BACKUP_DANCERS;

        public static int MAX_ZOMBIE_FOLLOWERS;

        public static int ZOMBIE_WAVE_DEBUG;

        public static int ZOMBIE_WAVE_CUTSCENE;

        public static int ZOMBIE_WAVE_UI;

        public static int ZOMBIE_WAVE_WINNER;

        public static int RENDER_GROUP_SHIELD;

        public static int RENDER_GROUP_ARMS;

        public static int RENDER_GROUP_OVER_SHIELD;

        public static int RENDER_GROUP_BOSS_BACK_LEG;

        public static int RENDER_GROUP_BOSS_FRONT_LEG;

        public static int RENDER_GROUP_BOSS_BACK_ARM;

        public static int RENDER_GROUP_BOSS_FIREBALL_ADDITIVE;

        public static int RENDER_GROUP_BOSS_FIREBALL_TOP;

        public static float CHILLED_SPEED_FACTOR;

        public static int ZOMBIE_LIMP_SPEED_FACTOR;

        public static int BUNGEE_ZOMBIE_HEIGHT;

        public static int DOG_WALKING_DISTANCE;

        public static int POGO_BOUNCE_TIME;

        public static int DOLPHIN_JUMP_TIME;

        public static float THOWN_ZOMBIE_GRAVITY;

        public static int TICKS_BETWEEN_EATS;

        public static float CLIP_HEIGHT_OFF;

        public static float CLIP_HEIGHT_LIMIT;

        public static SexyColor ZOMBIE_MINDCONTROLLED_COLOR;

        public static int ZOMBIE_BLINK_RATE;

        public static int BOSS_FLASH_HEALTH_FRACTION;

        public static float ZOMBIE_WALK_IN_FRONT_DOOR_Y;

        public static int BOBSLED_CRASH_TIME;

        public static int YUCKI_PAUSE_TIME;

        public static int YUCKI_SHORT_PAUSE_TIME;

        public static int YUCKI_HOLD_TIME;

        public static int YUCKI_WALK_TIME;

        public static float BOSS_BALL_OFFSET_Y;

        public static ZombieDefinition[] gZombieDefs;

        public static ZombieType[] gBossZombieList;

        public static bool TESTING_LOAD_BAR;

        public static int BAR_FADE_TIME;

        public static int NUM_ALMANAC_REANIMS;

        public static int NUM_ALMANAC_SEEDS;

        public static int NUM_ALMANAC_ZOMBIES;

        public static int NUM_ALMANAC_ZOMBIES_PERF_TEST;

        public static int BUTTON_SIZE;

        public static int BUTTONS_PER_ROW;

        public static readonly LawnFPoint[] gFlowerCenter;

        public static double MUSIC_SLIDER_THRESHOLD;

        public static int gUserVersionTilJuly07;

        public static int gUserVersionTilFeb08;

        public static int gUserVersionTilApril08;

        public static int gUserVersionTilMay08;

        public static int gUserVersionTilSep08;

        public static int gUserVersionTilNov08;

        public static int gUserVersionTilJan09;

        public static int gUserVersionTilApr09;

        public static int gUserVersion;

        public static ProjectileDefinition[] gProjectileDefinition;

        internal static int SEED_BANK_OFFSET_X;

        internal static int SEED_BANK_OFFSET_X_END;
    }
}
