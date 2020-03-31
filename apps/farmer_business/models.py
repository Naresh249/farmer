from django.db import models

class ModelBase(models.Model):
    """
        This is a abstract model class to add is_deleted, created_at and updated at fields in any model
    """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """ Soft delete """
        self.is_deleted = True
        self.save()

class Farmer(ModelBase):
	"""
	Model to store farmer details
	"""
	name 				= models.CharField(max_length=254)
	phone_number 		= models.CharField(max_length=13)
	language 			= models.CharField(max_length=254, null=True)


class FarmerFarm(ModelBase):
	"""
	Model to store farmer farm
	"""	
	farmer				= models.ForeignKey(Farmer, on_delete=models.CASCADE)
	area				= models.CharField(max_length=254)
	crop_grown			= models.CharField(max_length=254)
	sowing_date			= models.DateField()
	status				= models.CharField(max_length=100)

class FarmerFarmSchedule(ModelBase):
	"""
	Model to store farmer farm schedule
	"""
	farmer_farm			= models.ForeignKey(FarmerFarm, on_delete=models.CASCADE)
	days_after_sowing	= models.IntegerField(null=True, blank=False)
	fertiliser			= models.CharField(max_length=254)
	quantity			= models.FloatField(null=False)
	quantity_unit		= models.CharField(max_length=10, null=False)