"""
Here are the tools for KMC simulation
Author: Zeyu Deng
Email: dengzeyu@gmail.com
"""

import pickle
def save_project(project,fname):
    print('Saving:',fname)
    with open(fname,'wb') as fhandle:
        pickle.dump(project,fhandle)

def load_project(fname):
    print('Loading:',fname)
    with open(fname,'rb') as fhandle:
        obj = pickle.load(fhandle)
    return obj