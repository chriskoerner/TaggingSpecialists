# -*- coding: utf-8 -*-
from TagDictionary import TagDictionary
import pickle


TD = TagDictionary()

file_ = open('data/degree_tag')
for line in file_:
    row = line.strip('\n').split(' ')
    val = row[0]
    tag = row[1]
    TD[tag].set_degree(float(val))
    TD[tag].set_name(tag)
file_.close()    

file_ = open('data/usersWhoUseIt_tag')
for line in file_:
    row = line.strip('\n').split(' ')
    val = row[0]
    tag = row[1]
    TD[tag].set_frequency_user(float(val))
    TD[tag].set_name(tag)
file_.close()    

file_=open('data/tag_entropy.cooc.k=2_ohneselbstref')
for line in file_: 
    row = line.strip('\n').split('\t')
    TD[row[0].strip(' ')].set_entropy_user(float(row[1]))
    TD[tag].set_name(row[0].strip(' '))
file_.close()

file_ = open('data/count_resourcespertag')
for line in file_: 
    row = line.strip('\n').split(' ')
    TD[row[1]].set_frequency_resource(float(row[0]))
    TD[tag].set_name(row[1])
file_.close()

file_ = open('data/tag_tfidf.k=2')
for line in file_: 
    row = line.strip('\n').split('\t')
    TD[row[0]].set_tfidf(float(row[1]))
    TD[tag].set_name(row[0])
file_.close()

#normalize the distributions of the tag specifity values to have a max value of 1.0.
TD.normalize_dict()


#now expand the personomy file to be able to calculate specialist profile of a user
#to do so, add to each line the various spec levels of the tag
file_ = open('data/personomies_correct')
file_new = open('data/personomies_extended','wb')

linecount = 0
usercount = 0
for line in file_: 
    linecount += 1
    #if count > 1000: break
    row = line.strip('\n').split(' ')
    freq = int(row[0])
    new_username = row[1]
    tag = row[2]
    string = str(TD[tag].get_frequency_user()) + ' ' + str(TD[tag].get_frequency_resource()) + ' ' + str(TD[tag].get_degree()) + ' ' + str(TD[tag].get_entropy_user()) + ' ' + str(TD[tag].get_tfidf()) + '\n'
    l = line.strip('\n')
    newline = l + ' ' +string
    file_new.write(newline)
file_new.close()
file_.close()



#store TD for later use
#pickle.dump(TD, open('results/TagDictionary_Mendeley.pkl','wb'))
#TD = pickle.load(open('results/TagDictionary_Mendeley.pkl'))