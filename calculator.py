
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lower_name1 = name1.lower()
lower_name2 = name2.lower()
names = lower_name1 + lower_name2
count_name1_t = names.count("t")
count_name1_r = names.count("r")
count_name1_u = names.count("u")
count_name1_e = names.count("e")
total_letters_true = count_name1_t + count_name1_r + count_name1_u + count_name1_e

count_name1_l = names.count("l")
count_name1_o = names.count("o")
count_name1_v = names.count("v")
count_name1_e = names.count("e")
total_letters_love = count_name1_l + count_name1_o + count_name1_v + count_name1_e

total_number = int(str(total_letters_true) + str(total_letters_love)) 

if (total_number < 10 or total_number > 90):
  print (f"your score is {total_number}, you go together like coke and mentos")
elif (total_number >= 40 and total_number >= 50):
  print (f"your score is {total_number}, you're alright together.")
else: 
  print(f"your score is {total_number}")




