
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import HomePageView
from course.views import CourseListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", CourseListView.as_view(), name="course_list"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("courses/", include('course.urls')),
    #path('__debug__', include('debug_toolbar.urls')),
    path('api/', include('course.api.urls')),
    path('chat/', include('chat.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
