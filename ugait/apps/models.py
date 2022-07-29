from django.db import models
from django import forms

# Create your models here.


TOUR_THEME_CHOICES = (
    ("식사", "식사"),
    ("지역소개", "지역소개"),
    ("핫플/오락", "핫플/오락"),
    ("자연", "자연"),
    ("관광지", "관광지"),
    ("역사/박물관", "역사/박물관"),
    ("캠핑/글램핑", "캠핑/글램핑"),
)

TOUR_LANGUAGE = (
    ("영어", "영어"),
    ("불어", "불어"),
    ("스페인어", "스페인어"),
    ("독일어", "독일어"),
    ("러시아어", "러시아어"),
    ("중국어", "중국어"),
    ("일본어", "일본어"),
    ("한국어", "한국어"),
    ("베트남어", "베트남어"),
    ("아랍어", "아랍어"),
    ("이탈리아어", "이탈리아어"),
    ("포르투갈어", "포르투갈어"),
    ("태국어", "태국어"),
    ("몽골어", "몽골어"),
    ("그리스어", "그리스어"),
    ("힌디어", "힌디어"),
)

TOUR_UNIQUE = (
    ("자차투어가능", "자차투어가능"),
    ("캠핑장비보유", "캠핑장비보유"),
)


class TourTheme(models.Model):
    tour_theme = models.Choices(choices=TOUR_THEME_CHOICES)


class TourLang(models.Model):
    tour_lang = models.Choices(choices=TOUR_LANGUAGE)


class TourUniq(models.Model):
    tour_uniq = models.Choices(choices=TOUR_UNIQUE)


class User(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    location = models.CharField(max_length=30, default='seoul')


class Guide(models.Model):
    tourtheme = models.ForeignKey(
        TourTheme, related_name='tour_theme', on_delete=models.CASCADE)
    tourlang = models.ForeignKey(
        TourLang, related_name='tour_lang', on_delete=models.CASCADE)
    touruniq = models.ForeignKey(
        TourUniq, related_name='tour_uniq', on_delete=models.CASCADE)


class GuidePlan(models.Model):
    tourtheme = models.ForeignKey(
        TourTheme, related_name='tour_theme', on_delete=models.CASCADE)
    tourlang = models.ForeignKey(
        TourLang, related_name='tour_lang', on_delete=models.CASCADE)
    touruniq = models.ForeignKey(
        TourUniq, related_name='tour_uniq', on_delete=models.CASCADE)
    tour_sta_time = models.TimeField()
    tour_end_time = models.TimeField()


'''
class Guide(models.Model):
    mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    guide_profile = models.ImageField()
    star_rate = models.IntegerField()
    review_count = models.PositiveIntegerField()
    tour_sta_time = models.TimeField()
    tour_end_time = models.TimeField()
    car_tour_yn = models.CharField(max_length=1)
    camp_tour_yn = models.CharField(max_length=1)
    etc = models.TextField()



class Guide_Lang(models.Model):
    guide_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    # lang_cd =


class GuideMatching(models.Model):
    user_mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    guide_mb_id = models.ForeignKey(
        Member, related_name='id', on_delete=models.CASCADE)
    tour_type = models.CharField()  # choices
    tour_sta_time = models.TimeField()
    tour_end_time = models.TimeField()
    tour_day = models.DateField()
'''
