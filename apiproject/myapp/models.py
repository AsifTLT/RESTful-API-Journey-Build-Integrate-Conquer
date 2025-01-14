from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    
    def create(self, validated_data):
        return Contact.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.title = validated_data.get('title', instance.title)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
