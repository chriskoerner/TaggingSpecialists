# -*- coding: utf-8 -*-

class ExpertUser1:

    def __init__(self):
        #user_tag_vector helpers
        self.tas_sum = 0.0
        self.tag_sum = 0.0
        self.tag_fu_sum = []
        self.tag_fr_sum = []
        self.tag_d_sum = []
        self.tag_eu_sum = []
        self.tag_t_sum = []
        #user_trust_value helpers
        #trust is used to calculate the amount of tags for which spec_level for corresponding method could be retrieved versus the amount of tags in a personomy
        #trust 0 = all tags could be used, trust 1 = no tags of personomy could be used to calculate user specifity
        self.tag_fu_trust = 0.0
        self.tag_fr_trust = 0.0
        self.tag_eu_trust = 0.0
        self.tag_d_trust = 0.0
        self.tag_t_trust = 0.0

    def get_tag_sum(self):
        return self.tag_sum

    def get_tas_sum(self):
        return self.tas_sum

    def get_tag_fu_trust(self):
        return self.tag_fu_trust

    def get_tag_fr_trust(self):
        return self.tag_fr_trust

    def get_tag_eu_trust(self):
        return self.tag_eu_trust

    def get_tag_t_trust(self):
        return self.tag_t_trust

    def get_tag_d_trust(self):
        return self.tag_d_trust

    def get_tag_fu_trust(self):
        return self.tag_fu_trust

    def get_tag_fu_sum(self):
        return self.tag_fu_sum

    def get_tag_eu_sum(self):
        return self.tag_eu_sum

    def get_tag_fr_sum(self):
        return self.tag_fr_sum

    def get_tag_t_sum(self):
        return self.tag_t_sum

    def get_tag_d_sum(self):
        return self.tag_d_sum

    def reset_userdata(self):
        self.tag_sum = 1.0
        # fixxme: freq?
        # self.tas_sum = float(freq)
        self.tas_sum = float(0.0)
        self.tag_fu_sum = []
        self.tag_fr_sum = []
        self.tag_d_sum = []
        self.tag_eu_sum = []
        self.tag_t_sum = []
        self.tag_fu_trust = 0.0
        self.tag_fr_trust = 0.0
        self.tag_eu_trust = 0.0
        self.tag_d_trust = 0.0
        self.tag_t_trust = 0.0


    def add_userdata(self,freq, tag_fr, tag_fu, tag_eu, tag_t, tag_d):
        self.tas_sum += freq
        self.tag_sum += 1.0
        if tag_fu is not None: self.tag_fu_sum.append(  tag_fu*freq )
        else: self.tag_fu_trust += 1
        if tag_fr is not None: self.tag_fr_sum.append(  tag_fr*freq )
        else: self.tag_fr_trust += 1
        if tag_d is not None: self.tag_d_sum.append(  tag_d*freq )
        else: self.tag_d_trust += 1
        if tag_eu is not None: self.tag_eu_sum.append(  tag_eu*freq )
        else: self.tag_eu_trust += 1
        if tag_t is not None: self.tag_t_sum.append(  tag_t*freq )
        else: self.tag_t_trust += 1

    	