# -*- coding: utf-8 -*-

__author__ = 'kschoef'

import collections
from TagDictionary import TagDictionary
import json
import csv

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
    userdiscipline_dict = collections.defaultdict(list)
    userowndiscipline_dict = collections.defaultdict(str)
    for line in file_:
        row = line.strip('\n').split('\t')
        user = row[0]
        disciplines = json.loads(row[1])
        di = row[2]
        userdiscipline_dict[user] = disciplines
        userowndiscipline_dict[user] = di
    return userdiscipline_dict, userowndiscipline_dict


def relevantuserdisc_lookup(threshold=0.0):
    """ returns 2 values: a dict with the number of relevat automatically detected disciplines for each user
and the id of the self-added discipline for each user"""
    file_ = open('ground/users_distribution_overDiscipline.via_resources')
    count_abweichung = 0
    userdiscipline_dict = collections.defaultdict(list)
    userowndiscipline_dict = collections.defaultdict(str)
    for line in file_:
        row = line.strip('\n').split('\t')
        user = row[0]
        disciplines = json.loads(row[1])
        di = row[2]
        userowndiscipline_dict[user] = di
        #calculate
        if (threshold > 0.0 and threshold <= 1.0 and not disciplines=={}):
            m = max(disciplines.values())
            keys = disciplines.keys()
            for key in keys:
                if disciplines[key] < threshold*m:
                    del disciplines[key]
        userdiscipline_dict[user] = len(disciplines)
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




def read_normalizedTagGeneralityData():
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



def read_extended_personomy_file(line):
    row = line.strip('\n').split(' ')
    freq = float(row[0])
    username = row[1]
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
    return username, freq, tag_fr, tag_fu, tag_eu, tag_t, tag_d




def specialist_info_lookup(userlist=None):
    # userID nr_tag nr_tas fu trust fr trust eu trust eu trust t trust d trust nr_res
    reader = csv.reader(open('results/specialist_info', 'r'), delimiter='\t')
    count = 0
    for line in reader:
        # todo: what happens here?
        pass


  