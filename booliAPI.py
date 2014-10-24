import time
import os,binascii
import hashlib
import sys

def uri(resource, query, page=0):
	# Function uri generates a sha1 hash: sha1(callerId + timestamp + key + unique), a 40-char hexadecimal.
	# if page is not given, page=0

	callerId = ("slam")
	timestamp = int(time.time())
	key = ("VHhrvBJNdTU5JWxhppv57Mevid12fLWr9yWxKhes")
	unique = binascii.b2a_hex(os.urandom(16))

	fullstring = callerId+str(timestamp)+key+unique

	hash_object = hashlib.sha1(fullstring)
	hex_dig = hash_object.hexdigest()

	# In python, instead of adding strings with "+", %s can be used as a marker. (String formatting). strings to be inserted is then listed as a tuple ().
	# %s = string, %d = digit %f = float - man kan ven skriva tex %.5d >> sger hur mnga siffror talet ska ha totalt. 
	# For en float blir %.5f hur mnga decimaler talet ska ha. Las mer: String formatting.

	signature = ("&callerId=%s&time=%s&unique=%s&hash=%s") % (callerId, timestamp, unique, hex_dig)
	offset = page * 500

	return u"http://api.booli.se/%s?%s&sort=soldDate&direction=desc&limit=500&offset=%d%s" % (resource, query, offset, signature)

uri("areas", "stockholm") 
