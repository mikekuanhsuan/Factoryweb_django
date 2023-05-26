# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AProduct(models.Model):
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product'


class AProduct2(models.Model):
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    proportion = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'A_Product2'


class AProductMachine(models.Model):
    factory_id = models.CharField(db_column='Factory_ID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    moisture = models.DecimalField(db_column='Moisture', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    specific_surface = models.DecimalField(db_column='Specific_Surface', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    residual_on_sieve = models.DecimalField(db_column='Residual_On_Sieve', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_1_mill = models.DecimalField(db_column='Device_Value_1_Mill', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_1_pressure = models.DecimalField(db_column='Device_Value_1_pressure', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_2_mill = models.DecimalField(db_column='Device_Value_2_Mill', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_2_pressure = models.DecimalField(db_column='Device_Value_2_pressure', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_carrier = models.DecimalField(db_column='Device_Value_Carrier', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    device_value_blower = models.DecimalField(db_column='Device_Value_blower', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product_Machine'
        unique_together = (('factory_id', 'mill_id', 'dtime'),)


class AProductQuality(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    moisture = models.DecimalField(db_column='Moisture', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    specific_surface = models.DecimalField(db_column='Specific_Surface', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    residual_on_sieve = models.DecimalField(db_column='Residual_On_Sieve', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    visible = models.CharField(db_column='Visible', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_info = models.CharField(db_column='Client_Info', max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product_Quality'
        unique_together = (('factoryid', 'mill_id', 'dtime', 'datetime', 'productid'),)


class AProductQuality2(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    moisture = models.DecimalField(db_column='Moisture', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    specific_surface = models.DecimalField(db_column='Specific_Surface', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    residual_on_sieve = models.DecimalField(db_column='Residual_On_Sieve', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    visible = models.CharField(db_column='Visible', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    client_info = models.CharField(db_column='Client_Info', max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    laboratory = models.CharField(db_column='Laboratory', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product_Quality2'
        unique_together = (('factoryid', 'mill_id', 'dtime', 'datetime', 'productid', 'client_info', 'laboratory'),)


class AProductShipMapping(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    barrel_tank = models.IntegerField(db_column='Barrel_tank')  # Field name made lowercase.
    productid = models.CharField(db_column='ProductID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth')  # Field name made lowercase.
    height = models.IntegerField(db_column='Height')  # Field name made lowercase.
    diameter = models.IntegerField(db_column='Diameter')  # Field name made lowercase.
    bottom = models.IntegerField(db_column='Bottom')  # Field name made lowercase.
    proportion = models.DecimalField(max_digits=5, decimal_places=2)
    total_height = models.DecimalField(db_column='Total_Height', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product_Ship_Mapping'
        unique_together = (('factoryid', 'barrel_tank'),)


class AProductShipMessage(models.Model):
    dtime = models.DateTimeField(db_column='DTime', primary_key=True)  # Field name made lowercase.
    dhour = models.IntegerField(db_column='DHour')  # Field name made lowercase.
    factoryid = models.CharField(db_column='FactoryID', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    message = models.CharField(max_length=200, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'A_Product_Ship_Message'
        unique_together = (('dtime', 'dhour', 'factoryid'),)


class AProductShipData(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    dhour = models.IntegerField(db_column='DHour')  # Field name made lowercase.
    library_class = models.IntegerField(db_column='Library_Class')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'A_Product_Ship_data'
        unique_together = (('factoryid', 'datadate', 'dhour', 'library_class'),)


class DespatchName(models.Model):
    prod_id = models.CharField(db_column='PROD_ID', primary_key=True, max_length=2, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    prod_name = models.CharField(db_column='PROD_NAME', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cpackage = models.CharField(db_column='CPACKAGE', max_length=5, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Despatch_Name'


class Factory(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    factoryname = models.CharField(db_column='FactoryName', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aorder = models.IntegerField(db_column='aOrder', blank=True, null=True)  # Field name made lowercase.
    serverip = models.CharField(db_column='ServerIP', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tpc_act = models.CharField(db_column='Tpc_act', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tpc_pwd = models.CharField(db_column='Tpc_pwd', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factory'


class FactoryMill(models.Model):
    factoryid = models.CharField(db_column='FactoryID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factory_Mill'


class FactoryState(models.Model):
    dtime = models.DateTimeField(db_column='DTime', primary_key=True)  # Field name made lowercase.
    host1 = models.CharField(db_column='Host1', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    host2 = models.CharField(db_column='Host2', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    light = models.BooleanField(db_column='Light', blank=True, null=True)  # Field name made lowercase.
    message = models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Factory_State'
        unique_together = (('dtime', 'host1', 'host2'),)


class FtyPhoto(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    factoryid = models.CharField(db_column='FactoryID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    lane = models.CharField(db_column='Lane', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    licenseid = models.CharField(db_column='LicenseID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unsafety_person = models.CharField(db_column='Unsafety_Person', max_length=5, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    unsafety_hat = models.CharField(db_column='Unsafety_hat', max_length=5, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dust = models.CharField(db_column='Dust', max_length=5, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time1 = models.DateTimeField(db_column='Time1', blank=True, null=True)  # Field name made lowercase.
    time2 = models.DateTimeField(db_column='Time2', blank=True, null=True)  # Field name made lowercase.
    order_id1 = models.CharField(db_column='ORDER_ID1', max_length=11, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    work_id = models.CharField(db_column='WORK_ID', max_length=11, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fty_Photo'
        unique_together = (('id', 'factoryid'),)


class GAirComp(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    getdatetime = models.DateTimeField(db_column='GetDateTime', blank=True, null=True)  # Field name made lowercase.
    specific_power = models.DecimalField(db_column='Specific_Power', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    air_consumption = models.DecimalField(db_column='Air_Consumption', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    air_acc_01 = models.DecimalField(db_column='Air_acc_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    air_acc_02 = models.DecimalField(db_column='Air_acc_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c = models.DecimalField(db_column='Power_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_01 = models.DecimalField(db_column='Power_CH_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_02 = models.DecimalField(db_column='Power_CH_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_03 = models.DecimalField(db_column='Power_CH_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_04 = models.DecimalField(db_column='Power_CH_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_05 = models.DecimalField(db_column='Power_CH_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_01 = models.DecimalField(db_column='Power_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_02 = models.DecimalField(db_column='Power_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_03 = models.DecimalField(db_column='Power_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_04 = models.DecimalField(db_column='Power_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_05 = models.DecimalField(db_column='Power_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    worktime_01 = models.DecimalField(db_column='WorkTime_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_02 = models.DecimalField(db_column='WorkTime_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_03 = models.DecimalField(db_column='WorkTime_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_04 = models.DecimalField(db_column='WorkTime_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_05 = models.DecimalField(db_column='WorkTime_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Air_Comp'
        unique_together = (('factoryid', 'mid', 'datadate'),)


class GAirCompH(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    dhour = models.IntegerField(db_column='DHour')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    specific_power = models.DecimalField(db_column='Specific_Power', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    air_consumption = models.DecimalField(db_column='Air_Consumption', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    air_acc_01 = models.DecimalField(db_column='Air_acc_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    air_acc_02 = models.DecimalField(db_column='Air_acc_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c = models.DecimalField(db_column='Power_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_01 = models.DecimalField(db_column='Power_CH_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_02 = models.DecimalField(db_column='Power_CH_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_03 = models.DecimalField(db_column='Power_CH_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_04 = models.DecimalField(db_column='Power_CH_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_ch_05 = models.DecimalField(db_column='Power_CH_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_01 = models.DecimalField(db_column='Power_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_02 = models.DecimalField(db_column='Power_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_03 = models.DecimalField(db_column='Power_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_04 = models.DecimalField(db_column='Power_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_05 = models.DecimalField(db_column='Power_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    worktime_01 = models.DecimalField(db_column='WorkTime_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_02 = models.DecimalField(db_column='WorkTime_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_03 = models.DecimalField(db_column='WorkTime_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_04 = models.DecimalField(db_column='WorkTime_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_05 = models.DecimalField(db_column='WorkTime_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Air_Comp_H'
        unique_together = (('factoryid', 'mid', 'dtime'),)


class GAirCompMapping(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    air_acc_01 = models.CharField(db_column='Air_acc_01', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    air_acc_02 = models.CharField(db_column='Air_acc_02', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_01 = models.CharField(db_column='Power_01', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_02 = models.CharField(db_column='Power_02', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_03 = models.CharField(db_column='Power_03', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_04 = models.CharField(db_column='Power_04', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_05 = models.CharField(db_column='Power_05', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    worktime_01 = models.CharField(db_column='WorkTime_01', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    worktime_02 = models.CharField(db_column='WorkTime_02', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    worktime_03 = models.CharField(db_column='WorkTime_03', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    worktime_04 = models.CharField(db_column='WorkTime_04', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    worktime_05 = models.CharField(db_column='WorkTime_05', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Air_Comp_Mapping'
        unique_together = (('factoryid', 'mid'),)


class GMachine(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    device_num = models.CharField(db_column='Device_Num', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    class_name = models.CharField(db_column='Class_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bach = models.IntegerField(blank=True, null=True)
    count_tag = models.CharField(db_column='Count_Tag', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    count_total_tag = models.CharField(db_column='Count_Total_Tag', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    par = models.IntegerField(blank=True, null=True)
    machine_num = models.IntegerField(db_column='Machine_num', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine'
        unique_together = (('factoryid', 'device_num'),)


class GMachineAccess(models.Model):
    factory_id = models.CharField(db_column='Factory_ID', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    object_id = models.CharField(db_column='Object_ID', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    device_num = models.CharField(db_column='Device_Num', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    access_name = models.CharField(db_column='Access_Name', max_length=25, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    access_spec = models.TextField(db_column='Access_Spec', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    access_count = models.CharField(db_column='Access_Count', max_length=25, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    materials_num = models.CharField(db_column='Materials_Num', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    assets_num = models.CharField(db_column='Assets_Num', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    note = models.TextField(db_column='Note', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    next_date_pm = models.IntegerField(db_column='Next_Date_PM', blank=True, null=True)  # Field name made lowercase.
    link_tag = models.CharField(db_column='Link_Tag', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stop = models.CharField(db_column='Stop', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    file_path = models.CharField(db_column='File_Path', max_length=150, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_Access'


class GMachineCidKeyword(models.Model):
    cid = models.CharField(db_column='CID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    keyword_name = models.CharField(db_column='KeyWord_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_CID_KeyWord'


class GMachineKeyword(models.Model):
    keyword_name = models.CharField(db_column='KeyWord_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_Keyword'


class GMachineMtbf(models.Model):
    factory_id = models.CharField(db_column='Factory_ID', primary_key=True, max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    object_id = models.CharField(db_column='Object_ID', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    link_tag = models.CharField(db_column='Link_Tag', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stop_flag = models.CharField(db_column='Stop_Flag', max_length=2, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stop_time = models.DateTimeField(db_column='Stop_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_MTBF'
        unique_together = (('factory_id', 'object_id'),)


class GMachineRepair(models.Model):
    factory_id = models.CharField(db_column='Factory_ID', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    object_id = models.CharField(db_column='Object_ID', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cid = models.CharField(db_column='CID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    repair_num = models.CharField(db_column='Repair_Num', max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    parts_name = models.CharField(db_column='Parts_Name', max_length=25, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    change_date = models.DateField(db_column='Change_Date', blank=True, null=True)  # Field name made lowercase.
    calculate_change_date = models.DateField(db_column='Calculate_Change_Date', blank=True, null=True)  # Field name made lowercase.
    service_life = models.IntegerField(db_column='Service_Life', blank=True, null=True)  # Field name made lowercase.
    change_num = models.IntegerField(db_column='Change_Num', blank=True, null=True)  # Field name made lowercase.
    parts_detail = models.CharField(db_column='Parts_Detail', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mark_lable = models.CharField(db_column='Mark_Lable', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    change_reason = models.CharField(db_column='Change_Reason', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    change_person = models.CharField(db_column='Change_Person', max_length=3, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    work_time = models.DecimalField(db_column='Work_Time', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    caculate_work_time = models.DecimalField(db_column='Caculate_Work_Time', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    count_flag = models.CharField(db_column='Count_Flag', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    create_account = models.CharField(db_column='Create_Account', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField(db_column='Update_Time', blank=True, null=True)  # Field name made lowercase.
    stop = models.IntegerField(db_column='Stop', blank=True, null=True)  # Field name made lowercase.
    stop_time = models.DateTimeField(db_column='Stop_Time', blank=True, null=True)  # Field name made lowercase.
    stop_account = models.CharField(db_column='Stop_Account', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_Repair'
        unique_together = (('cid', 'repair_num'),)


class GMachineWorkhour(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    workhour = models.DecimalField(db_column='WorkHour', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Machine_WorkHour'
        unique_together = (('factoryid', 'tagname', 'ddate'),)


class GMachingWorkvalue30M(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=30, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mname = models.CharField(db_column='MName', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    mdate = models.DateTimeField(db_column='MDate')  # Field name made lowercase.
    mvalue = models.DecimalField(db_column='MValue', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_mvalue = models.DecimalField(db_column='Total_MValue', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Maching_WorkValue_30M'
        unique_together = (('factoryid', 'tagname', 'mdate'),)


class GMaintainLog(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    maintaindate = models.DateField(db_column='MaintainDate')  # Field name made lowercase.
    ver = models.IntegerField(db_column='Ver')  # Field name made lowercase.
    maintaindesc = models.CharField(db_column='MaintainDesc', max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maintaindetil = models.CharField(db_column='MaintainDetil', max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creatdate = models.DateField(db_column='CreatDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Maintain_Log'
        unique_together = (('factoryid', 'tagname', 'maintaindate', 'ver'),)


class GMillingMachine(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    dtime = models.IntegerField(db_column='DTime')  # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime')  # Field name made lowercase.
    motor_current_a = models.DecimalField(db_column='Motor_Current_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_current_b = models.DecimalField(db_column='Motor_Current_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_a = models.DecimalField(db_column='Motor_PowerKW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_b = models.DecimalField(db_column='Motor_PowerKW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_a = models.DecimalField(db_column='Bucket_Elevator_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_b = models.DecimalField(db_column='Bucket_Elevator_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_current = models.DecimalField(db_column='OSEPA_Current', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_rpm = models.DecimalField(db_column='OSEPA_RPM', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m1 = models.DecimalField(db_column='Bag_Colletcot_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m2 = models.DecimalField(db_column='Bag_Colletcot_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_s = models.DecimalField(db_column='Bag_Colletcot_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_a = models.DecimalField(db_column='TE_Mill_Bearing_In_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_a = models.DecimalField(db_column='TE_Mill_Bearing_Out_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_a = models.DecimalField(db_column='TE_Mill_Bearing_Oil_In_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_a = models.DecimalField(db_column='TE_Mill_Bearing_Oil_Out_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_b = models.DecimalField(db_column='TE_Mill_Bearing_In_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_b = models.DecimalField(db_column='TE_Mill_Bearing_Out_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_b = models.DecimalField(db_column='TE_Mill_Bearing_Oil_In_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_b = models.DecimalField(db_column='TE_Mill_Bearing_Oil_Out_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_a = models.DecimalField(db_column='TE_Mill_RAW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_a = models.DecimalField(db_column='TE_Mill_Air_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_b = models.DecimalField(db_column='TE_Mill_RAW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_b = models.DecimalField(db_column='TE_Mill_Air_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_s_in = models.DecimalField(db_column='TE_S_In', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_product = models.DecimalField(db_column='TE_Product', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_1_a = models.DecimalField(db_column='TE_Motor_1_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_2_a = models.DecimalField(db_column='TE_Motor_2_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_3_a = models.DecimalField(db_column='TE_Motor_3_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_4_a = models.DecimalField(db_column='TE_Motor_4_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_5_a = models.DecimalField(db_column='TE_Motor_5_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_6_a = models.DecimalField(db_column='TE_Motor_6_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_1_b = models.DecimalField(db_column='TE_Motor_1_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_2_b = models.DecimalField(db_column='TE_Motor_2_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_3_b = models.DecimalField(db_column='TE_Motor_3_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_4_b = models.DecimalField(db_column='TE_Motor_4_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_5_b = models.DecimalField(db_column='TE_Motor_5_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_6_b = models.DecimalField(db_column='TE_Motor_6_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_a = models.DecimalField(db_column='WP_Mill_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_b = models.DecimalField(db_column='WP_Mill_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_osepa = models.DecimalField(db_column='WP_OSEPA', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_in = models.DecimalField(db_column='WP_BC_S_IN', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_diff = models.DecimalField(db_column='WP_BC_S_Diff', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m1 = models.DecimalField(db_column='RPM_BC_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m2 = models.DecimalField(db_column='RPM_BC_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_s = models.DecimalField(db_column='RPM_BC_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m1 = models.DecimalField(db_column='OP_BC_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m2 = models.DecimalField(db_column='OP_BC_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_s = models.DecimalField(db_column='OP_BC_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_p = models.DecimalField(db_column='W_M1_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_c = models.DecimalField(db_column='W_M1_A_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_q = models.DecimalField(db_column='W_M1_A_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_p = models.DecimalField(db_column='W_M1_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_c = models.DecimalField(db_column='W_M1_B_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_q = models.DecimalField(db_column='W_M1_B_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_p = models.DecimalField(db_column='W_M2_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_c = models.DecimalField(db_column='W_M2_A_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_q = models.DecimalField(db_column='W_M2_A_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_p = models.DecimalField(db_column='W_M2_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_c = models.DecimalField(db_column='W_M2_B_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_q = models.DecimalField(db_column='W_M2_B_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Milling_Machine'
        unique_together = (('factoryid', 'mill_id', 'ddate', 'datatime'),)


class GMillingMachineMapping(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    motor_current_a = models.CharField(db_column='Motor_Current_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    motor_current_b = models.CharField(db_column='Motor_Current_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_a = models.CharField(db_column='Motor_PowerKW_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_b = models.CharField(db_column='Motor_PowerKW_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_a = models.CharField(db_column='Bucket_Elevator_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_b = models.CharField(db_column='Bucket_Elevator_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    osepa_current = models.CharField(db_column='OSEPA_Current', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    osepa_rpm = models.CharField(db_column='OSEPA_RPM', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m1 = models.CharField(db_column='Bag_Colletcot_M1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m2 = models.CharField(db_column='Bag_Colletcot_M2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_s = models.CharField(db_column='Bag_Colletcot_S', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_a = models.CharField(db_column='TE_Mill_Bearing_In_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_a = models.CharField(db_column='TE_Mill_Bearing_Out_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_a = models.CharField(db_column='TE_Mill_Bearing_Oil_In_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_a = models.CharField(db_column='TE_Mill_Bearing_Oil_Out_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_b = models.CharField(db_column='TE_Mill_Bearing_In_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_b = models.CharField(db_column='TE_Mill_Bearing_Out_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_b = models.CharField(db_column='TE_Mill_Bearing_Oil_In_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_b = models.CharField(db_column='TE_Mill_Bearing_Oil_Out_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_a = models.CharField(db_column='TE_Mill_RAW_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_air_a = models.CharField(db_column='TE_Mill_Air_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_b = models.CharField(db_column='TE_Mill_RAW_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_air_b = models.CharField(db_column='TE_Mill_Air_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_s_in = models.CharField(db_column='TE_S_In', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_product = models.CharField(db_column='TE_Product', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_1_a = models.CharField(db_column='TE_Motor_1_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_2_a = models.CharField(db_column='TE_Motor_2_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_3_a = models.CharField(db_column='TE_Motor_3_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_4_a = models.CharField(db_column='TE_Motor_4_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_5_a = models.CharField(db_column='TE_Motor_5_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_6_a = models.CharField(db_column='TE_Motor_6_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_1_b = models.CharField(db_column='TE_Motor_1_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_2_b = models.CharField(db_column='TE_Motor_2_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_3_b = models.CharField(db_column='TE_Motor_3_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_4_b = models.CharField(db_column='TE_Motor_4_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_5_b = models.CharField(db_column='TE_Motor_5_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_motor_6_b = models.CharField(db_column='TE_Motor_6_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_mill_a = models.CharField(db_column='WP_Mill_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_mill_b = models.CharField(db_column='WP_Mill_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_osepa = models.CharField(db_column='WP_OSEPA', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_in = models.CharField(db_column='WP_BC_S_IN', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_diff = models.CharField(db_column='WP_BC_S_Diff', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m1 = models.CharField(db_column='RPM_BC_M1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m2 = models.CharField(db_column='RPM_BC_M2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rpm_bc_s = models.CharField(db_column='RPM_BC_S', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_m1 = models.CharField(db_column='OP_BC_M1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_m2 = models.CharField(db_column='OP_BC_M2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_s = models.CharField(db_column='OP_BC_S', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_a_p = models.CharField(db_column='W_M1_A_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_a_c = models.CharField(db_column='W_M1_A_C', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_a_c2 = models.CharField(db_column='W_M1_A_C2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_a_q = models.CharField(db_column='W_M1_A_Q', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_b_p = models.CharField(db_column='W_M1_B_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_b_c = models.CharField(db_column='W_M1_B_C', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_b_c2 = models.CharField(db_column='W_M1_B_C2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_b_q = models.CharField(db_column='W_M1_B_Q', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_a_p = models.CharField(db_column='W_M2_A_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_a_c = models.CharField(db_column='W_M2_A_C', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_a_c2 = models.CharField(db_column='W_M2_A_C2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_a_q = models.CharField(db_column='W_M2_A_Q', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_b_p = models.CharField(db_column='W_M2_B_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_b_c = models.CharField(db_column='W_M2_B_C', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_b_c2 = models.CharField(db_column='W_M2_B_C2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_b_q = models.CharField(db_column='W_M2_B_Q', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Milling_Machine_Mapping'
        unique_together = (('factoryid', 'mill_id'),)


class GMillingMachineMin(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime')  # Field name made lowercase.
    motor_current_a = models.DecimalField(db_column='Motor_Current_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_current_b = models.DecimalField(db_column='Motor_Current_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_a = models.DecimalField(db_column='Motor_PowerKW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_b = models.DecimalField(db_column='Motor_PowerKW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_a = models.DecimalField(db_column='Bucket_Elevator_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_b = models.DecimalField(db_column='Bucket_Elevator_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_current = models.DecimalField(db_column='OSEPA_Current', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_rpm = models.DecimalField(db_column='OSEPA_RPM', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m1 = models.DecimalField(db_column='Bag_Colletcot_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m2 = models.DecimalField(db_column='Bag_Colletcot_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_s = models.DecimalField(db_column='Bag_Colletcot_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_a = models.DecimalField(db_column='TE_Mill_Bearing_In_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_a = models.DecimalField(db_column='TE_Mill_Bearing_Out_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_a = models.DecimalField(db_column='TE_Mill_Bearing_Oil_In_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_a = models.DecimalField(db_column='TE_Mill_Bearing_Oil_Out_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_in_b = models.DecimalField(db_column='TE_Mill_Bearing_In_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_out_b = models.DecimalField(db_column='TE_Mill_Bearing_Out_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_in_b = models.DecimalField(db_column='TE_Mill_Bearing_Oil_In_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_bearing_oil_out_b = models.DecimalField(db_column='TE_Mill_Bearing_Oil_Out_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_a = models.DecimalField(db_column='TE_Mill_RAW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_a = models.DecimalField(db_column='TE_Mill_Air_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_b = models.DecimalField(db_column='TE_Mill_RAW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_b = models.DecimalField(db_column='TE_Mill_Air_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_s_in = models.DecimalField(db_column='TE_S_In', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_product = models.DecimalField(db_column='TE_Product', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_1_a = models.DecimalField(db_column='TE_Motor_1_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_2_a = models.DecimalField(db_column='TE_Motor_2_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_3_a = models.DecimalField(db_column='TE_Motor_3_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_4_a = models.DecimalField(db_column='TE_Motor_4_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_5_a = models.DecimalField(db_column='TE_Motor_5_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_6_a = models.DecimalField(db_column='TE_Motor_6_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_1_b = models.DecimalField(db_column='TE_Motor_1_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_2_b = models.DecimalField(db_column='TE_Motor_2_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_3_b = models.DecimalField(db_column='TE_Motor_3_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_4_b = models.DecimalField(db_column='TE_Motor_4_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_5_b = models.DecimalField(db_column='TE_Motor_5_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_motor_6_b = models.DecimalField(db_column='TE_Motor_6_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_a = models.DecimalField(db_column='WP_Mill_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_b = models.DecimalField(db_column='WP_Mill_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_osepa = models.DecimalField(db_column='WP_OSEPA', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_in = models.DecimalField(db_column='WP_BC_S_IN', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_diff = models.DecimalField(db_column='WP_BC_S_Diff', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m1 = models.DecimalField(db_column='RPM_BC_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_m2 = models.DecimalField(db_column='RPM_BC_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rpm_bc_s = models.DecimalField(db_column='RPM_BC_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m1 = models.DecimalField(db_column='OP_BC_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m2 = models.DecimalField(db_column='OP_BC_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_s = models.DecimalField(db_column='OP_BC_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_p = models.DecimalField(db_column='W_M1_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_c = models.DecimalField(db_column='W_M1_A_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_q = models.DecimalField(db_column='W_M1_A_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_p = models.DecimalField(db_column='W_M1_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_c = models.DecimalField(db_column='W_M1_B_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_q = models.DecimalField(db_column='W_M1_B_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_p = models.DecimalField(db_column='W_M2_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_c = models.DecimalField(db_column='W_M2_A_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_q = models.DecimalField(db_column='W_M2_A_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_p = models.DecimalField(db_column='W_M2_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_c = models.DecimalField(db_column='W_M2_B_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_q = models.DecimalField(db_column='W_M2_B_Q', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Milling_Machine_Min'
        unique_together = (('factoryid', 'mill_id', 'datatime'),)


class GMillingPMachine(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    dtime = models.IntegerField(db_column='DTime')  # Field name made lowercase.
    datatime = models.DateTimeField(db_column='DataTime')  # Field name made lowercase.
    motor_powerkw_a = models.DecimalField(db_column='Motor_PowerKW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_b = models.DecimalField(db_column='Motor_PowerKW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_a = models.DecimalField(db_column='Bucket_Elevator_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_current = models.DecimalField(db_column='OSEPA_Current', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    osepa_rpm = models.DecimalField(db_column='OSEPA_RPM', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m1 = models.DecimalField(db_column='Bag_Colletcot_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m2 = models.DecimalField(db_column='Bag_Colletcot_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_s = models.DecimalField(db_column='Bag_Colletcot_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_a = models.DecimalField(db_column='TE_Mill_Air_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_a = models.DecimalField(db_column='TE_Mill_RAW_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_air_b = models.DecimalField(db_column='TE_Mill_Air_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_b = models.DecimalField(db_column='TE_Mill_RAW_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    te_s_in = models.DecimalField(db_column='TE_S_In', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_a = models.DecimalField(db_column='WP_Mill_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_mill_b = models.DecimalField(db_column='WP_Mill_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_osepa = models.DecimalField(db_column='WP_OSEPA', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_in = models.DecimalField(db_column='WP_BC_S_IN', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_diff = models.DecimalField(db_column='WP_BC_S_DIFF', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m1 = models.DecimalField(db_column='OP_BC_M1', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_m2 = models.DecimalField(db_column='OP_BC_M2', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    op_bc_s = models.DecimalField(db_column='OP_BC_S', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_a_p = models.DecimalField(db_column='W_M1_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m1_b_p = models.DecimalField(db_column='W_M1_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_a_p = models.DecimalField(db_column='W_M2_A_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    w_m2_b_p = models.DecimalField(db_column='W_M2_B_P', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Milling_P_Machine'
        unique_together = (('factoryid', 'mill_id', 'ddate', 'datatime'),)


class GMillingPMap(models.Model):
    factoryid = models.CharField(db_column='FactoryID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    motor_powerkw_a = models.CharField(db_column='Motor_PowerKW_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    motor_powerkw_b = models.CharField(db_column='Motor_PowerKW_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bucket_elevator_a = models.CharField(db_column='Bucket_Elevator_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    osepa_current = models.CharField(db_column='OSEPA_Current', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    osepa_rpm = models.CharField(db_column='OSEPA_RPM', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m1 = models.CharField(db_column='Bag_Colletcot_M1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_m2 = models.CharField(db_column='Bag_Colletcot_M2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bag_colletcot_s = models.CharField(db_column='Bag_Colletcot_S', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_air_a = models.CharField(db_column='TE_Mill_Air_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_a = models.CharField(db_column='TE_Mill_RAW_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_air_b = models.CharField(db_column='TE_Mill_Air_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_mill_raw_b = models.CharField(db_column='TE_Mill_RAW_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    te_s_in = models.CharField(db_column='TE_S_In', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_mill_a = models.CharField(db_column='WP_Mill_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_mill_b = models.CharField(db_column='WP_Mill_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_osepa = models.CharField(db_column='WP_OSEPA', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_in = models.CharField(db_column='WP_BC_S_IN', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    wp_bc_s_diff = models.CharField(db_column='WP_BC_S_DIFF', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_m1 = models.CharField(db_column='OP_BC_M1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_m2 = models.CharField(db_column='OP_BC_M2', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    op_bc_s = models.CharField(db_column='OP_BC_S', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_a_p = models.CharField(db_column='W_M1_A_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m1_b_p = models.CharField(db_column='W_M1_B_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_a_p = models.CharField(db_column='W_M2_A_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    w_m2_b_p = models.CharField(db_column='W_M2_B_P', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Milling_P_Map'


class GPower(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    getdatetime = models.DateTimeField(db_column='GetDateTime', blank=True, null=True)  # Field name made lowercase.
    power_kwh_total = models.DecimalField(db_column='Power_KWH_Total', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_a = models.DecimalField(db_column='Power_KWH_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_b = models.DecimalField(db_column='Power_KWH_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_c = models.DecimalField(db_column='Power_KWH_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_01 = models.DecimalField(db_column='Power_KWH_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_02 = models.DecimalField(db_column='Power_KWH_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_03 = models.DecimalField(db_column='Power_KWH_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_04 = models.DecimalField(db_column='Power_KWH_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_05 = models.DecimalField(db_column='Power_KWH_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_06 = models.DecimalField(db_column='Power_KWH_06', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_07 = models.DecimalField(db_column='Power_KWH_07', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_kwh_08 = models.DecimalField(db_column='Power_KWH_08', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_total = models.DecimalField(db_column='Power_C_Total', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_a = models.DecimalField(db_column='Power_C_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_b = models.DecimalField(db_column='Power_C_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_c = models.DecimalField(db_column='Power_C_C', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_06 = models.DecimalField(db_column='Power_C_06', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_07 = models.DecimalField(db_column='Power_C_07', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_c_08 = models.DecimalField(db_column='Power_C_08', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power'
        unique_together = (('factoryid', 'datadate'),)


class GPowerBill(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    mid = models.CharField(db_column='MID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    getdatetime = models.DateTimeField(db_column='GetDateTime', blank=True, null=True)  # Field name made lowercase.
    power_kwh = models.DecimalField(db_column='Power_KWH', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_peak = models.DecimalField(db_column='Power_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_half_peak = models.DecimalField(db_column='Power_Half_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    power_off_peak = models.DecimalField(db_column='Power_Off_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bill_total = models.DecimalField(db_column='Bill_Total', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bill_peak = models.DecimalField(db_column='Bill_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bill_half_peak = models.DecimalField(db_column='Bill_Half_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    bill_off_peak = models.DecimalField(db_column='Bill_Off_Peak', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_Bill'
        unique_together = (('factoryid', 'datadate', 'mid'),)


class GPowerCalender(models.Model):
    p_year = models.CharField(db_column='P_Year', max_length=4, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    p_date = models.DateField(db_column='P_Date', primary_key=True)  # Field name made lowercase.
    p_weekday = models.CharField(db_column='P_WeekDay', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    off_peak = models.BooleanField(db_column='Off_Peak', blank=True, null=True)  # Field name made lowercase.
    half_peak = models.BooleanField(db_column='Half_Peak', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_Calender'


class GPowerD(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    power_kwh_total = models.DecimalField(db_column='Power_KWH_Total', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_a = models.DecimalField(db_column='Power_KWH_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_b = models.DecimalField(db_column='Power_KWH_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_c = models.DecimalField(db_column='Power_KWH_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_01 = models.DecimalField(db_column='Power_KWH_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_02 = models.DecimalField(db_column='Power_KWH_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_03 = models.DecimalField(db_column='Power_KWH_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_04 = models.DecimalField(db_column='Power_KWH_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_05 = models.DecimalField(db_column='Power_KWH_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_06 = models.DecimalField(db_column='Power_KWH_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_07 = models.DecimalField(db_column='Power_KWH_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_08 = models.DecimalField(db_column='Power_KWH_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_total = models.DecimalField(db_column='Power_C_Total', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_a = models.DecimalField(db_column='Power_C_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_b = models.DecimalField(db_column='Power_C_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_c = models.DecimalField(db_column='Power_C_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_06 = models.DecimalField(db_column='Power_C_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_07 = models.DecimalField(db_column='Power_C_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_08 = models.DecimalField(db_column='Power_C_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_D'
        unique_together = (('factoryid', 'datadate'),)


class GPowerH1(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    timekey = models.CharField(db_column='TimeKey', max_length=14, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    stime = models.DateTimeField(db_column='STime')  # Field name made lowercase.
    etime = models.DateTimeField(db_column='ETime')  # Field name made lowercase.
    power_kwh = models.DecimalField(db_column='Power_KWH', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kwh = models.DecimalField(db_column='KWH', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    peak = models.DecimalField(db_column='Peak', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    partial_peak = models.DecimalField(db_column='Partial_Peak', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    partial_peak_sat = models.DecimalField(db_column='Partial_Peak_SAT', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    off_peak = models.DecimalField(db_column='Off_Peak', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_H1'
        unique_together = (('factoryid', 'timekey'),)


class GPowerM(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dmonth = models.CharField(db_column='DMonth', max_length=6, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    power_kwh_total = models.DecimalField(db_column='Power_KWH_Total', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_a = models.DecimalField(db_column='Power_KWH_A', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_b = models.DecimalField(db_column='Power_KWH_B', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_c = models.DecimalField(db_column='Power_KWH_C', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_01 = models.DecimalField(db_column='Power_KWH_01', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_02 = models.DecimalField(db_column='Power_KWH_02', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_03 = models.DecimalField(db_column='Power_KWH_03', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_04 = models.DecimalField(db_column='Power_KWH_04', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_05 = models.DecimalField(db_column='Power_KWH_05', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_06 = models.DecimalField(db_column='Power_KWH_06', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_07 = models.DecimalField(db_column='Power_KWH_07', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_kwh_08 = models.DecimalField(db_column='Power_KWH_08', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_total = models.DecimalField(db_column='Power_C_Total', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_a = models.DecimalField(db_column='Power_C_A', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_b = models.DecimalField(db_column='Power_C_B', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_c = models.DecimalField(db_column='Power_C_C', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_06 = models.DecimalField(db_column='Power_C_06', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_07 = models.DecimalField(db_column='Power_C_07', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    power_c_08 = models.DecimalField(db_column='Power_C_08', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    worktime_01 = models.DecimalField(db_column='WorkTime_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_02 = models.DecimalField(db_column='WorkTime_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_03 = models.DecimalField(db_column='WorkTime_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_04 = models.DecimalField(db_column='WorkTime_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_05 = models.DecimalField(db_column='WorkTime_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_06 = models.DecimalField(db_column='WorkTime_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_07 = models.DecimalField(db_column='WorkTime_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    worktime_08 = models.DecimalField(db_column='WorkTime_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_M'
        unique_together = (('factoryid', 'dmonth'),)


class GPowerMapping(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    power_kwh_total = models.CharField(db_column='Power_KWH_Total', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_total1 = models.CharField(db_column='Power_KWH_Total1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_a = models.CharField(db_column='Power_KWH_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_a1 = models.CharField(db_column='Power_KWH_A1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_b = models.CharField(db_column='Power_KWH_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_b1 = models.CharField(db_column='Power_KWH_B1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_c = models.CharField(db_column='Power_KWH_C', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_c1 = models.CharField(db_column='Power_KWH_C1', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_01 = models.CharField(db_column='Power_KWH_01', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_011 = models.CharField(db_column='Power_KWH_011', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_02 = models.CharField(db_column='Power_KWH_02', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_021 = models.CharField(db_column='Power_KWH_021', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_03 = models.CharField(db_column='Power_KWH_03', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_031 = models.CharField(db_column='Power_KWH_031', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_04 = models.CharField(db_column='Power_KWH_04', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_041 = models.CharField(db_column='Power_KWH_041', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_05 = models.CharField(db_column='Power_KWH_05', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_051 = models.CharField(db_column='Power_KWH_051', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_06 = models.CharField(db_column='Power_KWH_06', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_061 = models.CharField(db_column='Power_KWH_061', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_07 = models.CharField(db_column='Power_KWH_07', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_071 = models.CharField(db_column='Power_KWH_071', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_08 = models.CharField(db_column='Power_KWH_08', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    power_kwh_081 = models.CharField(db_column='Power_KWH_081', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dnote = models.CharField(db_column='DNOTE', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_Mapping'


class GPowerPeakDate(models.Model):
    peak_date = models.DateField(db_column='Peak_Date', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_Peak_Date'


class GPowerH(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    power_kwh_total = models.DecimalField(db_column='Power_KWH_Total', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_a = models.DecimalField(db_column='Power_KWH_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_b = models.DecimalField(db_column='Power_KWH_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_c = models.DecimalField(db_column='Power_KWH_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_01 = models.DecimalField(db_column='Power_KWH_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_02 = models.DecimalField(db_column='Power_KWH_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_03 = models.DecimalField(db_column='Power_KWH_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_04 = models.DecimalField(db_column='Power_KWH_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_05 = models.DecimalField(db_column='Power_KWH_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_06 = models.DecimalField(db_column='Power_KWH_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_07 = models.DecimalField(db_column='Power_KWH_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_kwh_08 = models.DecimalField(db_column='Power_KWH_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_total = models.DecimalField(db_column='Power_C_Total', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_a = models.DecimalField(db_column='Power_C_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_b = models.DecimalField(db_column='Power_C_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_c = models.DecimalField(db_column='Power_C_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_01 = models.DecimalField(db_column='Power_C_01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_02 = models.DecimalField(db_column='Power_C_02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_03 = models.DecimalField(db_column='Power_C_03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_04 = models.DecimalField(db_column='Power_C_04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_05 = models.DecimalField(db_column='Power_C_05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_06 = models.DecimalField(db_column='Power_C_06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_07 = models.DecimalField(db_column='Power_C_07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    power_c_08 = models.DecimalField(db_column='Power_C_08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Power_h'
        unique_together = (('factoryid', 'datadate', 'dtime'),)


class GSe(models.Model):
    se_id = models.CharField(db_column='SE_ID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    factoryid = models.CharField(db_column='FactoryID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    build_volume_kwh = models.DecimalField(db_column='Build_Volume_kwh', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_SE'


class GSeD(models.Model):
    se_id = models.CharField(db_column='SE_ID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    power_generation = models.DecimalField(db_column='Power_Generation', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lost_power = models.IntegerField(db_column='Lost_Power', blank=True, null=True)  # Field name made lowercase.
    kwh_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'G_SE_D'
        unique_together = (('se_id', 'ddate'),)


class GSeH(models.Model):
    se_id = models.CharField(db_column='SE_ID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    power_generation = models.DecimalField(db_column='Power_Generation', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    kwh_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'G_SE_H'
        unique_together = (('se_id', 'dtime'),)


class GSeM(models.Model):
    se_id = models.CharField(db_column='SE_ID', primary_key=True, max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    ddate = models.DateField(db_column='DDate')  # Field name made lowercase.
    power_generation = models.DecimalField(db_column='Power_Generation', max_digits=18, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    lost_power = models.IntegerField(db_column='Lost_Power', blank=True, null=True)  # Field name made lowercase.
    kwh_avg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'G_SE_M'
        unique_together = (('se_id', 'ddate'),)


class GTpc(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    electricity_period = models.CharField(db_column='Electricity_period', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    power_kw = models.IntegerField(db_column='Power_KW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_TPC'
        unique_together = (('factoryid', 'dtime', 'electricity_period'),)


class GTpcD(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateField(db_column='DTime')  # Field name made lowercase.
    electricity_period = models.CharField(db_column='Electricity_period', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    power_kw = models.IntegerField(db_column='Power_KW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_TPC_D'
        unique_together = (('factoryid', 'dtime', 'electricity_period'),)


class GTpcH(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    electricity_period = models.CharField(db_column='Electricity_period', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    power_kw = models.IntegerField(db_column='Power_KW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_TPC_H'
        unique_together = (('factoryid', 'dtime', 'electricity_period'),)


class GTpcM(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dtime = models.DateField(db_column='DTime')  # Field name made lowercase.
    electricity_period = models.CharField(db_column='Electricity_period', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    power_kw = models.IntegerField(db_column='Power_KW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_TPC_M'
        unique_together = (('factoryid', 'dtime', 'electricity_period'),)


class GWeighingH(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    datadate = models.DateField(db_column='DataDate')  # Field name made lowercase.
    dtime = models.DateTimeField(db_column='DTime')  # Field name made lowercase.
    m01_a = models.DecimalField(db_column='M01_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m01_b = models.DecimalField(db_column='M01_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m02_a = models.DecimalField(db_column='M02_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m02_b = models.DecimalField(db_column='M02_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m03_a = models.DecimalField(db_column='M03_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m03_b = models.DecimalField(db_column='M03_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m04_a = models.DecimalField(db_column='M04_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m04_b = models.DecimalField(db_column='M04_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m05_a = models.DecimalField(db_column='M05_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m05_b = models.DecimalField(db_column='M05_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m06_a = models.DecimalField(db_column='M06_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m06_b = models.DecimalField(db_column='M06_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m07_a = models.DecimalField(db_column='M07_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m07_b = models.DecimalField(db_column='M07_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m08_a = models.DecimalField(db_column='M08_A', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m08_b = models.DecimalField(db_column='M08_B', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m01_a1_c = models.DecimalField(db_column='M01_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m01_b1_c = models.DecimalField(db_column='M01_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m02_a1_c = models.DecimalField(db_column='M02_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m02_b1_c = models.DecimalField(db_column='M02_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m03_a1_c = models.DecimalField(db_column='M03_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m03_b1_c = models.DecimalField(db_column='M03_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m04_a1_c = models.DecimalField(db_column='M04_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m04_b1_c = models.DecimalField(db_column='M04_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m05_a1_c = models.DecimalField(db_column='M05_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m05_b1_c = models.DecimalField(db_column='M05_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m06_a1_c = models.DecimalField(db_column='M06_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m06_b1_c = models.DecimalField(db_column='M06_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m07_a1_c = models.DecimalField(db_column='M07_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m07_b1_c = models.DecimalField(db_column='M07_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m08_a1_c = models.DecimalField(db_column='M08_A1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m08_b1_c = models.DecimalField(db_column='M08_B1_C', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m01 = models.DecimalField(db_column='M01', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m02 = models.DecimalField(db_column='M02', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m03 = models.DecimalField(db_column='M03', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m04 = models.DecimalField(db_column='M04', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m05 = models.DecimalField(db_column='M05', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m06 = models.DecimalField(db_column='M06', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m07 = models.DecimalField(db_column='M07', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    m08 = models.DecimalField(db_column='M08', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Weighing_H'
        unique_together = (('factoryid', 'datadate', 'dtime'),)


class GWeighingMapping(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    m01_a = models.CharField(db_column='M01_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m01_b = models.CharField(db_column='M01_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m02_a = models.CharField(db_column='M02_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m02_b = models.CharField(db_column='M02_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m03_a = models.CharField(db_column='M03_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m03_b = models.CharField(db_column='M03_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m04_a = models.CharField(db_column='M04_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m04_b = models.CharField(db_column='M04_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m05_a = models.CharField(db_column='M05_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m05_b = models.CharField(db_column='M05_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m06_a = models.CharField(db_column='M06_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m06_b = models.CharField(db_column='M06_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m07_a = models.CharField(db_column='M07_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m07_b = models.CharField(db_column='M07_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m08_a = models.CharField(db_column='M08_A', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    m08_b = models.CharField(db_column='M08_B', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'G_Weighing_Mapping'


class Logerrormsg(models.Model):
    ddtime = models.DateTimeField(db_column='DDtime', primary_key=True)  # Field name made lowercase.
    msglog = models.CharField(db_column='MsgLog', max_length=1000, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=1000, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ischeck = models.BooleanField(db_column='IsCheck', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LogErrorMsg'


class OccDespatch(models.Model):
    work_id = models.CharField(db_column='WORK_ID', primary_key=True, max_length=11, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    dept_id = models.CharField(db_column='DEPT_ID', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    o_date = models.DateField(db_column='O_DATE', blank=True, null=True)  # Field name made lowercase.
    car_id = models.CharField(db_column='CAR_ID', max_length=8, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    order_id1 = models.CharField(db_column='ORDER_ID1', max_length=11, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=11, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cust_name = models.CharField(db_column='CUST_NAME', max_length=40, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    prod_id = models.CharField(db_column='PROD_ID', max_length=2, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    gross = models.DecimalField(db_column='GROSS', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    delivery = models.DecimalField(db_column='DELIVERY', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    tare = models.DecimalField(db_column='TARE', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    deli_wt = models.DecimalField(db_column='DELI_WT', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    i_time = models.CharField(db_column='I_TIME', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    o_time = models.CharField(db_column='O_TIME', max_length=15, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    scale_no = models.CharField(db_column='SCALE_NO', max_length=1, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    package = models.CharField(db_column='PACKAGE', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    print_sn = models.CharField(db_column='PRINT_SN', max_length=7, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OCC_Despatch'


class RMonthCondition(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    osepa_min = models.IntegerField(db_column='OSEPA_Min', blank=True, null=True)  # Field name made lowercase.
    osepa_max = models.IntegerField(db_column='OSEPA_Max', blank=True, null=True)  # Field name made lowercase.
    weight_min = models.IntegerField(db_column='Weight_Min', blank=True, null=True)  # Field name made lowercase.
    weight_max = models.IntegerField(db_column='Weight_Max', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_Month_Condition'
        unique_together = (('factoryid', 'mill_id', 'product'),)


class RMonthReoprt(models.Model):
    factoryid = models.CharField(db_column='FactoryID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    month = models.DateField(db_column='Month')  # Field name made lowercase.
    mill_id = models.CharField(db_column='Mill_ID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    product = models.CharField(db_column='Product', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    production_total_a = models.DecimalField(db_column='Production_Total_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    production_hour_a = models.DecimalField(db_column='Production_Hour_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    run_hour_a = models.DecimalField(db_column='Run_Hour_A', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    production_total_b = models.DecimalField(db_column='Production_Total_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    production_hour_b = models.DecimalField(db_column='Production_Hour_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    run_hour_b = models.DecimalField(db_column='Run_Hour_B', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R_Month_Reoprt'
        unique_together = (('factoryid', 'month', 'mill_id', 'product'),)


class Taglist(models.Model):
    servername = models.CharField(db_column='ServerName', primary_key=True, max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    sourcetag = models.CharField(db_column='SourceTag', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tagdesc = models.CharField(db_column='TagDesc', max_length=200, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rep_live = models.BooleanField(db_column='Rep_Live', blank=True, null=True)  # Field name made lowercase.
    rep_hour = models.BooleanField(db_column='Rep_Hour', blank=True, null=True)  # Field name made lowercase.
    rep_min = models.BooleanField(db_column='Rep_Min', blank=True, null=True)  # Field name made lowercase.
    tag_order = models.DecimalField(db_column='Tag_Order', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TagList'
        unique_together = (('servername', 'tagname'),)


class TagNameDesc(models.Model):
    tag_group = models.CharField(db_column='Tag_Group', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tag_mid = models.CharField(db_column='Tag_MID', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tag_sort = models.IntegerField(db_column='Tag_Sort')  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    sourcetag = models.CharField(db_column='SourceTag', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tag_desc = models.CharField(db_column='Tag_Desc', max_length=200, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tag_Name_Desc'
        unique_together = (('tag_group', 'servername', 'tagname', 'sourcetag'),)


class TagGroup(models.Model):
    group_id = models.CharField(db_column='Group_ID', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    group_desc = models.CharField(db_column='Group_DESC', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    group_sort = models.IntegerField(db_column='Group_Sort')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tag_group'


class ValueDaily(models.Model):
    datadatetime = models.DateTimeField(db_column='DataDateTime', primary_key=True)  # Field name made lowercase.
    servername = models.CharField(db_column='ServerName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Value_Daily'
        unique_together = (('datadatetime', 'servername', 'tagname'),)


class ValueHour(models.Model):
    datadatetime = models.DateTimeField(db_column='DataDateTime', primary_key=True)  # Field name made lowercase.
    sourceserver = models.CharField(db_column='SourceServer', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Value_Hour'
        unique_together = (('datadatetime', 'sourceserver', 'tagname'),)


class ValueMin(models.Model):
    datadatetime = models.DateTimeField(db_column='DataDateTime', primary_key=True)  # Field name made lowercase.
    sourceserver = models.CharField(db_column='SourceServer', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    tagname = models.CharField(db_column='TagName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=18, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Value_Min'
        unique_together = (('datadatetime', 'sourceserver', 'tagname'),)


class WLoginGroup(models.Model):
    groupid = models.AutoField(db_column='GroupId', primary_key=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Login_Group'


class WLoginGroupright(models.Model):
    group_id = models.AutoField(db_column='Group_ID', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    factoryid = models.CharField(db_column='FactoryID', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subid = models.CharField(db_column='SubID', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    right_id = models.IntegerField(db_column='Right_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Login_GroupRight'


class WLoginLogfile(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    time = models.DateTimeField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    detail = models.TextField(db_column='Detail', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Login_Logfile'


class WLoginRight(models.Model):
    right_id = models.IntegerField(db_column='Right_ID', primary_key=True)  # Field name made lowercase.
    right_name = models.CharField(db_column='Right_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Login_Right'


class WLoginUser(models.Model):
    user_id = models.AutoField(db_column='User_ID', primary_key=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='User_Name', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    factory_id = models.CharField(db_column='Factory_ID', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    create_time = models.DateTimeField(db_column='Create_Time', blank=True, null=True)  # Field name made lowercase.
    stop_time = models.DateTimeField(db_column='Stop_Time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Login_User'


class WSubPage(models.Model):
    num = models.AutoField(primary_key=True)
    subid = models.CharField(db_column='SubId', max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    subname = models.CharField(db_column='SubName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    suburl = models.TextField(db_column='SubUrl', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State')  # Field name made lowercase.
    webid = models.ForeignKey('WWebPage', models.DO_NOTHING, db_column='WebId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Sub_Page'


class WWebPage(models.Model):
    webid = models.CharField(db_column='WebID', primary_key=True, max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    webname = models.CharField(db_column='WebName', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    weburl = models.TextField(db_column='WebUrl', db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    orderbyid = models.IntegerField(db_column='OrderById', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'W_Web_Page'

class WeatherDay(models.Model):
    datadate = models.DateField(db_column='DataDate', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    uv = models.IntegerField(db_column='UV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Weather_Day'
        unique_together = (('datadate', 'area'),)


class WeatherHour(models.Model):
    dtime = models.DateTimeField(db_column='DTime', primary_key=True)  # Field name made lowercase.
    area = models.CharField(db_column='Area', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')  # Field name made lowercase.
    uv = models.IntegerField(db_column='UV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Weather_Hour'
        unique_together = (('dtime', 'area'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Chinese_Taiwan_Stroke_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    email = models.CharField(max_length=254, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    model = models.CharField(max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    name = models.CharField(max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    session_data = models.TextField(db_collation='Chinese_Taiwan_Stroke_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LocalhostCpuRam(models.Model):
    dtime = models.DateTimeField(db_column='Dtime', primary_key=True)  # Field name made lowercase.
    cpu = models.FloatField(db_column='CPU', blank=True, null=True)  # Field name made lowercase.
    ram = models.FloatField(db_column='RAM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localhost_CPU_RAM'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
