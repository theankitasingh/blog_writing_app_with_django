from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from diaries.utilities import *



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class requestcat(models.Model):
	name=models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	statuss=(
	("PENDING", "PENDING"), 
    ("REJECTED", "REJECTED"), 
    ("APPROVED", "APPROVED")
    )
	
	status=models.CharField(max_length=50,choices=statuss)
	def __str__(self):
			return self.name

class categorymodel(models.Model):
		
		name=models.CharField(max_length=100)
		# description=FroalaField(null=True)
		# add_date=models.DateTimeField(auto_now_add=True,null=True)
		slug=models.SlugField(max_length=1000,null=True,blank=True)
		
		def __str__(self):
			return self.name

		def save(self,*args,**kwargs):
			self.slug = generate_slug(self.name)
			super(categorymodel, self).save(*args, **kwargs)



class deardiaryModel(models.Model):
	title=models.CharField(max_length=1000)
	content=FroalaField()
	slug=models.SlugField(max_length=1000,null=True,blank=True)
	user = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
	image=models.ImageField(upload_to='deardiary')
	created_at=models.DateTimeField(auto_now_add=True)
	upload_to=models.DateTimeField(auto_now=True)
	category=models.CharField(max_length=100)
	likes=models.ManyToManyField(User, related_name="blog_posts")
	approved= models.BooleanField('Approved' , default=False)
	# categories_choices=(
	# ("1", ("NONE",['a','b','c'])), 
    # ("2", "TRAVELLING"), 
    # ("3", "COOKING"), 
    # ("4", "BLOGGING"), 
    # ("5", "PERSONAL ACCOUNT"), 
    # ("6", "BUSINESS"), 
    # ("7", "SOCIAL SERVICING"), 
    # ("8", "OTHERS"),
    # ("9", "CODING")
	# )
	# categories_choices =  (
    #         ('Python', 'Python'),
    #         ('Java', 'Java'),
    #         ('C', 'C'),
    #         ('C++', 'C++'),
    #         ('JavaScript', 'JavaScript'),
    #         ('PHP', 'PHP'),
    #         ('SQL', 'SQL'),
    #         ('Swift', 'Swift'),
    #         ('Ruby', 'Ruby'),
    #         ('Go', 'Go'),
    #         ('Other', 'Other'),

    #     )
	# [

#     ('NONE', 'NONE'),
#     ('TRAVELLING', (
#             ('TRAVELLING-Solo', 'TRAVELLING-Solo'),
#             ('TRAVELLING-Friends', 'TRAVELLING-Friends'),
#             ('TRAVELLING-Family', 'TRAVELLING-Family'),
#             ('TRAVELLING-None', 'TRAVELLING-None'),
#         )
#     ),
#     ('COOKING', (
#             ('COOKING-Veg', 'COOKING-Veg'),
#             ('COOKING- Non-veg', 'COOKING- Non-veg'),
            
#         )
#     ),
#     ('BLOGGING', (
#             ('BLOGGING- Mini-blog', 'BLOGGING- Mini-blog'),
#             ('BLOGGING- Full-blog', 'BLOGGING- Full-blog'),
#         )
#     ),
#     ('Personal', 'Personal'),
#     ('BUSINESS', (
#             ('BUSINESS- Mini-business', 'BUSINESS- Mini-business'),
#             ('BUSINESS- Large-business', 'BUSINESS- Large-business'),
#         )
#     ),
#     ('SOCIAL SERVICING', (
#             ('SOCIAL SERVICING- Personal', 'SOCIAL SERVICING- Personal'),
#             ('SOCIAL SERVICING- Professtional', 'SOCIAL SERVICING- Professtional'),
#         )
#     ),
#     ('CODING', (
#             ('CODING- Python', 'CODING- Python'),
#             ('CODING- Java', 'CODING- Java'),
#             ('CODING- C', 'CODING- C'),
#             ('CODING- C++', 'CODING- C++'),
#             ('CODING- JavaScript', 'CODING- JavaScript'),
#             ('CODING- PHP', 'CODING- PHP'),
#             ('CODING- SQL', 'CODING- SQL'),
#             ('CODING- Swift', 'CODING- Swift'),
#             ('CODING- Ruby', 'CODING- Ruby'),
#             ('CODING- Go', 'CODING- Go'),
#         )
#     ),
#     ('Others', 'Others'),
# ]
	#categories = models.CharField(max_length=50,choices=categories_choices)
	def __str__(self):
		return self.title

	def save(self,*args,**kwargs):
		self.slug = generate_slug(self.title)
		super(deardiaryModel, self).save(*args, **kwargs)



class ReviewRating(models.Model):
	Blog=models.ForeignKey(deardiaryModel, related_name="comments", on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=100,blank=True)
	review=FroalaField()
	rating=models.FloatField()
	ip=models.CharField(max_length=20,blank=True)
	status=models.BooleanField(default=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.subject