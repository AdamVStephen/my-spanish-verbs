#!/usr/bin/env python

"""
Classes and utilities to record my understanding of Spanish verb manipulation.

Rules taken from Collins Spanish Grammar.
"""

# TODO: extend to ar/er/ir
# TODO: handle unicode properly
# TODO: handle natural Spanish data entry with accents
# TODO: MarkDown output
# TODO: JavaScript/HTML output

from collections import OrderedDict

import pdb

presentTenseEndingsAR = {
            'yo' : 'o',
            'tu' : 'as',
            'el/ella/usted' : 'a',
            'nosotros' : 'amos',
            'vosotros' : 'ais',
            'ellos/ellas/ustedes' : 'an'
            }

presentTenseEndingsER = {
            'yo' : 'o',
            'tu' : 'es',
            'el/ella/usted' : 'e',
            'nosotros' : 'emos',
            'vosotros' : 'eis',
            'ellos/ellas/ustedes' : 'en'
            }

presentTenseEndingsIR = {
            'yo' : 'o',
            'tu' : 'es',
            'el/ella/usted' : 'e',
            'nosotros' : 'imos',
            'vosotros' : 'is',
            'ellos/ellas/ustedes' : 'en'
            }

class Conjugation:
    endingsDict = {
            'yo' : None,
            'tu' : None,
            'el' : None,
            'ella' : None,
            'usted' : None,
            'nosotros' : None,
            'vosotros' : None,
            'ellos' : None,
            'ellas' : None,
            'ustedes' : None
            }
    pronounsMap = OrderedDict({
        'yo' : ['yo'],
        'tu' : ['tu'],
        'el/ella/usted' : ['el', 'ella', 'usted'],
        'nosotros' : ['nosotros'],
        'vosotros' : ['vosotros'],
        'ellos/ellas/ustedes' : ['ellos', 'ellas', 'usted']
        })

    def __init__(self, name, endingsDict = None):
        self.name = name
        if endingsDict is not None:
            for pronoun, equivalents in self.pronounsMap.items():
                # Insert the combined form
                self.endingsDict[pronoun] = endingsDict[pronoun]
                for equivalent in equivalents:
                    print("%s : %s" % (pronoun, equivalent))
                    # Also expand the individual forms
                    self.endingsDict[equivalent] = endingsDict[pronoun]

    def apply(self, infinitive, pronoun):
        stub = infinitive[:-2]
        suffix = self.endingsDict[pronoun]
        return "%s%s" % (stub, suffix)

    def __repr__(self):
        r = []
        for pronoun, equivalents in self.pronounsMap.items():
            #pdb.set_trace()
            f = "%-20s : %s" % (pronoun, self.endingsDict[pronoun])
            r.append(f)
        return '\n'.join(r)

def ut_Conjugation():
    c = Conjugation("Present Tense AR", presentTenseEndingsAR)
    print(c)
    c = Conjugation("Present Tense ER", presentTenseEndingsER)
    print(c)
    c = Conjugation("Present Tense IR", presentTenseEndingsIR)
    print(c)
    print(c.apply('vivir', 'yo'))


class RegularVerb:
    def __init__(self, infinitive, conjugation):
        self.infinitive = infinitive
        self.conjugation = conjugation

    def __repr__(self):
        r = []
        r.append("Regular Verb : %s" % self.infinitive)
        for pronoun in self.conjugation.pronounsMap.keys():
            r.append("%-20s : %s" % (pronoun, self.conjugation.apply(self.infinitive, pronoun)))
        return '\n'.join(r)

def ut_RegularVerb():
    presentTenseAR = Conjugation("Present Tense AR", presentTenseEndingsAR)
    hablar = RegularVerb('hablar', presentTenseAR)
    print(hablar)

    presentTenseER = Conjugation("Present Tense ER", presentTenseEndingsER)
    comer = RegularVerb('comer', presentTenseER)
    print(comer)

    presentTenseIR = Conjugation("Present Tense IR", presentTenseEndingsIR)
    vivir = RegularVerb('vivir', presentTenseIR)
    print(vivir)

def unit_tests():
    ut_Conjugation()
    ut_RegularVerb()

if __name__ == '__main__':
    unit_tests()
