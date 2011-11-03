# -*- coding: utf-8 -*-
from lookup_utilities import read_normalizedTagGeneralityData
#import pickle

#read tag information
TD = read_normalizedTagGeneralityData()

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