# When you join a hockey team you get your name on the back of the jersey
# but the jersey may not be big enough to hold all the letters
# Ask the user for their first name
first_name = input("Please give me your first name: ").capitalize()
first_len = len(first_name)

# Ask the user for their last name
last_name = input("Please give me your last name: ").capitalize()
last_len = len(last_name)

# if first name is < 10 characters and last name is < 10 characters 
#       print first and last name on the jersey
# if first name >= 10 characters long and last name is < 10 characters
#       print first initial of first name and the entire last name
# if first name < 10 characters long and last name is >= 10 characters
#       print entire first name and first initial of last name
# if first name >= 10 characters long and last name is >= 10 characters
#       print last name only

# Test with the following values
# first name: Susan  last name: Ibach
# output: Susan Ibach
# first name: Susan  last name: ReallyLongLastName
# output: Susan R.
# first name: ReallyLongFirstName  last name: Ibach
# output: R. Ibach
# first name: ReallyLongFirstName  last name: ReallyLongLastName
# output: ReallyLongLastName

if last_len < 10:
   if first_len < 10:
      print (f'{first_name} {last_name}')
   else:
      print (f'{first_name[0]}. {last_name}')
else:
   if first_len < 10:
      print(f'{first_name} {last_name[0]}.')
   else:
      print(last_name)
      
      