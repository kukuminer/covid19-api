"""
FILE: integrator_interface.py
DESCRIPTION: Interface for integrators
AUTHOR: Liran Zheku
DATE: 13-April-2021
"""
class IntegratorInterface
	""" 
	Interface to extend integrators v2 and higher from.
	Features the minimum expected functions from an integrator 
	"""
	
	def get_time_series(self):
		pass
		
	def get_current(self):
		pass
		
	def get_country(self):
		pass
	
	def get_deaths(self):
		pass
		
	def get_recovered(self):
		pass
		
	def get_total(self):
		pass
		
	def get_confirmed(self):
		pass
		
	def get_active(self):
		pass
		
	def get_total(self):
		pass

