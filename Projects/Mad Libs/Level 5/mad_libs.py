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
    - With Statement
    - Enumerate Function
    - File Handling
        - open file
        - access modes
        - close file
    - Function Creation
        - type hinting

Notes:
    - Make sure your students fill out the project planner worksheet
      before beginning project
    - Emphasize the need for commenting their code even for simple
      projects
    - Students may also need a reminder to use proper variable naming
      conventions
    - Students may also need a reminder to use proper function naming
      conventions
    - Students may also need a reminder to type hint their function

Mad Lib Source:
    - https://thechirpingmoms.com/wp-content/uploads/2015/08/campingmadlib2.jpg
'''

def readlines_from_file(file_path: str) -> list[str]:
  """
  Description:
  -----------
  reads file into a list of lines

  Parameters:
  -----------
  file_path: str
    - path to file
  
  Return:
  ----------
  lines: list[str]
    - list of each in in file
  """
  with open(file_path, 'r') as f:
    lines = f.readlines()
  return lines

def replace_parts_of_speech(lines: list[str]) -> list[str]:
  """
  Description:
  -----------
  requests user input for each instance of parts of speech
  in mad lib

  Parameters:
  -----------
  lines: list[str]
    - list of each line in mad lib
  
  Return:
  ----------
  lines: list[str]
    - list of each line in mad lib updated with user input
  """
  for index, line in enumerate(lines):
    while '[' in line:
      word_type = line[line.index('[') + 1: line.index(']')]
      word = input(f'{word_type}: ')
      line = line.replace(f'[{word_type}]', f'{word}', 1)
    lines[index] = line
  return lines

def print_mad_lib(lines: list[str]) -> None:
  """
  Description:
  -----------
  displays mad lib in terminal

  Parameters:
  -----------
  lines: list[str]
    - list of each line in mad lib
  
  Return:
  ----------
  None
  """
  for line in lines:
    print(line, end='')

def main() -> None:
  mad_lib = readlines_from_file('MadLibs/Text Files/camping_mad_lib.txt')
  print('\nPlease enter words of the following types:\n')
  mad_lib = replace_parts_of_speech(mad_lib)
  print_mad_lib(mad_lib)

if __name__ == '__main__':
  main()