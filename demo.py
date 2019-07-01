from subject_verb_object_extract import findSVOs, nlp

str1 = "Then there’s a development setback on top of that that pushes you even further back."
str2 = "And that goes with that we’re going to do things differently, but we haven’t done that yet."
str3 = "Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a " \
       "seemingly interminable ground test of the Apollo 1 spacecraft."

tokens1 = nlp(str1)
svos1 = findSVOs(tokens1)
print("\n1")
print(str1)
print(svos1)

tokens2 = nlp(str2)
svos2 = findSVOs(tokens2)
print("\n2")
print(str2)
print(svos2)

tokens3 = nlp(str3)
svos3 = findSVOs(tokens3)
print("\n3")
print(str3)
print(svos3)
