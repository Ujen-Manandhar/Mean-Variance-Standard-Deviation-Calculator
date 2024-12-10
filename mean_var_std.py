import numpy as np


def calculate(li):
    # list containing less than 9 elements 
    if len(li) != 9:
        raise ValueError (f'List must contain nine numbers.')

    # take in list convert to array of 3x3
    np_list = np.array(li).reshape(3,3)

    #dictionary should be lists and not Numpy arrays
    calculations ={
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }

    # calcualation of mean of the array 
    calculations['mean']= [list(np.mean(np_list, axis= 0)),list(np.mean(np_list, axis= 1)), float(np.mean(np_list))]
    calculations['variance']= [list(np.var(np_list, axis= 0)),list(np.var(np_list, axis= 1)), float(np.var(np_list))]
    calculations['standard deviation']= [list(np.std(np_list, axis= 0)),list(np.std(np_list, axis= 1)), float(np.std(np_list))]
    calculations['max']= [list(np.max(np_list, axis= 0)),list(np.max(np_list, axis= 1)), int(np.max(np_list))]
    calculations['min']= [list(np.min(np_list, axis= 0)),list(np.min(np_list, axis= 1)), int(np.min(np_list))]
    calculations['sum']= [list(np.sum(np_list, axis= 0)),list(np.sum(np_list, axis= 1)), int(np.sum(np_list))]

    return calculations

if __name__ == '__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))