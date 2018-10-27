# Generated by Django 2.1.2 on 2018-10-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('origin', models.TextField()),
                ('forecast', models.TextField()),
                ('drug_category', models.TextField()),
                ('last_visit', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('sex', models.TextField()),
                ('specificities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('active_substance', models.TextField()),
                ('indications', models.TextField()),
                ('contraindications', models.TextField()),
                ('mode_of_application', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DrugByReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Drug')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('sex', models.TextField()),
                ('specificities', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PatientDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Disease')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_critical', models.BooleanField()),
                ('disease_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Disease')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Doctor')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='drugbyreceipt',
            name='receipt_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Receipt'),
        ),
    ]
