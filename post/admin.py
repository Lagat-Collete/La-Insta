from django.contrib import admin
from .models import Profile,Comments, Image
from django_summernote.admin import SummernoteModelAdmin


class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('comment',)
class ImageAdmin(SummernoteModelAdmin):
    summernote_fields = ('comments')
class ProfileAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio')

# Register your models here.
admin.site.register(Image,ImageAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comments,CommentAdmin)
