# -*- coding: utf-8 -*-

from collections import defaultdict
import Tag


__author__ = 'Karin Schöfegger'



###Bug: if you call a key, which does not exist yet, it is added to the dictionary with default Tag values


class TagDictionary(defaultdict):
  
    def __init__(self):
        super(TagDictionary,self).__init__(Tag.Tag)
        self.itemlist = super(TagDictionary,self).keys()
                
    def __setitem__(self, key, value):
          # TODO: what should happen to the order if
          #       the key is already in the dict    
	    self.itemlist.append(key)
	    super(TagDictionary,self).__setitem__(key, value)
         
    def __iter__(self):
         return iter(self.itemlist)
         
    def keys(self):
         return self.itemlist    
         
    def values(self):
         return [self[key] for key in self]  
         
    def itervalues(self):
         return ([self[key] for key in self])
         
    def values_degree(self):
	 return ([self[key].get_degree() for key in self])

    def values_frequency_user(self):
	 return ([self[key].get_frequency_user() for key in self])

    def values_frequency_resource(self):
	 return ([self[key].get_frequency_resource() for key in self])
	 
    def values_entropy_user(self):
	 return ([self[key].get_entropy_user() for key in self])
	 
    def values_entropy_resource(self):
	 return ([self[key].get_entropy_resource() for key in self])
	 
    def values_tfidf(self):
	 return ([self[key].get_tfidf() for key in self])
	 
    def values_degree_clean(self):
	 ret = []
	 k = []
         for key in self:
	   if (self[key].get_degree()):
	     ret.append(self[key].get_degree()) 
	     k.append(key)
	 return ret,k

    def values_frequency_user_clean(self):
         ret = []
	 k = []
	 for key in self:
	   if (self[key].get_frequency_user()):
	     ret.append(self[key].get_frequency_user())
	     k.append(key)
	 return ret,k

    def values_frequency_resource_clean(self):
         ret = []
         k = []
         for key in self:
	   if (self[key].get_frequency_resource()):
	     ret.append(self[key].get_frequency_resource())
	     k.append(key)
	 return ret,k
	 
    def values_entropy_user_clean(self):
         ret = []
         k = []
         for key in self:
	   if (self[key].get_entropy_user()):
	     ret.append(self[key].get_entropy_user())
	     k.append(key)
	 return ret,k
	 
    def values_entropy_resource_clean(self):
         ret = []
         k = []
         for key in self:
	   if (self[key].get_entropy_resource()):
	     ret.append(self[key].get_entropy_resource())
	     k.append(key)
	 return ret,k
	 
    def values_tfidf_clean(self):
         ret = []
         k = []
         for key in self:
	   if (self[key].get_tfidf()):
	     ret.append(self[key].get_tfidf())  
	     k.append(key)
	 return ret,k
	 
    def get_all_values(self):
      ret_d = []
      ret_f_u = []
      ret_f_r = []
      ret_e_r = []
      ret_e_u = []
      ret_t = []
      ret_key = []
      for key in self:
	  if (self[key].get_tfidf()) and (self[key].get_entropy_resource()) and (self[key].get_entropy_user()) and (self[key].get_frequency_resource()) and  (self[key].get_frequency_user()) and (self[key].get_degree()):
	    ret_d.append(self[key].get_degree())
	    ret_f_u.append(self[key].get_frequency_user())
	    ret_f_r.append(self[key].get_frequency_resource())
	    ret_e_u.append(self[key].get_entropy_user())
	    ret_e_r.append(self[key].get_entropy_resource())
	    ret_t.append(self[key].get_tfidf())
	    ret_key.append(self[key].get_name())
      return ret_d, ret_f_u, ret_f_r, ret_e_u, ret_e_r, ret_t, ret_key	
	 
    def normalize_dict(self):
      #normalize degree values
      m_deg = max(self.values_degree())
      m_fr_u = max(self.values_frequency_user())
      m_fr_r = max(self.values_frequency_resource())
      m_e_u = max(self.values_entropy_user())
      m_e_r = max(self.values_entropy_resource())
      m_t = max(self.values_tfidf())
      for key in self:
	tag = self[key]
	if (m_deg > 0.0) and (self[key].get_degree()):
	  self[key].set_degree(tag.get_degree() / m_deg)
	if (m_fr_r > 0.0) and (self[key].get_frequency_resource()):  
	  self[key].set_frequency_resource(tag.get_frequency_resource() / m_fr_r)
	if (m_fr_u > 0.0) and (self[key].get_frequency_user()):
	  self[key].set_frequency_user(tag.get_frequency_user() / m_fr_u)
	if (m_e_u > 0.0) and (self[key].get_entropy_user()):
	  self[key].set_entropy_user(tag.get_entropy_user() / m_e_u)
	if (m_e_r > 0.0) and (self[key].get_entropy_resource()):
	  self[key].set_entropy_resource(tag.get_entropy_resource() / m_e_r)
	if (m_t > 0.0) and (self[key].get_tfidf()):
	  self[key].set_tfidf(tag.get_tfidf() / m_t)
	
	 
	 
	 
if __name__ == '__main__':
  TD = TagDictionary()
  tag = Tag.Tag('testtag')
  tag.set_degree(4)
  tag.set_frequency_user(5)
  tag.set_frequency_resource(6)
  tag.set_entropy_user(7)
  tag.set_entropy_resource(8)
  tag.set_tfidf(9)
  
  tag1 = Tag.Tag('testtag1')
  tag1.set_degree(4)
  tag1.set_frequency_user(5)
  tag1.set_frequency_resource(6)
  tag1.set_entropy_user(7)
  tag1.set_entropy_resource(8)
  tag1.set_tfidf(9.0)
  
  TD[tag.get_name()] = tag
  TD[tag1.get_name()] = tag1
  print 'tfidf: ',TD.values_tfidf()
  print 'freq_user: ',TD.values_frequency_user()
  print 'freq_resource: ',TD.values_frequency_resource()
  print 'entr_user: ',TD.values_entropy_user()
  print 'freq_resource: ',TD.values_entropy_resource()
  print 'degree: ',TD.values_degree()
  print 'not defined tag: ', TD['testtag2'].get_name()
  
  TD.normalize_dict()
  print 'tfidf: ',TD.values_tfidf()
  print 'freq_user: ',TD.values_frequency_user()
  print 'freq_resource: ',TD.values_frequency_resource()
  print 'entr_user: ',TD.values_entropy_user()
  print 'freq_resource: ',TD.values_entropy_resource()
  print 'degree: ',TD.values_degree()
  
  print TD.get_all_values()
  print TD.values_frequency_user_clean()
  
      