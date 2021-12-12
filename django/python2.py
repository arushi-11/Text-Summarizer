import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string as str
import math

import nltk
nltk.download('stopwords')
nltk.download('punkt')


def get_tf(tokenized_sents):
    tf = {}
    for s in tokenized_sents:
        for w in s:
            tf[w] = tf.get(w,0) + 1
            
    return tf


def get_tokenized_sents(text):

    tokenized_sents = []
    
    # remove frequent words and punctuations
    unwanted_words = stopwords.words('english') + list(str.punctuation)
    
    sents = sent_tokenize(text)
    for s in sents:
        words = word_tokenize(s.lower())
        tokenized_sents.append([w for w in words if w not in unwanted_words])
    
    return sents, tokenized_sents


#def cosine_sim(s1_vector, s2_vector):
    assert len(s1_vector) == len(s2_vector)
    num = sum([s1_vector[sid]*s2_vector[sid] for sid in range(len(s1_vector))])
    den1 = sum([s1_vector[sid]**2 for sid in range(len(s1_vector))])
    den2 = sum([s2_vector[sid]**2 for sid in range(len(s1_vector))])
    
    cosine_sim = num / (math.sqrt(den1)*math.sqrt(den2))
    return cosine_sim

def word_overlap(s1, s2):
   
    # print("Intersection:", set(s1).intersection(set(s2)))
    return len(set(s1).intersection(set(s2)))/(len(s1) + len(s2))


def get_sim_matrix(tokenized_sents, threshold=0.3):
    sim_mat = np.zeros((len(tokenized_sents), len(tokenized_sents)))
    for s1_id, s1 in enumerate(tokenized_sents):
        for s2_id, s2 in enumerate(tokenized_sents):
            if word_overlap(s1, s2) >= threshold:
                sim_mat[s1_id, s2_id] = 1
    return sim_mat

def get_degree_centrality_summary(text, threshold = 0.1):
        
    original_sentences, tokenized_sentences = get_tokenized_sents(text)
    tf = get_tf(tokenized_sentences)    

    sim_mat = get_sim_matrix(tokenized_sentences, threshold)
   # print("SIM MAT:", sim_mat)
    degree_centrality = sim_mat.sum(axis=1)

    scores = {}

    for id, d in enumerate(degree_centrality):
        scores[id] = d
    
    sorted_scores = sorted(scores.items(), key = lambda x : x[1], reverse = True)
    #print("Sorted Scores:", sorted_scores)
    return [original_sentences[s[0]] for s in sorted_scores[0:3]]    


text = """That large animals require luxuriant vegetation has been a general assumption which has passed from one work to another,
           but I do not hesitate to say that it is completely false and that it has vitiated the reasoning of geologists on
 some points of great interest in the ancient history of the world. The prejudice has probably been derived from India, 
 and the Indian islands, where troops of elephants, noble forests, and impenetrable jungles are associated together in everyone’s mind. 
If, however, we refer to any work of travels through the southern parts of Africa, we shall find allusions in almost every page either to the desert character of the country or to the numbers of large animals inhabiting it. The same thing is rendered evident by the many engravings which have been published in various parts of the interior.

Dr Andrew Smith, who has lately succeeded in passing the Tropic of Capricorn, informs me that taking into consideration the whole of the 
southern part of Africa, there can be no doubt of its being a sterile country. On the southern coasts, there are some fine forests, but 
with these exceptions, the traveller may pass for days together through open plains, covered by poor and scanty vegetation. Now, if we 
look to the animals inhabiting these wide plains, we shall find their numbers extraordinarily great, and their bulk immense.

It may be supposed that although the species are numerous, the individuals of each kind are few. By the kindness of Dr Smith, 
I am enabled to show that the case is very different. He informs me that in one day’s march with the bullock-wagons, he saw, without 
wandering to any great distance on either side, between one-hundred and one-hundred and fifty rhinoceroses—the same day he saw several 
herds of giraffes, amounting together to nearly a hundred. 

At the distance of a little more than one hour’s march from their place of encampment on the previous night, his party actually killed 
eight hippopotamuses at one spot and saw many more. In this same river, there were likewise crocodiles. Of course, it was a case quite 
extraordinary to see so many great animals crowded together, but it evidently proves that they must exist in great numbers. Dr Smith 
describes that the country passed through that day as ‘being thinly covered with grass, and bushes about four feet high, and still more 
thinly with mimosa trees’.

Besides these large animals, anyone the least acquainted with the natural history of the Cape has read of 
the herds of antelopes, which can be compared only with the flocks of migratory birds. The numbers indeed of the 
lion, panther, and hyena, and the multitude of birds of prey, plainly speak of the abundance of the smaller quadrupeds. 
One evening, seven lions were counted at the same time prowling round Dr Smith’s encampment. .As this, an able naturalist 
remarked to me, each day the carnage in Southern Africa must indeed be terrific! I confess that it is truly surprising how 
such a number of animals can find support in a country producing so little food.

The larger quadrupeds no doubt roam over wide tracts in search of it; and their food chiefly consists of underwood, which 
probably contains many nutrients in a small bulk. Dr. Smith also informs me that the vegetation has a rapid growth; no sooner
 is a part consumed, than its place is supplied by a fresh stock. There can be no doubt, however, that our ideas respecting the 
 apparent amount of food necessary for the support of large quadrupeds are much exaggerated. The belief that where large quadrupeds
  exist, the vegetation must necessarily be luxuriant is more remarkable because the converse is far from true.

Mr. Burchell observed to me that when entering Brazil, nothing struck him more forcibly than the splendour of the South American 
vegetation contrasted with that of South Africa, together with the absence of all large quadrupeds. In his travels, he has suggested 
that the comparison of the respective weights (if there were sufficient data) of an equal number of the largest herbivorous quadrupeds 
of each country would be extremely curious. If we take on the one side, the elephants, hippopotamus, giraffe, bos caffer, elan, five 
species of rhinoceros; and on the American side, two tapirs, the guanaco, three deer, the vicuna, peccari, capybara (after which we 
must choose from the monkeys to complete the number), and then place these two groups alongside each other; it is not easy to conceive 
ranks more disproportionate in size.

After the above facts, we are compelled to conclude, against the anterior probability that among the Mammalia there exists
 no close relation between the bulk of the species, and the quantity of the vegetation in the countries which they inhabit."""

print(get_degree_centrality_summary(text, threshold=0.1))
    