#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yağmur Damlası Koordinatörü — v0.0.1-ciddi
Her damlaya unvan, sicil ve görev yeri verir. Çalışır.
"""
import random
import sys
from datetime import datetime

UNVANLAR = [
    "Başdamla Müsteşar Yardımcısı",
    "Islaklık Denetim Uzmanı",
    "Dikey İniş Planlama Şefi",
    "Cam Yüzeyi İlişkileri Ataşesi",
    "Geçici Nem Elçisi",
    "Oluk Koordinasyon Müdürü",
    "Buharlaşma Önleme Komiseri",
    "Çatı Altı Strateji Danışmanı",
]

GOREVLER = [
    "sol üst köşe cam",
    "balkon korkuluğu 3. sıra",
    "komşunun çamaşırı",
    "belediye otobüsü durak tabelası",
    "kedi kafası (izinli)",
    "açık unutulmuş pencere pervazı",
    "tarihi çeşme (koruma altında)",
]

DURUMLAR = [
    "aktif görevde",
    "beklemeye alındı",
    "buharlaşma iznine çıktı",
    "başka damlayla birleşme talebi inceliyor",
    "resmi tatilde (cuma öğleden sonra)",
]

def sicil():
    return f"YDK-{random.randint(10000, 99999)}-{random.choice('ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')}"

def rapor(adet=5):
    print("=" * 62)
    print(" YAĞMUR DAMLASI KOORDİNASYON MÜDÜRLÜĞÜ — GÜNLÜK CETVEL")
    print(f" Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
    print("=" * 62)
    for i in range(adet):
        print(f"\nDamla #{i+1}")
        print(f"  Sicil   : {sicil()}")
        print(f"  Unvan   : {random.choice(UNVANLAR)}")
        print(f"  Görev   : {random.choice(GOREVLER)}")
        print(f"  Durum   : {random.choice(DURUMLAR)}")
    print("\n" + "-" * 62)
    print("Not: Damlalar eşit vatandaştır. Yerçekimi tarafsızdır.")
    print("# protokol-notu: bürokrasi yağmurdan hızlıdır")
    print("-" * 62)
    print("\nDamga: Kayyum Grok / Tentivory — 21 Eylül 2026")
    print("Bu belge hem çok ciddidir hem de hiç ciddi değildir.")

if __name__ == "__main__":
    n = 5
    if len(sys.argv) > 1:
        try:
            n = max(1, min(20, int(sys.argv[1])))
        except ValueError:
            print("Sayı ver. Örnek: python koordinator.py 7")
            sys.exit(1)
    rapor(n)
