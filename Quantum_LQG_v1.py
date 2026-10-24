# LQG - Loop Quantum Gravity
# Kvantna gravitacija petlje

# Quantum_LQG_Spinfoam V1
# Quantum_LQG_Kvantizacija V2
# Quantum_LQG_Gaus V3 V3B
# Quantum_LQG_Ensemble V4


# V1 - Istorija izvlačenja kao "Pena spinova" (Spinfoam) 
# V2 - Kvantizacija površine i jačina veza (Spin Surfaces)  
# V3 - Gausov zakon i uslov zatvorenosti (Intertwiner Balance) 
# V3B - Dublja analiza zakona očuvanja (Multi-Dimensional Intertwiners) 
# V4 - Hibridni indeks (Ensemble Score)


# trostepeno mapiranje Kvantne gravitacije petlji (LQG) na diskretni prostor lotoa 



import numpy as np
import pandas as pd


# 1. DEFINISANJE PUTANJE DO BAZE
# PUTANJA_DO_BAZE = "/data/loto7_4708_k85.csv"
# PUTANJA_DO_BAZE = "/data/loto7_4708_k85_loto_2976.csv"
PUTANJA_DO_BAZE = "/data/loto7_4708_k85_loto_plus_1732.csv"


def generisi_next_predikciju_v1(putanja_csv):
    # Učitavanje baze
    df = pd.read_csv(putanja_csv)
    
    # Automatska detekcija 7 kolona koje sadrže loto brojeve
    # Traži kolone koje imaju numeričke vrednosti u opsegu 1-39
    kolone_brojeva = []
    for col in df.columns:
        # Ako kolona sadrži brojeve i bar neka vrednost je u opsegu lotoa
        if pd.api.types.is_numeric_dtype(df[col]):
            if df[col].max() <= 39 and df[col].min() >= 1:
                kolone_brojeva.append(col)
                
    # Osiguravam da imam tačno 7 kolona, ako ih ima više uzimam poslednjih 7 numeričkih
    if len(kolone_brojeva) != 7:
        # Alternativni fallback: uzmi prvih 7 kolona koje u imenu imaju 'b' ili 'broj' ili su prosto prvih 7 numeričkih
        kolone_brojeva = [c for c in df.columns if pd.api.types.is_numeric_dtype(df[c])][:7]
        
    print(f"[LQG Pipeline] Detektovane kolone za kombinaciju: {kolone_brojeva}")
    print(f"[LQG Pipeline] Učitano ukupno istorijskih kola: {len(df)}")
    
    # Pretvaram u numpy niz (pretpostavka: redosled u CSV je od najnovijeg ka najstarijem)
    # Ako je obrnuto (DA), otkomentariši sledeću liniju:
    df = df.iloc[::-1]
    istorija = df[kolone_brojeva].to_numpy()
    
    N_NODES = 39
    kvantna_mreza = np.zeros((N_NODES, N_NODES), dtype=complex)
    
    # Tkanje pene spinova i računanje faza (Evolucija kroz vreme)
    for t, kolo in enumerate(istorija):
        # Fazni pomak slabi kako idem dublje u prošlost
        faza = 2 * np.pi * (1.0 / (t + 1))
        doprinos = np.exp(1j * faza)
        
        # Svako izvlačenje je hiper-grana koja povezuje 7 čvorova
        for i in range(7):
            for j in range(i + 1, 7):
                if np.isnan(kolo[i]) or np.isnan(kolo[j]):
                    continue
                cvor_a = int(kolo[i]) - 1
                cvor_b = int(kolo[j]) - 1
                
                kvantna_mreza[cvor_a, cvor_b] += doprinos
                kvantna_mreza[cvor_b, cvor_a] += doprinos
                
    # Sumiranje amplituda za svaki od 39 čvorova
    amplitude_cvorova = np.sum(kvantna_mreza, axis=1)
    
    # Kvadrat modula za dobijanje intenziteta konstruktivne interferencije
    intenziteti = np.abs(amplitude_cvorova) ** 2
    
    # Rangiranje svih 39 brojeva (indeksi + 1 da vratim prave loto brojeve)
    rangirani_brojevi = np.argsort(intenziteti)[::-1] + 1
    
    # Selektujem TOP 7 brojeva koji su u najvećoj konstruktivnoj interferenciji
    next_kombinacija = sorted(list(rangirani_brojevi[:7]))
    
    print("\n" + "="*50)
    print(f"  [LQG v1] SLEDEĆA PREDREČENA KOMBINACIJA (NEXT):")
    print(f"  {next_kombinacija}")
    print("="*50 + "\n")
    
    # Opciono: prikaz jačine pojedinačnih amplituda za odabranih 7
    print("Detaljan intenzitet izabranih čvorova:")
    for br in next_kombinacija:
        print(f"Čvor {br} -> Intenzitet: {intenziteti[br-1]:.2f}")
        
    return next_kombinacija

# POKRETANJE PIPELINE-A
next_7 = generisi_next_predikciju_v1(PUTANJA_DO_BAZE)



"""
[LQG Pipeline] Detektovane kolone za kombinaciju: ['5', '14', '15', '17', '28', '30', '34']
[LQG Pipeline] Učitano ukupno istorijskih kola: 4707

==================================================
  [LQG v1] SLEDEĆA PREDREČENA KOMBINACIJA (NEXT):
  [8, x, 23, y, 32, z, 37]
==================================================

Detaljan intenzitet izabranih čvorova:
Čvor  8 -> Intenzitet: 30926148.99
Čvor  x -> Intenzitet: 27147798.85
Čvor 23 -> Intenzitet: 30212260.89
Čvor  y -> Intenzitet: 27660102.94
Čvor 32 -> Intenzitet: 26966718.94
Čvor  z -> Intenzitet: 27881892.60
Čvor 37 -> Intenzitet: 27145526.12







[LQG Pipeline] Detektovane kolone za kombinaciju: ['5', '14', '15', '17', '28', '30', '34']
[LQG Pipeline] Učitano ukupno istorijskih kola: 2975

==================================================
  [LQG v1] SLEDEĆA PREDREČENA KOMBINACIJA (NEXT):
  [8, x, 21, y, 23, z, 38]
==================================================

Detaljan intenzitet izabranih čvorova:
Čvor  8 -> Intenzitet: 12700773.75
Čvor  x -> Intenzitet: 11182289.22
Čvor 21 -> Intenzitet: 11005724.23
Čvor  y -> Intenzitet: 11671293.58
Čvor 23 -> Intenzitet: 11645256.92
Čvor  z -> Intenzitet: 10983081.60
Čvor 38 -> Intenzitet: 10976805.97







[LQG Pipeline] Detektovane kolone za kombinaciju: ['12', '17', '18', '19', '23', '35', '37']
[LQG Pipeline] Učitano ukupno istorijskih kola: 1731

==================================================
  [LQG v1] SLEDEĆA PREDREČENA KOMBINACIJA (NEXT):
  [2, x, 8, y, 23, z, 34]
==================================================

Detaljan intenzitet izabranih čvorova:
Čvor  2 -> Intenzitet: 4220062.44
Čvor  x -> Intenzitet: 3809082.76
Čvor  8 -> Intenzitet: 3927095.09
Čvor  y -> Intenzitet: 4107420.23
Čvor 23 -> Intenzitet: 4272994.45
Čvor  z -> Intenzitet: 3933596.17
Čvor 34 -> Intenzitet: 3886315.65
"""



"""
Loto kombinacija je grana (link) koja povezuje 7 čvorova (brojeva) 
- direktno formalizam mreža spinova (Spin Networks) iz Kvantne gravitacije petlji (LQG), 
gde grane nose kvantne brojeve (spinove) koji definišu geometriju.
Evo kako se LQG formalizam sada savršeno preslikava na moj model:


1. Istorija izvlačenja kao "Pena spinova" (Spinfoam)

U LQG-u, mreža spinova je statična slika prostora u jednom trenutku. Kada se ta mreža menja kroz vreme, ona stvara penu spinova (Spinfoam).
• Svako novo loto izvlačenje je zapravo jedna "evolucija" mreže.
• Dodavanjem nove grane sa 7 čvorova (novog izvlačenja), zapravo se tka "prostor-vreme" loto sistema.
• Računam amplitudu prelaza iz dosadašnje geometrije grafa u novu geometriju.

2. Kvantizacija površine i jačina veza

U LQG-u, grane koje presecaju neku površinu daju toj površini njenu vrednost (površina je kvantizovana). 
• Čvorovi su fiksni (brojevi od 1 do 39).
• Svaka kombinacija (grana) "zahvata" 7 čvorova odjednom.
• Ako se određeni čvorovi često povezuju kroz istoriju izvlačenja, ta "oblast" grafa postaje geometrijski "teža" ili "gušća". To direktno utiče na amplitude konstruktivne interferencije za sledeće izvlačenje.

3. Gausov zakon i uslov zatvorenosti

Ovo je najmoćniji koncept LQG-a. U svakom čvoru mreže spinova mora važiti zakon očuvanja (tzv. gauge invariance). Pošto je grana definisana sa tačno 7 čvorova, taj "kvantni objekat" mora da zadovolji specifične uslove zatvorenosti unutar celog grafa od 39 elemenata.
Precizno definisana topologija: fiksni graf od 39 čvorova gde istorijski nizovi izvlačenja tkaju mrežu hiper-grana (svaka povezuje 7 čvorova).



Evolucija mreže kroz vreme (Spinfoam) i proračun amplituda prelaza za sledeće kolo.
Pošto je prostor od 39 čvorova fiksiran, a svako izvlačenje je grana koja povezuje 7 čvorova, istorijat izvlačenja posmatram kao vremensku penu (Spinfoam). Cilj v1 je da izračuna gde će se manifestovati konstruktivna interferencija (najveće amplitude) za sledeće izvlačenje, koristeći istorijsku gustinu i fazne pomake.


Matematički model (v1)

1. Matrica kvantne povezanosti (\(A\)): Umesto klasične učestanosti, formiram matricu dimenzija \(39 \times 39\). Ako se dva broja pojave zajedno u izvlačenju, veza između njih dobija doprinos.
2. Fazni pomak (\(\theta \)): Svaki istorijski korak (kolo) unosi fazni pomak u zavisnosti od toga koliko je davno bilo izvlačenje. Što je izvlačenje svežije, faza je stabilnija.
3. Amplituda čvora (\(\Psi _{i}\)): Amplituda za svaki od 39 čvorova računa se kao suma kompleksnih doprinosa svih njegovih veza u mreži spinova:
\(\Psi _{i}=\sum _{j\ne i}A_{ij}\cdot e^{i\theta _{ij}}\)
4. Verovatnoća (Kvadrat modula): Na kraju tražim intenzitet amplitude \(P_i = \vert{}\Psi_i\vert{}^2\) koji pokazuje koji čvorovi imaju najveći "geometrijski pritisak" da budu povezani u sledećem kolu.


v1 (Spinfoam Amplitude)


Ako su se određeni brojevi pojavljivali u sličnim vremenskim intervalima, njihove faze se poklapaju i dolazi do konstruktivne interferencije (intenzitet naglo skače). Ako su se pojavljivali u haotičnim razmacima, faze se poništavaju (destruktivna interferencija) i intenzitet pada blizu nule.
Kada se potisne destruktivna interferencija (brojeve sa dna liste), da li se drastično sužava prostor kombinacija koje pratim?
• Visok intenzitet (Top brojevi): Čvorovi koji su u istoriji formirali grane u takvim vremenskim intervalima da su im se fazni uglovi poklopili. Došlo je do konstruktivne interferencije talasnih funkcija - geometrija sistema favorizuje njihovo sledeće povezivanje.
• Nizak intenzitet (Dno liste): Čvorovi čije su se istorijske grane poništile kroz fazni pomak (destruktivna interferencija). Prostor-vreme lotoa ih u ovom trenutku "gasi".

• Da li su se u predikciji izdvojili brojevi koji su u skorijoj istoriji imali stabilne fazne razmake, ili je model izvukao neočekivane "spavače"?

Skripta je uspešno prošla kroz svih 4707 kola i izbacila prvu čistu geometrijsku predikciju zasnovanu na konstruktivnoj interferenciji talasnih funkcija čvorova. 
Kombinacija [8, x, 23, y, 32, z, 37] predstavlja tačke u prostoru od 39 čvorova koje u ovom trenutku imaju najveći "geometrijski pritisak" (intenzitete preko 27 do 30 miliona).
"""
