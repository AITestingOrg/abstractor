'''
Main file for abstractor prototype
'''
from abstractor_module import abstractor, model_utils, train, person_names


def main():
    '''
    main function
    '''
    while True:
        str_input = input('1. Test Input, 2. Import data, 3. Train Model, 4. Test Model (Enter 1-4):')
        if str_input == '1':
            str_input = input('Enter your input: ')
            abstract = abstractor.Abstractor()
            print(abstract.get_abstraction(str_input))
        elif str_input == '2':
            print('Importing data...')
            model_utils.import_all()
            print('Done.')
        elif str_input == '3':
            str_input = input('Drop rate (0.35): ')
            drop_rate = float(str_input) if str_input != '' else 0.35
            str_input = input('Iterations (15): ')
            iters = int(str_input) if str_input != '' else 15
            print('Training model...')
            train.train_model(save=True, drop_rate=drop_rate, iters=iters)
            print('Done.')
        elif str_input == '4':
            print('Testing model...')
            train.test_model(person_names.last_name_train_data())
            print('Done.')
        else:
            print('Invalid input')


if __name__ == '__main__':
    main()
