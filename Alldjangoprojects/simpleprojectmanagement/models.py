from django.db import models

# Create your models here.
class Project(models.Model):
     title = models.CharField(max_length=50, verbose_name="Title")
     description = models.CharField(max_length=1000, verbose_name="Description")
     client_name = models.CharField(max_length=1000, verbose_name="owner")
     def __str__(self):
        return self.title
     class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
        ordering = ('id',)
        #db_tables =


class UserProfile(models.Model):
     username = models.CharField(max_length=50, verbose_name="Name")
     password = models.CharField(max_length=100, verbose_name="Password")
     phone = models.CharField(max_length=20, verbose_name="Phone number" , null=True, default=None, blank=True)
     age = models.DateField(verbose_name="age" , null=True,default=None, blank=True)
     last_login = models.DateTimeField(verbose_name="Date of last connection" , null=True, default=None, blank=True)
     email = models.EmailField(verbose_name="Email")
     experience_role = models.IntegerField(verbose_name="Senior",default=0)
     date_created = models.DateField(verbose_name="Date of Birthday",auto_now_add=True)
     def __str__(self):
        return self.username

class Supervisor(UserProfile):
     specialisation = models.CharField(max_length=50, verbose_name="Specialisation")

class Developer(UserProfile):
     supervisedby = models.ForeignKey(Supervisor, verbose_name="Supervisor", related_name="heyme", on_delete=models.CASCADE,)

class Task(models.Model):
     title = models.CharField(max_length=50, verbose_name="Title")
     description = models.CharField(max_length=1000, verbose_name="Description")
     time_elapsed = models.IntegerField(verbose_name="Elapsed time" , null=True, default=None, blank=True)
     importance = models.IntegerField(verbose_name="Importance")
     project = models.ForeignKey(Project, verbose_name="Project" ,null=True, default=None, blank=True, on_delete=models.CASCADE)
     app_user = models.ForeignKey(UserProfile, verbose_name="User" , related_name="hey", on_delete=models.CASCADE)
     #Relationship to add to the Task model
     developers = models.ManyToManyField(Developer ,through="DevelopersOnTask")

     def __str__(self):
        return self.title

class DevelopersOnTask(models.Model):
     developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
     task = models.ForeignKey(Task, on_delete=models.CASCADE)
     time_elapsed_dev = models.IntegerField(verbose_name="Time elapsed", null=True, default=None,blank=True)
