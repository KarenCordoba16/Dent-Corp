# Generated by Django 4.2.7 on 2023-11-03 01:20

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionesConsultorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio_asig', models.DateTimeField()),
                ('fecha_fin_asig', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Cajas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hr_ap_cj', models.DateTimeField()),
                ('fecha_hr_cr_cj', models.DateTimeField()),
                ('monto_ap_cj', models.FloatField()),
                ('monto_cr_cj', models.FloatField()),
                ('comentarios', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_ciu', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Coberturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_con', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoberturasXUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Consultorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cons', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_espec', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PagosServExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_serv', models.CharField(max_length=50)),
                ('fecha_cad_cont', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Planes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plan', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_prov', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RolXUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_Alta_usu', models.DateField()),
                ('fecha_baja_usu', models.DateField()),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.roles')),
            ],
        ),
        migrations.CreateModel(
            name='ServiciosOdontologicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_serv_odon', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_usu', models.CharField(max_length=9)),
                ('nom_usu', models.CharField(max_length=50)),
                ('ape_usu', models.CharField(max_length=50)),
                ('dom_usu', models.CharField(max_length=50)),
                ('tel_usu', models.CharField(max_length=14)),
                ('email_usu', models.EmailField(max_length=254)),
                ('contra_usu', models.CharField(max_length=50)),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.ciudades')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email adress')),
                ('groups', models.ManyToManyField(related_name='dcapp_users_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='dcapp_users_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hr_turno', models.DateTimeField()),
                ('autorizado', models.BooleanField()),
                ('id_asig_cons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.asignacionesconsultorio')),
                ('id_cob_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.coberturasxusuario')),
                ('id_rol_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.rolxusuario')),
                ('id_serv_odon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.serviciosodontologicos')),
            ],
        ),
        migrations.AddField(
            model_name='rolxusuario',
            name='id_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.usuarios'),
        ),
        migrations.CreateModel(
            name='PlanXCobertura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.coberturas')),
                ('id_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.planes')),
            ],
        ),
        migrations.CreateModel(
            name='FacturasServExt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_fack', models.CharField(max_length=200)),
                ('costo_fact', models.FloatField()),
                ('fecha_cad_fact', models.DateField()),
                ('fecha_pago_fact', models.DateField()),
                ('comprobante_pago', models.BooleanField()),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.cajas')),
                ('id_serv_ext', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.pagosservext')),
            ],
        ),
        migrations.CreateModel(
            name='FacturasOdontologicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costo_fact_pac', models.FloatField()),
                ('costo_fact_cob', models.FloatField()),
                ('costo_total_fact_odon', models.FloatField()),
                ('fecha_fact_odon', models.DateTimeField()),
                ('id_caja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.cajas')),
                ('id_turno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.turnos')),
            ],
        ),
        migrations.CreateModel(
            name='EspecXUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('id_espec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.especialidades')),
                ('id_rol_usu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.rolxusuario')),
            ],
        ),
        migrations.AddField(
            model_name='coberturasxusuario',
            name='id_plan_cob',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.planxcobertura'),
        ),
        migrations.AddField(
            model_name='coberturasxusuario',
            name='id_rol_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.rolxusuario'),
        ),
        migrations.AddField(
            model_name='ciudades',
            name='id_prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.provincias'),
        ),
        migrations.AddField(
            model_name='cajas',
            name='id_rol_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.rolxusuario'),
        ),
        migrations.AddField(
            model_name='asignacionesconsultorio',
            name='id_cons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.consultorios'),
        ),
        migrations.AddField(
            model_name='asignacionesconsultorio',
            name='id_espec_usu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DCapp.especxusuario'),
        ),
    ]
