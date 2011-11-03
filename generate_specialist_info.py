# -*- coding: utf-8 -*-

__author__ = 'kschoef'

from lookup_utilities import user_academicstatus_lookup, relevantuserdisc_lookup, user_nrresources_lookup


user_adacemicstatus_dict = user_academicstatus_lookup()
user_disciplines_dict, user_owndiscipline_dict = relevantuserdisc_lookup(threshold=0.75)
user_nres_dict = user_nrresources_lookup()

file_ = open('results/specialist_info_helperfile')
file_write = open('results/specialist_info','wb')


#the generated file contains, tab seperated:
#username nr_tag nr_tas fu trust fr trust eu trust eu trust t trust d trust nr_res

for line in file_:
    row = line.strip('\n').split('\t')
    user = row[0]
    #check if all data for user is available:
    try:
        prof = user_adacemicstatus_dict[user]
        derived_disc = user_disciplines_dict[user]
        disc = user_owndiscipline_dict[user]
        nr_res = user_nres_dict[user]
    except: continue # todo: if lookups fail for dicts --> skip user
    #if data available, write in file

    new_line = line.strip('\n')
    new_line += '\t'+str(nr_res)
    new_line += '\t'+str(prof)
    new_line += '\t'+str(derived_disc)
    new_line += '\t'+str(disc) + '\n'
    file_write.write(new_line)


file_write.close()          