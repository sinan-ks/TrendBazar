from django.urls import path
from store import views


urlpatterns = [

    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("home/",views.HomeView.as_view(),name="home"),
    path("signout/", views.SignOutView.as_view(), name="signout"),
    path("products/<int:pk>",views.ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:pk>/carts/add/",views.AddToCartView.as_view(),name="add-to-cart"),
    path("carts/all/",views.CartItemListView.as_view(), name="cart-list"),
    path("basket/items/<int:pk>/remove/",views.BasketItemDeleteView.as_view(), name="basket-item-delete"),
    path("basket/item/<int:pk>/quantity/change/",views.BasketItemUpdateQuantityView.as_view(), name="basket-item-qty-update"),
    path("checkout/", views.CheckOutView.as_view(), name="checkout"),
    path("orders/all/", views.MyOrdersView.as_view(), name="orders"),
    path("verify/", views.PaymentVerificationView.as_view(), name="verification"),
    
]