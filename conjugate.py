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


# Endings to learn and to use later



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


# Preterite

preteriteTenseEndingsAR = {
            'yo' : 'e',
            'tu' : 'aste',
            'el/ella/usted' : 'o',
            'nosotros' : 'amos',
            'vosotros' : 'asteis',
            'ellos/ellas/ustedes' : 'aron'
            }

preteriteTenseEndingsER = {
            'yo' : 'i',
            'tu' : 'iste',
            'el/ella/usted' : 'io',
            'nosotros' : 'imos',
            'vosotros' : 'isteis',
            'ellos/ellas/ustedes' : 'ieron'
            }

preteriteTenseEndingsIR = preteriteTenseEndingsER

# Future : using the pattern [:-2] needs to distinguish three cases, though w.r.t. the final infinitive, suffixes are the same

futureTenseEndingsAR = {
            'yo' : 'are',
            'tu' : 'aras',
            'el/ella/usted' : 'ara',
            'nosotros' : 'aremos',
            'vosotros' : 'areis',
            'ellos/ellas/ustedes' : 'aran'
            }

futureTenseEndingsER = {
            'yo' : 'ere',
            'tu' : 'eras',
            'el/ella/usted' : 'era',
            'nosotros' : 'eremos',
            'vosotros' : 'ereis',
            'ellos/ellas/ustedes' : 'eran'
            }

futureTenseEndingsIR = {
            'yo' : 'ire',
            'tu' : 'iras',
            'el/ella/usted' : 'ira',
            'nosotros' : 'iremos',
            'vosotros' : 'ireis',
            'ellos/ellas/ustedes' : 'iran'
            }





#
class Conjugation:
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
        self.endingsDict = {}
        self.setEndings(endingsDict)

    def setEndings(self, endingsDict = None):
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

    c = Conjugation("Preterite Tense AR", preteriteTenseEndingsAR)
    print(c)
    print(c.apply('hablar', 'yo'))


class RegularVerb:
    def __init__(self, infinitive, conjugation):
        self.infinitive = infinitive
        self.conjugation = conjugation

    def set(self, conjugation):
        self.conjugation = conjugation

    def __repr__(self):
        r = [""]
        r.append("Regular Verb : %s" % self.infinitive)
        r.append("Conjugation  : %s" % self.conjugation.name)
        r.append("")
        for pronoun in self.conjugation.pronounsMap.keys():
            r.append("\t%-20s : %s" % (pronoun, self.conjugation.apply(self.infinitive, pronoun)))
        return '\n'.join(r)

# Define our standard tenses

#pdb.set_trace()
presentTenseAR = Conjugation("Present Tense AR", presentTenseEndingsAR)
presentTenseER = Conjugation("Present Tense ER", presentTenseEndingsER)
presentTenseIR = Conjugation("Present Tense IR", presentTenseEndingsIR)

preteriteTenseAR = Conjugation("Preterite Tense AR", preteriteTenseEndingsAR)
preteriteTenseER = Conjugation("Preterite Tense ER", preteriteTenseEndingsER)
preteriteTenseIR = Conjugation("Preterite Tense IR", preteriteTenseEndingsIR)

futureTenseAR = Conjugation("Future Tense AR", futureTenseEndingsAR)
futureTenseER = Conjugation("Future Tense ER", futureTenseEndingsER)
futureTenseIR = Conjugation("Future Tense IR", futureTenseEndingsIR)

def ut_RegularVerb():
    #pdb.set_trace()
    hablar = RegularVerb('hablar', presentTenseAR)
    print(hablar)
    hablar.set(preteriteTenseAR)
    print(hablar)
    hablar.set(futureTenseAR)
    print(hablar)


    comer = RegularVerb('comer', presentTenseER)
    print(comer)
    vivir = RegularVerb('vivir', presentTenseIR)
    print(vivir)

def unit_tests():
    ut_Conjugation()
    ut_RegularVerb()

if __name__ == '__main__':
    unit_tests()
