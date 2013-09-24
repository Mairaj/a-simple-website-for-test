from django.db import models
class ContactUs(models.Model):
        name=models.CharField(max_length=30)
        email=models.CharField(max_length=30)
        mobile=models.BigIntegerField()
        message=models.TextField(max_length=100)

        def __unicode__(self):
                return self.name
class news(models.Model):
	news=models.TextField(max_length=500)
	date=models.DateTimeField(auto_now='true')
	def __unicode__(self):
		return self.news
	class Meta:
        	ordering = ['date']
