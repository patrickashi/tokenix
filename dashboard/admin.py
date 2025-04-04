from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Student
from .models import Profile
from .models import Feedback
from .models import Notification
from .models import BTC, DASH, Ethereum
from .models import Invest
from .models import Withdrawal
from .models import Contact

# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Feedback)
admin.site.register(Notification)

admin.site.register(BTC)
admin.site.register(DASH)
admin.site.register(Ethereum)
admin.site.register(Invest)
admin.site.register(Withdrawal)
admin.site.register(Contact)

#unregister groups
admin.site.unregister(Group)