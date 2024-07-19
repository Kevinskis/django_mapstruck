from django.db import models

class Conductores(models.Model):
    id_conductor = models.AutoField(db_column='ID_CONDUCTOR', primary_key=True)
    nombre = models.CharField(max_length=20)
    licencia = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)

    def _str_(self):
        return str(self.nombre)



class Gruas(models.Model):
    id_grua = models.AutoField(db_column='ID_GRUAS', primary_key=True)
    modelo = models.TextField()
    capacidad = models.PositiveIntegerField()
    estado = models.TextField()

    def _str_(self):
        return str(self.modelo)

class Clientes(models.Model):
    id_cliente = models.AutoField(db_column='ID_CLIENTE', primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField()
    email = models.CharField(max_length=30)
    id_vehiculo = models.PositiveIntegerField()

    def _str_(self):
        return str(self.nombre) + " " + str(self.apellidos)

class Ubicacion(models.Model):
    id_ubicacion = models.PositiveIntegerField(db_column='ID_UBICACION', primary_key=True)
    latitud = models.PositiveIntegerField()
    longitud = models.PositiveIntegerField()
    marca_tiempo = models.PositiveIntegerField()
    grua = models.ForeignKey(Gruas, on_delete=models.CASCADE, db_column='Grúas_ID_GRUAS')

    def _str_(self):
        return str(self.id_ubicacion)

class Servicios(models.Model):
    id_solicitud = models.AutoField(db_column='ID_SOLICITUD', primary_key=True)
    fecha_solicitud = models.CharField(max_length=10)
    estado = models.TextField()
    ubi_origen = models.TextField()
    ubi_final = models.TextField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, db_column='CLIENTES_ID_CLIENTE')
    grua = models.ForeignKey(Gruas, on_delete=models.CASCADE, db_column='Grúas_ID_GRUAS')
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE, db_column='CONDUCTORES_ID_CONDUCTOR')

    def _str_(self):
        return str(self.id_solicitud)

class Empresa(models.Model):
    id_empresa = models.AutoField(db_column='ID_EMPRESA', primary_key=True)
    direccion_emp = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    mail = models.CharField(max_length=20)
    encargado = models.TextField()
    id_servicio = models.TextField()
    grua = models.ForeignKey(Gruas, on_delete=models.CASCADE, db_column='Grúas_ID_GRUAS')
    conductor = models.ForeignKey(Conductores, on_delete=models.CASCADE, db_column='CONDUCTORES_ID_CONDUCTOR')

    def _str_(self):
        return str(self.id_empresa)

