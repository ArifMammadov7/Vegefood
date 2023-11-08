from django.contrib import admin
from core.models import *


# admin.site.register(News)
admin.site.register(Setting)
admin.site.register(Category)

admin.site.register(Testimonial)
admin.site.register(About)

admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(CarouselItem)
admin.site.register(Subscriber)



@admin.register(Product)  
class NewsAdmin(admin.ModelAdmin):
    list_display=['title','like','dislike','view','created_at','updated_at']
    search_fields=['title','content']
    list_filter=['created_at','updated_at']

    ordering=['-created_at']
    readonly_fields=('like','dislike','view','created_at','updated_at')

#     fieldsets=(
#     (None,{
#         'fields':('title','content','image','Category','is_active')
#     }),
#     ('Advanced options',{
#         'classes': ('collapse',),
#         'fields':('like','dislike','view','created_at','updated_at',)     
#     }),
# )

admin.site.site_header="Vegafood Admin"
admin.site.site_title="Vegafood Admin Portal"