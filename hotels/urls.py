from django.urls import path
from hotels.views import ( Homepage , HotelListView,HotelDetailView,CreateStripeCheckoutSessionView, SuccessView,CancelView)

urlpatterns = [
    path('',Homepage.as_view(),name='homepage'),
    path('hotels/',HotelListView.as_view(),name='hotel-list'),
    path('hotels/<int:pk>/',HotelDetailView.as_view(),name='hotel-detail'),

    path(
        "create-checkout-session/<int:pk>/",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session",
    ),

    path("success/", SuccessView.as_view(), name="success"),
    path("cancel/", CancelView.as_view(), name="cancel"),
]
