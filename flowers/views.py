from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import RegisterForm
from .models import CartItem, CustomerProfile

def home_view(request):
    if request.user.is_authenticated:
        return redirect('petals')
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def delivery_view(request):
    return render(request, 'delivery.html')

def ai_page_view(request):
    return render(request, 'ai-page.html')

def products_view(request):
    images = [
        '83.jpg', '69.jpg', '68.jpg', '64.jpg', '63.jpg', '62.jpg', '61.jpg',
        '45.jpg', '44.jpg', '22.jpg', '20.jpg', '8.jpg'
    ]
    return render(request, 'products.html', {'images': images})

@login_required
def petals_view(request):
    return render(request, 'petals.html')

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user)
    subtotal = sum(item.price * item.quantity for item in items)
    shipping_cost = 20
    discount = 0
    total = subtotal + shipping_cost - discount
    return render(request, 'cart.html', {
        'cart_items': items,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'discount': discount,
        'total': total
    })

@login_required
def checkout_view(request):
    return render(request, 'checkout.html')

@require_POST
@login_required
def submit_order(request):
    return render(request, 'checkout.html', {
        'success_message': '✅ تم إرسال الطلب بنجاح.'
    })

@login_required
def check_order_status(request):
    has_order = CartItem.objects.filter(user=request.user).exists()
    return JsonResponse({"status": "confirmed" if has_order else "empty"})

# ✅ إنشاء حساب وتحويل إلى تسجيل الدخول دون تسجيل الدخول تلقائيًا
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # ✅ إنشاء CustomerProfile تلقائيًا
            if not hasattr(user, 'customerprofile'):
                CustomerProfile.objects.create(
                    user=user,
                    phone='0000000000',  # مؤقتًا، يمكن تحديثه لاحقًا من الفورم
                    city='غير محدد'
                )

            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'forgot_password.html')

@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        print("📦 الصورة اللي وصلت:", image)

        if not product_name or not price:
            return JsonResponse({'success': False, 'error': 'بيانات غير مكتملة'})

        try:
            if request.user.is_authenticated:
                CartItem.objects.create(
                    user=request.user,
                    product_name=product_name,
                    price=price,
                    image=image
                )
                cart_count = CartItem.objects.filter(user=request.user).count()
                request.session['cart_count'] = cart_count
            else:
                guest_cart = request.session.get('guest_cart', [])
                guest_cart.append({
                    'product_name': product_name,
                    'price': price,
                    'quantity': 1,
                    'image': image
                })
                request.session['guest_cart'] = guest_cart
                cart_count = len(guest_cart)

            return JsonResponse({'success': True, 'count': cart_count})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'الطلب غير صالح'})

@csrf_exempt
@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        try:
            item = CartItem.objects.get(id=item_id, user=request.user)
            item.delete()

            items = CartItem.objects.filter(user=request.user)
            subtotal = sum(i.price * i.quantity for i in items)
            shipping_cost = 20
            discount = 0
            total = subtotal + shipping_cost - discount

            request.session['cart_count'] = items.count()

            return JsonResponse({
                'success': True,
                'summary_total': total,
                'cart_count': items.count()
            })
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'العنصر غير موجود'})
    return JsonResponse({'success': False, 'error': 'طلب غير صالح'})

@csrf_exempt
@login_required
def update_cart_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        try:
            item = CartItem.objects.get(id=item_id, user=request.user)
            item.quantity = int(quantity)
            item.save()

            item_total = item.quantity * item.price
            items = CartItem.objects.filter(user=request.user)
            subtotal = sum(i.price * i.quantity for i in items)
            shipping_cost = 20
            discount = 0
            total = subtotal + shipping_cost - discount

            request.session['cart_count'] = items.count()

            return JsonResponse({
                'success': True,
                'new_total': item_total,
                'summary_total': total,
                'cart_count': items.count()
            })
        except:
            return JsonResponse({'success': False, 'error': 'فشل التحديث'})
    return JsonResponse({'success': False, 'error': 'طلب غير صالح'})

def logout_view(request):
    logout(request)
    return redirect('home')
