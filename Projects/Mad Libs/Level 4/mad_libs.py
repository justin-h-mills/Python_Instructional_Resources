'''
Level 4 Mad Libs Project Example

Required Knowlege:
    - Variables
    - Data Types
        - String
        - List
    - Comments
    - Print Function
    - Input Function
    - String Formatting
    - For Loop Statement
    - Range Function
    - Len Function
    - While Loop Statement
    - Replace Function
    - File Handling
        - open file
        - access modes
        - close file

Notes:
    - Make sure your students fill out the project planner worksheet
      before beginning project
    - Emphasize the need for commenting their code even for simple
      projects
    - Students may also need a reminder to use proper variable naming
      conventions
    - Students may also need a reminder to close file after use

Mad Lib Source:
    - https://thechirpingmoms.com/wp-content/uploads/2015/08/campingmadlib2.jpg
'''

# open and read mad lib file
mad_lib = open('MadLibs/Text Files/camping_mad_lib.txt', 'r')

# read file into line list
mad_lib_lines = mad_lib.readlines()

# close file
mad_lib.close()

# let the user know what type of input is needed
print('\nPlease enter words of the following types:\n')

# loop through mad lib lines
for index in range(len(mad_lib_lines)):
  # replace instances of parts of speech with user input
  while '[' in mad_lib_lines[index]:
    word_type = mad_lib_lines[index][mad_lib_lines[index].index('[') + 1: mad_lib_lines[index].index(']')]
    word = input(f'{word_type}: ')
    mad_lib_lines[index] = mad_lib_lines[index].replace(f'[{word_type}]', f'{word}', 1)

# print each updated mad lib lines
for line in mad_lib_lines:
  print(line, end='')