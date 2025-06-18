from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ✅ لوحة التحكم
    path('admin/', admin.site.urls),

    # ✅ التوثيق
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),


    # ✅ الصفحة الرئيسية
    path('', views.home_view, name='home'),

    # ✅ الصفحات الثابتة
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('delivery/', views.delivery_view, name='delivery'),
    path('ai-page/', views.ai_page_view, name='ai_page'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('petals/', views.petals_view, name='petals'),
    path('products/', views.products_view, name='products'),

    # ✅ استعادة كلمة المرور
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),

    # ✅ عمليات السلة
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('update-cart-quantity/', views.update_cart_quantity, name='update_cart_quantity'),
    path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),

    # ✅ إرسال نموذج الدفع (Checkout)
    path('submit-order/', views.submit_order, name='submit_order'),

    # ✅ التحقق من وجود طلب (مرتبط بصفحة التوصيل)
    path('check-order/', views.check_order_status, name='check_order_status'),
]
