# Generated by Django 4.1.4 on 2023-07-24 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DMcoreapp', '0002_smo_socialmedia_smo_count_change_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress_report',
            name='status',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='perfomance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_week', models.IntegerField(blank=True, default=0, null=True)),
                ('previous_status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('current_week', models.IntegerField(blank=True, default=0, null=True)),
                ('current_status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('week_perfomance', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('client_perf_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.client_information')),
                ('client_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DMcoreapp.work')),
                ('pref_exe_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pfromance_exe', to='DMcoreapp.user_registration')),
                ('tl_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pfromance_tl', to='DMcoreapp.user_registration')),
            ],
        ),
    ]
