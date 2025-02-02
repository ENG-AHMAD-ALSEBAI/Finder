from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from properties.models import Property
from .models import WishlistItem
from users.models import User, UserInfo

# Create you views here.
@login_required(login_url='users:signin')
def account_wishlist(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id_user=user_id)
        user_info, created = UserInfo.objects.get_or_create(user=user)
        wishlist_items = WishlistItem.objects.filter(user_id=user_id).select_related('property')
        
        context = {
            'user': user,
            'user_info': user_info,
            'wishlist_items': wishlist_items
        }
        return render(request, 'real-estate-account-wishlist.html', context)
    return redirect('users:signin')

@login_required
def toggle_wishlist(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        try:
            property = Property.objects.get(id_property=property_id)
            user_id = request.session.get('user_id')
            user = User.objects.get(id_user=user_id)
            wishlist_item = WishlistItem.objects.filter(user=user, property=property).first()
            
            if wishlist_item:
                # إذا كان العقار موجود في المفضلة، نقوم بإزالته
                wishlist_item.delete()
                return JsonResponse({'status': 'removed'})
            else:
                # إذا لم يكن موجود، نقوم بإضافته
                WishlistItem.objects.create(user=user, property=property)
                return JsonResponse({'status': 'added'})
        except (Property.DoesNotExist, User.DoesNotExist):
            return JsonResponse({'status': 'error', 'message': 'Property or user not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@login_required
def toggle_wishlist_new(request):
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        try:
            property_obj = Property.objects.get(id_property=property_id)
            wishlist_item = WishlistItem.objects.filter(user=request.user, property=property_obj)
            
            if wishlist_item.exists():
                # Remove from wishlist
                wishlist_item.delete()
                return JsonResponse({
                    'status': 'success',
                    'action': 'removed',
                    'message': 'Property removed from wishlist'
                })
            else:
                # Add to wishlist
                WishlistItem.objects.create(user=request.user, property=property_obj)
                return JsonResponse({
                    'status': 'success',
                    'action': 'added',
                    'message': 'Property added to wishlist'
                })
                
        except Property.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Property not found'
            }, status=404)
            
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)

@login_required
def wishlist(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('users:signin')
    
    user = User.objects.get(id_user=user_id)
    wishlist_items = WishlistItem.objects.filter(user_id=user_id).select_related('property')
    return render(request, 'real-estate-account-wishlist.html', {
        'wishlist_items': wishlist_items,
        'user': user
    })

@login_required
def clear_wishlist(request):
    if request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            # حذف جميع العقارات من المفضلة للمستخدم الحالي
            WishlistItem.objects.filter(user_id=user_id).delete()
            return JsonResponse({'status': 'success', 'message': 'Wishlist cleared successfully'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
