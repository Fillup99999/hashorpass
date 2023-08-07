#Intro
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
def generate_wordlist(inputs):
    elements = inputs
    wordlist = []
    total_combinations = 0
    for i in range(1, len(elements) + 1):
        for combo in itertools.permutations(elements, i):
            word = ''.join(combo)
            if len(word) <= 12 and len(word) >= 6:
                total_combinations += 1
                wordlist.append(word)
                if total_combinations % 5000 == 0:
                    print("LOADING...",total_combinations, "passwords")
    print(str(total_combinations) + " passwords enumerated.")
    if total_combinations > 50000:
        question = input("The output is greater than 50,000 words (" + str(total_combinations) + ") do you want to continue? If you don't have a decent cpu you may want to cancel: (y/n)")
        if question.lower() == "y":
            return wordlist
        else:
            print("Action cancelled.")
    elif total_combinations <= 50000:
        return wordlist
    else:
        print("Error in generate_wordlist function.")


#Export to file function:
def export_list_to_file(word_list):
    with open("wordlist.txt", "w") as f:
        for item in word_list:
            f.write(str(item) + "\n")


#Master list creation:
masslist = []


#Input options for if no arguments were passed:

#Target Name
if args.name:
    target_name_split = args.name.split(",")
    target_first_name = target_name_split[0]
    target_last_name = target_name_split[1]
    target_middle_name = target_name_split[2]
    target_middle_i = target_middle_name[0]
    target_first_i = target_first_name[0]
    target_last_i = target_last_name[0]
    #Add to masslist
    for i in [target_last_i, target_first_i, target_first_name,target_last_name,target_middle_name,target_middle_i]:
        masslist.append(i)

#else:
#    target_first_name = input("Enter the target's first name: ")
#    target_last_name = input("Enter the target's last name: ")
#    target_middle_name = input("Enter the target's middle name or initial: ")
#    target_middle_i = target_middle_name[0]
#    target_first_i = target_first_name[0]
#    target_last_i = target_last_name[0]
#    #Add to masslist
#    for i in [target_last_i, target_first_i, target_first_name,target_last_name,target_middle_name,target_middle_i]:
#        masslist.append(i)


#Target DOB
if args.dob:
    dob_split = args.dob.split(".")
    birthyyyy = dob_split[2]
    birthyy = dob_split[3]
    birthmm = dob_split[0]
    birthdd = dob_split[1]
    #Add to masslist
    for i in [birthyyyy,birthyy,birthmm,birthdd]:
        masslist.append(i)

#else:
#    date_of_birth = input("Enter the Date of Birth: mm.dd.yyyy.yy: ")
#    dob_split = date_of_birth.split(".")
#    birthyyyy = dob_split[2]
#    birthyy = dob_split[3]
#    birthmm = dob_split[0]
#    birthdd = dob_split[1]
    #Add to masslist
#    for i in [birthyyyy,birthyy,birthmm,birthdd]:
#        masslist.append(i)


#None default remaining options:

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
    #Add to masslist
    for i in [baename,baemm,baedd,baeyyyy,baeyy]:
        masslist.append(i)


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
    #Add to masslist
    for i in [kidname,kidmm,kiddd,kidyyyy,kidyy]:
        masslist.append(i)


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
    #Add to masslist
    for i in [kid2name,kid2mm,kid2dd,kid2yyyy,kid2yy]:
        masslist.append(i)


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
    #Add to masslist
    for i in [kid3name,kid3mm,kid3dd,kid3yyyy,kid3yy]:
        masslist.append(i)


#Pets/Friends
if args.pet:
    petlist = args.pet.split(",")
    pet1 = petlist[0]
    masslist.append(pet1)
    if len(petlist) >= 2:
        pet2 = petlist[1]
        masslist.append(pet2)
    else: pass
    if len(petlist) >= 3:
        pet3 = petlist[2]
        masslist.append(pet3)
    else: pass
    if len(petlist) >= 4:
        pet4 = petlist[3]
        masslist.append(pet4)
    else: pass
    if len(petlist) == 5:
        pet5 = petlist[4]
        masslist.append(pet5)
    else: pass 


#Sports
if args.sport:
    sportlist = args.sport.split(",")
    sport1 = sportlist[0]
    masslist.append(sport1)
    if len(sportlist) >= 2:
        sport2 = sportlist[1]
        masslist.append(sport2)
    else: pass
    if len(sportlist) >= 3:
        sport3 = sportlist[2]
        masslist.append(sport3)
    else: pass
    if len(sportlist) >= 4:
        sport4 = sportlist[3]
        masslist.append(sport4)
    else: pass
    if len(sportlist) == 5:
        sport5 = sportlist[4]
        masslist.append(sport5)
    else: pass


#Important Years
if args.yrs:
    yrslist = args.yrs.split(",")
    yr1 = yrslist[0]
#last two year digits
    shyr1 = yr1[2:]
    masslist.append(yr1)
    masslist.append(shyr1)
    if len(yrslist) >= 2:
        yr2 = yrslist[1]
        shyr2 = yr2[2:]
        masslist.append(yr2)
        masslist.append(shyr2)
    else: pass
    if len(yrslist) >= 3:
        yr3 = yrslist[2]
        shyr3 = yr3[2:]
        masslist.append(yr3)
        masslist.append(shyr3)
    else: pass
    if len(yrslist) >= 4:
        yr4 = yrslist[3]
        shyr4 = yr4[2:]
        masslist.append(yr4)
        masslist.append(shyr4)
    else: pass
    if len(yrslist) == 5:
        yr5 = yrslist[4]
        shyr5 = yr5[2:]
        masslist.append(yr5)
        masslist.append(shyr5)
    else: pass


#Keywords
if args.key:
    keylist = args.key.split(",")
    key1 = keylist[0]
    masslist.append(key1)
    if len(keylist) >= 2:
        key2 = keylist[1]
        masslist.append(key2)
    else: pass
    if len(keylist) >= 3:
        key3 = keylist[2]
        masslist.append(key3)
    else: pass
    if len(keylist) >= 4:
        key4 = keylist[3]
        masslist.append(key4)
    else: pass
    if len(keylist) >= 5:
        key5 = keylist[4]
        masslist.append(key5)
    else: pass
    if len(keylist) >= 6:
        key6 = keylist[5]
        masslist.append(key6)
    else: pass
    if len(keylist) >= 7:
        key7 = keylist[6]
        masslist.append(key7)
    else: pass
    if len(keylist) >= 8:
        key8 = keylist[7]
        masslist.append(key8)
    else: pass
    if len(keylist) >= 9:
        key9 = keylist[8]
        masslist.append(key9)
    else: pass
    if len(keylist) == 10:
        key10 = keylist[9]
        masslist.append(key10)
    else: pass

#Call generator function
outputlist = []
wordlist1 = generate_wordlist(masslist)
wordlist2 = []
wordlist3 = []

#Special characters
for i in wordlist1:
    x = i + "$"
    wordlist2.append(x)
for i in wordlist1:
    y = i + "!"
    wordlist3.append(y)

#Outputlist merging all lists
outputlist += wordlist1
outputlist += wordlist2
outputlist += wordlist3



#Call export_list_to_file
export_list_to_file(outputlist)

#Success Statement
print("Complete. Open wordlist.txt and export to desired location.")











###################################### Alternate Routes? ###############################################
#Password Generator:
#import random
#import string

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