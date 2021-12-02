import random
from playsound import playsound

Catchphrazes = ['"Large Objects with small brains!"',
            '"About as useful as a fishnet condom!"',
            '"Die, will you?"',
            '"Let’s remember Ms. Wormwood!"', 
            '"That’s my finger doing BAD things!"', 
            '"Wham!"',
            '"That is a speeding bullet heading straight to the heart of your program!"',
            '"The result is death!"', 
            '"Oh god, that is horrible. I would never wish that upon someone."', 
            '"The PFM stands for "Putrid Food Management", "Pray For Me", and "Prevented From Matication""',
            '"Are you ready to die?!?!"',
            '"Your misery translates into my enjoyment"', 
            '"There is not a teacher in this world worth a dam, that does not have a sadistic streak a mile wide"']

#SoundFilez = [,,,,,,,,,,,,]

indexerizer = random.randint(0,12)

print(Catchphrazes[indexerizer])
#playsound('/path/file.mp3')