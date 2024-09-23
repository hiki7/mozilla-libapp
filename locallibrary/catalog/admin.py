from django.contrib import admin
from .models import Book, BookInstance, Genre, Author, Language


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    #list_display is used for displaying the info in general page
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields is used for displaying the attributes in the form, in which order. Usually, they are displayed vertically, but if we use tuple, we can display horizontally
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre') #we've defined the function instead of directly defining the genre field, since it is many_to_many field

    inlines = [BookInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    #diving into the sections, first value in the tuple is the Title of the sections
    fieldsets = (
        (None, {'fields': ('book', 'imprint', 'id')}),
        ('Availability', {'fields': ('status', 'due_back', 'borrower')}),
    )

# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Language)