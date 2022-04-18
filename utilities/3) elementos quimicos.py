#Este é um programa que permite que o usuário encontre as propriedades dos elementos químicos presentes na Tabela Periódica.

t("Encontre qualquer elemento da Tabela Periódica")

z = float(input("\nDigite o número atômico do elemento: "))

if z == 1:
    print("\nNome: Hidrogênio \nSímbolo: [H] \nTipo: Ametal \nNº atômico: 1 \nNº de prótons/elétrons: 1 \nMassa molecular: 1.008u \nConfiguração eletrônica: 1s^1\n")
elif z == 2:
    print("\nNome: Helio \nSímbolo: [He] \nTipo: Gás nobre \nNº atômico: 2 \nNº de prótons/elétrons: 2 \nMassa molecular: 4.003u \nConfiguração eletrônica: 1s^2\n")
elif z == 3:
    print("\nNome: Litio \nSímbolo: [Li] \nTipo: Metal alcalino \nNº atômico: 3 \nNº de prótons/elétrons: 3 \nMassa molecular: 6.941u \nConfiguração eletrônica: 1s^2, 2s^1\n")
elif z == 4:
    print("\nNome: Helio \nSímbolo: [Be] \nTipo: Metal alcalino-terroso \nNº atômico: 4 \nNº de prótons/elétrons: 4 \nMassa molecuclar: 9.012u \nConfiguração eletrônica: 1s^2, 2s^2\n")
elif z == 5:
    print("\nNome: Boro \nSímbolo: [B] \nTipo: Semimetal \nNº atômico: 5 \nNº de prótons/elétrons: 5 \nMassa molecular: 10.811u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^1\n")
elif z == 6:
    print("\nNome: Carbono \nSímbolo: [C] \nTipo: Ametal \nNº atômico: 6 \nNº de prótons/elétrons: 6 \nMassa molecular: 12.011u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^2\n")
elif z == 7:
    print("\nNome: Nitrogênio \nSímbolo: [N] \nTipo: Ametal \nNº atômico: 7 \nNº de prótons/elétrons: 7 \nMassa molecuclar: 14.007u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^3\n")
elif z == 8:
    print("\nNome: Oxigênio \nSímbolo: [O] \nTipo: Ametal \nNº atômico: 8 \nNº de prótons/elétrons: 8 \nMassa molecular: 15.999u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^4\n")
elif z == 9:
    print("\nNome: Fluor \nSímbolo: [F] \nTipo: Halogênio \nNº atômico: 9 \nNº de prótons/elétrons: 9 \nMassa molecular: 18.998u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^5\n")
elif z == 10:
    print("\nNome: Neônio \nSímbolo: [Ne] \nTipo: Gás nobre \nNº atômico: 10 \nNº de prótons/elétrons: 10 \nMassa molecular: 20.18u \nConfiguração eletrônica: 1s^2, 2s^2, 2p^6\n")
elif z == 11:
    print("\nNome: Sódio \nSímbolo: [Na] \nTipo: Metal alcalino \nNº atômico: 1 \nNº de prótons/elétrons: 11 \nMassa molecuclar: 20.99u \nConfiguração eletrônica: 3s^1\n")
elif z == 12:
    print("\nNome: Magnésio \nSímbolo: [Mg] \nTipo: Metal alcalino-terroso \nNº atômico: 12 \nNº de prótons/elétrons: 12 \nMassa molecular: 24.305u \nConfiguração eletrônica: 3s^2\n")
elif z == 13:
    print("\nNome: Alumínio \nSímbolo: [Al] \nTipo: Metal \nNº atômico: 13 \nNº de prótons/elétrons: 13 \nMassa molecular: 26.982u \nConfiguração eletrônica: 3s^2, 3p^1\n")
elif z == 14:
    print("\nNome: Silício \nSímbolo: [Si] \nTipo: Semimetal \nNº atômico: 14 \nNº de prótons/elétrons: 14 \nMassa molecuclar: 28.086u \nConfiguração eletrônica: 3s^2, 3p^2\n")
elif z == 15:
    print("\nNome: Fósforo \nSímbolo: [P] \nTipo: Ametal \nNº atômico: 15 \nNº de prótons/elétrons: 15 \nMassa molecular: 30.974u \nConfiguração eletrônica: 3s^2, 2p^3\n")
elif z == 16:
    print("\nNome: Enxofre \nSímbolo: [S] \nTipo: Ametal \nNº atômico: 16 \nNº de prótons/elétrons: 16 \nMassa molecular: 32.065u \nConfiguração eletrônica: 3s^2, 3p^4\n")
elif z == 17:
    print("\nNome: Cloro \nSímbolo: [Cl] \nTipo: Halogênio \nNº atômico: 17 \nNº de prótons/elétrons: 17 \nMassa molecular: 35.453u \nConfiguração eletrônica: 3s^2, 3p^5\n")
elif z == 18:
    print("\nNome: Argônio \nSímbolo: [Ar] \nTipo: Gás nobre \nNº atômico: 18 \nNº de prótons/elétrons: 18 \nMassa molecuclar: 39.948u \nConfiguração eletrônica: 3s^2, 3p^6\n")
elif z == 19:
    print("\nNome: Potássio \nSímbolo: [K] \nTipo: Metal alcalino \nNº atômico: 19 \nNº de prótons/elétrons: 19 \nMassa molecular: 39.098u \nConfiguração eletrônica: 4s^1\n")
elif z == 20:
    print("\nNome: Cálcio \nSímbolo: [Ca] \nTipo: Metal alcalino-terroso \nNº atômico: 20 \nNº de prótons/elétrons: 20 \nMassa molecular: 40.078u \nConfiguração eletrônica: 4s^2\n")
elif z == 21:
    print("\nNome: Escândio \nSímbolo: [Sc] \nTipo: Metal de transição \nNº atômico: 21 \nNº de prótons/elétrons: 21 \nMassa molecuclar: 44.956u \nConfiguração eletrônica: 3d^1, 4s^2\n")
elif z == 22:
    print("\nNome: Titânio \nSímbolo: [Ti] \nTipo: Metal de transição \nNº atômico: 22 \nNº de prótons/elétrons: 22 \nMassa molecular: 4.867u \nConfiguração eletrônica: 3d^2, 4s^2\n")
elif z == 23:
    print("\nNome: Vanádio \nSímbolo: [V] \nTipo: Metal de transição \nNº atômico: 23 \nNº de prótons/elétrons: 23 \nMassa molecular: 50.942u \nConfiguração eletrônica: 3d^2, 4s^2\n")
elif z == 24:
    print("\nNome: Cromo \nSímbolo: [Cr] \nTipo: Metal de transição \nNº atômico: 24 \nNº de prótons/elétrons: 24 \nMassa molecular: 51.996u \nConfiguração eletrônica: 3d^5, 4s^1\n")
elif z == 25:
    print("\nNome: Manganês \nSímbolo: [Mn] \nTipo: Metal de transição \nNº atômico: 25 \nNº de prótons/elétrons: 25 \nMassa molecuclar: 54.938u \nConfiguração eletrônica: 3d^5, 4s^2\n")
elif z == 26:
    print("\nNome: Ferro \nSímbolo: [Fe] \nTipo: Metal alcalino-terroso \nNº atômico: 26 \nNº de prótons/elétrons: 26 \nMassa molecular: 55.845u \nConfiguração eletrônica: 3d^6, 4s^2\n")
elif z == 27:
    print("\nNome: Cobalto \nSímbolo: [Co] \nTipo: Metal de transição \nNº atômico: 27 \nNº de prótons/elétrons: 27 \nMassa molecular: 58.933u \nConfiguração eletrônica: 3d^7, 4s^2\n")
elif z == 28:
    print("\nNome: Níquel \nSímbolo: [Ni] \nTipo: Metal de transição \nNº atômico: 28 \nNº de prótons/elétrons: 28 \nMassa molecuclar: 58.693u \nConfiguração eletrônica: 3d^8, 4s^2\n")
elif z == 29:
    print("\nNome: Cobre \nSímbolo: [Cu] \nTipo: Metal de transição \nNº atômico: 29 \nNº de prótons/elétrons: 29 \nMassa molecular: 63.546u \nConfiguração eletrônica: 3d^10, 4s^1\n")
elif z == 30:
    print("\nNome: Zinco \nSímbolo: [Zn] \nTipo: Metal de transição \nNº atômico: 30 \nNº de prótons/elétrons: 30 \nMassa molecular: 65.409u \nConfiguração eletrônica: 3d^10, 4s^2\n")
elif z == 31:
    print("\nNome: Gálio \nSímbolo: [Ga] \nTipo: Metal \nNº atômico: 31 \nNº de prótons/elétrons: 31 \nMassa molecular: 69.723u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^1\n")
elif z == 32:
    print("\nNome: Germânio \nSímbolo: [Ge] \nTipo: Semimetal \nNº atômico: 32 \nNº de prótons/elétrons: 32 \nMassa molecuclar: 72.64u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^2\n")
elif z == 33:
    print("\nNome: Arsênio \nSímbolo: [As] \nTipo: Semimetal \nNº atômico: 33 \nNº de prótons/elétrons: 33 \nMassa molecular: 74.922u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^3\n")
elif z == 34:
    print("\nNome: Selênio \nSímbolo: [Se] \nTipo: Ametal \nNº atômico: 34 \nNº de prótons/elétrons: 34 \nMassa molecular: 78.96u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^4\n")
elif z == 35:
    print("\nNome: Bromo \nSímbolo: [Br] \nTipo: Halogênio \nNº atômico: 35 \nNº de prótons/elétrons: 35 \nMassa molecuclar: 79.904u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^5\n")
elif z == 36:
    print("\nNome: Criptônio \nSímbolo: [Kr] \nTipo: Gás nobre \nNº atômico: 36 \nNº de prótons/elétrons: 36 \nMassa molecular: 83.798u \nConfiguração eletrônica: 3d^10, 4s^2, 4p^6\n")
elif z == 37:
    print("\nNome: Rubídio \nSímbolo: [Rb] \nTipo: Metal alcalino \nNº atômico: 37 \nNº de prótons/elétrons: 37 \nMassa molecular: 85.468u \nConfiguração eletrônica: 5s^1\n")
elif z == 38:
    print("\nNome: Estrôncio \nSímbolo: [Sr] \nTipo: Metal alcalino-terroso \nNº atômico: 38 \nNº de prótons/elétrons: 38 \nMassa molecular: 87.62u \nConfiguração eletrônica: 5s^2\n")
elif z == 39:
    print("\nNome: Ítrio \nSímbolo: [Y] \nTipo: Metal de transição \nNº atômico: 39 \nNº de prótons/elétrons: 39 \nMassa molecuclar: 88.906u \nConfiguração eletrônica: 4d^1, 5s^2\n")
elif z == 40:
    print("\nNome: Zircônio \nSímbolo: [Zr] \nTipo: Metal de transição \nNº atômico: 40 \nNº de prótons/elétrons: 40 \nMassa molecular: 91.224u \nConfiguração eletrônica: 4d^2, 5s^2\n")
elif z == 41:
    print("\nNome: Nióbio \nSímbolo: [Nb] \nTipo: Metal de transição \nNº atômico: 41 \nNº de prótons/elétrons: 41 \nMassa molecular: 92.906u \nConfiguração eletrônica: 4d^4, 5s^1\n")
elif z == 42:
    print("\nNome: Molibdênio \nSímbolo: [Mo] \nTipo: Metal de transição \nNº atômico: 42 \nNº de prótons/elétrons: 42 \nMassa molecuclar: 95.94u \nConfiguração eletrônica: 4d^5, 5s^1\n")
elif z == 43:
    print("\nNome: Tecnécio \nSímbolo: [Tc] \nTipo: Metal de transição \nNº atômico: 43 \nNº de prótons/elétrons: 43 \nMassa molecular: 98u \nConfiguração eletrônica: 4d^5, 5s^2\n")
elif z == 44:
    print("\nNome: Rutênio \nSímbolo: [Ru] \nTipo: Metal de transição \nNº atômico: 44 \nNº de prótons/elétrons: 44 \nMassa molecular: 101.07u \nConfiguração eletrônica: 4d^7, 5s^1\n")
elif z == 45:
    print("\nNome: Ródio \nSímbolo: [Rh] \nTipo: Metal de transição \nNº atômico: 45 \nNº de prótons/elétrons: 45 \nMassa molecular: 102.905u \nConfiguração eletrônica: 4d^8, 5s^1\n")
elif z == 46:
    print("\nNome: Paládio \nSímbolo: [Pd] \nTipo: Metal de transição \nNº atômico: 46 \nNº de prótons/elétrons: 46 \nMassa molecuclar: 106.42u \nConfiguração eletrônica: 4d^10, 5s^0\n")
elif z == 47:
    print("\nNome: Prata \nSímbolo: [Ag] \nTipo: Metal de transição \nNº atômico: 47 \nNº de prótons/elétrons: 47 \nMassa molecular: 107.868u \nConfiguração eletrônica: 4d^10, 5s^1\n")
elif z == 48:
    print("\nNome: Cádmio \nSímbolo: [Cd] \nTipo: Metal de transição \nNº atômico: 48 \nNº de prótons/elétrons: 48 \nMassa molecular: 112.411u \nConfiguração eletrônica: 4d^10, 5s^2\n")
elif z == 49:
    print("\nNome: Índio \nSímbolo: [In] \nTipo: Metal \nNº atômico: 49 \nNº de prótons/elétrons: 49 \nMassa molecuclar: 114.818u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^1\n")
elif z == 50:
    print("\nNome: Estanho \nSímbolo: [Sn] \nTipo: Metal \nNº atômico: 50 \nNº de prótons/elétrons: 50 \nMassa molecular: 118.71u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^2\n")
elif z == 51:
    print("\nNome: Antimônio \nSímbolo: [Sb] \nTipo: Semimetal de transição \nNº atômico: 51 \nNº de prótons/elétrons: 51 \nMassa molecular: 121.76u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^3\n")
elif z == 52:
    print("\nNome: Telúrio \nSímbolo: [Te] \nTipo: Semimetal \nNº atômico: 52 \nNº de prótons/elétrons: 52 \nMassa molecular: 127.6u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^4\n")
elif z == 53:
    print("\nNome: Iodo \nSímbolo: [I] \nTipo: Haloogênio \nNº atômico: 53 \nNº de prótons/elétrons: 53 \nMassa molecuclar: 126.904u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^5\n")
elif z == 54:
    print("\nNome: Xenônio \nSímbolo: [Xe] \nTipo: Gás nobre \nNº atômico: 54 \nNº de prótons/elétrons: 54 \nMassa molecular: 131.293u \nConfiguração eletrônica: 4d^10, 5s^2, 5p^6\n")
elif z == 55:
    print("\nNome: Césio \nSímbolo: [Cs] \nTipo: Metal alcalino \nNº atômico: 55 \nNº de prótons/elétrons: 55 \nMassa molecular: 132.905u \nConfiguração eletrônica: 6s^1\n")
elif z == 56:
    print("\nNome: Bário \nSímbolo: [Ba] \nTipo: Metal alcalino-terroso \nNº atômico: 56 \nNº de prótons/elétrons: 56 \nMassa molecuclar: 137.327u \nConfiguração eletrônica: 6s^2\n")
elif z == 57:
    print("\nNome: Lantânio \nSímbolo: [La] \nTipo: Ametal \nNº atômico: 57 \nNº de prótons/elétrons: 57 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 58:
    print("\nNome: Cério \nSímbolo: [Ce] \nTipo: Gás nobre \nNº atômico: 58 \nNº de prótons/elétrons: 58 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 59:
    print("\nNome: Praseodímio \nSímbolo: [Pr] \nTipo: Metal alcalino \nNº atômico: 59 \nNº de prótons/elétrons: 59 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 60:
    print("\nNome: Neodímio \nSímbolo: [Nd] \nTipo: Metal alcalino-terroso \nNº atômico: 60 \nNº de prótons/elétrons: 60 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 61:
    print("\nNome: Promécio \nSímbolo: [Pm] \nTipo: Semimetal \nNº atômico: 61 \nNº de prótons/elétrons: 61 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 62:
    print("\nNome: Samários \nSímbolo: [Sm] \nTipo: Ametal \nNº atômico: 62 \nNº de prótons/elétrons: 62 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 63:
    print("\nNome: Európio \nSímbolo: [Eu] \nTipo: Ametal \nNº atômico: 63 \nNº de prótons/elétrons: 63 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 64:
    print("\nNome: Gadolínio \nSímbolo: [Gd] \nTipo: Ametal \nNº atômico: 64 \nNº de prótons/elétrons: 64 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 65:
    print("\nNome: Térbio \nSímbolo: [Tb] \nTipo: Halogênio \nNº atômico: 65 \nNº de prótons/elétrons: 65 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 66:
    print("\nNome: Disprósio \nSímbolo: [Dy] \nTipo: Gás nobre \nNº atômico: 66 \nNº de prótons/elétrons: 66 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 67:
    print("\nNome: Hólmio \nSímbolo: [Ho] \nTipo: Metal alcalino \nNº atômico: 67 \nNº de prótons/elétrons: 67 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 68:
    print("\nNome: Érbio \nSímbolo: [Er] \nTipo: Metal alcalino-terroso \nNº atômico: 68 \nNº de prótons/elétrons: 68 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 69:
    print("\nNome: Túlio \nSímbolo: [Tm] \nTipo: Metal \nNº atômico: 69 \nNº de prótons/elétrons: 69 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 70:
    print("\nNome: Itérbio \nSímbolo: [Yb] \nTipo: Semimetal \nNº atômico: 70 \nNº de prótons/elétrons: 70 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 71:
    print("\nNome: Lutécio \nSímbolo: [Lu] \nTipo: Ametal \nNº atômico: 71 \nNº de prótons/elétrons: 71 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 72:
    print("\nNome: Háfnio \nSímbolo: [Hf] \nTipo: Ametal \nNº atômico: 72 \nNº de prótons/elétrons: 72 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 73:
    print("\nNome: Tântalo \nSímbolo: [Ta] \nTipo: Halogênio \nNº atômico: 73 \nNº de prótons/elétrons: 73 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 74:
    print("\nNome: Tugstênio \nSímbolo: [W] \nTipo: Gás nobre \nNº atômico: 74 \nNº de prótons/elétrons: 74 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 75:
    print("\nNome: Rênio \nSímbolo: [Re] \nTipo: Metal alcalino \nNº atômico: 75 \nNº de prótons/elétrons: 75 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 76:
    print("\nNome: Ósmio \nSímbolo: [Os] \nTipo: Metal alcalino-terroso \nNº atômico: 76 \nNº de prótons/elétrons: 76 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 77:
    print("\nNome: Irídio \nSímbolo: [Ir] \nTipo: Metal de transição \nNº atômico: 77 \nNº de prótons/elétrons: 77 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 78:
    print("\nNome: Platina \nSímbolo: [Pt] \nTipo: Metal de transição \nNº atômico: 78 \nNº de prótons/elétrons: 78 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 79:
    print("\nNome: Ouro \nSímbolo: [Au] \nTipo: Metal de transição \nNº atômico: 79 \nNº de prótons/elétrons: 79 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 80:
    print("\nNome: Mercúrio \nSímbolo: [Hg] \nTipo: Metal de transição \nNº atômico: 80 \nNº de prótons/elétrons: 80 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 81:
    print("\nNome: Tálio \nSímbolo: [Tl] \nTipo: Metal de transição \nNº atômico: 81 \nNº de prótons/elétrons: 81 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 82:
    print("\nNome: Chumbo \nSímbolo: [Pb] \nTipo: Metal alcalino-terroso \nNº atômico: 82 \nNº de prótons/elétrons: 82 \nMassa molecular: u \nConfiguração eletrônica: 3\n")
elif z == 83:
    print("\nNome: Bismuto \nSímbolo: [Bi] \nTipo: Metal de transição \nNº atômico: 83 \nNº de prótons/elétrons: 83 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 84:
    print("\nNome: Polônio \nSímbolo: [Po] \nTipo: Metal de transição \nNº atômico: 84 \nNº de prótons/elétrons: 84 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 85:
    print("\nNome: Astato \nSímbolo: [At] \nTipo: Metal de transição \nNº atômico: 85 \nNº de prótons/elétrons: 85 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 86:
    print("\nNome: Radônio \nSímbolo: [Rn] \nTipo: Metal de transição \nNº atômico: 86 \nNº de prótons/elétrons: 86 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 87:
    print("\nNome: Frâncio \nSímbolo: [Fr] \nTipo: Metal \nNº atômico: 87 \nNº de prótons/elétrons: 87 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 88:
    print("\nNome: Rádio \nSímbolo: [Ra] \nTipo: Semimetal \nNº atômico: 88 \nNº de prótons/elétrons: 88 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 89:
    print("\nNome: Actínio \nSímbolo: [Ac] \nTipo: Semimetal \nNº atômico: 89 \nNº de prótons/elétrons: 89 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 90:
    print("\nNome: Tório \nSímbolo: [Th] \nTipo: Ametal \nNº atômico: 90 \nNº de prótons/elétrons: 90 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 91:
    print("\nNome: Protactínio \nSímbolo: [Pa] \nTipo: Halogênio \nNº atômico: 91 \nNº de prótons/elétrons: 91 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 92:
    print("\nNome: Urânio \nSímbolo: [U] \nTipo: Gás nobre \nNº atômico: 92 \nNº de prótons/elétrons: 92 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 93:
    print("\nNome: Netúnio \nSímbolo: [Np] \nTipo: Metal alcalino \nNº atômico: 93 \nNº de prótons/elétrons: 93 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 94:
    print("\nNome: Plutônio \nSímbolo: [Pu] \nTipo: Metal alcalino-terroso \nNº atômico: 94 \nNº de prótons/elétrons: 94 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 95:
    print("\nNome: Amerício \nSímbolo: [Am] \nTipo: Metal de transição \nNº atômico: 95 \nNº de prótons/elétrons: 95 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 96:
    print("\nNome: Cúrio \nSímbolo: [Cm] \nTipo: Metal de transição \nNº atômico: 96 \nNº de prótons/elétrons: 96 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 97:
    print("\nNome: Berquélio \nSímbolo: [Bk] \nTipo: Metal de transição \nNº atômico: 97 \nNº de prótons/elétrons: 97 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 98:
    print("\nNome: Califórnio \nSímbolo: [Cf] \nTipo: Metal de transição \nNº atômico: 98 \nNº de prótons/elétrons: 98 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 99:
    print("\nNome: Einsténio \nSímbolo: [Es] \nTipo: Metal de transição \nNº atômico: 99 \nNº de prótons/elétrons: 99 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 100:
    print("\nNome: Férmio \nSímbolo: [Fm] \nTipo: Metal de transição \nNº atômico: 100 \nNº de prótons/elétrons: 100 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 101:
    print("\nNome: Mendelévio \nSímbolo: [Md] \nTipo: Metal de transição \nNº atômico: 101 \nNº de prótons/elétrons: 101 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 102:
    print("\nNome: Nobélio \nSímbolo: [No] \nTipo: Metal de transição \nNº atômico: 102 \nNº de prótons/elétrons: 102 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 103:
    print("\nNome: Laurêncio \nSímbolo: [Lr] \nTipo: Metal de transição \nNº atômico: 103 \nNº de prótons/elétrons: 103 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 104:
    print("\nNome: Rutherfórdio \nSímbolo: [Rf] \nTipo: Metal de transição \nNº atômico: 104 \nNº de prótons/elétrons: 104 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 105:
    print("\nNome: Dúbnio \nSímbolo: [Db] \nTipo: Metal \nNº atômico: 105 \nNº de prótons/elétrons: 105 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 106:
    print("\nNome: Seabórgio \nSímbolo: [Sg] \nTipo: Metal \nNº atômico: 106 \nNº de prótons/elétrons: 106 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 107:
    print("\nNome: Bóhrio \nSímbolo: [Bh] \nTipo: Semimetal de transição \nNº atômico: 107 \nNº de prótons/elétrons: 107 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 108:
    print("\nNome: Hássio \nSímbolo: [Hs] \nTipo: Metal de transição \nNº atômico: 108 \nNº de prótons/elétrons: 108 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 109:
    print("\nNome: Meitnério \nSímbolo: [Mt] \nTipo: Metal de transição \nNº atômico: 109 \nNº de prótons/elétrons: 109 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 110:
    print("\nNome: Darmstádio \nSímbolo: [Ds] \nTipo: Metal de transição \nNº atômico: 110 \nNº de prótons/elétrons: 110 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 111:
    print("\nNome: Roentgênio \nSímbolo: [Rg] \nTipo: Metal de transição \nNº atômico: 111 \nNº de prótons/elétrons: 111 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 112:
    print("\nNome: Copernício \nSímbolo: [Cn] \nTipo: Metal de transição \nNº atômico: 112 \nNº de prótons/elétrons: 112 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 113:
    print("\nNome: Nihônio \nSímbolo: [Nh] \nTipo: Metal de transição \nNº atômico: 113 \nNº de prótons/elétrons: 113 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 114:
    print("\nNome: Fleróvio \nSímbolo: [Fl] \nTipo: Metal de transição \nNº atômico: 114 \nNº de prótons/elétrons: 114 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 115:
    print("\nNome: Moscóvio \nSímbolo: [Mc] \nTipo: Metal de transição \nNº atômico: 115 \nNº de prótons/elétrons: 115 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 116:
    print("\nNome: Livermório \nSímbolo: [Lv] \nTipo: Metal \nNº atômico: 116 \nNº de prótons/elétrons: 116 \nMassa molecuclar: u \nConfiguração eletrônica: \n")
elif z == 117:
    print("\nNome: Tenessino \nSímbolo: [Ts] \nTipo: Metal \nNº atômico: 117 \nNº de prótons/elétrons: 117 \nMassa molecular: u \nConfiguração eletrônica: \n")
elif z == 118:
    print("\nNome: Oganessônio \nSímbolo: [Og] \nTipo: Semimetal de transição \nNº atômico: 118 \nNº de prótons/elétrons: 118 \nMassa molecular: u \nConfiguração eletrônica: \n")
