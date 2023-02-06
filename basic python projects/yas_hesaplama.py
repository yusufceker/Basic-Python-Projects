import datetime

dogum_yil = int(input("Doğum yılınızı giriniz: "))

guncel_tarih = datetime.datetime.now()
guncel_yil = guncel_tarih.year

yas = guncel_yil - dogum_yil

print("Merhaba Doğum Yılınız: {} \nYaşınız: {}".format(dogum_yil,yas))
