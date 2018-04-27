from django.db import models

class JsonModel(models.Model):
    gps_time=models.CharField(max_length=50, null=True)
    gps_latitude=models.CharField(max_length=50,null=True)
    gps_longitude = models.CharField(max_length=50,null=True)
    gps_altitude = models.CharField(max_length=50,null=True)
    gps_course = models.CharField(max_length=50,null=True)
    gps_speed = models.CharField(max_length=50,null=True)
    imu_ax= models.CharField(max_length=50,null=True)
    imu_ay = models.CharField(max_length=50,null=True)
    imu_az = models.CharField(max_length=50,null=True)
    imu_cx = models.CharField(max_length=50,null=True)
    imu_cy = models.CharField(max_length=50,null=True)
    imu_cz = models.CharField(max_length=50,null=True)
    imu_gx = models.CharField(max_length=50,null=True)
    imu_gy = models.CharField(max_length=50,null=True)
    imu_gz = models.CharField(max_length=50,null=True)
    barometer_temperature= models.CharField(max_length=50,null=True)
    barometer_Pressure= models.CharField(max_length=50,null=True)
    barometer_Altitude = models.CharField(max_length=50,null=True)
    time_milisenconds= models.CharField(max_length=50,null=True)
    gas_nh3 = models.CharField(max_length=50,null=True)
    gas_co= models.CharField(max_length=50,null=True)
    gas_no2 = models.CharField(max_length=50,null=True)
    gas_c3h8 = models.CharField(max_length=50,null=True)
    gas_c4h10 = models.CharField(max_length=50,null=True)
    gas_ch4= models.CharField(max_length=50,null=True)
    gas_h2= models.CharField(max_length=50,null=True)
    gas_c2h5oh= models.CharField(max_length=50,null=True)
    temperature_sht11= models.CharField(max_length=50,null=True)
    humidity_sht11= models.CharField(max_length=50,null=True)
    temperature_i2c= models.CharField(max_length=50,null=True)
    mean_temperature = models.CharField(max_length=50,null=True)
    voltaje_bateria = models.CharField(max_length=50, null=True)
class TramaCorta(models.Model):
    gps_time=models.CharField(max_length=50, null=True)
    gps_latitude=models.CharField(max_length=50, null=True)
    gps_longitude=models.CharField(max_length=50, null=True)
    gps_altitude=models.CharField(max_length=50, null=True)
    gps_course=models.CharField(max_length=50, null=True)
    gps_speed=models.CharField(max_length=50, null=True)
    barometer_Pressure=models.CharField(max_length=50, null=True)
    barometer_Altitude=models.CharField(max_length=50, null=True)
    temperature_sht11=models.CharField(max_length=50, null=True)
    voltaje_bateria=models.CharField(max_length=50, null=True)

class Compresores(models.Model):
    humidity=models.CharField(max_length=50,null=True)
    temperature=models.CharField(max_length=50,null=True)
    estado=models.CharField(max_length=50,null=True)


class Imagenes(models.Model):
    img=models.CharField(max_length=30000,null=True)


class LiveImg(models.Model):
    imgLive=models.CharField(max_length=30000,null=True)
