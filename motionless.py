import urllib.parse
import re

"""
    motionless is a library that takes the pain out of generating Google Static Map URLs.

    For example code and documentation see: 
        http://github.com/ryancox/motionless

    For details about the GoogleStatic Map API see: 
        http://code.google.com/apis/maps/documentation/staticmaps/

    If you encounter problems, log an issue on github. If you have questions, drop me an
    email at ryan.a.cox@gmail.com.

"""

"""

      Copyright 2010 Ryan A Cox - ryan.a.cox@gmail.com 

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License. 

"""



__author__ = "Ryan Cox <ryan.a.cox@gmail.com>"
__version__ = "1.0"   

class Color(object):
    COLORS = ['black', 'brown', 'green', 'purple', 'yellow', 'blue', 'gray', 'orange', 'red', 'white']
    pat = re.compile("0x[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8}")
    @staticmethod
    def is_valid_color(color):
        return Color.pat.match(color) or color in Color.COLORS
         

class Marker(object):
    SIZES =  ['tiny','mid','small']
    LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    def __init__(self, size, color, label):
        if size and size not in Marker.SIZES:
            raise ValueError("[%s] is not a valid marker size. Valid sizes include %s" % (size,Marker.SIZES))
       # if label and (len(label) <> 1 or not label in Marker.LABELS):
          #  raise ValueError("[%s] is not a valid label. Valid labels are a single character 'A'..'Z' or '0'..'9'"  % label)
        if color and color not in Color.COLORS:
            raise ValueError("[%s] is not a valid color. Valid colors include %s"  % ( color, Color.COLORS ))
        self.size = size
        self.color = color
        self.label = label

class AddressMarker(Marker):
    def __init__(self, address, size=None, color=None, label=None):
        Marker.__init__(self,size,color,label)
        self.address = address

class LatLonMarker(Marker):
    def __init__(self, lat, lon, size=None, color=None, label=None):
        Marker.__init__(self,size,color,label)
        self.latitude = lat
        self.longitude = lon

class Map(object):
    MAX_URL_LEN = 2048
    MAPTYPES = ['roadmap','satellite','hybrid','terrain']
    FORMATS = ['png','png8','png32','gif','jpg','jpg-baseline']
    MAX_X = 640
    MAX_Y = 640
    def __init__(self, size_x, size_y, maptype):

        self.base_url = 'http://maps.google.com/maps/api/staticmap?'
        self.size_x = size_x 
        self.size_y = size_y 
        self.sensor = False 
        self.format = 'png'
        self.maptype = maptype 

    def __str__(self):
        return self.generate_url()                        

    def check_parameters(self):
        if self.format not in Map.FORMATS:
            raise ValueError("[%s] is not a valid file format. Valid formats include %s" % (self.format,Map.FORMATS))
    
        if self.format not in Map.FORMATS:
            raise ValueError("[%s] is not a valid map type. Valid types include %s" % (self.maptype,Map.MAPTYPES))
        
        if self.size_x > Map.MAX_X or self.size_x < 1:
            raise ValueError("[%s] is not a valid x-dimension. Must be between 1 and %s" % (self.size_x,Map.MAX_X))

        if self.size_y > Map.MAX_Y or self.size_y < 1:
            raise ValueError("[%s] is not a valid y-dimension. Must be between 1 and %s" % (self.size_x,Map.MAX_Y))

    def _get_sensor(self):
        if self.sensor:
            return 'true'
        else:
            return 'false'

    def _check_url(self, url):
        if len(url) > Map.MAX_URL_LEN:
            raise ValueError("Generated URL is %s characters in length. Maximum is %s" % (len(url),Map.MAX_URL_LEN))

class CenterMap(Map):
    ZOOM_RANGE = range(1,21)
    def __init__(self, address=None, lat=None, lon=None, zoom=17, size_x=400, size_y=400, maptype='roadmap'):
        Map.__init__(self,size_x=size_x, size_y=size_y, maptype=maptype)                    
        if address: 
            self.center = urllib.parse.quote(address)
        elif lat and lon:
            self.center = "%s,%s" % (lat,lon)
        else:
            self.center = "1600 Amphitheatre Parkway Mountain View, CA"
        self.zoom = zoom 

    def check_parameters(self):
        super(CenterMap,self).check_parameters()
        
        if self.zoom not in CenterMap.ZOOM_RANGE:
            raise ValueError("[%s] is not a zoom setting. Must be between %s and %s" % (self.size_x,min(CenterMap.ZOOM_RANGE),max(CenterMap.ZOOM_RANGE)))

    def generate_url(self):
        self.check_parameters();
        url = "%smaptype=%s&format=%s&center=%s&zoom=%s&size=%sx%s&sensor=%s" % (
            self.base_url,
            self.maptype,
            self.format,
            self.center,
            self.zoom,
            self.size_x,
            self.size_y,
            self._get_sensor())
    
        self._check_url(url)
        return url

class VisibleMap(Map):
    def __init__(self, size_x=400, size_y=400, maptype='roadmap'):
        Map.__init__(self,size_x=size_x, size_y=size_y, maptype=maptype)                    
        self.locations = []

    def add_address(self, address):
        self.locations.append(urllib.parse.quote(address))

    def add_latlon(self, lat, lon):
        self.locations.append("%s,%s" % (urllib.parse.quote(lat),urllib.parse.quote(lon)))

    def generate_url(self):
        self.check_parameters();
        url = "%smaptype=%s&format=%s&size=%sx%s&sensor=%s&visible=%s" % (
            self.base_url,
            self.maptype,
            self.format,
            self.size_x,
            self.size_y,
            self._get_sensor(),
            "|".join(self.locations))

        self._check_url(url)
        return url

