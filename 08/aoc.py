import time
from pprint import pprint


def get_puzzle_input(filename='input-test.txt'):
    with open(filename, 'r') as f:
        return tuple(map(lambda x: (x.rsplit()[0], int(x.rsplit()[1])), f.readlines()))


class InfiniteLoop(BaseException):
    pass


def exec_cmd(puzzle_input, state):
    if state['cmd_index'] in state['history']:
        raise InfiniteLoop
    instruction = puzzle_input[state['cmd_index']]
    # pprint((instruction, state))
    state['history'].append(state['cmd_index'])
    if instruction[0] == 'jmp':
        state['cmd_index'] += instruction[1]
    elif instruction[0] == 'acc':
        state['acc'] += instruction[1]
        state['cmd_index'] += 1
    elif instruction[0] == 'nop':
        state['cmd_index'] += 1
    else:
        # pprint((instruction, state))
        raise NotImplementedError
    if len(puzzle_input) != state['cmd_index']:
        exec_cmd(puzzle_input, state)


def solve_part1(puzzle_input, state={'history': [], 'cmd_index': 0, 'acc': 0}):
    pprint(puzzle_input)

    try:
        exec_cmd(puzzle_input, state)
    except InfiniteLoop:
        return state['acc']


def solve_part2(puzzle_input, state={'history': [], 'cmd_index': 0, 'acc': 0}):
    success = False
    for i in range(0, len(puzzle_input)):
        if puzzle_input[i][0] not in ('jmp', 'nop'):
            continue
        try:
            fixed_program = list(puzzle_input)
            fixed_program[i] = list(fixed_program[i])
            fixed_program[i][0] = 'jmp' if puzzle_input[i][0] == 'nop' else 'nop'
            # print('########')
            # pprint(list(zip(puzzle_input, fixed_program)))
            exec_cmd(fixed_program, state)
            success = True
            break
        except InfiniteLoop:
            print(f'nope: {puzzle_input[i]}')
            state = {'history': [], 'cmd_index': 0, 'acc': 0}
    return state['acc']


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input('input.txt'))
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input('input.txt'))
t2 = time.process_time()

print(f's1 = {s1}, time: {t1 - t0}')
print(f's2 = {s2}, time: {t2 - t1}')
