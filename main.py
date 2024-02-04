# Authors - Mihir Phatak and Saloni Aswani
# 8 Puzzle Problem Using A* Algorithm


"""
Function to generate input states. It takes a linear input array and converts it into a 3 X 3 grid.
"""
def generateInputState(config):
    state = []
    c = 0
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(int(config[c]))
            c += 1
        state.append(temp)
    return state

"""
Function to print a state.
"""
def printState(state):
    for i in range(3):
        print(state[i])


"""
Accepting user input from user
"""
input_str = input('Enter initial state configuration between 0-8 where 0 is blank : \n').strip()
input_parts = input_str.split(' ')
initial_state = generateInputState(input_parts)

goal_str = input('Enter initial state configuration between 0-8 where 0 is blank : \n').strip()
goal_parts = goal_str.split(' ')
goal_state = generateInputState(goal_parts)

print('Initial state:')
printState(initial_state)
print('Goal state:')
printState(goal_state)