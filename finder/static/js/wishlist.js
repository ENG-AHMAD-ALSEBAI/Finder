document.addEventListener('DOMContentLoaded', function() {
    // تحديد جميع أزرار المفضلة
    const wishlistButtons = document.querySelectorAll('.wishlist-button');
    
    wishlistButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // التحقق من تسجيل الدخول
            if (!isUserLoggedIn()) {
                // إذا لم يكن المستخدم مسجل الدخول، نوجهه لصفحة تسجيل الدخول
                window.location.href = '/users/signin/';
                return;
            }
            
            const propertyId = this.dataset.propertyId;
            
            // إرسال طلب AJAX لإضافة/إزالة العقار من المفضلة
            fetch(`/wishlist/toggle/${propertyId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'added') {
                    // تغيير شكل الزر عند الإضافة
                    this.classList.add('active');
                    this.querySelector('i').classList.remove('fi-heart');
                    this.querySelector('i').classList.add('fi-heart-filled');
                    this.querySelector('i').style.color = '#dc3545'; // Deep red color
                    showToast('تمت الإضافة إلى المفضلة');
                } else {
                    // تغيير شكل الزر عند الإزالة
                    this.classList.remove('active');
                    this.querySelector('i').classList.remove('fi-heart-filled');
                    this.querySelector('i').classList.add('fi-heart');
                    this.querySelector('i').style.color = ''; // Reset color
                    showToast('تمت الإزالة من المفضلة');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showToast('حدث خطأ، يرجى المحاولة مرة أخرى');
            });
        });
    });
    
    // دالة للتحقق من تسجيل دخول المستخدم
    function isUserLoggedIn() {
        return document.body.classList.contains('user-logged-in');
    }
    
    // دالة للحصول على قيمة CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    // دالة لعرض رسالة toast
    function showToast(message) {
        const toast = document.createElement('div');
        toast.className = 'toast show position-fixed bottom-0 end-0 m-3';
        toast.setAttribute('role', 'alert');
        toast.innerHTML = `
            <div class="toast-body">
                ${message}
            </div>
        `;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 3000);
    }
});
