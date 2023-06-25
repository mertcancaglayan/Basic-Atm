# Bankamatik Uygulaması





BlakeHesap = {
    'ad' : 'Blake Lively ',
    'hesapNo' : '123456',
    'bakiye' : 3000,
    'ekhesap' : 2000
}

MertHesap = {
    'ad' : 'Mert Can Çağlayan',
    'hesapNo' : '123457',
    'bakiye' : 2000,
    'ekhesap' : 1000
}

islem = input('Hoşgeldiniz \n Lütfen Yapmak İstediğiniz işlemi belirtiniz (Çek,Yatır) ')
if islem == 'Çek':

    def paraCek(hesap, miktar):

        print(f"Merhaba {hesap['ad']}")

        if hesap['bakiye'] >= miktar :
            hesap['bakiye'] -= miktar
            print('Paranızı alabilirsiniz')

        else:
            toplam = hesap['bakiye'] + hesap['ekhesap']

            if toplam >= miktar:
                ekHesapKullanimi = input('ek hesap kullanılsın mı? [e/h)')
                if ekHesapKullanimi == 'e':

                    ekhesapkullanılacakmiktar = miktar - hesap['bakiye']
                    hesap['bakiye'] = 0
                    hesap['ekhesap'] -= ekhesapkullanılacakmiktar
                    print('paranızı alın')
                else:
                    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} var.")   
            else:
                print(f"Bakiye yetersiz. Toplam bakiyeniz {toplam}")     


    def bakiyeSorgula(hesap):
        print(f"{hesap['hesapNo']} no lu hesabınızda {hesap['bakiye']} tl bulunmaktadır. ek hesap limitiniz ise {hesap['ekhesap']} tl bulunmaktadır")


    bakiyeSorgula(BlakeHesap)
    cekpara = int(input('lütfen çekmek istediğiniz miktarı giriniz: '))
    paraCek(BlakeHesap, cekpara)
    bakiyeSorgula(BlakeHesap)
    print('*************')
    cekpara2 = int(input('lütfen çekmek istediğiniz miktarı giriniz: '))
    paraCek(BlakeHesap, cekpara2)
    bakiyeSorgula(BlakeHesap)
elif islem == 'Yatır':
    def parayatir(hesap, miktar):
        print(f"Merhaba {hesap['ad']}")
        hesap['bakiye'] += miktar
        
        
    
    def bakiyeSorgula(hesap):
        print(f"{hesap['hesapNo']} no lu hesabınızda {hesap['bakiye']} tl bulunmaktadır. ek hesap limitiniz ise {hesap['ekhesap']} tl bulunmaktadır")
        
    yatırhesap = int(input('Lütfen yatırmak istediğiniz miktarı giriniz: '))
    
    parayatir(BlakeHesap, yatırhesap)
    bakiyeSorgula(BlakeHesap)
else:
    print('Bitti')