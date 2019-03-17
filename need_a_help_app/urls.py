from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('main', views.AppMainView.as_view(), name='main'),
    path('top_rated', views.TopRatedView.as_view(), name='top_rated'),
    path('info/<int:pk>/', views.InfoDetailView.as_view(), name='info'),
    path('modal_info/<int:pk>/', views.ModalInfoDetailView.as_view(), name='modal_info'),
    path('add_favorite/<int:user_id>/<int:rep_id>/', views.add_favorite, name='add_favorite'),
    path('del_favorite/<int:user_id>/<int:rep_id>/', views.del_favorite, name='del_favorite'),
    path('favorites/', views.show_favs, name='favorites'),
    path('requests_user/<int:pk>', views.RequestsView.as_view(), name='requests_user'),
    path('add_request/', views.RequestCreateView.as_view(), name='add_request'),
    path('request/<int:pk>/', views.RequestDetailView.as_view(), name='request_detail'),
    path('request/<int:pk>/update/', views.RequestUpdateView.as_view(), name='request_update'),
    path('request/<int:pk>/delete/', views.RequestDeleteView.as_view(), name='request_delete'),
    path('search', views.search, name='search'),
    path('hire_repairman/<int:user_id>/<int:rep_id>/', views.hire_repairman, name='hire_repairman'),
    path('hired_user/<int:pk>', views.HiredListView.as_view(), name='hired_user'),
    path('requests_repairman/<int:pk>', views.RepairmanRequestsListView.as_view(), name='requests_repairman'),
    path('job_accept_repairman/<int:user_id>/<int:rep_id>/', views.job_accept, name='job_accept'),
    path('active_repairman/<int:pk>', views.RepairmanActiveListView.as_view(), name='active_repairman'),
    path('job_done_repairman/<int:user_id>/<int:rep_id>/', views.job_done, name='job_done'),
    path('done_repairman/<int:pk>', views.RepairmanDoneListView.as_view(), name='done_repairman'),
    path('repairman_apply/<int:us_id>/<int:req_id>/', views.repairman_apply, name='repairman_apply'),
    path('posted_job_hire/<int:us_id>/<int:req_id>/', views.posted_job_hire, name='posted_job_hire'),
    path('posted_job_done/<int:us_id>/<int:req_id>/', views.posted_job_done, name='posted_job_done'),
    path('repairman_apps/<int:pk>', views.RepairmanApplicationsListView.as_view(), name='repairman_apps'),
    path('job_hire/<int:pk>/delete/', views.JobHireDeleteView.as_view(), name='job_hire_delete'),
    path('cancel_application/<int:user_id>/<int:req_id>/', views.cancel_application, name='cancel_application'),
    path('client_repairman_job_delete/<int:user_id>/<int:rep_id>/<int:log_id>/<str:txt>/', views.client_repairman_job_delete, name='client_repairman_job_delete'),
    path('notifications_client/<int:pk>', views.NotificationsClientListView.as_view(), name='notifications_client'),
    path('notifications_repairman/<int:pk>', views.NotificationsRepairmanListView.as_view(), name='notifications_repairman'),
    path('rate/', views.rate, name='rate'),
    path('done_user/<int:pk>', views.UserDoneListView.as_view(), name='done_user'),
    path('repairman_feedbacks/<int:pk>', views.RepairmanFeedbacksListView.as_view(), name='repairman_feedbacks'),
    path('chat/', include('chat.urls')),
]
