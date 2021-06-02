from django.db import models

class Recruit(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	contact = models.EmailField(max_length=50)
	sex = models.CharField(max_length=50)
	title = models.CharField(max_length=50)
	link = models.URLField(max_length=200)

	def __str__(self):
		return self.name
class Login(models.Model):
	RecId = models.ForeignKey(Recruit, default=None, on_delete=models.CASCADE)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Item(models.Model):
	
	user = models.ManyToManyField(Recruit)
	title_tula = models.CharField(max_length=50)
	text = models.TextField(default="")
	video_file = models.FileField(upload_to='post_files',blank=True, null=True)
	book_donation = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	integer = models.IntegerField(null=True)
	comment = models.CharField(max_length=50)
	posting = models.ManyToManyField(Login)

	def __str__(self):
		return self.text


class Dmin(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Admindoing(models.Model):
	publications = models.ManyToManyField(Dmin)
	text = models.TextField(default="")
	integer = models.IntegerField(null=True)
	comment = models.CharField(max_length=50)