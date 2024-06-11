from django.contrib import admin
from .models import EduEligibility, CasteEligibility, Scheme, SchemeCasteMapping

class EduEligibilityAdmin(admin.ModelAdmin):
    list_display = ('choice',)
    search_fields = ('choice',)

class CasteEligibilityAdmin(admin.ModelAdmin):
    list_display = ('choice',)
    search_fields = ('choice',)

class SchemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'gender', 'start_date', 'end_date', 'link', 'procedure_to_apply', 'edu_eligibility')
    search_fields = ('name', 'description', 'gender')
    list_filter = ('gender', 'start_date', 'end_date', 'edu_eligibility')

class SchemeCasteMappingAdmin(admin.ModelAdmin):
    list_display = ('scheme', 'caste', 'min_age', 'max_age')
    search_fields = ('scheme__name', 'caste__choice')
    list_filter = ('scheme', 'caste')       
    raw_id_fields = ('scheme', 'caste')

admin.site.register(EduEligibility, EduEligibilityAdmin)
admin.site.register(CasteEligibility, CasteEligibilityAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(SchemeCasteMapping, SchemeCasteMappingAdmin)
