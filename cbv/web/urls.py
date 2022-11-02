from django.urls import path
from django.views import generic as views
from cbv.web.views import IndexView, Index2View, IndexViewWithTemplate, IndexViewWithListView

urlpatterns = (
    path('', IndexView.as_view()),
    path('2/', Index2View.as_view()),
    path('3/', IndexViewWithTemplate.as_view()),
    path('4/', IndexViewWithListView.as_view()),
    path('redirect-to-index/', views.RedirectView.as_view(url='/')),
)