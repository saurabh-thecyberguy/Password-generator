import random
alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['0','1','2','3','4','5','6','7','8','9']
special_char=['!','#','@','$','%','^','&','*','(',')','_','-','+']

total=int(input("Kindly specify the length of the password: "))
total_num=int(input("How many numbers you want in your password: "))
total_spec=int(input("How many special character you want in your pasword: "))

total_char=total-(total_num+total_spec)
rand_pwd=''
rand_list_pwd=[]
for char in range(0,total_char):
  rand_pwd+=alpha[random.randint(0,len(alpha)-1)]
  rand_list_pwd+=random.choice(alpha)

# print(rand_char)
# print(rand_char[0])

for n in range(0,total_num):
  rand_pwd+=num[random.randint(0,len(num)-1)]
  rand_list_pwd+=random.choice(num)
  


for sym in range(0,total_spec):
  rand_pwd+=special_char[random.randint(0,len(special_char)-1)]
  rand_list_pwd+=random.choice(special_char)
  
#print(rand_pwd)

#first way to derive password
password=''
for pwd in range(0,len(rand_pwd)-1):
  password+=rand_pwd[random.randint(0,len(rand_pwd)-1)]
print(f"Complecated password 1: {password}\n")

#second way to derive password
random.shuffle(rand_list_pwd)
#print(rand_list_pwd)
psd=''
for pwd in range(0,len(rand_list_pwd)-1):
  psd+=random.choice(rand_list_pwd)
print(f"Complecated password 2: {psd}")
  
