from typing import Dict

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from snippets.serializers import SexSerializer, AgeSerializer
from snippets.services import get_person_sex, get_person_age


@csrf_exempt
def check_sex(request, iin):
    """
    returns a sex of person by iin number.
    """
    if request.method == 'POST':
        sex: bool = get_person_sex(iin)
        data: Dict[str, bool] = {"sex": sex}
        results = SexSerializer(data).data
        return JsonResponse(results, status=200)


@csrf_exempt
def check_birthdate(request, iin):
    if request.method == 'POST':
        age: int = get_person_age(iin)
        data: Dict[str, int] = {"age": age}
        results = AgeSerializer(data).data
        return JsonResponse(results, status=200)
