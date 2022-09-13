from django.db import models
import uuid


class ModelWithPk(models.Model):
    """model with traditional id(pk) as a primary key"""

    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"Id:{self.id} name:{self.name}"


class ModelWithIdUuid(models.Model):
    """model with uuid as a primary key"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"Id:{self.id} name:{self.name}"
