from django.core.exceptions import ValidationError


class InstancesLimitModelMixin():
    instances_limit = 1

    def clean(self) -> None:
        if not self.__class__.objects.filter(pk=self.pk).exists() and \
                self.__class__.objects.count() == self.instances_limit:
            raise ValidationError(f'you can\'t create more than {self.instances_limit} model instances')
        return super().clean()