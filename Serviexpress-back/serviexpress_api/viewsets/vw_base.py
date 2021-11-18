from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        enterprise = None
        need_enterprise = False
        get_all = self.request.query_params.get('all', False)
        model = self.serializer_class.Meta.model
        fields = [field.name for field in model._meta.fields]
        queryset = model.objects.all()

        if 'enterprise' in fields:
            need_enterprise = True

        if need_enterprise:
            if self.request.method == 'GET':
                enterprise = self.request.query_params.get('enterprise', None)
            else:            
                enterprise = self.request.data.get('enterprise', None)
            if enterprise is None:
                raise ValidationError(detail='Enterprise is Required')
            queryset = queryset.filter(enterprise__pk=enterprise)

        if 'is_active' in fields and not get_all:
            queryset = queryset.filter(is_active=True)

        if 'created_at' in fields:
            queryset = queryset.order_by('-created_at')
            
        return queryset

    def destroy(self,request,pk):
        try:
            serializer = self.serializer_class
            model = self.serializer_class.Meta.model
            instance = model.objects.get(pk=pk)
            if hasattr(instance, 'is_active'):
                instance.is_active = False
                instance.save()
            else:
                instance.delete()
            return Response('ok')
        except Exception as error:
            return Response(dict(error='Ocurrió un Error'), status=400)