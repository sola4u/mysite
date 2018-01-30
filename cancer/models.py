from django.db import models

# Create your models here.
class Cancer(models.Model):
    card_id = models.IntegerField()
    card_type_choices =(
        (1,'发病卡'),
        (2,'死亡卡'),
    )
    card_type = models.IntegerField(choices=card_type_choices)
    icd_10_code = models.CharField(max_length=8,blank=True)
    icd_o_code = models.CharField(max_length=8,blank=True)
    patient_no = models.IntegerField()
    hospitalized_no = models.IntegerField()
    id_no = models.CharField(max_length=18,blank=True)
    name = models.CharField(max_length=40)
    gender_choices = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.IntegerField(choices=gender_choices)
    race = models.CharField(max_length=8)
    birth_date = models.DateField()
    exact_age = models.IntegerField()
    marriage = models.CharField(max_length=4)
    telephone = models.IntegerField()
    occupation = models.CharField(max_length=8)
    company = models.CharField(max_length=16)
    census_register = models.CharField(max_length=64)
    residence = models.CharField(max_length=64)
    diagnosis = models.CharField(max_length=16)
    pathology = models.CharField(max_length=8)
    diagnosis_choices = (
        (0,'死亡补发病'),
        (1,'临床'),
        (2,'X线、CT、超声、内镜'),
        (3,'手术、尸检（无病理）'),
        (4,'生化、免疫'),
        (5,'细胞学、血片'),
        (6,'病理（继发）'),
        (7,'病理（原发）'),
        (8,'尸检（有病理）'),
        (9,'不详'),
    )
    diagnose_type = models.IntegerField(choices=diagnosis_choices)
    diagnose_date = models.DateField()
    diagnose_hospital = models.CharField(max_length=16)
    follow_up_choice = (
        (1,'存活'),
        (2,'死亡'),
        (3,'移居'),
        (4,'失访'),
        (9,'不详'),
    )
    follow_up = models.IntegerField(choices=follow_up_choice)
    result = models.CharField(max_length=16)
    death_date = models.DateField()
    death_reason = models.CharField(max_length=16)
    death_point_choices = (
        (1,'医院'),
        (2,'疗养院'),
        (3,'晚期肿瘤病房'),
        (4,'家庭病房'),
        (5,'家中'),
        (6,'不详'),
    )
    death_point = models.IntegerField(choices=death_point_choices)
    reporter = models.CharField(max_length=8)
    death_point = models.CharField(max_length=16)
    report_hospital = models.CharField(max_length=16)
    report_date = models.DateField()
    pre_diagnosis = models.CharField(max_length=16,blank=True)
    pre_diagnose_date = models.DateField(blank=True)

