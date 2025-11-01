# Update views.py with correct template paths

from django.shortcuts import render
import random
from django.utils import timezone

BLOGS = [
    "My journey into software development: lessons learned in my first year. - Ayiko Chrispus",
    "Why I love Python: readability, community, and rapid prototyping. - Ayiko Chrispus",
    "Deploying small Django apps: simple tips for students and beginners. - Ayiko Chrispus",
]

IMAGES = [
    # Use static file paths (served from STATICFILES) or full URLs
    "https://picsum.photos/id/1011/800/500",
    "https://picsum.photos/id/1025/800/500",
    "https://picsum.photos/id/1035/800/500",
]

def blog(request):
    selected_blog = random.choice(BLOGS)
    selected_image = random.choice(IMAGES)
    context = {'blog_text': selected_blog, 'image_url': selected_image, 'now': timezone.now()}
    return render(request, 'blog/blog.html', context)

def show_all(request):
    context = {'blogs': BLOGS, 'images': IMAGES, 'now': timezone.now()}
    return render(request, 'blog/show_all.html', context)

def about(request):
    context = {'about_text': "Ayiko Chrispus — Bootcamp student. Replace this with your short bio.", 'now': timezone.now()}
    return render(request, 'blog/about.html', context)