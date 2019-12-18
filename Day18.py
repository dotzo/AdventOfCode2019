# https://adventofcode.com/2019/day/18

from collections import deque, defaultdict
from copy import copy

INPUT = open('day18-input.txt','r').read().strip()
INPUT = INPUT.split('\n')

BOARD = copy(INPUT)

WALL = '#'
FREE = '.'
START = '@'
KEYS = ''.join([chr(n) for n in range(ord('a'), ord('z')+1)])
LOCKS = ''.join([chr(n) for n in range(ord('A'), ord('Z')+1)])

def find_start():
    for i, row in enumerate(BOARD):
        for j, col in enumerate(BOARD[i]):
            if col == START:
                return i, j

def find_keys():
    keys = set()
    for i, row in enumerate(BOARD):
        for j, col in enumerate(BOARD[i]):
            if col in KEYS:
                keys.add(col)

    return (1 << len(keys)) - 1

def find_all_keys_shortest_path():
    start_i, start_j = find_start()
    all_keys = find_keys()

    keys_to_index = {name: number for number, name in enumerate(KEYS)}
    locks_to_index = {name: number for number, name in enumerate(LOCKS)}

    seen = defaultdict(set) #places I've visited whilst holding a particular set of keys
    q = deque() # states of the search

    ## Seed Conditions
    # steps taken, num keys holding, key bitmask, i, j
    q.append((0,0,0,start_i,start_j))
    seen[0].add((start_i,start_j))

    # helper functions
    can_walk = lambda mask, lock: (1 << locks_to_index[lock]) & mask
    have_key = lambda mask, key: (1 << keys_to_index[key]) & mask

    while q:
        num_steps, num_keys, keyring, i, j = q.popleft()

        for ni, nj in [
            [i + 1, j],
            [i - 1, j],
            [i, j - 1],
            [i, j + 1]
        ]:
            new_pos = BOARD[ni][nj]
            # OOB
            if not (0 <= ni < len(BOARD) and 0 <= nj < len(BOARD[0])):
                continue
            # wall
            elif new_pos == WALL:
                continue
            # lock I can't open
            elif new_pos in LOCKS and (not can_walk(keyring, new_pos)):
                continue

            # free to procede
            else:
                new_steps = num_steps + 1
                new_num_keys = num_keys
                new_keyring = keyring
                

                # I've encountered a new key
                if new_pos in KEYS and (not have_key(new_keyring, new_pos)):
                    new_num_keys += 1
                    new_keyring |= (1 << keys_to_index[new_pos])


                # all keys is return condition
                if new_keyring == all_keys:
                    return new_steps

                # if we've been here before, do nothing
                # otherwise document it
                if (ni, nj) in seen[new_keyring]:
                    continue
                else:
                    q.append((new_steps, new_num_keys, new_keyring, ni, nj))
                    seen[new_keyring].add((ni,nj))

    return -1

print(find_all_keys_shortest_path())