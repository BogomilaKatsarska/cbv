from django.urls import path
from django.views import generic as views
from cbv.web.views import IndexView, Index2View, IndexViewWithTemplate, IndexViewWithListView, EmployeeDetailsView, \
    EmployeeCreateView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('2/', Index2View.as_view()),
    path('3/', IndexViewWithTemplate.as_view()),
    path('4/', IndexViewWithListView.as_view()),
    path('create/', EmployeeCreateView.as_view(), name='employee create'),
    path('redirect-to-index', views.RedirectView.as_view(url='/'), name='redirect to index'),
    path('details/<int:pk>/', EmployeeDetailsView.as_view(), name='employee details'),
)