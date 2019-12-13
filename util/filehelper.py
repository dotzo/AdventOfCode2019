def lines_to_list(file, to_type=int):
    return [*map(to_type, open(file, 'r').readlines())]

def csv_to_list(file, to_type=int):
    return [*map(to_type, open(file, 'r').read().strip().split(','))]