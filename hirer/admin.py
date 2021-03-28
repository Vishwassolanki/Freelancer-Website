from django.contrib import admin
from .models import hirer_profile, post_job, job_status, payment_hirer, reviews_hirer


# Register your models here.
admin.site.register(hirer_profile)
admin.site.register(post_job)
admin.site.register(job_status)
admin.site.register(payment_hirer)
admin.site.register(reviews_hirer)