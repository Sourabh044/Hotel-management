from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import TimestampedModel , User
from django.conf import settings
# Create your models here.
class Hotel(TimestampedModel):
    '''Hotel Model Class'''
    name = models.CharField(_("Hotel name"), max_length=100, blank=False,null=False)
    fee_cancellation = models.BooleanField(_("Fee Cancellation"),default=True)
    total_rooms = models.IntegerField(_("Total Rooms"),default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Owner"), on_delete=models.CASCADE)



class HotelImages(TimestampedModel):
    image = models.ImageField(_("Hotel Image"), upload_to="hotel_images/", height_field=None, width_field=None, max_length=None)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Uploaded by"), on_delete=models.CASCADE)
    