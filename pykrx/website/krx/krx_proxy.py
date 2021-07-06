
""" Singleton to store proxy """
class Proxy(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "instance"):
			cls.instance = super(Proxy, cls).__new__(cls)
		return cls.instance

	def __init__(ins):
		if 'value' not in ins.__dict__.keys():
			ins.value = dict()

	def set(ins, proxy:dict):
		for key in proxy.keys():
			if (key != "http") and (key != "https"):
				raise ValueError("Wrong proxy format")
		ins.value = proxy
		
	def get(ins):
		return ins.value

