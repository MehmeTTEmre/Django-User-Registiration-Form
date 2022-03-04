from django.contrib import admin
from .models import Form
from django_admin_listfilter_dropdown.filters import DropdownFilter

# Register your models here.

class FormAdmin(admin.ModelAdmin):

    list_display = ["Id", "name", "surname"]
    list_filter = ( ('Id', DropdownFilter),
                    ('name', DropdownFilter),
                    ('surname', DropdownFilter),
                    ('TCNumber', DropdownFilter),
                    ('tel', DropdownFilter),
                    ('city', DropdownFilter),
                    ('state', DropdownFilter))
    search_fields = ["Id", "name", "surname", "TCNumber", "tel", "city", "state"]

    list_per_page = 25
    list_max_show_all = 25

    class Meta:
        model = Form

admin.site.register(Form, FormAdmin)


