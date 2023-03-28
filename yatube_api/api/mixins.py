from rest_framework import mixins, viewsets


class CreateGetlistViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    pass
