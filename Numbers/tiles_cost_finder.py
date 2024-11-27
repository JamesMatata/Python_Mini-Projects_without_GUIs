"""
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, 
using a cost entered by the user.
"""

def get_int_value(what):
    not_int = True
    while not_int:
        user_input = input(f'Enter the {what}: ')
        try:
            value = float(user_input)
            return value
        except ValueError:
            print('Please enter an integer or float')
            continue
        except:
            print('Error provide the value again')
            continue
        

print('\n' + 'Total tile cost Calculator'.center(70, '-') + '\n')
width = get_int_value('Width(cm)')
length = get_int_value('Length(cm)')

unit_cost = get_int_value('cost per 100cm2')

area = length*width

total_units = area/100

total_cost = total_units*unit_cost

print('\n')
print(''.center(70, '#'))

print(f'The total cost of the {total_units} units is {total_cost}'.center(70, ' '))
print('\n')

