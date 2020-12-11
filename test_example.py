from subject_verb_object_extract import findSVOs, printDeps, nlp

tok = nlp("expert spacy users are very kind to dogs")
svos = findSVOs(tok)
printDeps(tok)
print(svos)

