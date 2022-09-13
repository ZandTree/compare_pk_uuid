from django.core.management.base import BaseCommand
from compare.models import ModelWithPk, ModelWithIdUuid
from ._utils import calc_exec_time

# import random
# from faker import Faker
# fake = Faker()


@calc_exec_time
def create_pk_model():
    """create 2000 objects ModelWithPk in db.sqlite3"""
    return [ModelWithPk.objects.create(name=f"Name - {i}") for i in range(2000)]


@calc_exec_time
def find_last_pk_model():
    """find the last object in the rows for model ModelWithPk"""
    return ModelWithPk.objects.last()


@calc_exec_time
def create_uuid_model():
    """create 2000 objects ModelWithIdUuid in db.sqlite3"""
    return [ModelWithIdUuid.objects.create(name=f"Name - {i}") for i in range(2000)]


@calc_exec_time
def find_last_uuid_model():
    """find the last object in the rows for model ModelWithIdUuid"""
    return ModelWithIdUuid.objects.last()


class Command(BaseCommand):
    help = "Create a bulk of Post model objects and connected models (via FK and M2M)"

    def handle(self, *args, **options):
        output_decor_func = create_pk_model()
        # output_decor_func = create_uuid_model()
        # output_decor_func = find_last_pk_model()
        # output_decor_func = find_last_uuid_model()
        self.stdout.write(self.style.SUCCESS(f"result: {output_decor_func}"))


"""
================== pk ====================================

=========== create
Creating 2000 objects in db.sqlit3
took 226.85 sec; 2000 queries made
========== find the last in the rows
took: 0.008964399807155132 sec; queries qty: 1

================== uuid ==================================

============ create
Creating 2000 objects in db.sqlit3
took 191.32 sec; 2000 queries made
============ find the last elem in the rows
result: Took: 0.0038521001115441322 sec; queries qty: 1
==========================================================
Conclusion: usage uuid as a primary key in django model
does not seem to effect the performance on the queries (at least)
create 2000 objetcs: 226.85 sec (pk) vs  191.32 (uuid)
find the last object: 0.0089 sec(pk) vs  0.0038 (uuid) 

"""
