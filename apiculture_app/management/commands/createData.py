from django.core.management.base import BaseCommand, CommandError
from apiculture_app.models import Beetype,Beeyard,Contamination,Gathering,Hive,Intervention,Gathering
from django.db import transaction

class Command(BaseCommand):
    help = "Importing data for solo project"
    
    # @transaction.atomic
    # def handle(self, *args, **options):
    #     instance_one = MyModelOne.object.create(
    #     prop_1='yo',
    #     prop_4='yo4'
    # )
    # MyModelTwo.object.create(
    #     prop_two='yototo',
    #     my_model_one_relation=instance_one
    # )
    # self.stdout.write(
    #     self.style.SUCCESS('Data has been imported successfully')
    # )