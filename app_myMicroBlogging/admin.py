from django.contrib import admin
from app_myMicroBlogging.models import my_user, micro_post,favorito, lista, hashtag
# Register your models here.

admin.site.register(my_user)
admin.site.register(micro_post)
admin.site.register(favorito)
admin.site.register(lista)
admin.site.register(hashtag)