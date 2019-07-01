# Subject Verb Object extractor

An improved version of an often quoted Internet resources for Subject/Verb/Object extraction using Spacy.
- Added passive sentence support
- Added noun-phrase expansion
- Added more comprehensive CCONJ support
- Fixed 'that' resolution
- Still not perfect, could do with further improvements, feel free to submit your own improvements.

## Installation

Uses Python 3.5+ and Spacy for its parser

```
pip install -r requirements

# use spacy to download its small model
python -m spacy download en_core_web_sm
```

## Test

Review the tests to see how it all works

```
python -m unittest discover -p "*_test.py"
```

## Example

```
from subject_verb_object_extract import findSVOs, nlp
tokens = nlp("Seated in Mission Control, Chris Kraft neared the end of a tedious Friday afternoon as he monitored a seemingly interminable ground test of the Apollo 1 spacecraft.")
svos = findSVOs(tokens)
print(svos)
```

outputs a list of tuples, each tuple containing the Subject,Verb,Object

```
[('Chris Kraft', 'neared', 'the end of a tedious Friday afternoon'), ('he', 'monitored', 'a interminable ground test of the Apollo spacecraft')]
```

Alternatively, run `demo.py` to see its use.
