# Copyright 2017 Peter de Vocht
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from subject_verb_object_extract import findSVOs, printDeps, nlp


# test the subject/verb/object_extraction
class SubjectVerbOjectExtractTest(unittest.TestCase):
    def __init__(self, methodName: str):
        unittest.TestCase.__init__(self, methodName)

    # test
    def test_svo_1(self):
        tok = nlp("the annoying person that was my boyfriend hit me")
        svos = findSVOs(tok)
        printDeps(tok)  # just show what printDeps() does
        self.assertTrue(set(svos) == {('the annoying person', 'was', 'my boyfriend'), ('the annoying person', 'hit', 'me')})


    def test_svo_2(self):
        tok = nlp("making $12 an hour? where am i going to go? I have no other financial assistance available and he certainly won't provide support.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('I', '!have', 'other financial assistance available'), ('he', '!provide', 'support')})

    def test_svo_3(self):
        tok = nlp("I don't have other assistance")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('I', '!have', 'other assistance')})

    def test_svo_4(self):
        tok = nlp("They ate the pizza with anchovies.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('They', 'ate', 'the pizza')})

    def test_svo_5(self):
        tok = nlp("I have no other financial assistance available and he certainly won't provide support.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('I', '!have', 'other financial assistance available'), ('he', '!provide', 'support')})

    def test_svo_6(self):
        tok = nlp("I have no other financial assistance available, and he certainly won't provide support.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('I', '!have', 'other financial assistance available'),
                                      ('he', '!provide', 'support')})

    def test_svo_7(self):
        tok = nlp("he did not kill me")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', '!kill', 'me')})

    def test_svo_8(self):
        tok = nlp("he is an evil man that hurt my child and sister")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'is', 'an evil man'),
                                      ('an evil man', 'hurt', 'my child'),
                                      ('an evil man', 'hurt', 'sister')})

    def test_svo_9(self):
        tok = nlp("he told me i would die alone with nothing but my career someday")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'told', 'me')})

    def test_svo_10(self):
        tok = nlp("I wanted to kill him with a hammer.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('I', 'kill', 'him')})

    def test_svo_11(self):
        tok = nlp("because he hit me and also made me so angry I wanted to kill him with a hammer.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'hit', 'me'), ('I', 'kill', 'him')})

    def test_svo_12(self):
        tok = nlp("he and his brother shot me")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'shot', 'me'), ('his brother', 'shot', 'me')})

    def test_svo_13(self):
        tok = nlp("he and his brother shot me and my sister")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'shot', 'me'), ('he', 'shot', 'my sister'),
                                      ('his brother', 'shot', 'me'), ('his brother', 'shot', 'my sister')})

    def test_svo_14(self):
        tok = nlp("the boy raced the girl who had a hat that had spots.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('the boy', 'raced', 'the girl'), ('who', 'had', 'a hat'),
                                      ('a hat', 'had', 'spots')})

    def test_svo_15(self):
        tok = nlp("he spit on me")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'spit', 'me')})

    def test_svo_16(self):
        tok = nlp("he didn't spit on me")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', '!spit', 'me')})

    def test_svo_17(self):
        tok = nlp("the boy raced the girl who had a hat that didn't have spots.")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('the boy', 'raced', 'the girl'), ('who', 'had', 'a hat'),
                                      ('a hat', '!have', 'spots')})

    def test_svo_18(self):
        tok = nlp("he is a nice man that didn't hurt my child and sister")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', 'is', 'a nice man'), ('a nice man', '!hurt', 'my child'),
                                      ('a nice man', '!hurt', 'sister')})

    def test_svo_19(self):
        tok = nlp("he didn't spit on me and my child")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', '!spit', 'me'), ('he', '!spit', 'my child')})

    def test_svo_20(self):
        tok = nlp("he didn't spit on me or my child")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', '!spit', 'me'), ('he', '!spit', 'my child')})

    def test_svo_21(self):
        tok = nlp("he didn't spit on me nor my child")
        svos = findSVOs(tok)
        # printDeps(tok)
        self.assertTrue(set(svos) == {('he', '!spit', 'me'), ('he', '!spit', 'my child')})

    def test_svo_22(self):
        tok = nlp("he beat and hurt me")
        # printDeps(tok)
        svos = findSVOs(tok)
        self.assertTrue(set(svos) == {('he', 'beat', 'me'), ('he', 'hurt', 'me')})

    def test_svo_23(self):
        tok = nlp("I was beaten by him")
        # printDeps(tok)
        svos = findSVOs(tok)
        self.assertTrue(set(svos) == {('him', 'beat', 'I')})

    def test_svo_24(self):
        tok = nlp("lessons were taken by me")
        # printDeps(tok)
        svos = findSVOs(tok)
        self.assertTrue(set(svos) == {('me', 'take', 'lessons')})

    def test_svo_25(self):
        tok = nlp("Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a seemingly interminable ground test of the Apollo 1 spacecraft.")
        # printDeps(tok)
        svos = findSVOs(tok)
        self.assertTrue(set(svos) == {('Chris Kraft', 'neared', 'the end of a tedious Friday afternoon'), ('he', 'monitored', 'a interminable ground test of the Apollo spacecraft')})
