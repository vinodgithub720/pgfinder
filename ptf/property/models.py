# from django.db import models

# class Property_type(models.Model):
#     name=models.CharField(max_length=50)

#     class meta:
#         db_table='Property_type'




from django.db import models
from user.models import User

class City(models.Model):
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.city

    class Meta:
        db_table='city_name'

class Property_type(models.Model):
    type=models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        db_table='type_name'

class Property_info(models.Model):
    name=models.CharField(max_length=50)
    PG_type=models.ForeignKey(Property_type, on_delete=models.CASCADE, null=True)
    owners_name=models.CharField(max_length=50)
    # rera=models.BooleanField(default=True)
    garden=models.BooleanField(default=True)
    construction_year=models.DateField()
    city=models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    rent=models.IntegerField(default=False)
    photos=models.ImageField(upload_to='media', default=True)
    BHK=models.IntegerField(default=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table='property_info'






class Properties(models.Model):
    Property_info=models.ForeignKey(Property_info,on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=50)
    for_rent=models.BooleanField(default=False)
    for_sell=models.BooleanField(default=False)
    price=models.IntegerField()
    status=models.BooleanField(default=False)

    class Meta:
         db_table='Properties'


# Create your models here.
# class Project(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     technology = models.CharField(max_length=100)
#     estimated_time = models.IntegerField()
#     start_date = models.DateField()
#     completion_date = models.DateField()
    
#     class Meta:
#         db_table = 'project'
    
#     def __str__(self):
#         return self.title                    
      
class ProjectTeam(models.Model):
    Project = models.ForeignKey(Property_info, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        db_table = 'project_team'
           
