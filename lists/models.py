from django.db import models

class List(models.Model):
	pass
	
class Item(models.Model):
	text = models.TextField(default='')
	# 1.9 or below
	# list = models.ForeignKey(List, default=None)
	# 2.0 +
	list = models.ForeignKey(List, on_delete=models.CASCADE)
	# list = models.ForeignKey(List, on_delete=models.PROTECT, default=None)