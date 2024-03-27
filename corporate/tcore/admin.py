from django.contrib import admin
from django.http import HttpRequest
from .models import Contact,About, Service, Slider,Category,Blog,Settings
from modeltranslation.admin import TranslationAdmin
from .admin_mixins import CommonMedia

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    
    full_name.short_description = 'Full Name'  # Opsiyonel: Yönetici arayüzünde görüntülenecek alanın adını tanımlar.

    list_display = ('full_name','phone','email',)

    
@admin.register(About)
class AboutAdmin(TranslationAdmin,CommonMedia):
    list_display=('title',)

    def has_add_permission(self,request, obj=None):
        return False
    
    def has_delete_permission(self,request,obj=None):
        return False
    
@admin.register(Service)
class ServiceAdmin(TranslationAdmin,CommonMedia):
    list_display=('title',)

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display=('title','image',)

@admin.register(Category)
class CategoryAdmin(TranslationAdmin,CommonMedia):
    list_display=('name',)

@admin.register(Blog)
class BlogAdmin(TranslationAdmin,CommonMedia):
    list_display=('title','content','views')

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'description', 'phone_fixed', 'phone_mobile', 'fax', 'email')