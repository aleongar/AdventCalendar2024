import sys
from solution.exercise4 import Exercise #cambiar para cambiar de ejercicio


if __name__ == '__main__':
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        data = file.read() 
        
    ex = Exercise(data)
    print(ex.solution())
    print(ex.solution2())