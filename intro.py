# Intro to Python ################################################################################
# print("Hello World")

# Strings #######################################################################################
my_message = 'Aayushi\'s World'
message = '''Tom and Jerry 
was a good cartoon'''
# print(my_message, message, len(my_message), my_message[7], my_message[:7], 
#       my_message[10:], my_message.lower(), my_message.upper(), my_message.count("s"),
#       my_message.find("World"), my_message.find("Universe"))

new_message = my_message.replace("World", "Universe")
# print(my_message, new_message)

greeting = "Hello"
name = "Erisha"
# new_greeting = '{}, {}. Welcome!'.format(greeting, name)
new_greeting = f'{greeting}, {name.upper()}. Welcome!'
# print(new_greeting)

# print(dir(name))
# print(help(str))
print(help(str.lower))