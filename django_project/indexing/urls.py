from django.urls import include, path
from rest_framework import routers

from .views import *


app_name = 'Index'

router = routers.DefaultRouter()
router.register('graderesult', GradeResultViewSet, basename='graderesult')

urlpatterns = [
    path('', index, name='index'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/create-group', CreateGroup.as_view(), name='group'),
    path('accounts/profile/<int:pk>/update', GroupUpdateView.as_view(), name='group-update'),
    path('accounts/profile/student-groups', GroupListView.as_view(), name='student-groups'),
    path('accounts/profile/create-student', CreateStudent.as_view(), name='student'),

    path('accounts/profile/lca/create', LCACreateView.as_view(), name='lca-create'),
    path('accounts/profile/lca/<int:pk>', LCADetailView.as_view(), name='lca-detail'),
    path('accounts/profile/lca/<int:pk>/print', LCAPrintView.as_view(), name='lca-print'),
    path('accounts/profile/lca/<int:pk>/performance', PerformancePrintView.as_view(), name='performance'),
    path('accounts/profile/lca/<int:pk>/delete/', LCADeleteView.as_view(), name='lca-delete'),

    path('accounts/profile/lca/<int:pk>/gss/create', GradeServiceSetCreateView.as_view(), name='gss-create'),
    path('accounts/profile/gradeservice/create', GradeServiceCreateView.as_view(), name='gradeservice-create'),
    path('accounts/profile/formholding/create', FormHoldingCreateView.as_view(), name='formholding-create'),
    path('accounts/profile/orderholding/create', OrderHoldingCreateView.as_view(), name='orderholding-create'),
    # Таблицы
    path('accounts/profile/table', table, name='table'),
    path('accounts/profile/table-list', table_list, name='table-list'),
    path('accounts/profile/table/<int:pk>', table_delate, name='table-delete'),
    path('accounts/profile/table/<int:pk>/update', Update_Table_View.as_view(), name='table-update'),

    path('gradeitems/<int:pk>/update', GradeItemUpdateAPIView.as_view()),
    path('lca/<int:lca_id>/', include(router.urls)),
    path('lca/<int:lca_id>/result', ResultAPIView.as_view()),
]
