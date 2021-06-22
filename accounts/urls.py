from accounts import views
from django.urls import path
from rest_framework import routers
router = routers.SimpleRouter()
#Phone
# router.register(r'phones', views.PhoneViewset)
router.register(r'complete_user_profile', views.UserViewSet)
# router.register(r'seller', views.sellerViewSet)

# router.register(r'agent', views.AgentViewSet)

# router.register(r'actioneer', views.AuctioneerViewSet)

# urlpatterns = [
#     path('send_sms_code/',views.send_sms_code),
#     path('verify_phone/<int:sms_code>',views.verify_phone),
#    ]
urlpatterns = router.urls