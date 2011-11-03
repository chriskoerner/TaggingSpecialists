# -*- coding: utf-8 -*-

__author__ = 'Karin Schöfegger'

class Tag():

    def __init__(self, tagstr = None):
        """ class to model a tag and it's measures"""
        self.name = tagstr
        self.degree = None
        self.tfidf  = None
        self.entropy_user = None
        self.entropy_resource = None
        self.frequency_user = None
        self.frequency_resource = None


    def get_name(self):
        """ return tag name """
        return self.name

    def set_name(self,tagstr):
        self.name = tagstr

    def set_degree(self,value):
        if value >= 0.0:
            self.degree = float(value)
        else: print 'Wrong value for tag degree!'

    def set_frequency_user(self,value):
        if value >= 0.0:
            self.frequency_user = float(value)
        else: print 'Wrong value for tag frequency!'

    def set_frequency_resource(self,value):
        if value >= 0.0:
            self.frequency_resource = float(value)
        else: print 'Wrong value for tag frequency!'

    def set_entropy_user(self,value):
        if value >= 0.0:
            self.entropy_user = float(value)
        else: print 'Wrong value for tag entropy!'

    def set_entropy_resource(self,value):
        if value >= 0.0:
            self.entropy_resource = float(value)
        else: print 'Wrong value for tag entropy!'

    def set_tfidf(self,value):
        if value >= 0.0:
            self.tfidf = float(value)
        else: print 'Wrong value for tag tfidf!', value, self.name

    def get_degree(self):
        return self.degree

    def get_frequency_user(self):
        return self.frequency_user

    def get_frequency_resource(self):
        return self.frequency_resource

    def get_entropy_user(self):
        return self.entropy_user

    def get_entropy_resource(self):
        return self.entropy_resource

    def get_tfidf(self):
        return self.tfidf
