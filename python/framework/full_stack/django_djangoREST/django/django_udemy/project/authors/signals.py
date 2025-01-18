from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from authors.models import Profile

User = get_user_model

#Quando for salvo, será emitido o sinal, que é a função: create_profile
# Conectando user ao post_save
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwags):

    #Verifica se o profile está sendo criado
    if created:
        
        profile = Profile.objects.create(author=instance)
        profile.save()