from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_reciver(sender, instance, created, **kwargs):
    if created: # มีการสร้าง User ใหม่
        UserProfile.objects.create(user=instance)
    else:  # ไม่ได้  create User เพียงแต่ update  User
        try:
            #  อัพเดท UserProfile หากมีอยู่แล้ว
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # สร้าง UserProfile หากไม่เคยมี
            UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
        pass

# post_save.connect(post_save_create_profile_reciver)