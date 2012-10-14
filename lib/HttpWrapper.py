import urllib
import urllib2
import cookielib

class HTTPWrapper:
	def __init__(self, KeepCookies=True):
		if(KeepCookies):
			self.cj = cookielib.CookieJar()
			self.HTTP = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		else:
			self.HTTP = urllib2.build_opener()
	
	def Req(self, URL, data={}):
		return self.HTTP.open(URL,urllib.urlencode(data)).read()

	def GetBetween(self, s, leader, trailer):
		end_of_leader = s.index(leader) + len(leader)
	  	start_of_trailer = s.index(trailer, end_of_leader)
  		return s[end_of_leader:start_of_trailer]