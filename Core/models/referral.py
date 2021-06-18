from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Referral(models.Model):
    # The user who referred another user
    recruiter = models.ForeignKey(to=User, related_name="recruiter_user", null=True, on_delete=models.SET_NULL)
    # The user who is being referred
    referred = models.OneToOneField(to=User, related_name="referred_user", null=True, on_delete=models.SET_NULL)
    # Commission Amount
    commission = models.PositiveIntegerField(blank=True, default=0)
    # Time of Creation
    time_stamp = models.DateTimeField(auto_now_add=True)
    # Time of update
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["recruiter", "referred"]

