from django.contrib import admin

# Register your models here.

from .models import Form

class FormAdmin(admin.ModelAdmin):

    list_display = ["Id", "name", "surname"]
    list_filter = ["city"]
    search_fields = ["Id", "name", "surname", "TCNumber", "tel", "city", "state"]

    

    class Meta:
        model = Form

admin.site.register(Form, FormAdmin)


