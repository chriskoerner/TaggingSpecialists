# -*- coding: utf-8 -*-


import pickle
import collections
from numpy import median

from list_utilities import normalize_data
from lookup_utilities import user_nrresources_lookup, read_extended_personomy_file
from ExpertUser1 import ExpertUser1

from parameters import * #NB: not in github
#NB: we define an active tagger as someone who has:
#1) at least > xx resources 
#2) at least > xx tags 
#3) at least > xx tag assignments



#read some data
dict_userres = user_nrresources_lookup()

file_ = open('data/personomies_extended')
#file_new = open('results/specialists_data_corrected','wb')


#initialize variables
username = []
fu = []
fr = []
eu = []
t = []
d = []
tas = []
tag_freq = []
fu_t = []
fr_t = []
eu_t = []
t_t = []
d_t = []

expertUser = ExpertUser1()

#define helper function


old_username = ''

for line in file_:

    new_username, freq, tag_fr, tag_fu, tag_eu, tag_t, tag_d = read_extended_personomy_file(line)

    if (new_username == old_username) or (old_username == ''):
        #just add data
        expertUser.add_userdata(freq, tag_fr, tag_fu, tag_eu, tag_t, tag_d)

    elif not(old_username == ''):
        #save data for user and proceed to next user
        if (dict_userres[old_username] > ACTIVETAGGER_RESOURCE_THRESHOLD) and (expertUser.tag_sum > ACTIVETAGGER_TAG_THRESHOLD) and (expertUser.tas_sum > ACTIVETAGGER_TAS_THRESHOLD):
            tag_sum = expertUser.get_tag_sum()
            tas_sum = expertUser.get_tas_sum()
            tas.append(tas_sum)
            tag_freq.append(tag_sum)
            username.append(old_username)
            #if (old_username == '1165'): print tag_sum, tas_sum, tag_fu_sum, tag_fr_sum, tag_t_sum, tag_d_sum, tag_eu_sum
            if not(expertUser.get_tag_fu_trust() > TRUST_LIMIT*tag_sum): fu.append(median(expertUser.get_tag_fu_sum()) / (tas_sum ))
            else: fu.append(-1.0)
            fu_t.append(expertUser.get_tag_fu_trust() / tag_sum)

            if not(expertUser.get_tag_fr_trust() > TRUST_LIMIT*tag_sum): fr.append(median(expertUser.get_tag_fr_sum()) / (tas_sum))
            else: fr.append(-1.0)
            fr_t.append(expertUser.get_tag_fr_trust() / tag_sum)

            if not(expertUser.get_tag_eu_trust() > TRUST_LIMIT*tag_sum): eu.append(median(expertUser.get_tag_eu_sum()) / (tas_sum))
            else: eu.append(-1.0)
            eu_t.append(expertUser.get_tag_eu_trust() / tag_sum)

            if not(expertUser.get_tag_t_trust() > TRUST_LIMIT*tag_sum): t.append(median(expertUser.get_tag_t_sum()) / (tas_sum))
            else: t.append(-1.0)
            d_t.append(expertUser.get_tag_d_trust() / tag_sum)

            if not(expertUser.get_tag_d_trust() > TRUST_LIMIT*tag_sum): d.append(median(expertUser.get_tag_d_sum()) / (tas_sum))
            else: d.append(-1.0)
            t_t.append(expertUser.get_tag_t_trust() / tag_sum)

            #print len(username), len(d), len(fr), len(fu), len(eu), len(t)
        expertUser = ExpertUser1()
        expertUser.add_userdata(freq, tag_fr, tag_fu, tag_eu, tag_t, tag_d)

    old_username = new_username

if (dict_userres[old_username] > ACTIVETAGGER_RESOURCE_THRESHOLD) and (tag_sum > ACTIVETAGGER_TAG_THRESHOLD) and (tas_sum > ACTIVETAGGER_TAS_THRESHOLD):
    tag_sum = expertUser.get_tag_sum()
    tas_sum = expertUser.get_tas_sum()
    tas.append(tas_sum)
    tag_freq.append(tag_sum)
    username.append(old_username)
    #if (old_username == '1165'): print tag_sum, tas_sum, tag_fu_sum, tag_fr_sum, tag_t_sum, tag_d_sum, tag_eu_sum
    if not(expertUser.get_tag_fu_trust() > TRUST_LIMIT*tag_sum): fu.append(median(expertUser.get_tag_fu_sum()) / (tas_sum ))
    else: fu.append(-1.0)
    fu_t.append(expertUser.get_tag_fu_trust() / tag_sum)

    if not(expertUser.get_tag_fr_trust() > TRUST_LIMIT*tag_sum): fr.append(median(expertUser.get_tag_fr_sum()) / (tas_sum))
    else: fr.append(-1.0)
    fr_t.append(expertUser.get_tag_fr_trust() / tag_sum)

    if not(expertUser.get_tag_eu_trust() > TRUST_LIMIT*tag_sum): eu.append(median(expertUser.get_tag_eu_sum()) / (tas_sum))
    else: eu.append(-1.0)
    eu_t.append(expertUser.get_tag_eu_trust() / tag_sum)

    if not(expertUser.get_tag_t_trust() > TRUST_LIMIT*tag_sum): t.append(median(expertUser.get_tag_t_sum()) / (tas_sum))
    else: t.append(-1.0)
    d_t.append(expertUser.get_tag_d_trust() / tag_sum)

    if not(expertUser.get_tag_d_trust() > TRUST_LIMIT*tag_sum): d.append(median(expertUser.get_tag_d_sum()) / (tas_sum))
    else: d.append(-1.0)
    t_t.append(expertUser.get_tag_t_trust() / tag_sum)





fu_n = normalize_data(fu)
fr_n = normalize_data(fr)
eu_n = normalize_data(eu)
t_n = normalize_data(t)
d_n = normalize_data(d)

pickle.dump(fu_n,open('results/spec_frequser_distr.pkl','wb'))
pickle.dump(eu_n,open('results/spec_entruser_distr.pkl','wb'))
pickle.dump(fr_n,open('results/spec_freqres_distr.pkl','wb'))
pickle.dump(t_n,open('results/spec_tfidf_distr.pkl','wb'))
pickle.dump(d_n,open('results/spec_degree_distr.pkl','wb'))
pickle.dump(username,open('results/spec_usernamnes.pkl','wb'))

file_write = open('results/specialist_info_helperfile','wb')

for i in range(len(username)):
    str_ = str(username[i])
    str_ += '\t'+str(tag_freq[i])
    str_ += '\t'+str(tas[i])
    str_ += '\t'+str(fu_n[i]) + '\t' + str(fu_t[i])
    str_ += '\t'+str(fr_n[i]) + '\t' + str(fr_t[i])
    str_ += '\t'+str(eu_n[i]) + '\t' + str(eu_t[i])
    str_ += '\t'+str(t_n[i]) + '\t' + str(t_t[i])
    str_ += '\t'+str(d_n[i]) + '\t' + str(d_t[i])
    str_ += '\n'
    file_write.write(str_)

file_write.close()    