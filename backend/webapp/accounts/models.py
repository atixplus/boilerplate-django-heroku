from django.db import models

  
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to=profile_image_path, default='defaults/img/default-user.png')
    # phone = models.CharField(_('telephone'), max_length=12, blank=True, null=True)

    state = models.CharField(max_length=50, blank=True, null=True)
    state_update_at = models.DateField()
    
    def __str__(self):
        """Return username's name."""
        return f'{self.user.username} profile'