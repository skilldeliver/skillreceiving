import os
import sys
from datetime import datetime

current_day = str(datetime.now().day).zfill(2)

snippet = f"""
def part_one(data):
    pass

def part_two(data):
    pass

with open('inputs/day{current_day}.txt') as f:
    data = [p for p in f.read().split('\\n\\r')]
    print(part_one(data))
    print(part_two(data))
"""

def create_files()->None:
    """
    Creates files for the source code of the solution and
    the input of the exercise. 
    """
    source_code = f'day{current_day}.py'
    input_file = f'inputs/day{current_day}.txt'

    with open(source_code, 'w') as f, open(input_file, 'w') as _:
        f.write(snippet)

    print(f'Day{current_day}. files created!')

def main()->None:
    """
    Main function to create or run files.
    First if it is missing the files for the current day -
            it will create them.
    Then launcher.py runs the current day.
    If an argument is passed for example launcer.py 5 -
            it will run the file for the passed day.
    """

if __name__ == '__main__':
    if len(os.listdir('inputs/')) != int(current_day):
        create_files()
    else:
        if len(sys.argv) > 1:
                current_day = sys.argv[1].zfill(2)
        print(f'Answers for Day{current_day}:')
        os.system(f'python day{current_day}.py')