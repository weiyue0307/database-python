from django.contrib import admin
from .models import user,dessert,dessert_shop,comment,administrator

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')
    search_fields = ('username','account')

class dessertAdmin(admin.ModelAdmin):
    list_display = ('name','itshop')
    search_fields = ('name','itshop')
    #filter_horizontal = ('shops',)

class commentAdmin(admin.ModelAdmin):
    list_display = ('commentid', 'dessert_name', 'content')
    list_filter = ('comment_date',)
    date_hierarchy = 'comment_date'
    ordering = ('-comment_date',)
    fields = ('commentid', 'dessert_name', 'dessert_shop_name', 'content', 'user_name')

class administratorAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')


admin.site.register(user, UserAdmin)
admin.site.register(dessert, dessertAdmin)
admin.site.register(dessert_shop)
admin.site.register(comment, commentAdmin)
admin.site.register(administrator, administratorAdmin)

