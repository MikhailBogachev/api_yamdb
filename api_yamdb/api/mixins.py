from rest_framework import viewsets, mixins


class GetPostDeleteViewSet(viewsets.GenericViewSet,
                           mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           mixins.DestroyModelMixin):
    pass
