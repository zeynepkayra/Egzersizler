print(""" ################################## REINFORCEMENT PLATE CALCULATIONS####################################
================================================ AWWA==================================Mech.Eng.HamiKESERCI

################ P Internal pressure as psi
################ D-MainPipe Outter Diameter as inc
################ d-Branch Outter Diameter as inc
################ Δ-Between MainPipe and Branch Degree as decimal

        #  --------------------------------------------------------  #
      #                       (P x d^2)                                #
     <                PDV= ------------                                 >
      #                       D x sinΔ                                 #
        #  --------------------------------------------------------  #   """)


P = int(input("Please enter the     P : "))
D = int(input("Please enter the     D : "))
d = int(input("Please enter the     d : "))
Delta = int(input("Please enter the  Δ: "))
if Delta == 90:
    sinΔ = 1
elif Delta == 60:
    sinΔ = float(0.86)
elif Delta == 30:
    sinΔ = float(0.5)
else:
    print("Please Calculate the sinΔ for the calculations")

print("PDV: PDV is control for the which reinforcement plate that we use")
PDV = int(P * d ** 2) / (D * sinΔ * sinΔ)
print(PDV)
M1 = float(25 * 10 ** (-5))
M2 = int(1)
if PDV > 6000:
    print("use Crotch Plate")
    """ #############Continiue the Crotch Calculatıons###############"""
    dp = int(input("Use the 13.7 graph for the     dp: "))
    t1 = input("use the 13.7 graph for the         t1: ")
    t = float(input("select new thickness of plate  t: "))
    print(type(t))
    a = float(Delta / 360)
    print(type(a))
    b = float(0.917)
    print(type(b))
    x = b - a
    print(type(x))
    Nw = int(input("Use the 13.8 graph for the  Nw: "))
    Nb = int(input("Use the 13.8 graph for the  Nb: "))
    Qw = int(input("Use the 13.9 graph for the  Qw: "))
    Qb = int(input("Use the 13.9 graph for the  Qb: "))
    dw = Nw * dp
    print("dw:", dw)
    db = Nb * dp
    print("db:", db)
    dw2 = Qw * dw
    print("dw2:", dw2)
    db2 = Qb * db
    print("db2:", db2)
    tmp = float(input("mainpipe thickness: "))
    print(type(tmp))
    tbp = float(input("branch thickness  : "))
    print(type(tbp))
    Pw = P
    Pd = P * 1, 5
    radm = float(0)
    radm = D / 2
    radm1 = float(0)
    radm1 = radm - tmp
    radb = float(0)
    radb = d / 2
    radb1 = float(0)
    radb1 = radb - tbp
    Rmp = radm1
    print("main pipe inside radius: ", radm1)
    print(type(Rmp))
    Rbp = radb1
    print("branch pipe radius: ", radb1)
    print(type(Rbp))
    dts = float(0)
    dts = float(input("for single crotch 13.10 graph d\'t dts:"))
    print(type(dts))
    dpt = float(0)
    dts = float(input("depth of plate for two crotch 13.10 graph dt dpt:"))
    print(type(dpt))
    dwrt = int(dw * ((int(t1) / int(t)) ** x))
    print("new depth of the plate d1=dw", dwrt)
    dbrt = int(db * ((int(t1) / int(t)) ** x))
    print("new depth of the plate d1=db: ", dbrt)
    dwrs = (dw2 * ((int(t1) / int(t)) ** x))
    print("new depth of the plate as d\'w d1=dw2: ", dwrs)
    dbrs = (db2 * ((int(t1) / int(t)) ** x))
    print("new depth of the plate as d\'b d1=db2:  ", dbrs)
    if Rmp == Rbp:
        dts = (dts + Rmp)
        dpt = (dpt + Rbp)
        print(dts)
        print(dpt)
    print(" USE THE VALUE OF SINGULAR CROTCH PLATE")
    print("dwrs:", int(dwrs), "dbrs:", int(dbrs), "dts: ", int(dts))
    print("USE THE VALUE OF TWO CROTCH PLATE")
    print("dwrt: ", int(dwrt), "dbrt: ", int(dbrt), "dpt :", int(dpt))
    print(' ################# Calculations Finished #########################')

elif 4000 < PDV < 6000 and d / D > float(0, 7):
    M = M1
    print("Use Wrapper Plate")
elif PDV < 4000 and d / D > float(0, 7):
    M = M2
    print("Use Wrapper Plate")
elif 4000 < PDV < 6000 and d / D <= float(0, 7):
    M = M1
    print("Use Collar Plate")
elif PDV < 4000 and d / D <= float(0, 7):
    M = M2
    print("Use Wrapper Plate")


# Hocam programı çalıştırdığınızda input değerleri sırasıyla bu değerleri girmenz gerekıyor : 870-30-30-90-32-1-1.2-1-1-1-1-0.94-0.94-19.5-14