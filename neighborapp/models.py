from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Neighbourhood(models.Model):
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    # occupants_count=models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls, name):
        return cls.objects.filter(name__icontains=name)

    @classmethod
    def update_neighbourhood(cls, id, name):
        update=cls.objects.filter(id=id).update(name=name)
        return update

class Profile(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    neighbourhood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()


class Business(models.Model):
  name=models.CharField(max_length=50)
  user=models.ForeignKey(Profile,on_delete=models.CASCADE)
  email=models.EmailField()
  neighbourhood=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def save_business(self):
    self.save()

  def delete_business(self):
    self.delete()

  @classmethod
  def find_business(cls, name):
    return cls.objects.filter(name__icontains=name) 

  @classmethod  
  def update_business(cls, id, name):
      update=cls.objects.filter(id=id).update(name=name)
      return update



