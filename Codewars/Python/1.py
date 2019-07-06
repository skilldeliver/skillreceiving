from collections import namedtuple

def validateBattlefield(field):
    battleship, cruisers, destroyers, submarines = 1, 2, 3, 4
    Ship = namedtuple('Ship', 'points horizontally')

    for row in field:
        for cell in row:
            if cell == 1:
                ship_cell = right_check_all(cords, field)
                if len(ship) == 1:
                    ship_points = down_check_all(cords, field)
                
                
                
                
    return True

def right_check_all(cords, field):
    ship = [cords]
    while (cords['x'] + 1) in range(10):
        cords['x'] += 1
        if field[cords['y']][cords['x']] == 1:
            ship.append(cords)
        else:
            return ship
    return ship

def down_check_all(cords, field):
    ship = [cords]
    while (cords['y'] + 1) in range(10):
        cords['y'] += 1
        if field[cords['y']][cords['x']] == 1:
            ship.append(cords)
        else:
            return ship
    return ship


battleField = [  [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

[
 ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09'],
 ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
 ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
 ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
 ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49'],
 ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
 ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
 ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
 ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89'],
 ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99'],
]