# -*- coding: utf-8 -*-

__author__ = 'kschoef'

from lookup_utilities import user_academicstatus_lookup, user_discipline_lookup, user_nrresources_lookup

user_adacemicstatus_dict = user_academicstatus_lookup()
user_disciplines_dict, user_owndiscipline_dict = user_discipline_lookup()
user_nres_dict = user_nrresources_lookup()

file_ = open('results/specialist_info_helperfile','wb')
file_write = open('results/specialist_info','wb')

for line in file_:
        row = line.strip('\n').split('\t')
        user = row[0]
        fail = False        
        #check if all data for user is available:
        try:
	  prof = user_adacemicstatus_dict[user] 
	  derived_disc = len(user_disciplines_dict[user])  
	  disc = user_owndiscipline_dict[user]
	  nr_Res = user_nres_dict[user]
	  except: fail = True  
	#if data available, write in file  
        if not(fail):
	  new_line = line.strip('\n')
	  new_line += 
        