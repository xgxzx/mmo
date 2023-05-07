from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit_profile'),
    # Category
    path('categories/', views.category_list_view, name='mmorpg/category/vcategory_list'),
    # path('category/create/', create_category, name='mmorpg/category/create_category'),
    # Post
    path('', post_list, name='post_list'),
    # path('post/create', PostCreate.as_view(), name='mmorpg/post_create'),
    # path('post/<int:pk>/', PostDetail.as_view(), name='mmorpg/post_detail'),
    # path('post/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    # path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
