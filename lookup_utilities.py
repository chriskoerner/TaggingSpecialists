# -*- coding: utf-8 -*-

__author__ = 'kschoef'

import collections
from TagDictionary import TagDictionary


def user_academicstatus_lookup():
  file_ = open('data/user_academicStatusId')
  userprof_dict = {}
  count_ = 0
  for line in file_:
      count_ += 1
      if count_ > 1:
	row = line.strip('\n').split('\t')
	user = row[0]
	if row[1] != 'NULL':
	  prof = int(row[1])
	else: prof = -1	
	userprof_dict[user]=prof
   return userprof_dict


def user_discipline_lookup():            
  file_ = open('ground/users_distribution_overDiscipline.via_resources')
  count_abweichung = 0
  userdiscipline_dict = defaultdict(list)
  userowndiscipline_dict = defaultdict(str)
  for line in file_: 
      row = line.strip('\n').split('\t')
      user = row[0]
      disciplines = json.loads(row[1])
      di = row[2]
      userdiscipline_dict[user] = disciplines
      userowndiscipline_dict[user] = di
  return userdiscipline_dict, userowndiscipline_dict
  
  
def user_nrresources_lookup(): 
  file_ = open('data/user_resources_count')
  dict_userres = collections.defaultdict(int)
  for line in file_:
      row = line.strip('\n').split(' ')
      val = int(row[0])
      user = row[1]
      dict_userres[user] += val 
  return dict_userres
  
  
  
  
def read_normalizedTagGeneralityData()
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
    
    return TD	   