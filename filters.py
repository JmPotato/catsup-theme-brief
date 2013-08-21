def gravatar(email):
	import hashlib
	size=48 * 2
	hashed_email = hashlib.md5(email).hexdigest()
	url = "http://9429127371.a.uxengine.net/avatar/" + hashed_email
	url += '?s=%s' % size
	return url