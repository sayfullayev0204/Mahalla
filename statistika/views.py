from rest_framework import generics, status
from accounts.models import Tuman, Maktab, Mahalla
from .serializers import MahallaSerializer, MaktabSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from adduser.models import Certificate
from accounts.permissions import (
    IsAdmin,
    IsHokim,
    IsHokimYordamchisi,
    IsTumanMasul,
    IsTumanYoshlarIshlari,
    IsMahallaMasul,
    IsMahallaYoshlarIshlari,
    IsMaktabMasul,
    IsMaktabYoshlarIshlari,
)

# Tuman


class Tumandone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Tuman.objects.get(id=tuman_id)
        # tuman english uchun
        eng_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
        ).count()
        eng_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
        ).count()
        all_en = tuman.plan_en_b2 + tuman.plan_en_c1
        if all_en != 0:
            enuqimoqda = (eng_start / all_en) * 100
            entugatgan = (eng_end / all_en) * 100
        else:
            enuqimoqda = 0

        nem_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
        ).count()
        nem_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
        ).count()
        all_nem = (tuman.plan_deorother_c1 + tuman.plan_deorother_b2) / 100
        if all_nem != 0:
            nemuqimoqda = (nem_start / all_nem) * 100
            nemtugatgan = (nem_end / all_nem) * 100
        else:
            nemuqimoqda = 0
        all_uqimoqda = nem_start + eng_start
        return Response(
            {
                "tuman_name": tuman.name,
                "all_uqimoqda": all_uqimoqda,
                "tuman_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )


class Tumanen(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Tuman.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start.count(),
                "en_b2_end": en_b2_end.count(),
                "en_c1_start": en_c1_start.count(),
                "en_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


class Tumannem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Tuman.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_nem": all_en,
                "all_nem_percent": percent,
                "nem_sertifikat": en_end,
                "nem_end_percent": en_percent,
                "nem_b2_start": en_b2_start.count(),
                "nem_b2_end": en_b2_end.count(),
                "nem_c1_start": en_c1_start.count(),
                "nem_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


# class ViloyatListCreateAPIView(generics.ListCreateAPIView):
#     permission_classes = [IsHokim, IsHokimYordamchisi, IsAdmin]
#     queryset = Viloyat.objects.all()
#     serializer_class = ViloyatSerializer


# Mahalla


class Mahalladone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Mahalla.objects.get(id=tuman_id)
        # tuman english uchun
        eng_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
        ).count()
        eng_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
        ).count()
        all_en = tuman.plan_en_b2 + tuman.plan_en_c1
        if all_en != 0:
            enuqimoqda = (eng_start / all_en) * 100
            entugatgan = (eng_end / all_en) * 100
        else:
            enuqimoqda = 0

        nem_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
        ).count()
        nem_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
        ).count()
        all_nem = (tuman.plan_deorother_c1 + tuman.plan_deorother_b2) / 100
        if all_nem != 0:
            nemuqimoqda = (nem_start / all_nem) * 100
            nemtugatgan = (nem_end / all_nem) * 100
        else:
            nemuqimoqda = 0
        all_uqimoqda = nem_start + eng_start
        return Response(
            {
                "tuman_name": tuman.name,
                "all_uqimoqda": all_uqimoqda,
                "tuman_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )


class Mahallaen(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Mahalla.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start.count(),
                "en_b2_end": en_b2_end.count(),
                "en_c1_start": en_c1_start.count(),
                "en_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


class Mahallanem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Mahalla.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_nem": all_en,
                "all_nem_percent": percent,
                "nem_sertifikat": en_end,
                "nem_end_percent": en_percent,
                "nem_b2_start": en_b2_start.count(),
                "nem_b2_end": en_b2_end.count(),
                "nem_c1_start": en_c1_start.count(),
                "nem_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


class MahallaListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari,
    ]

    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer


# maktab


class Maktabdone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari
        | IsMaktabMasul
        | IsMaktabYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Maktab.objects.get(id=tuman_id)
        # tuman english uchun
        eng_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
        ).count()
        eng_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
        ).count()
        all_en = tuman.plan_en_b2 + tuman.plan_en_c1
        if all_en != 0:
            enuqimoqda = (eng_start / all_en) * 100
            entugatgan = (eng_end / all_en) * 100
        else:
            enuqimoqda = 0

        nem_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
        ).count()
        nem_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
        ).count()
        all_nem = (tuman.plan_deorother_c1 + tuman.plan_deorother_b2) / 100
        if all_nem != 0:
            nemuqimoqda = (nem_start / all_nem) * 100
            nemtugatgan = (nem_end / all_nem) * 100
        else:
            nemuqimoqda = 0
        all_uqimoqda = nem_start + eng_start
        return Response(
            {
                "tuman_name": tuman.name,
                "all_uqimoqda": all_uqimoqda,
                "tuman_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )


class Maktaben(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari
        | IsMaktabMasul
        | IsMaktabYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Maktab.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="english",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="english",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start.count(),
                "en_b2_end": en_b2_end.count(),
                "en_c1_start": en_c1_start.count(),
                "en_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


class Maktabnem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari
        | IsMaktabMasul
        | IsMaktabYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        tuman = Maktab.objects.get(id=tuman_id)
        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2
        all_en = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        percent = (all_en / all_paln_en) * 100
        en_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2" and "C1",
        ).count()
        en_percent = (en_end / (tuman.plan_en_c1 + tuman.plan_en_b2)) * 100
        en_b2_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="B2",
        )
        en_b2_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="B2",
        )
        en_c1_start = Certificate.objects.filter(
            status="uqimoqda",
            title="nemesis",
            overel="C1",
        )
        en_c1_end = Certificate.objects.filter(
            status="tugatgan",
            title="nemesis",
            overel="C1",
        )
        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_nem": all_en,
                "all_nem_percent": percent,
                "nem_sertifikat": en_end,
                "nem_end_percent": en_percent,
                "nem_b2_start": en_b2_start.count(),
                "nem_b2_end": en_b2_end.count(),
                "nem_c1_start": en_c1_start.count(),
                "nem_c1_end": en_c1_end.count(),
            },
            status=status.HTTP_200_OK,
        )


class MaktabListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin
        | IsHokim
        | IsHokimYordamchisi
        | IsTumanMasul
        | IsTumanYoshlarIshlari
        | IsMahallaMasul
        | IsMahallaYoshlarIshlari
        | IsMaktabMasul
        | IsMaktabYoshlarIshlari,
    ]
    queryset = Maktab.objects.all()
    serializer_class = MaktabSerializer
