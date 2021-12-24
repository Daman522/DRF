from user.models import *
from .models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=CustomUser)
def post_save_generator_code(sender,instance,created,*args, **kwargs):
    print(created,args,kwargs)
    if created:
        Code.objects.create(user=instance)
    else:
        c = Code.objects.get(user=instance)
        c.save()