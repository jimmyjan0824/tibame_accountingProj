from django.db import models
from django.db.models import DateField,CharField,ForeignKey,IntegerField

# Create your models here.
BALANCE_TYPE=((u'收入',u'收入'),(u'支出',u'支出'))

class Category(models.Model):
	category = CharField(max_length=20)

	def __str__(self):
		return self.category

class Record(models.Model):
	date = DateField()
	description = CharField(max_length=300)
	category = ForeignKey(Category,on_delete=models.SET_NULL,null=True)
	cash = IntegerField()
	balanceType = CharField(choices=BALANCE_TYPE,max_length=2)

	def __str__(self):
		return self.description