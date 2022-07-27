'''
Level 3 Mad Libs Project Example

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

Notes:
    - Make sure your students fill out the project planner worksheet
      before beginning project
    - Emphasize the need for commenting their code even for simple
      projects
    - Students may also need a reminder to use proper variable naming
      conventions

Mad Lib Source:

https://thechirpingmoms.com/wp-content/uploads/2015/08/campingmadlib2.jpg
'''

# let the user know what type of input is needed
print('\nPlease enter words of the following types:\n')

# request user input with associated prompt
nouns = []

for noun in range(11):
  nouns.append(input('Noun: '))

noun_place = input('Noun(Place): ')

verbs = []

for verb in range(2):
  verbs.append(input('Verb: '))

adjectives = []

for adjectives in range(2):
  adjectives.append(input('Adjective: '))

# output mad lib with filled in blanks from user's words
print(f'{nouns[0]} and {nouns[1]} wanted to go camping.')
print('First they needed a tent. They decided to make a tent')
print(f'out of {nouns[2]} and {nouns[3]}. Next they')
print('packed other things they would need for camping like')
print(f'{nouns[4]} and {nouns[5]}. They were')
print(f'ready to go! They started {verbs[0]} into the woods.')
print(f'They got nervous when they saw a {nouns[6]}.')
print(f'Then they realized it was just a silly {nouns[7]}.')
print(f'When they found a campsite they unpacked the {nouns[8]}')
print(f'and then decided to go {verbs[1]}. Now they were tired')
print('and asked their parents to help them make a campfire. They used')
print(f'{nouns[9]} and {nouns[10]} to build a fire. It was very')
print(f'{adjectives[0]}. They sat around the campfire telling {adjectives[1]}')
print('stories. Finally it was time to go to sleep. They had a great camping')
print(f'trip! Next time they want to camp at the {noun_place}!')