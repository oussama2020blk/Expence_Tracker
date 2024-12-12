from django.contrib import admin
from .models import CurrentBalance, TrackingHistory
# Register your models here.

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"
admin.site.register(CurrentBalance)

@admin.action(description="Mark selected stories as Credit")
def make_credit(modeladmin, request, queryset):
    queryset.update(expense_type="p")


class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'amount',
        'current_balance',
        'expense_type',
        'description',
        'created_at',
        'display_age'
    ]

    actions = [make_credit]

    def display_age(self, obj):
        if obj.amount > 0:
            return "Positive"
        return "Negative"

    search_fields = ['expense_type', 'description']
    list_filter = ['expense_type']
    ordering = ['-created_at']
admin.site.register(TrackingHistory, TrackingHistoryAdmin)
