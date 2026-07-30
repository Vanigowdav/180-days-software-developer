#User name and Email generator 
first_name = "Anan"
last_name = "Virat"
full_name = first_name + ' ' + last_name
birth_year = 1998
year = str(birth_year)
username_birth_year = first_name[0:4] + year[-2:]
print("Name_and_Year:",username_birth_year)
email = f'{first_name}.{last_name}@gmail.com'
print("Email:",email)
privacy = f'{first_name} {last_name[0]}**{last_name[-1]}'
print('Privacy:', privacy)