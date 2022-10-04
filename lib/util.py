"""
Utility function
"""

from string import punctuation

def lower_and_remove_punctuation(dict_elt : dict) -> dict:
    '''
    dict_elt : Lower and remove the punctuation in an element of a dictionary of the dataset, it requires ['text']
    return the dict after updating the text value
    '''
    dict_elt['text'] = dict_elt['text'].lower().translate(str.maketrans('', '', punctuation))
    return dict_elt