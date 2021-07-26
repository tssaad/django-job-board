# get data from model ----> json
from rest_framework import routers, serializers, viewsets
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['JOBowner', 'JOBTitle', 'JOBJobtype','JOBDescription','JOBCreated_at','JOBVacancy','JOBSalary',
                'JOBExperience', 'JOBCategory','JOBImage','JOBSlug'
        ]
