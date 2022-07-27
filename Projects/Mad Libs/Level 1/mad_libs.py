'''
Level 1 Mad Libs Project Example

Required Knowlege:
    - Variables
    - Data Types
        - String
    - Comments
    - Print Function
    - Input Function
    - String Concatenation

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
noun_one = input('Noun: ')
noun_two = input('Noun: ')
noun_three = input('Noun: ')
noun_four = input('Noun: ')
noun_five = input('Noun: ')
noun_six = input('Noun: ')
noun_seven = input('Noun: ')
noun_eight = input('Noun: ')
noun_nine = input('Noun: ')
noun_ten = input('Noun: ')
noun_eleven = input('Noun: ')
noun_twelve = input('Noun(Place): ')

verb_one = input('Verb: ')
verb_two = input('Verb: ')

adjective_one = input('Adjective: ')
adjective_two = input('Adjective: ')

# output mad lib with filled in blanks from user's words
print(noun_one + ' and ' + noun_two + ' wanted to go camping.')
print('First they needed a tent. They decided to make a tent')
print('out of ' + noun_three + ' and ' + noun_four + '. Next they')
print('packed other things they would need for camping like')
print(noun_five + ' and ' + noun_six + '. They were')
print('ready to go! They started ' + verb_one + ' into the woods.')
print('They got nervous when they saw a ' + noun_seven + '.')
print('Then they realized it was just a silly ' + noun_eight + '.')
print('When they found a campsite they unpacked the ' + noun_nine)
print('and then decided to go ' + verb_two + '. Now they were tired')
print('and asked their parents to help them make a campfire. They used')
print(noun_ten + ' and ' + noun_eleven + ' to build a fire. It was very')
print(adjective_one + '. They sat around the campfire telling ' + adjective_two)
print('stories. Finally it was time to go to sleep. They had a great camping')
print('trip! Next time they want to camp at the ' + noun_twelve + '!')