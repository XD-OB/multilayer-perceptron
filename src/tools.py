# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/13 23:48:04 by obelouch          #+#    #+#              #
#    Updated: 2021/03/13 23:48:04 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from mylib.consts import bcolors, errors
from os import path

def     exit_usage(error, filename="file"):
    '''
    Print the error Msg and Exit 
    '''
    print(f'\n{bcolors.FAIL}Error{bcolors.ENDC}: ', end='')
    if error == errors.ARG_NBR:
        print('Wrong number of arguments!')
    elif error == errors.NO_ARG:
        print('No files is provided!')
    elif error == errors.NOT_FILE:
        print(f'File "{filename}" not found!')
    elif error == errors.NOT_CSV:
        print(f'Wrong extension of the file "{filename}", accept only CSV!')
    elif error == errors.WRONG_FLAG:
        print('Wrong option used!')
    elif error == errors.DATA_DIM:
        print('Wrong data shape!')
    else:
        print(f'Can\'t read the file {filename}!')
    print(f'{bcolors.WARNING}Usage{bcolors.ENDC}: ', end='')
    print('python3 display_data.py <_dataset_>')
    exit(1)


def     get_filename(args):
    '''
    Check & Get the file name from args
    '''
    if len(args) != 1:
        exit_usage(errors.ARG_NBR)
    # Check the CSV file
    if not path.exists(args[0]):
        exit_usage(errors.NOT_FILE, args[0])
    if not args[0].endswith('.csv'):
        exit_usage(errors.NOT_CSV, args[0])
    # Return file name
    return args[0]
