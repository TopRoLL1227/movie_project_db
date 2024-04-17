from django.contrib import admin, messages
from .models import Movie, Director, Actors, Dressing_Room
from django.db.models import QuerySet


class RatingFilter(admin.SimpleListFilter):
    title = 'Rating films'
    parameter_name = 'Rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low rating'),
            ('40-59', 'Avarage rating'),
            ('60-79', 'Hight rating'),
            ('>=80', 'Very hight rating'),
        ]

    def queryset(self, request, queryset):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        if self.value() == '40-50':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        return queryset


# Register your models here.
admin.site.register(Director)
admin.site.register(Actors)
admin.site.register(Dressing_Room)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    exclude = ['slug', 'budget']
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status', 'director']
    list_editable = ['rating', 'year', 'budget', 'director']
    filter_horizontal = ['actors']
    ordering = ['-rating']
    list_per_page = 10
    actions = ['set_dollars', 'set_uah', 'set_eur']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', RatingFilter, 'currency']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Why i should see it'
        if mov.rating < 70:
            return 'It can be see'
        if mov.rating <= 85:
            return 'Good choise'
        return 'Top'

    @admin.action(description='Встановити валюту в USD')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Встановити валюту у UAH')
    def set_uah(self, request, qs):
        count_refresh = qs.update(currency=Movie.UAH)
        self.message_user(
            request,
            f'It has {count_refresh} refreshed')

    @admin.action(description='Встановити валюту у EUR')
    def set_eur(self, request, qs):
        qs.update(currency=Movie.EUR)
