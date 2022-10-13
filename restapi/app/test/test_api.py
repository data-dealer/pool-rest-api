import json
from rest_framework import status
from django.test import TestCase, Client
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
import numpy as np

from ..models import Pool
from ..serializers import PoolSerializer



class TestCaseBase(APITestCase):
    def setUp(self):
        data = {
            "poolId": 1,
            "poolValues": [
                1,
                7,
                2,
                6
            ]
        }
        serializer = PoolSerializer(data=data)
        if serializer.is_valid():
            serializer.save()


class PoolTest(TestCaseBase):

    def test_create(self):
        url = reverse('pool')
        data = {
            "poolId": 12354,
            "poolValues": [
                1,
                7,
                2,
                6
            ]
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update(self):
        url = reverse('pool')
        data = {
            "poolId": 1,
            "poolValues": [
                3,
                4,
                5
            ]
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PoolQuantileTest(TestCaseBase):
    def test_quantile(self):
        url = reverse('poolQuantile')
        data = {
            "poolId": 1,
            "percentile": 99
        }
        response = self.client.post(url, data=data)

        pool_obj = Pool.objects.get(
            poolId=data["poolId"],
        )
        self.assertEqual(
            round(float(response.json()['quantile']), 6),
            round(np.quantile(pool_obj.poolValues, data['percentile']/100), 6)
        )


