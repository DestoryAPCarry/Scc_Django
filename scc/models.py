from django.db import models

# Create your models here.
#================用户名 密码  first & last name==========================
class User_Infomation(models.Model):
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    sex = models.CharField(max_length=50)
    def __str__(self):
        return self.name

#==============================admin========================
class uhome_admin(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    basicInFo = models.TextField()
    basicSkill = models.TextField()
    hobby = models.TextField()
    edu = models.TextField()
    time = models.DateTimeField()
    def __str__(self):
        return self.name

#========================skill admin================
class skill_admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    skill1 = models.CharField(max_length=50)
    skill2 = models.CharField(max_length=50)
    skill3 = models.CharField(max_length=50)
    skill4 = models.CharField(max_length=50)
    skill5 = models.CharField(max_length=50)
    skill6 = models.CharField(max_length=50)
    skill7 = models.CharField(max_length=50)
    skill8 = models.CharField(max_length=50)
    precent1 = models.CharField(max_length=50)
    precent2 = models.CharField(max_length=50)
    precent3 = models.CharField(max_length=50)
    precent4 = models.CharField(max_length=50)
    precent5 = models.CharField(max_length=50)
    precent6 = models.CharField(max_length=50)
    precent7 = models.CharField(max_length=50)
    precent8 = models.CharField(max_length=50)
    study1 = models.CharField(max_length=50)
    study2 = models.CharField(max_length=50)
    study3 = models.CharField(max_length=50)
    study4 = models.CharField(max_length=50)
    study5 = models.CharField(max_length=50)
    study6 = models.CharField(max_length=50)
    study7 = models.CharField(max_length=50)
    study8 = models.CharField(max_length=50)




