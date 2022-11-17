import numpy as np

class ShorthandNumpyArray(object):
    '''
    Defines a shorthand notation to create a numpy array
    e.g.
        _ = ShorthandArray()
        A = _[1,2,3]
    '''
    def __getitem__(self, key):
        if isinstance(key, tuple):
            return np.array(key)
        else:
            return np.array([key])

# _ = ShorthandArray()

if __name__ == "__main__":
    pass