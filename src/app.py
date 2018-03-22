'''
Main file for abstractor prototype
'''
from abstractor_module import abstractor, model_utils, train


def main():
    '''
    main function
    '''
    while True:
        str_input = input('1. Test Input, 2. Import data, 3. Train Model (Enter 1-3):')
        if str_input == '1':
            str_input = input('Enter your input: ')
            abstract = abstractor.Abstractor()
            print(abstract.get_abstraction(str_input))
        elif str_input == '2':
            print('Importing data...')
            model_utils.import_all()
            print('Done.')
        elif str_input == '3':
            print('Training model...')
            train.train_model(save=True)
            print('Done.')
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()
