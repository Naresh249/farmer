from django.shortcuts import render

from django.views.generic import View

class Farmer(View):
	"""
	Farmer Data Collector View
	"""
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		"""
		View to render and collect former data
		"""
		return render(request, self.template_name, {'message': 'rendering former dashboard'})
		
