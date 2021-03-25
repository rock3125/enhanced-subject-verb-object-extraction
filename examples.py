from subject_verb_object_extract import findSVOs, printDeps, nlp

tok = nlp("expert spacy users are very kind to dogs")
svos = findSVOs(tok)
printDeps(tok)
print(svos)


tok = nlp("both sides should understand that")
svos = findSVOs(tok)
printDeps(tok)
print(svos)
