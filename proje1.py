import calendar

def sekil_cizdirme():
    print("╔════════════════════════════╗")
    print("║       ŞEKİL ÇİZDİRME       ║")
    print("╚════════════════════════════╝")
    yukseklik = int(input("Üçgenin yüksekliği: "))
    for i in range(1, yukseklik + 1):
        print(" " * (yukseklik - i) + "*" * (2 * i - 1))
    print()


def takvim_goster():
    print("╔════════════════════════════╗")
    print("║           TAKVİM           ║")
    print("╚════════════════════════════╝")
    yil = int(input("Yılı girin: "))
    ay = int(input("Ayı girin (1-12): "))
    print()
    print(calendar.month(yil, ay))


def carpim_tablosu():
    print("╔════════════════════════════╗")
    print("║       ÇARPIM TABLOSU       ║")
    print("╚════════════════════════════╝")
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end=" ")
        print()
    print()


def ritmik_sayma():
    print("╔════════════════════════════╗")
    print("║        RİTMİK SAYMA        ║")
    print("╚════════════════════════════╝")
    adim = int(input("Kaçar kaçar saysın?: "))
    hedef = int(input("Nereye kadar?: "))
    for i in range(0, hedef + 1, adim):
        print(i, end=" ")
    print("\n")


def oyunlar_menusu():
    while True:
        print("╔════════════════════════════╗")
        print("║         OYUNLAR            ║")
        print("╠════════════════════════════╣")
        print("║ 1- MARIO                   ║")
        print("║ 2- YILAN OYUNU             ║")
        print("║ 3- ADAM ASMACA             ║")
        print("║ 4- GERİ DÖN                ║")
        print("╚════════════════════════════╝")
        secim = input("Seçiminiz: ")

        if secim == "1":
            print("🏃‍♂️ Mario zıplıyor!  🍄\n")
        elif secim == "2":
            print("🐍 Yılan oyunu çalıştı... \n")
        elif secim == "3":
            print("🪢 Adam Asmaca hazırlanıyor...\n")
        elif secim == "4":
            print(">> Ana menüye dönülüyor...\n")
            break
        else:
            print(">> Geçersiz seçim! Tekrar dene.\n")


def menu():
    print("╔════════════════════════════╗")
    print("║      PYTHON ÇALIŞMALARI    ║")
    print("╠════════════════════════════╣")
    print("║ 1- HESAP MAKİNESİ          ║")
    print("║ 2- OYUNLAR                 ║")
    print("║ 3- ŞEKİL ÇİZDİRME          ║")
    print("║ 4- TAKVİM                  ║")
    print("║ 5- RİTMİK SAYMA            ║")
    print("║ 6- NOT HESAPLAMA           ║")
    print("║ 7- ÇARPIM TABLOSU          ║")
    print("║ 8- BMI HESAPLAMA           ║")
    print("║ 9- DÖVİZ UYGULAMASI        ║")
    print("║10- SICAKLIK ÇEVİRME        ║")
    print("║11- ÇIKIŞ (e)               ║")
    print("╚════════════════════════════╝")
    secim = input("Seçimini yap: ")
    return secim


# Ana döngü
while True:
    secilen = menu()

    if secilen == "1":
        print(">> HESAP MAKİNESİ açılıyor...\n")
    elif secilen == "2":
        oyunlar_menusu()
    elif secilen == "3":
        sekil_cizdirme()
    elif secilen == "4":
        takvim_goster()
    elif secilen == "5":
        ritmik_sayma()
    elif secilen == "6":
        print(">> NOT HESAPLAMA başlatılıyor...\n")
    elif secilen == "7":
        carpim_tablosu()
    elif secilen == "8":
        print(">> BMI HESAPLAMA başlatılıyor...\n")
    elif secilen == "9":
        print(">> DÖVİZ UYGULAMASI başlatılıyor...\n")
    elif secilen == "10":
        print(">> SICAKLIK ÇEVİRME başlatılıyor...\n")
    elif secilen.lower() == "e" or secilen == "11":
        print(">> ÇIKIŞ yapılıyor, kendine iyi bak 👋")
        break
    else:
        print(">> Geçersiz seçim! Tekrar dene.\n")
