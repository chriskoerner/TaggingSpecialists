# -*- coding: utf-8 -*-


import pickle
import collections
from numpy import median


#NB: we define an active tagger as someone who has:
#1) at least > 20 resources 
#2) at least > 5 tags 
#3) at least > 60 tag assignments


file_ = open('data/user_resources_count')
dict_userres = collections.defaultdict(int)
for line in file_:
    row = line.strip('\n').split(' ')
    val = int(row[0])
    user = row[1]
    dict_userres[user] += val



   

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
fu_t = []
fr_t = []
eu_t = []
t_t = []
d_t = []

#user_tag_vector helpers
tas_sum = 0.0
tag_sum = 0.0
tag_fu_sum = []
tag_fr_sum = []
tag_d_sum = []
tag_eu_sum = []
tag_t_sum = []

#user_trust_value helpers
#trust is used to calculate the amount of tags for which spec_level for corresponding method could be retrieved versus the amount of tags in a personomy
#trust 0 = all tags could be used, trust 1 = no tags of personomy could be used to calculate user specifity
tag_fu_trust = 0.0
tag_fr_trust = 0.0
tag_eu_trust = 0.0
tag_d_trust = 0.0
tag_t_trust = 0.0

#set threshold for trust level, the lower the less strict the level is
trust_lim = 0.7

#file_write= open('results/help_file','wb')

old_username = ''
for line in file_:
      #linecount += 1
      #if len(username) > 2: break
      #print line
      row = line.strip('\n').split(' ')
      freq = float(row[0])
      new_username = row[1]
      #if (new_username == '1165'): print line
      tag = row[2]
      if not(row[3] == 'None'): tag_fu = float(row[3])
      else: tag_fu = None
      if not(row[4] == 'None'): tag_fr = float(row[4])
      else: tag_fr = None
      if not(row[5] == 'None'): tag_d = float(row[5])
      else: tag_d = None
      if not(row[6] == 'None'): tag_eu = float(row[6])
      else: tag_eu = None
      if not(row[7] == 'None'): tag_t = float(row[7])
      else: tag_t = None
      
      if (new_username == old_username) or (old_username == ''):
	tas_sum += freq
	tag_sum += 1.0
	if not(tag_fu == None): tag_fu_sum.append( tag_fu*freq )
	else: tag_fu_trust += 1
	if not(tag_fr == None): tag_fr_sum.append(  tag_fr*freq )
	else: tag_fr_trust += 1
	if not(tag_d == None): tag_d_sum.append(  tag_d*freq )
	else: tag_d_trust += 1
	if not(tag_eu == None): tag_eu_sum.append(  tag_eu*freq )
	else: tag_eu_trust += 1
	if not(tag_t == None): tag_t_sum.append(  tag_t*freq )
	else: tag_t_trust += 1
	#if (old_username == '1165'): 
	  #print 'first', freq, tag_fu, tag_fr, tag_t, tag_d, tag_eu
	  #print 'after',tag_fu_sum, tag_fr_sum, tag_t_sum, tag_d_sum, tag_eu_sum
      elif not(old_username == ''):
	if (dict_userres[old_username] > 20) and (tag_sum > 5) and (tas_sum > 60):
	    tas.append(tas_sum)
	    username.append(old_username)
	    #if (old_username == '1165'): print tag_sum, tas_sum, tag_fu_sum, tag_fr_sum, tag_t_sum, tag_d_sum, tag_eu_sum
	    if not(tag_fu_trust > trust_lim*tag_sum): fu.append(median(tag_fu_sum) / (tas_sum ))
	    else: fu.append(-1.0)
	    if not(tag_fr_trust > trust_lim*tag_sum): fr.append(median(tag_fr_sum) / (tas_sum))
	    else: fr.append(-1.0)
	    if not(tag_eu_trust > trust_lim*tag_sum): eu.append(median(tag_eu_sum) / (tas_sum))
	    else: eu.append(-1.0)
	    if not(tag_t_trust > trust_lim*tag_sum): t.append(median(tag_t_sum) / (tas_sum))
	    else: t.append(-1.0)
	    if not(tag_d_trust > trust_lim*tag_sum): d.append(median(tag_d_sum) / (tas_sum))
	    else: d.append(-1.0)
	    fu_t.append(tag_fu_trust / tag_sum)
	    fr_t.append(tag_fr_trust / tag_sum)
	    eu_t.append(tag_eu_trust / tag_sum)
	    d_t.append(tag_d_trust / tag_sum)
	    t_t.append(tag_t_trust / tag_sum)
	    #print len(username), len(d), len(fr), len(fu), len(eu), len(t)
	tag_sum = 1.0
	tas_sum = float(freq)
	tag_fu_sum = []
	tag_fr_sum = []
	tag_d_sum = []
	tag_eu_sum = []
	tag_t_sum = []
	tag_fu_trust = 0.0
	tag_fr_trust = 0.0
	tag_eu_trust = 0.0
	tag_d_trust = 0.0
	tag_t_trust = 0.0
	if not(tag_fu == None): tag_fu_sum.append(  tag_fu*freq )
	else: tag_fu_trust += 1
	if not(tag_fr == None): tag_fr_sum.append(  tag_fr*freq )
	else: tag_fr_trust += 1
	if not(tag_d == None): tag_d_sum.append(  tag_d*freq )
	else: tag_d_trust += 1
	if not(tag_eu == None): tag_eu_sum.append(  tag_eu*freq )
	else: tag_eu_trust += 1
	if not(tag_t == None): tag_t_sum.append(  tag_t*freq )
	else: tag_t_trust += 1
      old_username = new_username

if (dict_userres[old_username] > 20) and (tag_sum > 5) and (tas_sum > 60):
    tas.append(tas_sum)
    username.append(old_username)
    if not(tag_fu_trust > trust_lim*tag_sum): fu.append(median(tag_fu_sum) / (tas_sum))
    else: fu.append(-1.0)
    if not(tag_fr_trust > trust_lim*tag_sum): fr.append(median(tag_fr_sum) / (tas_sum))
    else: fr.append(-1.0)
    if not(tag_eu_trust > trust_lim*tag_sum): eu.append(median(tag_eu_sum) / (tas_sum))
    else: eu.append(-1.0)
    if not(tag_t_trust > trust_lim*tag_sum): t.append(median(tag_t_sum) / (tas_sum))
    else: t.append(-1.0)
    if not(tag_d_trust > trust_lim*tag_sum): d.append(median(tag_d_sum) / (tas_sum))
    else: d.append(-1.0)
    fu_t.append(tag_fu_trust / tag_sum)
    fr_t.append(tag_fr_trust / tag_sum)
    eu_t.append(tag_eu_trust / tag_sum)
    d_t.append(tag_d_trust / tag_sum)
    t_t.append(tag_t_trust / tag_sum)  



#normalize data to be in the range of [0,1].
#NB: some values are -1, which basically means that the trust of this user is 1.0 - which in turn means that the specifity of the user could not be calculated
def normalize_data(list_):
  max_ = max(list_)
  list_c = copy.deepcopy(list_)
  for i in range(list_c.count(-1.0)):
    list_c.remove(-1.0)
  min_ = min(list_c)
  for i in range(len(list_)):
    if not(list_[i] == -1):
      list_[i] = float(list_[i])/(max_-min_)  
    else:
      list_[i] = -1.0
  return list_
  
  
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