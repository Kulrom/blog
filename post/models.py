from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=255)
	post_date = models.DateTimeField(auto_now_add=True)
	edit_date = models.DateTimeField(auto_now=True)
	markdown = models.TextField()
	public = models.BooleanField()

	def __unicode__(self):
		return self.title;