from svo_extraction.subject_verb_object_extract import findSVOs, get_spacy_nlp_sm_model

str1 = "Then there’s a development setback on top of that that pushes you even further back."
str2 = "And that goes with that we’re going to do things differently, but we haven’t done that yet."
str3 = "Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a " \
       "seemingly interminable ground test of the Apollo 1 spacecraft."

nlp =  get_spacy_nlp_sm_model()
svos = findSVOs(nlp, str1, removepunctuation=True, uncontracttext=True)
print(svos)

svos = findSVOs(nlp, str2, removepunctuation=True, uncontracttext=True)
print(svos)

svos = findSVOs(nlp, str3, removepunctuation=True, uncontracttext=True)
print(svos)

print("*"*20)

svos = findSVOs(nlp, str1, removepunctuation=False, uncontracttext=False)
print(svos)

svos = findSVOs(nlp, str2, removepunctuation=False, uncontracttext=False)
print(svos)

svos = findSVOs(nlp, str3, removepunctuation=False, uncontracttext=False)
print(svos)
