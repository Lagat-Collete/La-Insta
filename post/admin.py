from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('comment',)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('comments')
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio')

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comments,CommentAdmin)

