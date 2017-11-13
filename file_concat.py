"""
Getting text data from the current directory and returning a a new .txt file
with concatinated data.
"""
import os
import os.path

# Ceck this!
OUT_DIR = '../concat.txt'


def get_files():
    '''
    Return all the wiki_xx filenames in a list
    '''
    filenames = []

    for i in range(0, (len([name for name in os.listdir('.') if os.path.isfile(name)] - 1))):
        filenames.append('wiki_%s' % i)

    return filenames

def concat_files():
    '''
    Returning a plain text file containing all the files form get_files() list
    '''

    with open(OUT_DIR, 'w') as target:
        for fname in get_files():
            with open(fname) as inner_target:
                target.write(inner_target.read())

concat_files()
