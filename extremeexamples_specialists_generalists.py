# -*- coding: utf-8 -*-
import copy
from scipy import stats
import json
import pickle


#to plot example specialists and generalists
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts
from pytagcloud import create_tag_image, create_html_data, make_tags, \
    LAYOUT_HORIZONTAL, LAYOUTS, LAYOUT_MIX


from parameters import * #NB: not in gitbub

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#now calculate and plot some generalists / specialists data

fu_n = pickle.load(open('results/spec_frequser_distr.pkl'))
eu_n = pickle.load(open('results/spec_entruser_distr.pkl'))
fr_n = pickle.load(open('results/spec_freqres_distr.pkl'))
t_n = pickle.load(open('results/spec_tfidf_distr.pkl'))
d_n = pickle.load(open('results/spec_degree_distr.pkl'))
username = pickle.load(open('results/spec_usernamnes.pkl'))
  


def specialist_generalist_threshold(list_):
    d_sort = copy.deepcopy(list_)
    for i in range(d_sort.count(-1.0)):
	d_sort.remove(-1.0)
	d_sort.sort()
    dmax = stats.scoreatpercentile(d_sort,GENERALIST_THRESHOLD) 
    dmin = stats.scoreatpercentile(d_sort,SPECIALIST_THRESHOLD)
    return dmin,dmax
   

##plot some stat data
#lmin,lmax = specialist_generalist_threshold(fr_n)
#pylab.hist(numpy.log(fr_n))
#pylab.xlabel('Resource-Frequency based specialist distribution')
#pylab.ylabel('#Users')
#pylab.plot([numpy.log(lmin), numpy.log(lmax)],[0,6000],'g')
#pylab.plot([numpy.log(lmin), numpy.log(lmax)],[0,6000],'g')

#lmin,lmax = specialist_generalist_threshold(fu_n)
#pylab.hist(numpy.log(fu_n))
#pylab.xlabel('User-Frequency based specialist distribution')
#pylab.ylabel('#Users')
#pylab.plot([numpy.log(lmin), numpy.log(lmin)],[0,7000],'g')
#pylab.plot([numpy.log(lmax), numpy.log(lmax)],[0,7000],'g')

#d_sort = copy.deepcopy(eu_n)
#for i in range(d_sort.count(-1.0)):
	#d_sort.remove(-1.0)
	#d_sort.sort()
#for i in range(d_sort.count(0.0)):
	#d_sort.remove(-0.0)
	#d_sort.sort()
#lmin,lmax = specialist_generalist_threshold(eu_n)
#pylab.hist(numpy.log(d_sort))
#pylab.xlabel('User-Entropy based specialist distribution')
#pylab.ylabel('#Users')
#pylab.plot([numpy.log(lmin), numpy.log(lmin)],[0,6000],'g')
#pylab.plot([numpy.log(lmax), numpy.log(lmax)],[0,6000],'g')

#d_sort = copy.deepcopy(t_n)
#lmin,lmax = specialist_generalist_threshold(t_n)
#pylab.hist(numpy.log(t_n))
#pylab.xlabel('Tf-Idf based specialist distribution')
#pylab.ylabel('#Users')
#pylab.plot([numpy.log(lmin), numpy.log(lmin)],[0,6000],'g')
#pylab.plot([numpy.log(lmax), numpy.log(lmax)],[0,6000],'g')

#d_sort = copy.deepcopy(d_n)
#for i in range(d_sort.count(-1.0)):
	#d_sort.remove(-1.0)
	#d_sort.sort()
#for i in range(d_sort.count(0.0)):
	#d_sort.remove(0.0)
	#d_sort.sort()
#lmin,lmax = specialist_generalist_threshold(d_n)
#pylab.hist(numpy.log(d_sort))
#pylab.xlabel('Tag-degree based specialist distribution')
#pylab.ylabel('#Users')
#pylab.plot([numpy.log(lmin), numpy.log(lmin)],[0,7000],'g')
#pylab.plot([numpy.log(lmax), numpy.log(lmax)],[0,7000],'g')
    
    
    
def get_specialist_generalist_names(username,speclevellist):
  lmin,lmax = specialist_generalist_threshold(speclevellist)
  print lmin, lmax
  ret_max = []
  ret_min = []
  for i in range(len(username)):
    if not(speclevellist[i] == -1):
      if speclevellist[i] >= lmax: ret_max.append(username[i])    
      elif speclevellist[i] <= lmin: ret_min.append(username[i])
  return ret_min, ret_max  


fr_spec, fr_gen = get_specialist_generalist_names(username, fr_n)
fu_spec, fu_gen = get_specialist_generalist_names(username, fu_n)
eu_spec, eu_gen = get_specialist_generalist_names(username, eu_n)
t_spec, t_gen = get_specialist_generalist_names(username, t_n)
d_spec, d_gen = get_specialist_generalist_names(username, d_n)

#calc
absolute_specialists = set(t_spec).intersection(eu_spec).intersection(fu_spec).intersection(fr_spec).intersection(d_spec)
absolute_generalists = set(t_gen).intersection(eu_gen).intersection(fu_gen).intersection(fr_gen).intersection(d_gen)

#store data
pickle.dump(absolute_specialists, open('results/absolute_specialists_10','wb'))
pickle.dump(absolute_generalists, open('results/absolute_generalists_10','wb'))




      
def print_user_htmltagclouds(list_usernames,path):      
      
      file_ = open('data/personomies_extended')
      tag_t_cloud = []
      tag_fr_cloud = []
      tag_cloud_tags = []
      tag_d_cloud = []
      tag_sum = 0.0
      tas_sum = 0.0
      old_usernameprint = ''
      sum_clouds = 0
      sum_clouds_not = 0
      for line in file_:
	    row = line.strip('\n').split(' ')
	    freq = float(row[0])
	    new_username = row[1]
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
	    else: 
	      tag_t = None
	    if new_username in list_usernames:
	      if (new_username == old_username) or (old_username == ''):
		tas_sum += freq
		tag_sum += 1.0
		#if not(tag_fr == None): tag_fr_cloud.append((tag,tag_fr*freq)) 
		#if not(tag_d == None): tag_d_cloud.append((tag,tag_d*freq)) 
		#if not(tag_eu == None): tag_eu_sum.append(tag_eu*freq)	  
		if not(tag_t == None): tag_t_cloud.append((tag,tag_t*freq))
		tag_cloud_tags.append((tag,freq))
		old_usernameprint = old_username
	      else:
		  if not(tag_cloud_tags == []) and (len(tag_cloud_tags)>1) and tag_sum < PRINT_TAG_THRESHOLD:
		    sum_clouds += 1
		    if sum_clouds > PRINT_CLOUDS: break
		    tags_adjusted = []
		    sum_ = 0.0
		    for pair in tag_cloud_tags:
		      print pair
		      tags_adjusted.append((pair[0].replace('%20',' '),pair[1]))
		      sum_ += pair[1]
		    if not(sum_ == len(tags_adjusted)):	
		      tags = make_tags(tags_adjusted)
		      for layout in LAYOUTS:
			  data, html_text = create_html_data(tags, size=(600, 500), fontname='Lobster', fontzoom=1)
			  html_file = open(path+'tagcloud_'+str(old_usernameprint)+'_'+'10'+'.html', 'w')
			  html_file.write(html_text)
			  html_file.close()
		  else: sum_clouds_not += 1
		  tag_sum = 1.0
		  #tag_t_cloud = [(tag,tag_t*freq)]
		  #tag_fr_cloud = [(tag,tag_fr*freq)]
		  #tag_d_cloud = [(tag,tag_d*freq)]	    
		  if not(tag_t == None): tag_cloud_tags = [(tag,freq)]
		  else: tag_cloud_tags = []
		  old_usernameprint = new_username	    
	    old_username = new_username      
	    
      print 'Number of clouds printed:',sum_clouds,' and number of users dropped:',sum_clouds_not
      


print_user_htmltagclouds(absolute_specialists,'info/specialists')
print_user_htmltagclouds(absolute_generalists,'info/generalists')
