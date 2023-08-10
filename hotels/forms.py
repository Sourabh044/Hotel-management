from django import forms



class HotelBookingForm(forms.Form):
    rooms = forms.IntegerField(max_value=10,min_value=1,initial=1, required=True)
    ac = forms.BooleanField( required=True, initial=True)