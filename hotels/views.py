from typing import Any, Dict
from django.shortcuts import render , redirect
from django.views import View , generic
from django.contrib import messages
from hotels.models import Hotel
from hotels.forms import HotelBookingForm
import stripe
from django.conf import settings
from django.contrib.auth.models import update_last_login

stripe.api_key = settings.STRIPE_SECRET_KEY
class Homepage(View):
    '''Hompage View'''
    def get(self,request,format=None):
        return render(request,'homepage.html',{'homepage':True})


class HotelListView(generic.ListView):
    model = Hotel
    context_object_name = "hotels"
    template_name = "hotels_list.html"
    paginate_by = 10

class HotelDetailView(generic.DetailView):
    model = Hotel
    template_name = "hotels/hotel_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['hotel_booking_form'] = HotelBookingForm()
        return context
 
class SuccessView(generic.TemplateView):
    template_name = "hotels/success.html"

class CancelView(generic.TemplateView):
    template_name = "hotels/cancel.html"


class CreateStripeCheckoutSessionView(View):
    """
    Create a checkout session and redirect the user to Stripe's checkout page
    """

    def post(self, request, *args, **kwargs):
        hotel = Hotel.objects.get(id=self.kwargs["pk"])

        form = HotelBookingForm(request.POST)
        
        if not form.is_valid():
            messages.warning(request,'Error occured')
            return redirect('hotel-list')
        rooms = form.cleaned_data['rooms']
        ac = form.cleaned_data['ac']

        amount = rooms * hotel.room_rate
        if ac:
            amount += 10
        checkout_session = stripe.checkout.Session.create(
            customer_email=request.user.email,
            payment_method_types=["card"],
            line_items=[
                {   
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": int(amount) * 100,
                        "product_data": {
                            "name": hotel.name,
                            "description": hotel.description,
                            "images": [
                                f"{settings.BACKEND_DOMAIN}/{hotel.main_image.url}"
                            ],
                        },
                    },
                    "quantity": rooms,
                }
            ],
            metadata={"hotel_id": hotel.id},
            mode="payment",
            success_url=settings.PAYMENT_SUCCESS_URL,
            cancel_url=settings.PAYMENT_CANCEL_URL,
        )
        return redirect(checkout_session.url)