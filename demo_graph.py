from svo_extraction.subject_verb_object_extract import findSVOs, get_spacy_nlp_sm_model
from svo_extraction.graph import SVONetwork
import spacy

nlp =  spacy.load('en_core_web_md')
text = "The bee-eaters are near passerine birds of the family Meropidae, containing three genera and twenty-seven species. Most species are found in Africa and Asia, with a few in southern Europe, Australia, and New Guinea. They are characterised by richly coloured plumage and slender bodies, and usually by elongated central tail feathers. All have long down-turned bills and medium to long wings, which may be pointed or round. They predominantly eat flying insects, caught on the wing from an open perch. Most bee-eaters are gregarious, forming colonies and nesting in burrows. The eggs are white, with typically five to the clutch. Most species are monogamous, and both parents care for the young, sometimes with assistance from related birds in the colony. Bee-eaters may be killed by raptors; their nests are raided by rodents and snakes, and they can carry various parasites. Some species are adversely affected by human activity or"
svos = findSVOs(nlp, text, removepunctuation=True, uncontracttext=True)
print(svos)
net = SVONetwork(svos)
#mygraph = net.createSVOGraph(direction="indirect", save_image=True, name_image="myimage.png")
#mygraph = net.createSVOGraph(direction="direct", save_image=True, name_image="myimage.png")
mygraph = net.createSVOGraph(direction="direct", save_image=False, display_grap=True)
