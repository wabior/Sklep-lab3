from django.contrib import admin

# Register your models here.
from .models import Produkty
from .models import Producent
from .models import Kategoria
from .models import Comment
from .models import Tagi
admin.site.register(Produkty)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Comment)
admin.site.register(Tagi)

