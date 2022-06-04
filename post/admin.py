from django.contrib import admin
from .models import Profile,Comments, Image
from django_summernote.admin import SummernoteModelAdmin


class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('comment',)

# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comments,CommentAdmin)
