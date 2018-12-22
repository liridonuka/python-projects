from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from .signals import object_viewed_signal
User = settings.AUTH_USER_MODEL

# Create your models here.

class History(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stamp_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} by {} on {}".format(self.content_object, self.user, self.stamp_on.strftime("%Y-%m-%d %H:%M:%S"))

    class Meta:
        verbose_name_plural = "Histories"

def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    new_history = History.objects.create(
        user = request.user,
        content_type = ContentType.objects.get_for_model(sender),
        object_id = instance.id,
    )
object_viewed_signal.connect(object_viewed_receiver)
