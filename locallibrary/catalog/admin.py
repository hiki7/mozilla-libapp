from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') #we've defined the function instead of directly defining the genre field, since it is many_to_many field


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')

# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language)