'''
Main file for abstractor prototype
'''
from AbstractorModule import abstractor


def main():
    '''
    main function
    '''
    while True:
        str_input = input('Enter your input: ')
        print(abstractor.get_abstraction(str_input))


if __name__ == '__main__':
    main()
