# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    display_data.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/03/13 22:42:14 by obelouch          #+#    #+#              #
#    Updated: 2021/03/13 22:42:14 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from src.tools import get_filename, exit_usage
from mylib.csvTools import get_df_from_csv
from mylib.libft import get_flags_and_args
from mylib.math import ft_standarize
from mylib.consts import errors
from sklearn.utils import shuffle
import pandas as pd
import numpy as np


def     get_X_Y(df):
    '''
    from df get Xs and Ys for training and testing
    '''
    # grouping by result dataframe column
    ### splitting dataframe by groups
    grouped = df.groupby(df[1])
    df_benin = grouped.get_group('B')
    df_malin = grouped.get_group('M')
    # Split to test and train
    split_B = int(len(df_benin) * 0.9)
    split_M = int(len(df_malin) * 0.9)
    df_train = shuffle(pd.concat(
        [
            df_benin[:split_B],
            df_malin[:split_M]
        ],
        ignore_index=True,
        sort=False
    ))
    df_test = shuffle(pd.concat(
        [
            df_benin[split_B:],
            df_malin[split_M:]
        ],
        ignore_index=True,
        sort=False
    ))
    # Build Xs and Ys Matrices
    ### train
    X_train = np.concatenate(
        (
            ft_standarize(df_train[1]),
            ft_standarize(df_train.iloc[:, 2:]),
        ),
        # concat in columns
        axis=1
    )
    Y_train = df_train[1]
    ### test
    X_test = np.concatenate(
        (
            ft_standarize(df_test[1]),
            ft_standarize(df_test.iloc[:, 2:]),
        ),
        # concat in columns
        axis=1
    )
    Y_test = df_test[1]
    print(X_train)



def     main():
    '''
    Display data
    '''
    # Get Arguments and flags
    flags, args = get_flags_and_args()
    # check & get the CSV file name
    filename = get_filename(args)
     # take the dataframe from the files
    df = get_df_from_csv(filename)
    # Check Dimensions of the df columns
    if df.shape[1] != 32:
        exit_usage(errors.DATA_DIM)
    # Get Training and Testing Xs and Ys
    #X_train, Y_train, X_test, Y_test = get_X_Y(df)
    get_X_Y(df)


# Launch program
if __name__ == "__main__":
    main()
