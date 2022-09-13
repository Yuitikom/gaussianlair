from django.urls import path
from . import views
from .views import AddCategory, UpdateCategory, DeleteCategory

urlpatterns = [
    path('/createcategory', AddCategory.as_view(), name='createcategory'),
    path('',views.categorypage, name='categories'),
    path('/<str:category_name>', views.categoryviewpage,name='category'),
    path('<category>/edit/<int:pk>', UpdateCategory.as_view(), name='editcategory'),
    path('<category>/<int:pk>/deletecategory', DeleteCategory.as_view(), name='deletecategory'),
]

