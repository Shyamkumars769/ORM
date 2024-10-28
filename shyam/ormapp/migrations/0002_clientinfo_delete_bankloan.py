# Generated by Django 5.1.2 on 2024-10-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('full_name', models.CharField(max_length=120)),
                ('account_no', models.IntegerField(primary_key='account_id', serialize=False)),
                ('IFSC_code', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('Phone_Number', models.IntegerField()),
                ('Loan_amount', models.IntegerField()),
                ('Interest', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='BankLoan',
        ),
    ]
