# Generated by Django 5.0.2 on 2025-07-05 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PFEProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_id', models.CharField(max_length=50, unique=True, verbose_name='référence')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('description', models.TextField(verbose_name='description')),
                ('domain', models.CharField(choices=[('informatique', 'Informatique'), ('genie_civil', 'Génie Civil'), ('genie_mecanique', 'Génie Mécanique'), ('genie_electrique', 'Génie Électrique'), ('gestion', 'Gestion'), ('marketing', 'Marketing'), ('finance', 'Finance'), ('autre', 'Autre')], max_length=50, verbose_name='domaine')),
                ('supervisor_name', models.CharField(max_length=100, verbose_name='nom du superviseur')),
                ('supervisor_email', models.EmailField(max_length=254, verbose_name='email du superviseur')),
                ('supervisor_department', models.CharField(max_length=100, verbose_name='département du superviseur')),
                ('objectives', models.TextField(blank=True, verbose_name='objectifs')),
                ('requirements', models.TextField(blank=True, verbose_name='prérequis')),
                ('deliverables', models.TextField(blank=True, verbose_name='livrables')),
                ('duration_weeks', models.PositiveIntegerField(default=12, verbose_name='durée en semaines')),
                ('technologies', models.TextField(blank=True, verbose_name='technologies')),
                ('tools', models.TextField(blank=True, verbose_name='outils')),
                ('status', models.CharField(choices=[('draft', 'Brouillon'), ('published', 'Publié'), ('archived', 'Archivé')], default='draft', max_length=20, verbose_name='statut')),
                ('is_featured', models.BooleanField(default=False, verbose_name='mis en avant')),
                ('max_candidates', models.PositiveIntegerField(default=1, verbose_name='nombre maximum de candidats')),
                ('current_candidates', models.PositiveIntegerField(default=0, verbose_name='nombre de candidats actuels')),
                ('academic_year', models.CharField(default='2024-2025', max_length=20, verbose_name='année académique')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='date de publication')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pfe_projects_created', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'projet PFE',
                'verbose_name_plural': 'projets PFE',
                'db_table': 'pfe_project',
                'ordering': ['-created_at'],
            },
        ),
    ]
