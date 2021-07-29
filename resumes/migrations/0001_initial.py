from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobpostings', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpostings.jobposting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'applies',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('is_done', models.BooleanField(default=False)),
                ('file_url', models.URLField(null=True)),
                ('content', models.JSONField(default=dict)),
                ('is_file', models.BooleanField(default=False)),
                ('file_uuid', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'resumes',
            },
        ),
        migrations.CreateModel(
            name='ResumeApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.apply')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resumes.resume')),
            ],
            options={
                'db_table': 'resumes_applies',
                'unique_together': {('resume', 'apply')},
            },
        ),
        migrations.AddField(
            model_name='resume',
            name='applies',
            field=models.ManyToManyField(related_name='resume', through='resumes.ResumeApply', to='resumes.Apply'),
        ),
        migrations.AddField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
