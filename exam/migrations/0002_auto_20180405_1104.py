# Generated by Django 2.0.1 on 2018-04-05 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExaminerLacThroughModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['examiner'],
            },
        ),
        migrations.RemoveField(
            model_name='examiner',
            name='name',
        ),
        migrations.AddField(
            model_name='examinerlacthroughmodel',
            name='examiner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Examiner'),
        ),
        migrations.AddField(
            model_name='examinerlacthroughmodel',
            name='lac',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Lac'),
        ),
        migrations.AddField(
            model_name='examiner',
            name='name',
            field=models.ManyToManyField(through='exam.ExaminerLacThroughModel', to='exam.Lac'),
        ),
    ]
