from django.shortcuts import render

# Create your views here.
def blog(requste):
   return render(requste , 'real-estate-blog.html')

def blog_single(requste):
   return render(requste , 'real-estate-blog-single.html')
