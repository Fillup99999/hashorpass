import argparse
import itertools

print("""Welcome to #ash or Pass?
for help with extra options and keywords rerun as './hashorpass.py -h' basic options are prompted.""")

#Options to pass arguments, this is optional and some of the options will be prompted if not selected.
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="Enter the target's name: 'first,last,middle'")
parser.add_argument("--dob", help="Enter the DOB 'mm.dd.yyyy.yy'")
parser.add_argument("--bae", help="Enter spouse/partner's name = 'first,mm.dd.yyyy.yy'")
parser.add_argument("--kid", help="Enter favorite child's name and dob = 'stephanie,mm.dd.yyyy.yy'")
parser.add_argument("--kid2", help="Enter child's name = 'franklin,mm.dd.yyyy.yy'")
parser.add_argument("--kid3", help="Enter child's name = 'richierich,mm.dd.yyyy.yy'")
parser.add_argument("--pet", help="Enter up to 5 pet or friend names = 'spike,spot,keke,glubglub'")
parser.add_argument("--sport", help="Enter favorite sport teams and chants (up to 5 inputs) 'blueeagles,tokyostars,benchwarmers'")
parser.add_argument("--yrs", help="Enter up to 5 important years '1945,1776,0033'")
parser.add_argument("--key", help="Enter up to 10 keywords or hobbies 'photography,butts,hacking'")
parser.add_argument("-a", action="store_true", help="option a")
parser.add_argument("-b", action="store_true", help="option b")
parser.add_argument("-c", action="store_true", help="option c")
parser.add_argument("-d", action="store_true", help="option d")
args = parser.parse_args()

#Word List Generator:
def generate_wordlist(*inputs):
    elements = inputs
    wordlist = []

    for i in range(1, len(elements) + 1):
        for combination in itertools.permutations(elements, i):
            word = ''.join(combination)
            if len(word) <= 12 and len(word) >= 6:
                wordlist.append(word)
    return wordlist


#Input options for if no args were passed.

if args.name:
      target_name_split = args.name.split(",")
      target_first_name = target_name_split[0]
      target_last_name = target_name_split[1]
      target_middle_name = target_name_split[2]
      target_middle_i = target_middle_name[0]
      target_first_i = target_first_name[0]
      target_last_i = target_last_name[0]

else:
      target_first_name = input("Enter the target's first name: ")
      target_last_name = input("Enter the target's last name: ")
      target_middle_name = input("Enter the target's middle name or initial: ")
      target_middle_i = target_middle_name[0]
      target_first_i = target_first_name[0]
      target_last_i = target_last_name[0]

if args.dob:
      dob_split = args.dob.split(".")
      birthyyyy = dob_split[2]
      birthyy = dob_split[3]
      birthmm = dob_split[0]
      birthdd = dob_split[1]
else:
      date_of_birth = input("Enter the Date of Birth: mm.dd.yyyy.yy: ")
      splitbirth = date_of_birth.split(".")
      birthyyyy = splitbirth[2]
      birthyy = splitbirth[3]
      birthmm = splitbirth[0]
      birthdd = splitbirth[1]


#Remaining options:

#Spouse/Partner
if args.bae:
    baelist = args.bae.split(",")
    baename = baelist[0]
    baedob = baelist[1]
    baedoblist = baedob.split(".")
    baemm = baedoblist[0]
    baedd = baedoblist[1]
    baeyyyy = baedoblist[2]
    baeyy = baedoblist[3]

#Favorite Kid
if args.kid:
    kidlist = args.kid.split(",")
    kidname = kidlist[0]
    kiddob = kidlist[1]
    kiddoblist = kiddob.split(".")
    kidmm = kiddoblist[0]
    kiddd = kiddoblist[1]
    kidyyyy = kiddoblist[2]
    kidyy = kiddoblist[3]

#Kid 2
if args.kid2:
    kid2list = args.kid2.split(",")
    kid2name = kid2list[0]
    kid2dob = kid2list[1]
    kid2doblist = kid2dob.split(".")
    kid2mm = kid2doblist[0]
    kid2dd = kid2doblist[1]
    kid2yyyy = kid2doblist[2]
    kid2yy = kid2doblist[3]

#Kid 3
if args.kid3:
    kid3list = args.kid3.split(",")
    kid3name = kid3list[0]
    kid3dob = kid3list[1]
    kid3doblist = kid3dob.split(".")
    kid3mm = kid3doblist[0]
    kid3dd = kid3doblist[1]
    kid3yyyy = kid3doblist[2]
    kid3yy = kid3doblist[3]

#Pets/Friends
if args.pet:
    petlist = args.pet.split(",")
    pet1 = petlist[0]
    pet2 = petlist[1]
    pet3 = petlist[2]
    pet4 = petlist[3]
    pet5 = petlist[4]

#Sports
if args.sport:
    sportlist = args.sport.split(",")
    sport1 = sportlist[0]
    sport2 = sportlist[1]
    sport3 = sportlist[2]
    sport4 = sportlist[3]
    sport5 = sportlist[4]

#Important Years
if args.yrs:
    yrslist = args.yrs.split(",")
    yr1 = yrslist[0]
#last two year digits
    shyr1 = yr1[2:]
    yr2 = yrslist[1]
    shyr2 = yr2[2:]
    yr3 = yrslist[2]
    shyr3 = yr3[2:]
    yr4 = yrslist[3]
    shyr4 = yr4[2:]
    yr5 = yrslist[4]
    shyr5 = yr5[2:]

#Keywords
if args.key:
    keylist = args.key.split(",")
    key1 = keylist[0]
    key2 = keylist[1]
    key3 = keylist[2]
    key4 = keylist[3]
    key5 = keylist[4]
    key6 = keylist[5]
    key7 = keylist[6]
    key8 = keylist[7]
    key9 = keylist[8]
    key10 = keylist[9]


print(target_first_name,target_last_name,target_middle_name,target_middle_i,date_of_birth, splitbirth, birthyyyy, birthyy, birthmm, birthdd)
#print(baelist, baename,baedob,baedoblist,baemm,baedd,baeyyyy,baeyy)
wordlist1 = generate_wordlist(target_last_i, target_first_i, target_first_name,target_last_name,target_middle_name,target_middle_i,birthyyyy,birthyy,birthdd,birthmm)
print(wordlist1)


#SAMPLEEEE
#Password Generator:
#import random
#
# import string

# Custom password generation
#def generate_custom_password():
    # Implement your custom password generation logic here
    # This can include combining different elements, patterns, or using specific rules
    # Here's a simple example:
    #password = target_first_name.lower() + target_last_name.lower() + random.choice(string.digits)
    #return password

# Brute force password generation using a word list
#def generate_brute_force_password():
    #word_list = ["apple", "banana", "cherry", "orange", "grape"]
    #password = random.choice(word_list) + random.choice(word_list) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)
    #return password


# Generate passwords
#passwords = []
#for _ in range(5):  # Generate 5 passwords
    #if random.random() < 0.5:  # 50% chance of using custom password generation
        #password = generate_custom_password()
    #else:  # 50% chance of using brute force password generation
        #password = generate_brute_force_password()
    #passwords.append(password)

# Print the generated passwords
#for password in passwords:
    #print(password)