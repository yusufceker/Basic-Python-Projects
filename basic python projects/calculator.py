secim = int(input( "Yapacağınız işlemi seçiniz\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme: "))

sayı1 = int(input("1. sayıyı  giriniz: "))
sayı2 = int(input("2. sayıyı  giriniz: "))


if secim == 1:
    print("Sonuc: {}".format(sayı1 + sayı2))
elif secim == 2:
    print("Sonuc: {}".format(sayı1 - sayı2))
elif secim == 3:
    print("Sonuc: {}".format(sayı1 * sayı2))
elif secim == 4:
    print("Sonuc: {}".format(sayı1 / sayı2))
else:
    print("Hatalı giriş yaptınız, lütfen tekrar deneyin")