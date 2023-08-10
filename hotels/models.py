from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import TimestampedModel 
from django.conf import settings
# Create your models here.
class Hotel(TimestampedModel):
    '''Hotel Model Class'''

    DAY = 0
    HOURLY = 1

    ROOM_RATE_CHOICES = (
        (DAY,'By Day'),
        (HOURLY,'By Hour'),
    )

    name = models.CharField(_("Hotel name"), max_length=100, blank=False,null=False)
    fee_cancellation = models.BooleanField(_("Fee Cancellation"),default=True)
    total_rooms = models.IntegerField(_("Total Rooms"),default=0)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Owner"), on_delete=models.CASCADE)
    description = models.CharField(_("Description"), max_length=500,default='Great Hotel')
    room_rate = models.DecimalField(decimal_places=2, max_digits=10)
    room_rate_type = models.SmallIntegerField(_("Room rate type"),help_text=_('Tells how hotels charges by room.'),choices=ROOM_RATE_CHOICES)
    main_image = models.ImageField(_("Hotel Image"),blank=True,null=True, upload_to="hotel_main_images/", height_field=None, width_field=None, max_length=None)


    @property
    def get_room_rate_string(self):
        if self.room_rate_type == 0:
            return f"{self.room_rate} per Day."
        elif self.room_rate_type == 1:
            return f"{self.room_rate} per Hour."
        

    class Meta:
        ordering = ("created_at",)

class HotelImages(TimestampedModel):
    '''Images related to the Hotels'''
    hotel = models.ForeignKey(Hotel, verbose_name=_("Hotel Images"), on_delete=models.CASCADE, related_name='hotelimages')
    image = models.ImageField(_("Hotel Image"), upload_to="hotel_images/", height_field=None, width_field=None, max_length=None)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Uploaded by"), on_delete=models.CASCADE)
    