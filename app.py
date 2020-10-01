import random

#Open the txt file and store it into a variable
input_file = open('./poem.txt', 'r')


line_list = input_file.readlines()
#Function to print every line of the txt file
def get_file_lines(poem):
    all_lines = []
    for line in poem:
        all_lines.append(line)
    return all_lines

print(get_file_lines(line_list))
print("--------------------------")
print("--------------------------")

#Function to print the entire poem starting with last line
def lines_printed_backwards(poem):
    #Store each line from the poem into a list
    line_list = [line.strip() for line in poem]
        #Reverse the list and print each line in the reversed order
    for line in reversed(line_list):
        print(line)

lines_printed_backwards(line_list)
print("--------------------------")
print("--------------------------")

#Function to randomly print a line from the poem for the length of the poem
def lines_printed_random(poem):

    line_list = [line.strip() for line in poem]
    #Get the length of the list minus 1 since the first object is 0
    length = len(line_list) - 1
    #Make a loop that only runs the length of the poem and gets a random num from 0 to the length and print 
    # the line that matches that list id
    for _ in range(0, length):
        random_num = random.randint(0, length)
        print(line_list[random_num])

    
lines_printed_random(line_list)   
print("--------------------------")
print("--------------------------")

def lines_printed_custom(poem):
    line_list = [line.strip() for line in poem]
    #Printing each line in all uppercase
    for line in line_list:
        print(line.upper())

lines_printed_custom(line_list)