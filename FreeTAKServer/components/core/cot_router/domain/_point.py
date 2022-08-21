#######################################################
# 
# point.py
# Python implementation of the CoT point
# Generated by Enterprise Architect
# Created on(FTSProtocolObject):      11-Feb-2020 11(FTSProtocolObject):08(FTSProtocolObject):07 AM
# Original author: Corvo
# 
#######################################################
# Latitude referred to the WGS 84 ellipsoid in degrees
from .model_constants.PointVariables import PointVariables as vars
from FreeTAKServer.components.core.abstract_component.cot_node import CoTNode
from FreeTAKServer.components.core.abstract_component.cot_property import CoTProperty


class point(CoTNode):

    def __init__(self, configuration, model, le=vars().LE, ce=vars().CE, hae=vars().HAE, lon=vars().LON, lat=vars().LAT):        
        super().__init__(self.__class__.__name__, configuration, model)
        self.cot_attributes["le"] = le
        self.cot_attributes["ce"] = ce
        self.cot_attributes["hae"] = hae
        self.cot_attributes["lon"] = lon
        self.cot_attributes["lat"] = lat

    @CoTProperty
    def ce(self): 
        return self.cot_attributes.get("ce", None)

    @ce.setter
    def ce(self, ce):
        self.cot_attributes["ce"]=ce 

    @CoTProperty
    def le(self): 
        return self.cot_attributes.get("le", None)

    @le.setter
    def le(self,le):  
        self.cot_attributes["le"]=le

    @CoTProperty
    def lat(self):
        return self.cot_attributes.get("lat", None)

    @lat.setter
    def lat(self, lat):  
        self.cot_attributes["lat"]=lat

    @CoTProperty
    def lon(self):
        return self.cot_attributes.get("lon", None)

    @lon.setter
    def lon(self,lon):
        self.cot_attributes["lon"]=lon

    @CoTProperty
    def hae(self):
        return self.cot_attributes.get("hae", None)

    @hae.setter
    def hae(self,hae):
        self.cot_attributes["hae"] = hae