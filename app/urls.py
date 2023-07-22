from app import views
# from app import sentiment
from django.urls import path
# from django.contrib.auth import views as auth_views
# app_name = 'app'

urlpatterns = [

    # path('sentiment/', views.sentiment_data, name="sentiment_data"),
    # path('login/', views.loginPage, name="loginPage"),
    # path('login/', auth_views.LoginView.as_view(), name='loginPage'),
    path('login/', views.loginPage, name='loginPage'),
    path('',views.Index,name='index'),
    path('logout/', views.logoutUser, name="logoutPage"),
    path('register/', views.register, name="register"),
    
    path('activate-user/<uidb64>/<token>',views.activate_user, name='activate'),
    
    path('profile/', views.Profile, name='profile'),
    path('products/', views.Products, name='products'),
    path('products/<str:id>', views.Product_detail, name='product'),
    path('category/', views.Category, name='category'),
    path('category/<str:name>', views.Categories_view, name='categories'),
    path('contact/', views.Contact, name='contact'),
    path('about/', views.About, name='about'),
    path('review/<int:p_id>/', views.submit_review, name='review'),
    
    path('cart/', views.Cart_view, name='cart'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('password_reset/', views.password_reset_request, name="password_reset"),
    path('update_item/',views.updateItem,name="update_item"),
    
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/change_address', views.change_addrs, name='change_address'),
    path('shippindaddress/', views.shippingAddress, name='shippindaddress'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('invoice/<int:id>', views.invoice, name='invoice'),
    
]
