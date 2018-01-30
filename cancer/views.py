from django.shortcuts import render
from .models import Cancer
from django import forms
import datetime
from django.conf import settings

# Create your views here.
class Patient(forms.Form):
    

def add_patient(request):
    if request.method == 'POST':
        new_patient = Patient(request)
        if new_patient.is_valid():
            card_id = new_patient.cleaned_data['card_id']
            card_type = new_patient.cleaned_data['card_type']
            icd_10_code = new_patient.cleaned_data['icd_10_code']
            icd_o_code = new_patient.cleaned_data['icd_o_code']
            patient_no = new_patient.cleaned_data['patient_no']
            hospitalized_no = new_patient.cleaned_data['hospitalized_no']
            id_no = new_patient.cleaned_data['id_no']
            name = new_patient.cleaned_data['name']
            race = new_patient.cleaned_data['race']
            birth_date = new_patient.cleaned_data['birth_date']
            exact_age = new_patient.cleaned_data['exact_age']
            marriage = new_patient.cleaned_data['marriage']
            telephone = new_patient.cleaned_data['telephone']
            occupation = new_patient.cleaned_data['occupation']
            company = new_patient.cleaned_data['company']
            census_register = new_patient.cleaned_data['new_patient']
            residence = new_patient.cleaned_data['residence']
            diagnosis = new_patient.cleaned_data['diagnosis']
            pathology = new_patient.cleaned_data['pathology']
            diagnose_type = new_patient.cleaned_data['diagnose_type']
            diagnose_date = new_patient.cleaned_data['diagnose_date']
            diagnose_hospital = new_patient.cleaned_data['diagnose_hospital']
            follow_up = new_patient.cleaned_data['follow_up']
            death_date = new_patient.cleaned_data['death_date']
            death_reason = new_patient.cleaned_data['death_reason']
            death_point = new_patient.cleaned_data['death_point']
            reporter = new_patient.cleaned_data['reporter']
            report_hospital = new_patient.cleaned_data['report_hospital']
            report_date = new_patient.cleaned_data['report_date']
            pre_diagnosis = new_patient.cleaned_data['pre_diagnosis']
            pre_diagnose_date = new_patient.cleaned_data['pre_diagnose_date']
            Patient.objects.create(card_id=card_id, card_type=card_type,icd_10_code=icd_10_code,
                                   icd_o_code=icd_o_code,patient_no=patient_no,hospitalized_no=hospitalized_no,
                                   id_no=id_no,name=name,gender=gender,race=race,birth_date=birth_date,
                                   exact_age=exact_age,marriage=marriage,telephone=telephone,occupation=occupation,
                                   company=company,census_register=census_register,residence=residence,
                                   diagnosis=diagnosis,pathology=pathology,diagnose_type=diagnose_type,
                                   diagnose_date=diagnose_date,diagnose_hospital=diagnose_hospital,
                                   death_date=death_date,death_reason=death_reason,reporter=reporter,
                                   pre_diagnosis=pre_diagnosis,pre_diagnose_date=pre_diagnose_date,
                                   follow_up=follow_up,death_point=death_point).save()
            return render(request,'cancer/add_patient.html',{'form':new_patient})
    else:
        new_patient = Patient()
    return render(request,'cancer/add_patient.html',{'form':new_patient})

def bianhao(request):
    a = CanPatient.objects.all().last().card_id
    if a.is_valid():
        b = a + 1
    else:
        b = 1
    return b
