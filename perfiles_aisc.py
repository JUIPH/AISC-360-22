"""
Librería de Perfiles W del AISC
Propiedades geométricas y mecánicas en unidades métricas
"""


class PropiedadesPerfilW:
    """
    Clase para almacenar las propiedades de un perfil W del AISC

    Parámetros:
    -----------
    d : float
        Altura total del perfil (cm)
    bf : float
        Ancho del patín (cm)
    tf : float
        Espesor del patín (cm)
    tw : float
        Espesor del alma (cm)
    A : float
        Área de la sección transversal (cm²)
    Ix : float
        Momento de inercia alrededor del eje X (cm⁴)
    Sx : float
        Módulo de sección elástico alrededor del eje X (cm³)
    Zx : float
        Módulo de sección plástico alrededor del eje X (cm³)
    rx : float
        Radio de giro alrededor del eje X (cm)
    Iy : float
        Momento de inercia alrededor del eje Y (cm⁴)
    Sy : float
        Módulo de sección elástico alrededor del eje Y (cm³)
    Zy : float
        Módulo de sección plástico alrededor del eje Y (cm³)
    ry : float
        Radio de giro alrededor del eje Y (cm)
    J : float
        Constante de torsión (cm⁴)
    Cw : float
        Constante de alabeo (cm⁶)
    ho : float
        Distancia entre centroides de los patines (cm)
    Fy : float
        Esfuerzo de fluencia del acero (kgf/cm²)
    Fu : float
        Esfuerzo último del acero (kgf/cm²)
    """

    def __init__(self, d, bf, tf, tw, A, Ix, Sx, Zx, rx, Iy, Sy, Zy, ry, J, Cw, ho, Fy=3515, Fu=4570):
        self.d = d  # Altura del perfil (cm)
        self.bf = bf  # Ancho del patín (cm)
        self.tf = tf  # Espesor del patín (cm)
        self.tw = tw  # Espesor del alma (cm)
        self.A = A  # Área (cm²)
        self.Ix = Ix  # Momento de inercia X (cm⁴)
        self.Sx = Sx  # Módulo de sección elástico X (cm³)
        self.Zx = Zx  # Módulo de sección plástico X (cm³)
        self.rx = rx  # Radio de giro X (cm)
        self.Iy = Iy  # Momento de inercia Y (cm⁴)
        self.Sy = Sy  # Módulo de sección elástico Y (cm³)
        self.Zy = Zy  # Módulo de sección plástico Y (cm³)
        self.ry = ry  # Radio de giro Y (cm)
        self.J = J  # Constante de torsión (cm⁴)
        self.Cw = Cw  # Constante de alabeo (cm⁶)
        self.ho = ho  # Distancia entre centroides de patines (cm)
        self.Fy = Fy  # Esfuerzo de fluencia (kgf/cm²)
        self.Fu = Fu  # Esfuerzo último (kgf/cm²)

    def __repr__(self):
        return f"PropiedadesPerfilW(d={self.d}, bf={self.bf}, A={self.A})"

    def __str__(self):
        return (f"Perfil W - d={self.d} cm, bf={self.bf} cm, A={self.A} cm², "
                f"Ix={self.Ix} cm⁴, Iy={self.Iy} cm⁴")


# =============================================================================
# PERFILES W DEL AISC - PROPIEDADES EN UNIDADES MÉTRICAS
# =============================================================================

# Serie W44
w44x335 = PropiedadesPerfilW(d=114.05, bf=40.16, tf=3.61, tw=2.36, A=642.58, Ix=527934.82, Sx=9258.25, Zx=10409.15,
                             rx=28.68, Iy=54789.93, Sy=2728.35, Zy=4131.37, ry=9.22, J=312.98, Cw=6746259.74, ho=110.44,
                             Fy=3515, Fu=4570)
w44x290 = PropiedadesPerfilW(d=112.65, bf=39.88, tf=3.05, tw=2.01, A=556.13, Ix=453349.76, Sx=8049.82, Zx=9012.26,
                             rx=28.55, Iy=46633.85, Sy=2338.43, Zy=3540.09, ry=9.17, J=206.90, Cw=5656699.37, ho=109.60,
                             Fy=3515, Fu=4570)
w44x230 = PropiedadesPerfilW(d=109.73, bf=39.37, tf=2.36, tw=1.57, A=441.29, Ix=352862.44, Sx=6432.97, Zx=7150.46,
                             rx=28.27, Iy=35689.36, Sy=1812.67, Zy=2738.74, ry=9.02, J=102.06, Cw=4194879.00, ho=107.37,
                             Fy=3515, Fu=4570)

# Serie W40
w40x503 = PropiedadesPerfilW(d=106.50, bf=42.47, tf=5.18, tw=3.33, A=964.52, Ix=548688.37, Sx=10309.23, Zx=11797.72,
                             rx=23.85, Iy=86066.08, Sy=4053.79, Zy=6145.81, ry=9.45, J=880.26, Cw=8847551.57, ho=101.32,
                             Fy=3515, Fu=4570)
w40x397 = PropiedadesPerfilW(d=102.92, bf=41.15, tf=3.99, tw=2.57, A=760.00, Ix=416930.90, Sx=8105.35, Zx=9175.91,
                             rx=23.42, Iy=64558.64, Sy=3138.19, Zy=4752.23, ry=9.22, J=463.55, Cw=6368811.42, ho=98.93,
                             Fy=3515, Fu=4570)
w40x331 = PropiedadesPerfilW(d=100.33, bf=40.26, tf=3.28, tw=2.13, A=634.84, Ix=340773.08, Sx=6794.44, Zx=7649.30,
                             rx=23.19, Iy=52238.27, Sy=2594.78, Zy=3917.88, ry=9.07, J=295.08, Cw=4987879.95, ho=97.05,
                             Fy=3515, Fu=4570)

# Serie W36
w36x300 = PropiedadesPerfilW(d=94.74, bf=40.64, tf=2.77, tw=1.78, A=575.48, Ix=292881.35, Sx=6182.91, Zx=6943.19,
                             rx=22.53, Iy=43965.44, Sy=2164.22, Zy=3278.70, ry=8.74, J=214.82, Cw=4492472.62, ho=91.97,
                             Fy=3515, Fu=4570)
w36x232 = PropiedadesPerfilW(d=91.95, bf=39.88, tf=2.11, tw=1.37, A=444.52, Ix=221943.75, Sx=4827.51, Zx=5384.65,
                             rx=22.35, Iy=33169.41, Sy=1663.68, Zy=2516.13, ry=8.64, J=105.18, Cw=3219466.88, ho=89.84,
                             Fy=3515, Fu=4570)
w36x194 = PropiedadesPerfilW(d=90.37, bf=30.48, tf=2.13, tw=1.27, A=371.61, Ix=183787.46, Sx=4068.38, Zx=4509.13,
                             rx=22.25, Iy=15569.18, Sy=1021.94, Zy=1567.74, ry=6.48, J=86.99, Cw=1270506.24, ho=88.24,
                             Fy=3515, Fu=4570)
w36x160 = PropiedadesPerfilW(d=88.90, bf=30.48, tf=1.73, tw=1.02, A=306.45, Ix=149762.81, Sx=3369.02, Zx=3722.60,
                             rx=22.10, Iy=12569.87, Sy=825.16, Zy=1264.52, ry=6.40, J=48.26, Cw=998533.44, ho=87.17,
                             Fy=3515, Fu=4570)
w36x135 = PropiedadesPerfilW(d=87.63, bf=30.48, tf=1.40, tw=0.79, A=258.06, Ix=122819.88, Sx=2804.84, Zx=3080.64,
                             rx=21.82, Iy=10088.61, Sy=662.26, Zy=1012.90, ry=6.25, J=25.75, Cw=760855.68, ho=86.23,
                             Fy=3515, Fu=4570)

# Serie W33
w33x241 = PropiedadesPerfilW(d=87.50, bf=40.64, tf=2.39, tw=1.40, A=462.58, Ix=233569.68, Sx=5340.42, Zx=5983.61,
                             rx=22.48, Iy=36522.48, Sy=1798.19, Zy=2721.29, ry=8.89, J=148.64, Cw=3777691.87, ho=85.11,
                             Fy=3515, Fu=4570)
w33x201 = PropiedadesPerfilW(d=85.34, bf=40.13, tf=1.96, tw=1.17, A=385.48, Ix=191064.28, Sx=4478.12, Zx=4994.99,
                             rx=22.28, Iy=29670.69, Sy=1479.40, Zy=2239.35, ry=8.79, J=84.77, Cw=2895289.92, ho=83.38,
                             Fy=3515, Fu=4570)
w33x152 = PropiedadesPerfilW(d=83.44, bf=28.96, tf=1.88, tw=1.07, A=291.61, Ix=143975.72, Sx=3452.00, Zx=3814.84,
                             rx=22.23, Iy=11902.04, Sy=822.58, Zy=1262.90, ry=6.40, J=64.77, Cw=1142125.44, ho=81.56,
                             Fy=3515, Fu=4570)
w33x130 = PropiedadesPerfilW(d=82.30, bf=28.96, tf=1.57, tw=0.89, A=249.03, Ix=120929.76, Sx=2941.76, Zx=3243.87,
                             rx=22.05, Iy=9912.26, Sy=685.16, Zy=1049.68, ry=6.30, J=38.71, Cw=887709.12, ho=80.73,
                             Fy=3515, Fu=4570)
w33x118 = PropiedadesPerfilW(d=81.59, bf=28.96, tf=1.40, tw=0.76, A=226.45, Ix=108012.48, Sx=2648.65, Zx=2913.55,
                             rx=21.87, Iy=8797.42, Sy=607.87, Zy=929.68, ry=6.25, J=27.42, Cw=761690.88, ho=80.19,
                             Fy=3515, Fu=4570)

# Serie W30
w30x211 = PropiedadesPerfilW(d=79.88, bf=38.81, tf=2.16, tw=1.27, A=404.52, Ix=173886.24, Sx=4355.48, Zx=4862.26,
                             rx=20.73, Iy=28654.08, Sy=1477.42, Zy=2237.42, ry=8.41, J=117.42, Cw=2744958.72, ho=77.72,
                             Fy=3515, Fu=4570)
w30x173 = PropiedadesPerfilW(d=77.85, bf=38.05, tf=1.73, tw=1.07, A=331.61, Ix=139331.52, Sx=3580.65, Zx=3978.71,
                             rx=20.52, Iy=22752.26, Sy=1196.13, Zy=1808.39, ry=8.28, J=63.87, Cw=2041709.44, ho=76.12,
                             Fy=3515, Fu=4570)
w30x132 = PropiedadesPerfilW(d=76.20, bf=26.67, tf=1.65, tw=0.97, A=253.55, Ix=104887.68, Sx=2753.87, Zx=3039.35,
                             rx=20.35, Iy=8264.52, Sy=620.00, Zy=953.55, ry=5.72, J=46.13, Cw=751822.08, ho=74.55,
                             Fy=3515, Fu=4570)
w30x124 = PropiedadesPerfilW(d=75.69, bf=26.42, tf=1.57, tw=0.89, A=237.42, Ix=98273.55, Sx=2598.06, Zx=2864.52,
                             rx=20.35, Iy=7735.48, Sy=585.81, Zy=897.42, ry=5.72, J=39.35, Cw=694870.08, ho=74.12,
                             Fy=3515, Fu=4570)
w30x116 = PropiedadesPerfilW(d=75.18, bf=26.67, tf=1.42, tw=0.84, A=222.58, Ix=91659.42, Sx=2439.35, Zx=2689.03,
                             rx=20.27, Iy=7206.45, Sy=540.65, Zy=826.45, ry=5.69, J=30.97, Cw=633564.48, ho=73.76,
                             Fy=3515, Fu=4570)
w30x108 = PropiedadesPerfilW(d=74.68, bf=26.42, tf=1.32, tw=0.76, A=207.10, Ix=84544.90, Sx=2264.52, Zx=2493.87,
                             rx=20.22, Iy=6593.55, Sy=499.35, Zy=763.87, ry=5.64, J=24.52, Cw=566904.96, ho=73.36,
                             Fy=3515, Fu=4570)
w30x99 = PropiedadesPerfilW(d=74.17, bf=26.67, tf=1.17, tw=0.64, A=189.68, Ix=76547.10, Sx=2064.52, Zx=2267.74,
                            rx=20.12, Iy=5896.77, Sy=442.58, Zy=676.13, ry=5.59, J=16.77, Cw=482293.76, ho=73.00,
                            Fy=3515, Fu=4570)
w30x90 = PropiedadesPerfilW(d=73.66, bf=26.42, tf=1.04, tw=0.61, A=172.26, Ix=68966.13, Sx=1873.55, Zx=2051.61,
                            rx=20.02, Iy=5264.52, Sy=398.71, Zy=609.03, ry=5.54, J=12.26, Cw=424941.12, ho=72.62,
                            Fy=3515, Fu=4570)

# Serie W27
w27x178 = PropiedadesPerfilW(d=71.12, bf=35.81, tf=1.93, tw=1.19, A=341.29, Ix=133709.03, Sx=3761.29, Zx=4194.84,
                             rx=19.79, Iy=20736.77, Sy=1158.71, Zy=1753.55, ry=7.80, J=89.03, Cw=1875774.72, ho=69.19,
                             Fy=3515, Fu=4570)
w27x146 = PropiedadesPerfilW(d=69.34, bf=35.56, tf=1.57, tw=0.97, A=280.00, Ix=107548.39, Sx=3102.58, Zx=3437.42,
                             rx=19.61, Iy=16469.03, Sy=926.45, Zy=1400.00, ry=7.67, J=49.03, Cw=1389535.68, ho=67.77,
                             Fy=3515, Fu=4570)
w27x114 = PropiedadesPerfilW(d=68.07, bf=25.91, tf=1.57, tw=0.84, A=218.71, Ix=84461.29, Sx=2483.23, Zx=2738.71,
                             rx=19.66, Iy=6777.42, Sy=523.87, Zy=803.87, ry=5.56, J=38.06, Cw=607741.44, ho=66.50,
                             Fy=3515, Fu=4570)
w27x102 = PropiedadesPerfilW(d=67.31, bf=25.40, tf=1.42, tw=0.79, A=195.48, Ix=75631.61, Sx=2248.39, Zx=2473.55,
                             rx=19.66, Iy=6031.61, Sy=475.48, Zy=727.74, ry=5.56, J=29.03, Cw=538064.64, ho=65.89,
                             Fy=3515, Fu=4570)
w27x94 = PropiedadesPerfilW(d=66.80, bf=25.40, tf=1.27, tw=0.74, A=180.65, Ix=69435.48, Sx=2079.35, Zx=2283.87,
                            rx=19.61, Iy=5515.48, Sy=434.84, Zy=664.52, ry=5.51, J=22.58, Cw=480386.88, ho=65.53,
                            Fy=3515, Fu=4570)
w27x84 = PropiedadesPerfilW(d=66.04, bf=25.40, tf=1.12, tw=0.64, A=161.29, Ix=61187.10, Sx=1853.55, Zx=2028.39,
                            rx=19.51, Iy=4833.55, Sy=381.29, Zy=581.29, ry=5.46, J=15.48, Cw=407225.28, ho=65.92,
                            Fy=3515, Fu=4570)

# Serie W24
w24x162 = PropiedadesPerfilW(d=63.25, bf=32.77, tf=1.73, tw=1.07, A=310.97, Ix=109631.61, Sx=3468.39, Zx=3869.03,
                             rx=18.77, Iy=17238.71, Sy=1052.26, Zy=1593.55, ry=7.44, J=74.19, Cw=1579693.44, ho=61.52,
                             Fy=3515, Fu=4570)
w24x146 = PropiedadesPerfilW(d=62.74, bf=32.51, tf=1.57, tw=0.97, A=280.00, Ix=98523.87, Sx=3141.94, Zx=3491.61,
                             rx=18.77, Iy=15319.35, Sy=942.58, Zy=1426.45, ry=7.39, J=56.77, Cw=1401858.56, ho=61.17,
                             Fy=3515, Fu=4570)
w24x131 = PropiedadesPerfilW(d=62.23, bf=32.26, tf=1.40, tw=0.89, A=251.61, Ix=87416.13, Sx=2809.68, Zx=3114.84,
                             rx=18.67, Iy=13483.87, Sy=836.77, Zy=1264.52, ry=7.32, J=42.58, Cw=1225858.56, ho=60.83,
                             Fy=3515, Fu=4570)
w24x117 = PropiedadesPerfilW(d=61.73, bf=32.26, tf=1.24, tw=0.79, A=224.52, Ix=77391.61, Sx=2508.39, Zx=2774.84,
                             rx=18.57, Iy=11896.77, Sy=738.71, Zy=1115.48, ry=7.29, J=31.61, Cw=1067380.80, ho=60.49,
                             Fy=3515, Fu=4570)
w24x104 = PropiedadesPerfilW(d=61.21, bf=32.01, tf=1.09, tw=0.74, A=199.35, Ix=68133.55, Sx=2226.45, Zx=2454.84,
                             rx=18.49, Iy=10393.55, Sy=649.68, Zy=979.35, ry=7.21, J=22.58, Cw=915612.48, ho=60.12,
                             Fy=3515, Fu=4570)
w24x94 = PropiedadesPerfilW(d=60.96, bf=22.86, tf=1.29, tw=0.74, A=180.00, Ix=63069.03, Sx=2069.03, Zx=2281.29,
                            rx=18.72, Iy=4999.35, Sy=437.42, Zy=672.26, ry=5.26, J=23.87, Cw=421777.92, ho=59.67,
                            Fy=3515, Fu=4570)
w24x84 = PropiedadesPerfilW(d=60.45, bf=22.86, tf=1.14, tw=0.66, A=160.65, Ix=55803.87, Sx=1847.74, Zx=2032.26,
                            rx=18.62, Iy=4383.87, Sy=383.87, Zy=589.03, ry=5.21, J=16.77, Cw=361612.80, ho=60.31,
                            Fy=3515, Fu=4570)
w24x76 = PropiedadesPerfilW(d=59.94, bf=22.86, tf=1.02, tw=0.58, A=145.16, Ix=49871.61, Sx=1664.52, Zx=1828.39,
                            rx=18.54, Iy=3893.55, Sy=340.65, Zy=522.58, ry=5.18, J=11.61, Cw=311225.28, ho=60.92,
                            Fy=3515, Fu=4570)
w24x68 = PropiedadesPerfilW(d=59.69, bf=22.61, tf=0.89, tw=0.53, A=130.32, Ix=44122.58, Sx=1479.35, Zx=1621.94,
                            rx=18.39, Iy=3403.23, Sy=301.29, Zy=461.29, ry=5.11, J=8.39, Cw=264709.12, ho=60.80,
                            Fy=3515, Fu=4570)
w24x62 = PropiedadesPerfilW(d=59.44, bf=17.78, tf=1.02, tw=0.58, A=118.71, Ix=41393.55, Sx=1393.55, Zx=1530.97,
                            rx=18.67, Iy=1803.87, Sy=203.23, Zy=315.48, ry=3.89, J=10.97, Cw=125806.08, ho=58.42,
                            Fy=3515, Fu=4570)
w24x55 = PropiedadesPerfilW(d=58.93, bf=17.78, tf=0.89, tw=0.51, A=105.81, Ix=36393.55, Sx=1235.48, Zx=1352.26,
                            rx=18.57, Iy=1567.74, Sy=176.77, Zy=273.55, ry=3.84, J=7.10, Cw=105225.28, ho=58.04,
                            Fy=3515, Fu=4570)

# Serie W21
w21x201 = PropiedadesPerfilW(d=56.39, bf=31.24, tf=2.01, tw=1.30, A=385.81, Ix=104804.52, Sx=3717.42, Zx=4175.48,
                             rx=16.48, Iy=16969.03, Sy=1086.45, Zy=1653.55, ry=6.63, J=115.48, Cw=1434838.56, ho=54.38,
                             Fy=3515, Fu=4570)
w21x182 = PropiedadesPerfilW(d=55.63, bf=31.24, tf=1.78, tw=1.19, A=348.39, Ix=93447.10, Sx=3361.29, Zx=3762.58,
                             rx=16.38, Iy=15069.03, Sy=965.16, Zy=1465.81, ry=6.58, J=87.10, Cw=1260322.56, ho=53.85,
                             Fy=3515, Fu=4570)
w21x166 = PropiedadesPerfilW(d=55.12, bf=30.99, tf=1.63, tw=1.09, A=318.71, Ix=84339.35, Sx=3061.94, Zx=3422.58,
                             rx=16.26, Iy=13583.87, Sy=876.77, Zy=1330.97, ry=6.53, J=67.74, Cw=1121548.80, ho=53.49,
                             Fy=3515, Fu=4570)
w21x147 = PropiedadesPerfilW(d=54.36, bf=30.48, tf=1.42, tw=0.97, A=282.58, Ix=73231.61, Sx=2694.84, Zx=3000.00,
                             rx=16.10, Iy=11731.61, Sy=770.32, Zy=1166.45, ry=6.45, J=47.10, Cw=956870.88, ho=52.94,
                             Fy=3515, Fu=4570)
w21x132 = PropiedadesPerfilW(d=53.85, bf=30.48, tf=1.27, tw=0.89, A=253.55, Ix=65150.97, Sx=2421.29, Zx=2690.32,
                             rx=16.03, Iy=10393.55, Sy=682.58, Zy=1033.55, ry=6.40, J=34.19, Cw=834838.56, ho=52.58,
                             Fy=3515, Fu=4570)
w21x122 = PropiedadesPerfilW(d=53.59, bf=30.48, tf=1.17, tw=0.81, A=233.55, Ix=59820.00, Sx=2233.55, Zx=2477.42,
                             rx=16.00, Iy=9544.52, Sy=626.45, Zy=948.39, ry=6.38, J=27.10, Cw=755806.08, ho=52.42,
                             Fy=3515, Fu=4570)
w21x111 = PropiedadesPerfilW(d=53.09, bf=30.23, tf=1.04, tw=0.74, A=213.55, Ix=53739.35, Sx=2024.52, Zx=2241.94,
                             rx=15.87, Iy=8529.68, Sy=564.52, Zy=853.55, ry=6.32, J=19.35, Cw=660000.00, ho=52.05,
                             Fy=3515, Fu=4570)
w21x101 = PropiedadesPerfilW(d=52.83, bf=30.48, tf=0.94, tw=0.66, A=193.55, Ix=48075.48, Sx=1821.29, Zx=2013.55,
                             rx=15.77, Iy=7598.71, Sy=499.35, Zy=754.84, ry=6.27, J=13.55, Cw=572129.28, ho=51.89,
                             Fy=3515, Fu=4570)
w21x93 = PropiedadesPerfilW(d=52.32, bf=20.83, tf=1.22, tw=0.74, A=178.71, Ix=45597.42, Sx=1744.52, Zx=1928.39,
                            rx=15.98, Iy=3768.39, Sy=361.94, Zy=557.42, ry=4.59, J=18.71, Cw=266064.96, ho=51.10,
                            Fy=3515, Fu=4570)
w21x83 = PropiedadesPerfilW(d=51.82, bf=20.83, tf=1.07, tw=0.66, A=159.35, Ix=40177.42, Sx=1551.61, Zx=1712.90,
                            rx=15.88, Iy=3268.39, Sy=313.55, Zy=482.58, ry=4.52, J=12.58, Cw=221225.28, ho=50.75,
                            Fy=3515, Fu=4570)
w21x73 = PropiedadesPerfilW(d=51.56, bf=20.83, tf=0.94, tw=0.58, A=140.65, Ix=35174.19, Sx=1366.45, Zx=1503.87,
                            rx=15.80, Iy=2851.61, Sy=273.55, Zy=419.35, ry=4.50, J=8.71, Cw=187096.32, ho=50.62,
                            Fy=3515, Fu=4570)
w21x68 = PropiedadesPerfilW(d=51.31, bf=20.83, tf=0.86, tw=0.53, A=130.32, Ix=32612.26, Sx=1272.26, Zx=1398.71,
                            rx=15.80, Iy=2601.29, Sy=249.68, Zy=382.58, ry=4.47, J=6.77, Cw=168193.92, ho=50.45,
                            Fy=3515, Fu=4570)
w21x62 = PropiedadesPerfilW(d=52.07, bf=20.83, tf=0.79, tw=0.51, A=118.71, Ix=30000.00, Sx=1153.55, Zx=1271.61,
                            rx=15.90, Iy=2393.55, Sy=229.68, Zy=351.61, ry=4.49, J=5.16, Cw=153870.72, ho=51.28,
                            Fy=3515, Fu=4570)
w21x57 = PropiedadesPerfilW(d=51.56, bf=16.51, tf=0.91, tw=0.51, A=109.03, Ix=27935.48, Sx=1084.52, Zx=1194.84,
                            rx=16.00, Iy=1351.61, Sy=163.87, Zy=254.84, ry=3.51, J=6.13, Cw=86967.84, ho=50.65, Fy=3515,
                            Fu=4570)
w21x50 = PropiedadesPerfilW(d=51.31, bf=16.51, tf=0.79, tw=0.46, A=96.13, Ix=24387.10, Sx=951.61, Zx=1046.45, rx=15.93,
                            Iy=1169.03, Sy=141.94, Zy=220.65, ry=3.48, J=4.19, Cw=72580.80, ho=50.52, Fy=3515, Fu=4570)
w21x48 = PropiedadesPerfilW(d=51.05, bf=20.32, tf=0.69, tw=0.43, A=91.61, Ix=23580.65, Sx=924.52, Zx=1016.77, rx=16.05,
                            Iy=1967.74, Sy=193.55, Zy=296.77, ry=4.63, J=3.87, Cw=124129.28, ho=50.36, Fy=3515, Fu=4570)
w21x44 = PropiedadesPerfilW(d=52.32, bf=16.51, tf=0.71, tw=0.43, A=84.52, Ix=22193.55, Sx=848.39, Zx=932.26, rx=16.21,
                            Iy=1085.81, Sy=131.61, Zy=204.52, ry=3.58, J=3.23, Cw=66774.72, ho=51.61, Fy=3515, Fu=4570)

# Serie W18
w18x192 = PropiedadesPerfilW(d=48.01, bf=28.19, tf=2.01, tw=1.32, A=368.39, Ix=83461.29, Sx=3479.35, Zx=3929.03,
                             rx=15.04, Iy=13900.00, Sy=986.45, Zy=1509.68, ry=6.15, J=109.03, Cw=1076129.28, ho=46.00,
                             Fy=3515, Fu=4570)
w18x175 = PropiedadesPerfilW(d=47.50, bf=28.19, tf=1.83, tw=1.19, A=335.48, Ix=75547.10, Sx=3181.94, Zx=3584.52,
                             rx=15.01, Iy=12566.45, Sy=891.61, Zy=1364.52, ry=6.12, J=83.87, Cw=967096.32, ho=45.67,
                             Fy=3515, Fu=4570)
w18x158 = PropiedadesPerfilW(d=46.99, bf=28.19, tf=1.65, tw=1.09, A=303.23, Ix=67966.45, Sx=2893.55, Zx=3254.84,
                             rx=14.96, Iy=11316.77, Sy=803.23, Zy=1228.39, ry=6.10, J=63.87, Cw=867096.32, ho=45.34,
                             Fy=3515, Fu=4570)
w18x143 = PropiedadesPerfilW(d=46.48, bf=27.94, tf=1.47, tw=0.99, A=274.19, Ix=60551.61, Sx=2605.81, Zx=2927.74,
                             rx=14.86, Iy=10066.45, Sy=720.65, Zy=1101.29, ry=6.05, J=47.10, Cw=768193.92, ho=45.01,
                             Fy=3515, Fu=4570)
w18x130 = PropiedadesPerfilW(d=45.97, bf=27.69, tf=1.32, tw=0.89, A=249.03, Ix=54303.23, Sx=2362.58, Zx=2651.61,
                             rx=14.78, Iy=8983.87, Sy=649.68, Zy=990.32, ry=6.00, J=35.48, Cw=679354.56, ho=44.65,
                             Fy=3515, Fu=4570)
w18x119 = PropiedadesPerfilW(d=45.72, bf=27.94, tf=1.19, tw=0.81, A=228.39, Ix=49221.94, Sx=2153.55, Zx=2415.48,
                             rx=14.68, Iy=8180.65, Sy=585.81, Zy=893.55, ry=5.99, J=26.45, Cw=611225.28, ho=44.53,
                             Fy=3515, Fu=4570)
w18x106 = PropiedadesPerfilW(d=45.21, bf=27.69, tf=1.04, tw=0.74, A=203.23, Ix=43140.65, Sx=1909.68, Zx=2138.71,
                             rx=14.58, Iy=7127.74, Sy=514.84, Zy=785.81, ry=5.92, J=18.39, Cw=523870.72, ho=44.17,
                             Fy=3515, Fu=4570)
w18x97 = PropiedadesPerfilW(d=44.96, bf=27.94, tf=0.94, tw=0.66, A=185.81, Ix=38725.81, Sx=1724.52, Zx=1927.74,
                            rx=14.43, Iy=6427.74, Sy=460.00, Zy=702.58, ry=5.87, J=12.90, Cw=459354.56, ho=44.02,
                            Fy=3515, Fu=4570)
w18x86 = PropiedadesPerfilW(d=45.97, bf=27.94, tf=0.84, tw=0.58, A=165.16, Ix=34310.97, Sx=1493.55, Zx=1664.52,
                            rx=14.43, Iy=5764.52, Sy=412.90, Zy=630.97, ry=5.92, J=9.03, Cw=406451.52, ho=45.13,
                            Fy=3515, Fu=4570)
w18x76 = PropiedadesPerfilW(d=45.21, bf=27.94, tf=0.74, tw=0.53, A=145.81, Ix=30312.90, Sx=1341.29, Zx=1491.61,
                            rx=14.40, Iy=5101.29, Sy=365.16, Zy=556.13, ry=5.92, J=6.45, Cw=355806.08, ho=45.47,
                            Fy=3515, Fu=4570)
w18x71 = PropiedadesPerfilW(d=45.97, bf=19.05, tf=1.02, tw=0.61, A=136.13, Ix=29589.68, Sx=1288.39, Zx=1434.84,
                            rx=14.73, Iy=2393.55, Sy=251.61, Zy=389.68, ry=4.19, J=9.03, Cw=154838.56, ho=44.95,
                            Fy=3515, Fu=4570)
w18x65 = PropiedadesPerfilW(d=45.72, bf=19.05, tf=0.91, tw=0.53, A=124.52, Ix=26699.35, Sx=1169.03, Zx=1298.71,
                            rx=14.63, Iy=2143.87, Sy=225.16, Zy=347.74, ry=4.14, J=6.45, Cw=135483.84, ho=44.81,
                            Fy=3515, Fu=4570)
w18x60 = PropiedadesPerfilW(d=45.72, bf=19.05, tf=0.84, tw=0.51, A=114.84, Ix=24554.84, Sx=1075.48, Zx=1194.84,
                            rx=14.63, Iy=1977.42, Sy=207.74, Zy=320.65, ry=4.14, J=5.16, Cw=123870.72, ho=44.88,
                            Fy=3515, Fu=4570)
w18x55 = PropiedadesPerfilW(d=45.72, bf=19.05, tf=0.76, tw=0.46, A=105.16, Ix=22410.32, Sx=981.94, Zx=1090.97, rx=14.61,
                            Iy=1811.61, Sy=190.32, Zy=293.55, ry=4.14, J=3.87, Cw=112258.08, ho=44.96, Fy=3515, Fu=4570)
w18x50 = PropiedadesPerfilW(d=45.72, bf=19.05, tf=0.69, tw=0.41, A=95.48, Ix=20100.00, Sx=880.65, Zx=976.13, rx=14.50,
                            Iy=1645.16, Sy=172.90, Zy=266.45, ry=4.14, J=2.90, Cw=100645.44, ho=45.03, Fy=3515, Fu=4570)
w18x46 = PropiedadesPerfilW(d=45.97, bf=15.24, tf=0.79, tw=0.46, A=88.39, Ix=19393.55, Sx=844.52, Zx=936.77, rx=14.81,
                            Iy=973.55, Sy=127.74, Zy=199.35, ry=3.32, J=3.55, Cw=52258.08, ho=45.18, Fy=3515, Fu=4570)
w18x40 = PropiedadesPerfilW(d=45.47, bf=15.24, tf=0.69, tw=0.41, A=76.77, Ix=16783.87, Sx=739.35, Zx=818.71, rx=14.78,
                            Iy=835.48, Sy=109.68, Zy=171.61, ry=3.30, J=2.26, Cw=42580.80, ho=45.78, Fy=3515, Fu=4570)
w18x35 = PropiedadesPerfilW(d=44.96, bf=15.24, tf=0.61, tw=0.36, A=67.10, Ix=14472.26, Sx=644.52, Zx=710.97, rx=14.68,
                            Iy=719.35, Sy=94.52, Zy=147.74, ry=3.28, J=1.61, Cw=35483.84, ho=45.35, Fy=3515, Fu=4570)

# Serie W16
w16x100 = PropiedadesPerfilW(d=43.18, bf=25.40, tf=1.17, tw=0.76, A=191.61, Ix=41977.42, Sx=1945.16, Zx=2187.10,
                             rx=14.81, Iy=5931.61, Sy=467.10, Zy=717.42, ry=5.56, J=22.58, Cw=419354.56, ho=42.01,
                             Fy=3515, Fu=4570)
w16x89 = PropiedadesPerfilW(d=42.67, bf=25.40, tf=1.02, tw=0.66, A=170.32, Ix=36810.97, Sx=1725.81, Zx=1933.55,
                            rx=14.71, Iy=5185.81, Sy=408.39, Zy=626.45, ry=5.51, J=15.48, Cw=359354.56, ho=41.65,
                            Fy=3515, Fu=4570)
w16x77 = PropiedadesPerfilW(d=42.16, bf=25.40, tf=0.89, tw=0.58, A=147.74, Ix=31644.52, Sx=1502.58, Zx=1680.00,
                            rx=14.63, Iy=4440.00, Sy=349.68, Zy=536.77, ry=5.49, J=10.32, Cw=299354.56, ho=41.27,
                            Fy=3515, Fu=4570)
w16x67 = PropiedadesPerfilW(d=41.91, bf=25.40, tf=0.76, tw=0.51, A=128.39, Ix=27561.29, Sx=1316.13, Zx=1467.74,
                            rx=14.63, Iy=3860.00, Sy=304.52, Zy=466.45, ry=5.49, J=6.77, Cw=250967.04, ho=41.15,
                            Fy=3515, Fu=4570)
w16x57 = PropiedadesPerfilW(d=40.89, bf=18.03, tf=0.89, tw=0.53, A=109.03, Ix=23996.77, Sx=1174.19, Zx=1307.74,
                            rx=14.83, Iy=1811.61, Sy=201.29, Zy=312.90, ry=4.09, J=7.10, Cw=105225.28, ho=40.00,
                            Fy=3515, Fu=4570)
w16x50 = PropiedadesPerfilW(d=40.64, bf=18.03, tf=0.79, tw=0.46, A=95.48, Ix=21018.71, Sx=1035.48, Zx=1151.61, rx=14.83,
                            Iy=1562.58, Sy=173.55, Zy=269.68, ry=4.04, J=4.84, Cw=88387.20, ho=39.85, Fy=3515, Fu=4570)
w16x45 = PropiedadesPerfilW(d=40.39, bf=17.78, tf=0.71, tw=0.43, A=86.45, Ix=18790.32, Sx=931.61, Zx=1035.48, rx=14.76,
                            Iy=1396.77, Sy=157.42, Zy=244.52, ry=4.01, J=3.55, Cw=78064.64, ho=39.68, Fy=3515, Fu=4570)
w16x40 = PropiedadesPerfilW(d=40.64, bf=17.78, tf=0.66, tw=0.41, A=76.77, Ix=17145.16, Sx=844.52, Zx=938.71, rx=14.93,
                            Iy=1314.84, Sy=148.39, Zy=230.32, ry=4.14, J=2.90, Cw=73548.48, ho=39.98, Fy=3515, Fu=4570)
w16x36 = PropiedadesPerfilW(d=40.39, bf=17.78, tf=0.58, tw=0.36, A=69.03, Ix=15251.61, Sx=756.77, Zx=838.71, rx=14.86,
                            Iy=1149.03, Sy=129.68, Zy=201.29, ry=4.09, J=2.10, Cw=63548.48, ho=39.81, Fy=3515, Fu=4570)
w16x31 = PropiedadesPerfilW(d=39.88, bf=14.02, tf=0.61, tw=0.38, A=59.35, Ix=13357.42, Sx=670.32, Zx=739.35, rx=15.01,
                            Iy=635.48, Sy=90.65, Zy=142.58, ry=3.28, J=1.94, Cw=31612.80, ho=39.27, Fy=3515, Fu=4570)
w16x26 = PropiedadesPerfilW(d=39.37, bf=13.97, tf=0.51, tw=0.30, A=49.68, Ix=10883.87, Sx=553.55, Zx=607.74, rx=14.81,
                            Iy=518.71, Sy=74.19, Zy=116.13, ry=3.23, J=1.13, Cw=24709.12, ho=38.86, Fy=3515, Fu=4570)

# Serie W14
w14x808 = PropiedadesPerfilW(d=45.21, bf=43.18, tf=7.62, tw=4.83, A=1548.39, Ix=330225.81, Sx=14612.90, Zx=16677.42,
                             rx=14.61, Iy=99900.00, Sy=4627.74, Zy=7154.84, ry=8.03, J=1619.35, Cw=6667096.32, ho=37.59,
                             Fy=3515, Fu=4570)
w14x730 = PropiedadesPerfilW(d=43.43, bf=42.42, tf=6.81, tw=4.32, A=1398.71, Ix=286354.84, Sx=13193.55, Zx=15000.00,
                             rx=14.30, Iy=86066.45, Sy=4058.06, Zy=6280.65, ry=7.85, J=1258.06, Cw=5667096.32, ho=36.62,
                             Fy=3515, Fu=4570)
w14x665 = PropiedadesPerfilW(d=42.16, bf=41.66, tf=6.22, tw=3.94, A=1274.19, Ix=255193.55, Sx=12109.68, Zx=13774.19,
                             rx=14.17, Iy=75464.52, Sy=3622.58, Zy=5612.90, ry=7.70, J=1019.35, Cw=4800000.00, ho=35.94,
                             Fy=3515, Fu=4570)
w14x605 = PropiedadesPerfilW(d=40.89, bf=41.15, tf=5.64, tw=3.58, A=1159.35, Ix=226354.84, Sx=11070.97, Zx=12580.65,
                             rx=13.97, Iy=66150.00, Sy=3216.13, Zy=4983.87, ry=7.55, J=829.03, Cw=4100000.00, ho=35.25,
                             Fy=3515, Fu=4570)
w14x550 = PropiedadesPerfilW(d=39.62, bf=40.39, tf=5.13, tw=3.25, A=1054.84, Ix=199193.55, Sx=10051.61, Zx=11419.35,
                             rx=13.74, Iy=57483.87, Sy=2848.39, Zy=4415.48, ry=7.39, J=667.74, Cw=3467096.32, ho=34.49,
                             Fy=3515, Fu=4570)
w14x500 = PropiedadesPerfilW(d=38.61, bf=39.88, tf=4.65, tw=2.95, A=958.06, Ix=176612.90, Sx=9148.39, Zx=10387.10,
                             rx=13.57, Iy=50483.87, Sy=2532.26, Zy=3925.81, ry=7.26, J=541.29, Cw=2967096.32, ho=33.96,
                             Fy=3515, Fu=4570)
w14x455 = PropiedadesPerfilW(d=37.59, bf=39.37, tf=4.24, tw=2.69, A=872.26, Ix=156612.90, Sx=8332.26, Zx=9451.61,
                             rx=13.41, Iy=44150.00, Sy=2243.87, Zy=3477.42, ry=7.11, J=438.71, Cw=2534193.92, ho=33.35,
                             Fy=3515, Fu=4570)
w14x426 = PropiedadesPerfilW(d=36.83, bf=39.12, tf=3.94, tw=2.51, A=816.77, Ix=145193.55, Sx=7887.74, Zx=8935.48,
                             rx=13.34, Iy=40566.45, Sy=2074.19, Zy=3215.48, ry=7.04, J=379.35, Cw=2267096.32, ho=32.89,
                             Fy=3515, Fu=4570)
w14x398 = PropiedadesPerfilW(d=36.07, bf=38.61, tf=3.68, tw=2.34, A=763.23, Ix=133612.90, Sx=7406.45, Zx=8387.10,
                             rx=13.23, Iy=37150.00, Sy=1925.16, Zy=2983.87, ry=6.98, J=319.35, Cw=2000000.00, ho=32.39,
                             Fy=3515, Fu=4570)
w14x370 = PropiedadesPerfilW(d=35.56, bf=38.35, tf=3.40, tw=2.16, A=709.68, Ix=122612.90, Sx=6896.77, Zx=7806.45,
                             rx=13.16, Iy=33900.00, Sy=1767.74, Zy=2738.71, ry=6.91, J=267.74, Cw=1767096.32, ho=32.16,
                             Fy=3515, Fu=4570)
w14x342 = PropiedadesPerfilW(d=34.80, bf=37.85, tf=3.15, tw=2.01, A=656.13, Ix=112196.77, Sx=6451.61, Zx=7287.10,
                             rx=13.08, Iy=30650.00, Sy=1619.35, Zy=2509.68, ry=6.83, J=225.81, Cw=1567096.32, ho=31.65,
                             Fy=3515, Fu=4570)
w14x311 = PropiedadesPerfilW(d=34.04, bf=37.34, tf=2.87, tw=1.83, A=596.13, Ix=101032.26, Sx=5935.48, Zx=6700.00,
                             rx=13.01, Iy=27150.00, Sy=1454.84, Zy=2254.84, ry=6.76, J=183.87, Cw=1367096.32, ho=31.17,
                             Fy=3515, Fu=4570)
w14x283 = PropiedadesPerfilW(d=33.53, bf=36.83, tf=2.62, tw=1.68, A=542.58, Ix=90612.90, Sx=5406.45, Zx=6106.45,
                             rx=12.93, Iy=24233.87, Sy=1316.13, Zy=2041.94, ry=6.68, J=150.00, Cw=1200000.00, ho=30.91,
                             Fy=3515, Fu=4570)
w14x257 = PropiedadesPerfilW(d=32.77, bf=36.32, tf=2.39, tw=1.52, A=492.26, Ix=81032.26, Sx=4951.61, Zx=5580.65,
                             rx=12.85, Iy=21650.00, Sy=1193.55, Zy=1848.39, ry=6.63, J=122.58, Cw=1034193.92, ho=30.38,
                             Fy=3515, Fu=4570)
w14x233 = PropiedadesPerfilW(d=32.26, bf=35.81, tf=2.16, tw=1.37, A=447.10, Ix=72612.90, Sx=4503.23, Zx=5077.42,
                             rx=12.75, Iy=19400.00, Sy=1083.87, Zy=1677.42, ry=6.58, J=99.35, Cw=901290.24, ho=30.10,
                             Fy=3515, Fu=4570)
w14x211 = PropiedadesPerfilW(d=31.75, bf=35.56, tf=1.96, tw=1.24, A=404.52, Ix=65032.26, Sx=4096.77, Zx=4612.90,
                             rx=12.68, Iy=17400.00, Sy=977.42, Zy=1512.90, ry=6.55, J=79.35, Cw=787096.32, ho=29.79,
                             Fy=3515, Fu=4570)
w14x193 = PropiedadesPerfilW(d=31.24, bf=35.05, tf=1.78, tw=1.14, A=370.32, Ix=58532.26, Sx=3748.39, Zx=4219.35,
                             rx=12.58, Iy=15650.00, Sy=893.55, Zy=1380.65, ry=6.50, J=64.52, Cw=687096.32, ho=29.46,
                             Fy=3515, Fu=4570)
w14x176 = PropiedadesPerfilW(d=30.73, bf=34.80, tf=1.63, tw=1.04, A=337.42, Ix=52612.90, Sx=3425.81, Zx=3854.84,
                             rx=12.50, Iy=14150.00, Sy=813.55, Zy=1258.06, ry=6.48, J=52.58, Cw=600000.00, ho=29.10,
                             Fy=3515, Fu=4570)
w14x159 = PropiedadesPerfilW(d=30.23, bf=34.29, tf=1.47, tw=0.94, A=305.16, Ix=46780.65, Sx=3096.77, Zx=3480.65,
                             rx=12.40, Iy=12650.00, Sy=738.71, Zy=1141.94, ry=6.43, J=42.58, Cw=520000.00, ho=28.76,
                             Fy=3515, Fu=4570)
w14x145 = PropiedadesPerfilW(d=29.97, bf=39.88, tf=1.32, tw=0.84, A=278.06, Ix=42532.26, Sx=2838.71, Zx=3193.55,
                             rx=12.37, Iy=11483.87, Sy=576.13, Zy=893.55, ry=6.43, J=34.19, Cw=453548.16, ho=28.65,
                             Fy=3515, Fu=4570)
w14x132 = PropiedadesPerfilW(d=29.46, bf=39.62, tf=1.19, tw=0.76, A=253.55, Ix=38283.87, Sx=2600.00, Zx=2919.35,
                             rx=12.30, Iy=10316.13, Sy=520.65, Zy=806.45, ry=6.38, J=27.10, Cw=399354.56, ho=28.27,
                             Fy=3515, Fu=4570)
w14x120 = PropiedadesPerfilW(d=29.21, bf=39.37, tf=1.07, tw=0.69, A=230.97, Ix=34533.87, Sx=2367.74, Zx=2654.84,
                             rx=12.22, Iy=9316.13, Sy=473.55, Zy=733.55, ry=6.35, J=21.29, Cw=351612.80, ho=28.14,
                             Fy=3515, Fu=4570)
w14x109 = PropiedadesPerfilW(d=28.96, bf=39.12, tf=0.97, tw=0.61, A=209.03, Ix=31033.87, Sx=2141.94, Zx=2400.00,
                             rx=12.17, Iy=8400.00, Sy=429.68, Zy=664.52, ry=6.33, J=16.13, Cw=308387.20, ho=27.99,
                             Fy=3515, Fu=4570)
w14x99 = PropiedadesPerfilW(d=28.45, bf=38.61, tf=0.89, tw=0.56, A=190.32, Ix=27783.87, Sx=1954.84, Zx=2187.10,
                            rx=12.09, Iy=7566.45, Sy=391.61, Zy=606.45, ry=6.30, J=12.26, Cw=270967.04, ho=27.56,
                            Fy=3515, Fu=4570)
w14x90 = PropiedadesPerfilW(d=28.19, bf=38.35, tf=0.79, tw=0.51, A=172.90, Ix=24866.45, Sx=1764.52, Zx=1974.19,
                            rx=12.00, Iy=6816.13, Sy=355.48, Zy=550.00, ry=6.27, J=8.71, Cw=235483.84, ho=27.40,
                            Fy=3515, Fu=4570)
w14x82 = PropiedadesPerfilW(d=27.94, bf=25.40, tf=0.89, tw=0.51, A=157.42, Ix=22700.00, Sx=1625.81, Zx=1816.13,
                            rx=12.01, Iy=3150.00, Sy=248.39, Zy=385.81, ry=4.47, J=9.68, Cw=119354.56, ho=27.05,
                            Fy=3515, Fu=4570)
w14x74 = PropiedadesPerfilW(d=27.94, bf=25.40, tf=0.79, tw=0.46, A=142.58, Ix=20366.45, Sx=1458.06, Zx=1625.81,
                            rx=11.96, Iy=2816.13, Sy=221.94, Zy=344.52, ry=4.45, J=6.77, Cw=104129.28, ho=27.15,
                            Fy=3515, Fu=4570)
w14x68 = PropiedadesPerfilW(d=27.69, bf=25.40, tf=0.74, tw=0.41, A=130.32, Ix=18533.87, Sx=1341.29, Zx=1496.13,
                            rx=11.91, Iy=2566.45, Sy=202.58, Zy=314.19, ry=4.42, J=5.16, Cw=93548.48, ho=26.95, Fy=3515,
                            Fu=4570)
w14x61 = PropiedadesPerfilW(d=27.43, bf=25.15, tf=0.66, tw=0.38, A=117.42, Ix=16450.00, Sx=1200.00, Zx=1335.48,
                            rx=11.84, Iy=2266.45, Sy=180.65, Zy=280.65, ry=4.39, J=3.55, Cw=80000.00, ho=26.77, Fy=3515,
                            Fu=4570)
w14x53 = PropiedadesPerfilW(d=33.02, bf=20.32, tf=0.66, tw=0.36, A=101.29, Ix=14533.87, Sx=880.65, Zx=983.87, rx=11.99,
                            Iy=1066.45, Sy=105.16, Zy=164.52, ry=3.25, J=3.55, Cw=32580.80, ho=32.36, Fy=3515, Fu=4570)
w14x48 = PropiedadesPerfilW(d=32.77, bf=20.32, tf=0.61, tw=0.33, A=91.61, Ix=13150.00, Sx=803.23, Zx=896.77, rx=11.96,
                            Iy=966.45, Sy=95.48, Zy=149.68, ry=3.25, J=2.58, Cw=28387.20, ho=32.16, Fy=3515, Fu=4570)
w14x43 = PropiedadesPerfilW(d=32.26, bf=20.32, tf=0.53, tw=0.30, A=82.58, Ix=11566.45, Sx=718.06, Zx=800.00, rx=11.84,
                            Iy=850.00, Sy=83.87, Zy=131.61, ry=3.20, J=2.10, Cw=24129.28, ho=31.73, Fy=3515, Fu=4570)
w14x38 = PropiedadesPerfilW(d=37.85, bf=17.02, tf=0.51, tw=0.30, A=72.90, Ix=10650.00, Sx=563.23, Zx=628.39, rx=12.09,
                            Iy=434.84, Sy=51.13, Zy=80.65, ry=2.44, J=1.61, Cw=9677.52, ho=37.34, Fy=3515, Fu=4570)
w14x34 = PropiedadesPerfilW(d=35.56, bf=16.76, tf=0.46, tw=0.28, A=65.16, Ix=9400.00, Sx=529.03, Zx=589.03, rx=12.01,
                            Iy=385.81, Sy=46.13, Zy=72.26, ry=2.44, J=1.29, Cw=8387.20, ho=35.10, Fy=3515, Fu=4570)
w14x30 = PropiedadesPerfilW(d=35.05, bf=16.51, tf=0.41, tw=0.25, A=57.42, Ix=8150.00, Sx=465.16, Zx=516.77, rx=11.91,
                            Iy=333.87, Sy=40.65, Zy=63.87, ry=2.41, J=0.97, Cw=7096.32, ho=34.64, Fy=3515, Fu=4570)
w14x26 = PropiedadesPerfilW(d=34.80, bf=12.70, tf=0.46, tw=0.25, A=49.68, Ix=7233.87, Sx=415.48, Zx=462.58, rx=12.09,
                            Iy=186.45, Sy=29.35, Zy=46.45, ry=1.94, J=0.97, Cw=3225.60, ho=34.34, Fy=3515, Fu=4570)
w14x22 = PropiedadesPerfilW(d=34.29, bf=12.70, tf=0.38, tw=0.23, A=42.58, Ix=6066.45, Sx=354.19, Zx=393.55, rx=11.96,
                            Iy=155.48, Sy=24.52, Zy=38.71, ry=1.91, J=0.65, Cw=2580.80, ho=33.91, Fy=3515, Fu=4570)

# Serie W12
w12x336 = PropiedadesPerfilW(d=34.29, bf=32.26, tf=3.00, tw=1.91, A=644.52, Ix=93033.87, Sx=5429.03, Zx=6193.55,
                             rx=12.01, Iy=23233.87, Sy=1441.94, Zy=2225.81, ry=6.00, J=200.00, Cw=1300000.00, ho=31.29,
                             Fy=3515, Fu=4570)
w12x305 = PropiedadesPerfilW(d=33.53, bf=31.75, tf=2.74, tw=1.75, A=585.81, Ix=83866.45, Sx=5006.45, Zx=5706.45,
                             rx=11.96, Iy=20650.00, Sy=1300.00, Zy=2006.45, ry=5.94, J=161.29, Cw=1134193.92, ho=30.79,
                             Fy=3515, Fu=4570)
w12x279 = PropiedadesPerfilW(d=32.77, bf=31.50, tf=2.49, tw=1.60, A=535.48, Ix=75700.00, Sx=4622.58, Zx=5258.06,
                             rx=11.89, Iy=18400.00, Sy=1167.74, Zy=1800.00, ry=5.87, J=130.97, Cw=1001290.24, ho=30.28,
                             Fy=3515, Fu=4570)
w12x252 = PropiedadesPerfilW(d=32.26, bf=30.99, tf=2.26, tw=1.45, A=483.87, Ix=67866.45, Sx=4209.68, Zx=4787.10,
                             rx=11.84, Iy=16400.00, Sy=1058.06, Zy=1632.26, ry=5.82, J=105.81, Cw=887096.32, ho=30.00,
                             Fy=3515, Fu=4570)
w12x230 = PropiedadesPerfilW(d=31.75, bf=30.48, tf=2.06, tw=1.32, A=441.29, Ix=61450.00, Sx=3870.97, Zx=4403.23,
                             rx=11.81, Iy=14733.87, Sy=967.74, Zy=1490.32, ry=5.77, J=86.45, Cw=787096.32, ho=29.69,
                             Fy=3515, Fu=4570)
w12x210 = PropiedadesPerfilW(d=31.24, bf=30.23, tf=1.88, tw=1.19, A=403.23, Ix=55533.87, Sx=3554.84, Zx=4038.71,
                             rx=11.73, Iy=13233.87, Sy=875.48, Zy=1348.39, ry=5.72, J=69.68, Cw=687096.32, ho=29.36,
                             Fy=3515, Fu=4570)
w12x190 = PropiedadesPerfilW(d=30.73, bf=29.72, tf=1.70, tw=1.09, A=364.52, Ix=49700.00, Sx=3235.48, Zx=3677.42,
                             rx=11.68, Iy=11816.13, Sy=795.48, Zy=1225.81, ry=5.69, J=56.13, Cw=600000.00, ho=29.03,
                             Fy=3515, Fu=4570)
w12x170 = PropiedadesPerfilW(d=30.48, bf=29.21, tf=1.52, tw=0.97, A=326.45, Ix=43866.45, Sx=2880.65, Zx=3270.97,
                             rx=11.59, Iy=10400.00, Sy=712.90, Zy=1096.77, ry=5.64, J=43.87, Cw=520000.00, ho=28.96,
                             Fy=3515, Fu=4570)
w12x152 = PropiedadesPerfilW(d=29.97, bf=28.96, tf=1.35, tw=0.87, A=291.61, Ix=38700.00, Sx=2583.87, Zx=2929.03,
                             rx=11.51, Iy=9233.87, Sy=637.42, Zy=980.65, ry=5.61, J=33.55, Cw=451612.80, ho=28.62,
                             Fy=3515, Fu=4570)
w12x136 = PropiedadesPerfilW(d=29.72, bf=28.45, tf=1.22, tw=0.79, A=260.65, Ix=34533.87, Sx=2325.81, Zx=2635.48,
                             rx=11.51, Iy=8233.87, Sy=579.35, Zy=890.32, ry=5.61, J=26.77, Cw=399354.56, ho=28.50,
                             Fy=3515, Fu=4570)
w12x120 = PropiedadesPerfilW(d=29.21, bf=28.19, tf=1.07, tw=0.71, A=230.32, Ix=30033.87, Sx=2058.06, Zx=2332.26,
                             rx=11.40, Iy=7150.00, Sy=507.74, Zy=780.65, ry=5.56, J=19.35, Cw=339354.56, ho=28.14,
                             Fy=3515, Fu=4570)
w12x106 = PropiedadesPerfilW(d=28.70, bf=27.94, tf=0.94, tw=0.61, A=203.23, Ix=25866.45, Sx=1803.23, Zx=2041.94,
                             rx=11.28, Iy=6150.00, Sy=440.65, Zy=677.42, ry=5.49, J=13.55, Cw=279354.56, ho=27.76,
                             Fy=3515, Fu=4570)
w12x96 = PropiedadesPerfilW(d=28.45, bf=27.69, tf=0.86, tw=0.56, A=184.52, Ix=23533.87, Sx=1654.84, Zx=1867.74,
                            rx=11.28, Iy=5600.00, Sy=404.52, Zy=622.58, ry=5.51, J=10.65, Cw=249354.56, ho=27.59,
                            Fy=3515, Fu=4570)
w12x87 = PropiedadesPerfilW(d=28.19, bf=27.43, tf=0.76, tw=0.51, A=167.10, Ix=21200.00, Sx=1503.23, Zx=1696.77,
                            rx=11.25, Iy=5033.87, Sy=367.10, Zy=564.52, ry=5.49, J=7.74, Cw=219354.56, ho=27.43,
                            Fy=3515, Fu=4570)
w12x79 = PropiedadesPerfilW(d=27.94, bf=27.18, tf=0.69, tw=0.47, A=151.61, Ix=19200.00, Sx=1374.19, Zx=1548.39,
                            rx=11.25, Iy=4566.45, Sy=336.13, Zy=516.77, ry=5.49, J=5.81, Cw=195483.84, ho=27.25,
                            Fy=3515, Fu=4570)
w12x72 = PropiedadesPerfilW(d=27.69, bf=26.67, tf=0.64, tw=0.43, A=138.06, Ix=17533.87, Sx=1267.74, Zx=1425.81,
                            rx=11.25, Iy=4150.00, Sy=311.61, Zy=479.35, ry=5.49, J=4.52, Cw=175483.84, ho=27.05,
                            Fy=3515, Fu=4570)
w12x65 = PropiedadesPerfilW(d=27.43, bf=26.42, tf=0.58, tw=0.39, A=124.52, Ix=15700.00, Sx=1145.16, Zx=1287.10,
                            rx=11.23, Iy=3733.87, Sy=282.58, Zy=435.48, ry=5.48, J=3.55, Cw=155483.84, ho=26.85,
                            Fy=3515, Fu=4570)
w12x58 = PropiedadesPerfilW(d=27.18, bf=25.40, tf=0.53, tw=0.36, A=111.61, Ix=14033.87, Sx=1032.26, Zx=1161.29,
                            rx=11.20, Iy=3350.00, Sy=264.52, Zy=406.45, ry=5.48, J=2.58, Cw=139354.56, ho=26.65,
                            Fy=3515, Fu=4570)
w12x53 = PropiedadesPerfilW(d=30.48, bf=25.40, tf=0.51, tw=0.35, A=101.29, Ix=12700.00, Sx=832.26, Zx=935.48, rx=11.20,
                            Iy=3033.87, Sy=239.35, Zy=367.74, ry=5.48, J=2.26, Cw=126451.52, ho=29.97, Fy=3515, Fu=4570)
w12x50 = PropiedadesPerfilW(d=30.23, bf=20.32, tf=0.64, tw=0.38, A=95.48, Ix=12200.00, Sx=807.74, Zx=906.45, rx=11.30,
                            Iy=1500.00, Sy=147.74, Zy=230.97, ry=3.96, J=3.23, Cw=57096.32, ho=29.59, Fy=3515, Fu=4570)
w12x45 = PropiedadesPerfilW(d=29.97, bf=20.32, tf=0.58, tw=0.33, A=86.45, Ix=10933.87, Sx=729.68, Zx=819.35, rx=11.25,
                            Iy=1350.00, Sy=133.55, Zy=208.39, ry=3.96, J=2.26, Cw=49354.56, ho=29.39, Fy=3515, Fu=4570)
w12x40 = PropiedadesPerfilW(d=29.72, bf=20.32, tf=0.51, tw=0.30, A=76.77, Ix=9700.00, Sx=653.55, Zx=732.90, rx=11.23,
                            Iy=1200.00, Sy=118.71, Zy=185.81, ry=3.96, J=1.61, Cw=42580.80, ho=29.21, Fy=3515, Fu=4570)
w12x35 = PropiedadesPerfilW(d=30.48, bf=16.51, tf=0.53, tw=0.30, A=67.10, Ix=8866.45, Sx=581.94, Zx=653.55, rx=11.51,
                            Iy=633.87, Sy=76.77, Zy=120.65, ry=3.07, J=1.61, Cw=19354.56, ho=29.95, Fy=3515, Fu=4570)
w12x30 = PropiedadesPerfilW(d=30.23, bf=16.51, tf=0.44, tw=0.26, A=57.42, Ix=7566.45, Sx=500.65, Zx=561.29, rx=11.46,
                            Iy=533.87, Sy=64.52, Zy=101.29, ry=3.05, J=1.13, Cw=15483.84, ho=29.79, Fy=3515, Fu=4570)
w12x26 = PropiedadesPerfilW(d=29.97, bf=16.51, tf=0.38, tw=0.23, A=49.68, Ix=6533.87, Sx=436.77, Zx=489.03, rx=11.46,
                            Iy=458.06, Sy=55.48, Zy=87.10, ry=3.04, J=0.81, Cw=12580.80, ho=29.59, Fy=3515, Fu=4570)
w12x22 = PropiedadesPerfilW(d=29.72, bf=10.16, tf=0.43, tw=0.26, A=42.58, Ix=5700.00, Sx=384.52, Zx=430.97, rx=11.56,
                            Iy=166.45, Sy=32.77, Zy=51.61, ry=1.98, J=0.81, Cw=2580.80, ho=29.29, Fy=3515, Fu=4570)
w12x19 = PropiedadesPerfilW(d=29.46, bf=10.16, tf=0.36, tw=0.24, A=36.77, Ix=4900.00, Sx=333.55, Zx=373.55, rx=11.53,
                            Iy=141.29, Sy=27.87, Zy=43.87, ry=1.96, J=0.65, Cw=2096.32, ho=29.10, Fy=3515, Fu=4570)
w12x16 = PropiedadesPerfilW(d=29.21, bf=10.16, tf=0.28, tw=0.23, A=30.65, Ix=4066.45, Sx=279.35, Zx=312.26, rx=11.51,
                            Iy=116.13, Sy=22.90, Zy=36.13, ry=1.94, J=0.48, Cw=1612.80, ho=28.93, Fy=3515, Fu=4570)
w12x14 = PropiedadesPerfilW(d=28.96, bf=10.16, tf=0.23, tw=0.20, A=26.45, Ix=3500.00, Sx=241.94, Zx=270.32, rx=11.51,
                            Iy=98.71, Sy=19.35, Zy=30.65, ry=1.93, J=0.32, Cw=1290.24, ho=28.73, Fy=3515, Fu=4570)

# Serie W10
w10x112 = PropiedadesPerfilW(d=28.70, bf=25.65, tf=1.24, tw=0.76, A=214.84, Ix=26700.00, Sx=1861.29, Zx=2112.90,
                             rx=11.15, Iy=5900.00, Sy=460.65, Zy=716.13, ry=5.23, J=28.39, Cw=287096.32, ho=27.46,
                             Fy=3515, Fu=4570)
w10x100 = PropiedadesPerfilW(d=28.19, bf=25.40, tf=1.12, tw=0.69, A=191.61, Ix=23900.00, Sx=1696.77, Zx=1925.81,
                             rx=11.15, Iy=5283.87, Sy=416.13, Zy=645.16, ry=5.23, J=21.94, Cw=251612.80, ho=27.07,
                             Fy=3515, Fu=4570)
w10x88 = PropiedadesPerfilW(d=27.69, bf=25.40, tf=0.99, tw=0.61, A=168.39, Ix=21033.87, Sx=1519.35, Zx=1722.58,
                            rx=11.15, Iy=4650.00, Sy=366.45, Zy=567.74, ry=5.26, J=16.13, Cw=215483.84, ho=26.70,
                            Fy=3515, Fu=4570)
w10x77 = PropiedadesPerfilW(d=27.18, bf=25.15, tf=0.87, tw=0.53, A=147.74, Ix=18300.00, Sx=1348.39, Zx=1525.81,
                            rx=11.12, Iy=4066.45, Sy=323.87, Zy=501.29, ry=5.26, J=11.29, Cw=183870.72, ho=26.31,
                            Fy=3515, Fu=4570)
w10x68 = PropiedadesPerfilW(d=26.92, bf=25.15, tf=0.76, tw=0.46, A=130.97, Ix=15900.00, Sx=1182.58, Zx=1335.48,
                            rx=11.02, Iy=3533.87, Sy=281.29, Zy=435.48, ry=5.20, J=7.74, Cw=155483.84, ho=26.16,
                            Fy=3515, Fu=4570)
w10x60 = PropiedadesPerfilW(d=26.42, bf=25.15, tf=0.66, tw=0.41, A=115.48, Ix=13733.87, Sx=1041.94, Zx=1177.42,
                            rx=10.90, Iy=3033.87, Sy=241.94, Zy=374.19, ry=5.13, J=5.16, Cw=127096.32, ho=25.76,
                            Fy=3515, Fu=4570)
w10x54 = PropiedadesPerfilW(d=26.16, bf=25.15, tf=0.59, tw=0.37, A=103.87, Ix=12200.00, Sx=933.55, Zx=1054.84, rx=10.85,
                            Iy=2700.00, Sy=215.48, Zy=333.55, ry=5.10, J=3.87, Cw=111225.28, ho=25.57, Fy=3515, Fu=4570)
w10x49 = PropiedadesPerfilW(d=25.91, bf=25.15, tf=0.56, tw=0.34, A=94.19, Ix=11200.00, Sx=864.52, Zx=976.77, rx=10.90,
                            Iy=2500.00, Sy=198.71, Zy=308.39, ry=5.15, J=3.23, Cw=102580.80, ho=25.35, Fy=3515, Fu=4570)
w10x45 = PropiedadesPerfilW(d=25.65, bf=20.32, tf=0.62, tw=0.36, A=86.45, Ix=10166.45, Sx=793.55, Zx=896.77, rx=10.85,
                            Iy=1283.87, Sy=126.45, Zy=197.42, ry=3.86, J=3.55, Cw=49354.56, ho=25.03, Fy=3515, Fu=4570)
w10x39 = PropiedadesPerfilW(d=25.40, bf=20.07, tf=0.53, tw=0.32, A=75.48, Ix=8866.45, Sx=699.35, Zx=787.10, rx=10.85,
                            Iy=1116.13, Sy=111.61, Zy=174.19, ry=3.84, J=2.42, Cw=41612.80, ho=24.87, Fy=3515, Fu=4570)
w10x33 = PropiedadesPerfilW(d=24.89, bf=20.07, tf=0.43, tw=0.29, A=63.23, Ix=7400.00, Sx=595.48, Zx=670.32, rx=10.82,
                            Iy=933.87, Sy=93.23, Zy=145.81, ry=3.84, J=1.61, Cw=33548.48, ho=24.46, Fy=3515, Fu=4570)
w10x30 = PropiedadesPerfilW(d=25.65, bf=14.02, tf=0.51, tw=0.30, A=57.42, Ix=6866.45, Sx=536.13, Zx=606.45, rx=10.95,
                            Iy=391.61, Sy=55.81, Zy=87.74, ry=2.61, J=1.61, Cw=10000.00, ho=25.14, Fy=3515, Fu=4570)
w10x26 = PropiedadesPerfilW(d=25.40, bf=14.02, tf=0.44, tw=0.25, A=49.68, Ix=5933.87, Sx=467.74, Zx=528.39, rx=10.95,
                            Iy=333.87, Sy=47.74, Zy=74.84, ry=2.59, J=1.13, Cw=8064.64, ho=24.96, Fy=3515, Fu=4570)
w10x22 = PropiedadesPerfilW(d=25.15, bf=13.97, tf=0.36, tw=0.22, A=42.58, Ix=5033.87, Sx=400.65, Zx=451.61, rx=10.87,
                            Iy=283.87, Sy=40.65, Zy=63.87, ry=2.59, J=0.81, Cw=6451.52, ho=24.79, Fy=3515, Fu=4570)
w10x19 = PropiedadesPerfilW(d=26.16, bf=10.24, tf=0.39, tw=0.25, A=36.45, Ix=4466.45, Sx=341.94, Zx=385.81, rx=11.07,
                            Iy=133.87, Sy=26.13, Zy=41.29, ry=1.91, J=0.81, Cw=2580.80, ho=25.77, Fy=3515, Fu=4570)
w10x17 = PropiedadesPerfilW(d=25.91, bf=10.24, tf=0.33, tw=0.24, A=31.61, Ix=3866.45, Sx=298.71, Zx=337.42, rx=11.05,
                            Iy=114.19, Sy=22.32, Zy=35.48, ry=1.91, J=0.65, Cw=2096.32, ho=25.58, Fy=3515, Fu=4570)
w10x15 = PropiedadesPerfilW(d=25.65, bf=10.16, tf=0.27, tw=0.23, A=27.10, Ix=3300.00, Sx=257.42, Zx=290.97, rx=11.05,
                            Iy=96.77, Sy=19.10, Zy=30.32, ry=1.89, J=0.48, Cw=1612.80, ho=25.38, Fy=3515, Fu=4570)
w10x12 = PropiedadesPerfilW(d=25.27, bf=10.16, tf=0.21, tw=0.19, A=22.58, Ix=2700.00, Sx=213.55, Zx=241.29, rx=10.95,
                            Iy=79.35, Sy=15.65, Zy=24.84, ry=1.87, J=0.32, Cw=1290.24, ho=25.06, Fy=3515, Fu=4570)

# Serie W8
w8x67 = PropiedadesPerfilW(d=22.86, bf=20.96, tf=0.94, tw=0.58, A=128.39, Ix=9733.87, Sx=851.61, Zx=982.58, rx=8.71,
                           Iy=2116.13, Sy=202.58, Zy=318.71, ry=4.06, J=13.55, Cw=79354.56, ho=21.92, Fy=3515, Fu=4570)
w8x58 = PropiedadesPerfilW(d=22.35, bf=20.83, tf=0.81, tw=0.51, A=111.61, Ix=8366.45, Sx=748.39, Zx=861.29, rx=8.66,
                           Iy=1833.87, Sy=176.13, Zy=276.77, ry=4.06, J=9.03, Cw=66774.72, ho=21.54, Fy=3515, Fu=4570)
w8x48 = PropiedadesPerfilW(d=21.84, bf=20.57, tf=0.68, tw=0.40, A=92.26, Ix=6833.87, Sx=626.45, Zx=719.35, rx=8.61,
                           Iy=1500.00, Sy=145.81, Zy=229.03, ry=4.04, J=5.48, Cw=52258.08, ho=21.16, Fy=3515, Fu=4570)
w8x40 = PropiedadesPerfilW(d=21.59, bf=20.32, tf=0.56, tw=0.36, A=76.77, Ix=5600.00, Sx=519.35, Zx=596.77, rx=8.53,
                           Iy=1233.87, Sy=121.61, Zy=191.61, ry=4.01, J=3.23, Cw=41612.80, ho=21.03, Fy=3515, Fu=4570)
w8x35 = PropiedadesPerfilW(d=21.34, bf=20.32, tf=0.49, tw=0.31, A=67.10, Ix=4900.00, Sx=459.68, Zx=527.74, rx=8.56,
                           Iy=1083.87, Sy=106.77, Zy=168.39, ry=4.04, J=2.26, Cw=35483.84, ho=20.85, Fy=3515, Fu=4570)
w8x31 = PropiedadesPerfilW(d=20.32, bf=20.32, tf=0.43, tw=0.29, A=59.35, Ix=4333.87, Sx=427.10, Zx=489.68, rx=8.56,
                           Iy=966.45, Sy=95.16, Zy=149.68, ry=4.04, J=1.61, Cw=31612.80, ho=19.89, Fy=3515, Fu=4570)
w8x28 = PropiedadesPerfilW(d=20.57, bf=16.51, tf=0.52, tw=0.29, A=53.55, Ix=4000.00, Sx=389.03, Zx=446.45, rx=8.64,
                           Iy=466.45, Sy=56.45, Zy=88.71, ry=2.95, J=1.77, Cw=12580.80, ho=20.05, Fy=3515, Fu=4570)
w8x24 = PropiedadesPerfilW(d=20.32, bf=16.51, tf=0.43, tw=0.25, A=46.13, Ix=3466.45, Sx=341.94, Zx=391.61, rx=8.64,
                           Iy=400.00, Sy=48.39, Zy=75.81, ry=2.95, J=1.13, Cw=9677.52, ho=19.89, Fy=3515, Fu=4570)
w8x21 = PropiedadesPerfilW(d=21.08, bf=13.34, tf=0.40, tw=0.25, A=40.32, Ix=3100.00, Sx=294.84, Zx=337.42, rx=8.76,
                           Iy=216.13, Sy=32.42, Zy=50.97, ry=2.32, J=0.97, Cw=3870.72, ho=20.68, Fy=3515, Fu=4570)
w8x18 = PropiedadesPerfilW(d=20.83, bf=13.34, tf=0.33, tw=0.23, A=34.84, Ix=2633.87, Sx=253.55, Zx=290.32, rx=8.69,
                           Iy=183.87, Sy=27.58, Zy=43.55, ry=2.29, J=0.65, Cw=3064.64, ho=20.50, Fy=3515, Fu=4570)
w8x15 = PropiedadesPerfilW(d=20.57, bf=10.20, tf=0.32, tw=0.25, A=28.71, Ix=2300.00, Sx=223.87, Zx=255.48, rx=8.94,
                           Iy=100.65, Sy=19.74, Zy=31.29, ry=1.87, J=0.65, Cw=1290.24, ho=20.25, Fy=3515, Fu=4570)
w8x13 = PropiedadesPerfilW(d=20.32, bf=10.16, tf=0.25, tw=0.23, A=24.52, Ix=1933.87, Sx=190.97, Zx=217.42, rx=8.89,
                           Iy=83.87, Sy=16.52, Zy=26.13, ry=1.85, J=0.48, Cw=967.84, ho=20.07, Fy=3515, Fu=4570)
w8x10 = PropiedadesPerfilW(d=20.04, bf=10.01, tf=0.52, tw=0.43, A=19.10, Ix=1281.99, Sx=128, Zx=145, rx=8.18, Iy=86.99,
                           Sy=17, Zy=27, ry=2.14, J=1.77, Cw=8297.76, ho=19.5, Fy=3515, Fu=4570)

# Serie W6
w6x25 = PropiedadesPerfilW(d=16.00, bf=15.01, tf=0.46, tw=0.32, A=47.74, Ix=1316.13, Sx=164.52, Zx=193.55, rx=5.26,
                           Iy=283.87, Sy=37.90, Zy=59.35, ry=2.44, J=1.29, Cw=5806.08, ho=15.54, Fy=3515, Fu=4570)
w6x20 = PropiedadesPerfilW(d=15.49, bf=15.01, tf=0.36, tw=0.26, A=38.39, Ix=1033.87, Sx=133.55, Zx=156.77, rx=5.18,
                           Iy=224.52, Sy=29.90, Zy=46.77, ry=2.41, J=0.81, Cw=4193.92, ho=15.13, Fy=3515, Fu=4570)
w6x16 = PropiedadesPerfilW(d=15.24, bf=10.16, tf=0.40, tw=0.26, A=30.65, Ix=900.00, Sx=118.06, Zx=137.42, rx=5.41,
                           Iy=83.87, Sy=16.52, Zy=26.13, ry=1.65, J=0.81, Cw=967.84, ho=14.84, Fy=3515, Fu=4570)
w6x15 = PropiedadesPerfilW(d=14.99, bf=15.01, tf=0.28, tw=0.23, A=28.71, Ix=766.45, Sx=102.26, Zx=119.35, rx=5.16,
                           Iy=166.45, Sy=22.19, Zy=34.52, ry=2.41, J=0.48, Cw=2903.04, ho=14.71, Fy=3515, Fu=4570)
w6x12 = PropiedadesPerfilW(d=15.24, bf=10.16, tf=0.28, tw=0.23, A=22.90, Ix=666.45, Sx=87.42, Zx=101.94, rx=5.38,
                           Iy=66.45, Sy=13.10, Zy=20.65, ry=1.70, J=0.48, Cw=645.44, ho=14.96, Fy=3515, Fu=4570)
w6x9 = PropiedadesPerfilW(d=14.99, bf=10.01, tf=0.55, tw=0.43, A=17.29, Ix=483.87, Sx=65.81, Zx=76.77, rx=5.28, Iy=50.00,
                          Sy=10.10, Zy=15.81, ry=1.70, J=0.32, Cw=387.20, ho=14.51, Fy=3515, Fu=4570)

# Serie W5
w5x19 = PropiedadesPerfilW(d=12.95, bf=12.78, tf=1.09, tw=0.69, A=35.87, Ix=1094.69, Sx=167, Zx=190, rx=5.51,
                           Iy=380.02, Sy=59, Zy=91, ry=3.25, J=13.15, Cw=13668.48, ho=12.52, Fy=3515, Fu=4570)
w5x16 = PropiedadesPerfilW(d=12.73, bf=12.70, tf=0.91, tw=0.61, A=30.39, Ix=890.74, Sx=140, Zx=158, rx=5.41,
                           Iy=312.59, Sy=49, Zy=75, ry=3.2, J=7.99, Cw=10902.56, ho=12.34, Fy=3515, Fu=4570)

# Serie W4
w4x13 = PropiedadesPerfilW(d=10.57, bf=10.31, tf=0.88, tw=0.71, A=24.71, Ix=470.34, Sx=89, Zx=103, rx=4.37,
                           Iy=160.67, Sy=31, Zy=48, ry=2.54, J=6.29, Cw=3759.50, ho=10.32, Fy=3515, Fu=4570)

# =============================================================================
# DICCIONARIO DE PERFILES - ACCESO RÁPIDO
# =============================================================================

perfiles_w = {
    # W44
    'w44x335': w44x335, 'w44x290': w44x290, 'w44x230': w44x230,

    # W40
    'w40x503': w40x503, 'w40x397': w40x397, 'w40x331': w40x331,

    # W36
    'w36x300': w36x300, 'w36x232': w36x232, 'w36x194': w36x194,
    'w36x160': w36x160, 'w36x135': w36x135,

    # W33
    'w33x241': w33x241, 'w33x201': w33x201, 'w33x152': w33x152,
    'w33x130': w33x130, 'w33x118': w33x118,

    # W30
    'w30x211': w30x211, 'w30x173': w30x173, 'w30x132': w30x132,
    'w30x124': w30x124, 'w30x116': w30x116, 'w30x108': w30x108,
    'w30x99': w30x99, 'w30x90': w30x90,

    # W27
    'w27x178': w27x178, 'w27x146': w27x146, 'w27x114': w27x114,
    'w27x102': w27x102, 'w27x94': w27x94, 'w27x84': w27x84,

    # W24
    'w24x162': w24x162, 'w24x146': w24x146, 'w24x131': w24x131,
    'w24x117': w24x117, 'w24x104': w24x104, 'w24x94': w24x94,
    'w24x84': w24x84, 'w24x76': w24x76, 'w24x68': w24x68,
    'w24x62': w24x62, 'w24x55': w24x55,

    # W21
    'w21x201': w21x201, 'w21x182': w21x182, 'w21x166': w21x166,
    'w21x147': w21x147, 'w21x132': w21x132, 'w21x122': w21x122,
    'w21x111': w21x111, 'w21x101': w21x101, 'w21x93': w21x93,
    'w21x83': w21x83, 'w21x73': w21x73, 'w21x68': w21x68,
    'w21x62': w21x62, 'w21x57': w21x57, 'w21x50': w21x50,
    'w21x48': w21x48, 'w21x44': w21x44,

    # W18
    'w18x192': w18x192, 'w18x175': w18x175, 'w18x158': w18x158,
    'w18x143': w18x143, 'w18x130': w18x130, 'w18x119': w18x119,
    'w18x106': w18x106, 'w18x97': w18x97, 'w18x86': w18x86,
    'w18x76': w18x76, 'w18x71': w18x71, 'w18x65': w18x65,
    'w18x60': w18x60, 'w18x55': w18x55, 'w18x50': w18x50,
    'w18x46': w18x46, 'w18x40': w18x40, 'w18x35': w18x35,

    # W16
    'w16x100': w16x100, 'w16x89': w16x89, 'w16x77': w16x77,
    'w16x67': w16x67, 'w16x57': w16x57, 'w16x50': w16x50,
    'w16x45': w16x45, 'w16x40': w16x40, 'w16x36': w16x36,
    'w16x31': w16x31, 'w16x26': w16x26,

    # W14
    'w14x808': w14x808, 'w14x730': w14x730, 'w14x665': w14x665,
    'w14x605': w14x605, 'w14x550': w14x550, 'w14x500': w14x500,
    'w14x455': w14x455, 'w14x426': w14x426, 'w14x398': w14x398,
    'w14x370': w14x370, 'w14x342': w14x342, 'w14x311': w14x311,
    'w14x283': w14x283, 'w14x257': w14x257, 'w14x233': w14x233,
    'w14x211': w14x211, 'w14x193': w14x193, 'w14x176': w14x176,
    'w14x159': w14x159, 'w14x145': w14x145, 'w14x132': w14x132,
    'w14x120': w14x120, 'w14x109': w14x109, 'w14x99': w14x99,
    'w14x90': w14x90, 'w14x82': w14x82, 'w14x74': w14x74,
    'w14x68': w14x68, 'w14x61': w14x61, 'w14x53': w14x53,
    'w14x48': w14x48, 'w14x43': w14x43, 'w14x38': w14x38,
    'w14x34': w14x34, 'w14x30': w14x30, 'w14x26': w14x26,
    'w14x22': w14x22,

    # W12
    'w12x336': w12x336, 'w12x305': w12x305, 'w12x279': w12x279,
    'w12x252': w12x252, 'w12x230': w12x230, 'w12x210': w12x210,
    'w12x190': w12x190, 'w12x170': w12x170, 'w12x152': w12x152,
    'w12x136': w12x136, 'w12x120': w12x120, 'w12x106': w12x106,
    'w12x96': w12x96, 'w12x87': w12x87, 'w12x79': w12x79,
    'w12x72': w12x72, 'w12x65': w12x65, 'w12x58': w12x58,
    'w12x53': w12x53, 'w12x50': w12x50, 'w12x45': w12x45,
    'w12x40': w12x40, 'w12x35': w12x35, 'w12x30': w12x30,
    'w12x26': w12x26, 'w12x22': w12x22, 'w12x19': w12x19,
    'w12x16': w12x16, 'w12x14': w12x14,

    # W10
    'w10x112': w10x112, 'w10x100': w10x100, 'w10x88': w10x88,
    'w10x77': w10x77, 'w10x68': w10x68, 'w10x60': w10x60,
    'w10x54': w10x54, 'w10x49': w10x49, 'w10x45': w10x45,
    'w10x39': w10x39, 'w10x33': w10x33, 'w10x30': w10x30,
    'w10x26': w10x26, 'w10x22': w10x22, 'w10x19': w10x19,
    'w10x17': w10x17, 'w10x15': w10x15, 'w10x12': w10x12,

    # W8
    'w8x67': w8x67, 'w8x58': w8x58, 'w8x48': w8x48,
    'w8x40': w8x40, 'w8x35': w8x35, 'w8x31': w8x31,
    'w8x28': w8x28, 'w8x24': w8x24, 'w8x21': w8x21,
    'w8x18': w8x18, 'w8x15': w8x15, 'w8x13': w8x13,
    'w8x10': w8x10,

    # W6
    'w6x25': w6x25, 'w6x20': w6x20, 'w6x16': w6x16,
    'w6x15': w6x15, 'w6x12': w6x12, 'w6x9': w6x9,

    # W5
    'w5x19': w5x19, 'w5x16': w5x16,

    # W4
    'w4x13': w4x13,
}


# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def obtener_perfil(nombre):
    """
    Obtiene un perfil por su nombre.

    Parámetros:
    -----------
    nombre : str
        Nombre del perfil (ej: 'w8x10', 'W8X10', 'w8x10')

    Retorna:
    --------
    PropiedadesPerfilW : Objeto con las propiedades del perfil

    Ejemplo:
    --------
    >>> perfil = obtener_perfil('w8x10')
    >>> print(f"Área: {perfil.A} cm²")
    Área: 19.10 cm²
    """
    nombre_lower = nombre.lower()
    if nombre_lower in perfiles_w:
        return perfiles_w[nombre_lower]
    else:
        raise ValueError(f"Perfil '{nombre}' no encontrado. Use listar_perfiles() para ver disponibles.")


def listar_perfiles(serie=None):
    """
    Lista los perfiles disponibles, opcionalmente filtrados por serie.

    Parámetros:
    -----------
    serie : str, opcional
        Serie de perfiles a listar (ej: 'W8', 'W12'). Si no se especifica, lista todos.

    Retorna:
    --------
    list : Lista de nombres de perfiles disponibles

    Ejemplo:
    --------
    >>> listar_perfiles('W8')
    ['w8x10', 'w8x13', 'w8x15', 'w8x18', 'w8x21', ...]
    """
    if serie is None:
        return sorted(list(perfiles_w.keys()))
    else:
        serie_lower = serie.lower()
        return sorted([p for p in perfiles_w.keys() if p.startswith(serie_lower)])


def comparar_perfiles(nombre1, nombre2):
    """
    Compara las propiedades de dos perfiles.

    Parámetros:
    -----------
    nombre1 : str
        Nombre del primer perfil
    nombre2 : str
        Nombre del segundo perfil

    Ejemplo:
    --------
    >>> comparar_perfiles('w8x10', 'w8x13')
    """
    p1 = obtener_perfil(nombre1)
    p2 = obtener_perfil(nombre2)

    print(f"\n{'=' * 60}")
    print(f"Comparación entre {nombre1.upper()} y {nombre2.upper()}")
    print(f"{'=' * 60}")
    print(f"{'Propiedad':<15} {nombre1.upper():>15} {nombre2.upper():>15} {'Diferencia':>12}")
    print(f"{'-' * 60}")

    propiedades = ['d', 'bf', 'tf', 'tw', 'A', 'Ix', 'Iy', 'Sx', 'Sy', 'Zx', 'Zy', 'rx', 'ry']
    unidades = {
        'd': 'cm', 'bf': 'cm', 'tf': 'cm', 'tw': 'cm',
        'A': 'cm²', 'Ix': 'cm⁴', 'Iy': 'cm⁴',
        'Sx': 'cm³', 'Sy': 'cm³', 'Zx': 'cm³', 'Zy': 'cm³',
        'rx': 'cm', 'ry': 'cm'
    }

    for prop in propiedades:
        val1 = getattr(p1, prop)
        val2 = getattr(p2, prop)
        diff = ((val2 - val1) / val1) * 100
        print(f"{prop:<15} {val1:>15.2f} {val2:>15.2f} {diff:>11.1f}%")
