from django.db import models
from django.contrib.auth.models import User

class BlogApp(models.Model):
	title = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'images/', default = '/images/x.jpg', blank=True, null=True)
	body = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	upvote = models.IntegerField(default = 0)
	user_upvoted = models.TextField(default = "")

	def __str__(self):
		return self.title

	def summary(self):
		return (self.body[:100]+'. . . ')

	def pub_date_pretty(self):
		return self.pub_date.strftime("%b %e, %Y")
	

class Comment(models.Model):
	name = models.CharField(max_length = 40)
	comment = models.TextField()
	blog = models.ForeignKey(BlogApp, on_delete = models.CASCADE)
	flag = models.IntegerField(default = 0)

	def __str__(self):
		return self.comment
