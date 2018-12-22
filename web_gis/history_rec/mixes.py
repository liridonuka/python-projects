from .signals import object_viewed_signal

class ObjectViewedMix:
    def dispatch(self,request, *args, **kwargs):
        try:
            instance = self.get_object()
        except self.model.DoesNotExist:
            instance = None

        if request.user.is_authenticated and instance is not None:
            object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return super(ObjectViewedMix,self).dispatch(request,*args,**kwargs)
