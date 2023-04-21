from allauth.socialaccount.models import SocialAccount
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()


def save_social_user_name(sender, instance, created, **kwargs):
    if created:
        user = User.objects.get(id=instance.user.id)
        if instance.provider == "microsoft":
            user.name = instance.extra_data.get("displayName")
        elif instance.provider == "google":
            user.name = instance.extra_data.get("name")
        user.save()


post_save.connect(save_social_user_name, sender=SocialAccount)
