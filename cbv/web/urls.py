from django.urls import path

from cbv.web.views import IndexView, Index2View

urlpatterns = (
    path('', IndexView.get_view()),
    path('2/', Index2View.get_view()),
)