birthdays = {'Jon': 'July 17', 'Shauna': 'Jan 27', 'Lynette': 'July 10'}

while True:
    print("Who's birthday is it that you are looking for? To cancel, press enter!")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have that person's name in my archives. Would you like to add it? Press Y or N")
        answer = input()
        if answer == 'Y':
            new_name = name
            print("Please enter their birthday")
            new_birthday = input()
            birthdays[name] = new_birthday
            print('It has been added')
            print(new_name + "'s birthday has been added as " + new_birthday)
            print('Here is a list of birthdays you have saved...')
            print(birthdays)
        else:
            print('Alrighty Then')