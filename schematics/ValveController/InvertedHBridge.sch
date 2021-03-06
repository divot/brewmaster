EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:ValveController-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L BC557 Q207
U 1 1 563A46DF
P 6050 3500
AR Path="/563A8614/563A46DF" Ref="Q207"  Part="1" 
AR Path="/563A6BDC/563A46DF" Ref="Q307"  Part="1" 
AR Path="/563A7438/563A46DF" Ref="Q407"  Part="1" 
AR Path="/563A83B0/563A46DF" Ref="Q507"  Part="1" 
F 0 "Q207" H 6250 3575 50  0000 L CNN
F 1 "BC557" H 6250 3500 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 6250 3425 50  0000 L CIN
F 3 "" H 6050 3500 50  0000 L CNN
	1    6050 3500
	1    0    0    1   
$EndComp
$Comp
L BC547 Q208
U 1 1 563A46E6
P 6050 4150
AR Path="/563A8614/563A46E6" Ref="Q208"  Part="1" 
AR Path="/563A6BDC/563A46E6" Ref="Q308"  Part="1" 
AR Path="/563A7438/563A46E6" Ref="Q408"  Part="1" 
AR Path="/563A83B0/563A46E6" Ref="Q508"  Part="1" 
F 0 "Q208" H 6250 4225 50  0000 L CNN
F 1 "BC547" H 6250 4150 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 6250 4075 50  0000 L CIN
F 3 "" H 6050 4150 50  0000 L CNN
	1    6050 4150
	1    0    0    -1  
$EndComp
$Comp
L R R209
U 1 1 563A46ED
P 5700 3500
AR Path="/563A8614/563A46ED" Ref="R209"  Part="1" 
AR Path="/563A6BDC/563A46ED" Ref="R309"  Part="1" 
AR Path="/563A7438/563A46ED" Ref="R409"  Part="1" 
AR Path="/563A83B0/563A46ED" Ref="R509"  Part="1" 
F 0 "R209" V 5780 3500 50  0000 C CNN
F 1 "1K" V 5700 3500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5630 3500 30  0001 C CNN
F 3 "" H 5700 3500 30  0000 C CNN
	1    5700 3500
	0    1    1    0   
$EndComp
$Comp
L R R210
U 1 1 563A46F4
P 5700 4150
AR Path="/563A8614/563A46F4" Ref="R210"  Part="1" 
AR Path="/563A6BDC/563A46F4" Ref="R310"  Part="1" 
AR Path="/563A7438/563A46F4" Ref="R410"  Part="1" 
AR Path="/563A83B0/563A46F4" Ref="R510"  Part="1" 
F 0 "R210" V 5780 4150 50  0000 C CNN
F 1 "1K" V 5700 4150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5630 4150 30  0001 C CNN
F 3 "" H 5700 4150 30  0000 C CNN
	1    5700 4150
	0    1    1    0   
$EndComp
$Comp
L BC547 Q204
U 1 1 563A46FB
P 5350 3750
AR Path="/563A8614/563A46FB" Ref="Q204"  Part="1" 
AR Path="/563A6BDC/563A46FB" Ref="Q304"  Part="1" 
AR Path="/563A7438/563A46FB" Ref="Q404"  Part="1" 
AR Path="/563A83B0/563A46FB" Ref="Q504"  Part="1" 
F 0 "Q204" H 5550 3825 50  0000 L CNN
F 1 "BC547" H 5550 3750 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 5550 3675 50  0000 L CIN
F 3 "" H 5350 3750 50  0000 L CNN
	1    5350 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 3700 6150 3950
Wire Wire Line
	5550 3500 5450 3500
Wire Wire Line
	5450 3500 5450 3550
$Comp
L R R206
U 1 1 563A4705
P 5000 3750
AR Path="/563A8614/563A4705" Ref="R206"  Part="1" 
AR Path="/563A6BDC/563A4705" Ref="R306"  Part="1" 
AR Path="/563A7438/563A4705" Ref="R406"  Part="1" 
AR Path="/563A83B0/563A4705" Ref="R506"  Part="1" 
F 0 "R206" V 5080 3750 50  0000 C CNN
F 1 "10K" V 5000 3750 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4930 3750 30  0001 C CNN
F 3 "" H 5000 3750 30  0000 C CNN
	1    5000 3750
	0    1    1    0   
$EndComp
$Comp
L GND #PWR038
U 1 1 563A470C
P 5450 3950
AR Path="/563A8614/563A470C" Ref="#PWR038"  Part="1" 
AR Path="/563A6BDC/563A470C" Ref="#PWR08"  Part="1" 
AR Path="/563A7438/563A470C" Ref="#PWR018"  Part="1" 
AR Path="/563A83B0/563A470C" Ref="#PWR028"  Part="1" 
F 0 "#PWR038" H 5450 3700 50  0001 C CNN
F 1 "GND" H 5450 3800 50  0000 C CNN
F 2 "" H 5450 3950 60  0000 C CNN
F 3 "" H 5450 3950 60  0000 C CNN
	1    5450 3950
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR039
U 1 1 563A4712
P 6150 4350
AR Path="/563A8614/563A4712" Ref="#PWR039"  Part="1" 
AR Path="/563A6BDC/563A4712" Ref="#PWR09"  Part="1" 
AR Path="/563A7438/563A4712" Ref="#PWR019"  Part="1" 
AR Path="/563A83B0/563A4712" Ref="#PWR029"  Part="1" 
F 0 "#PWR039" H 6150 4100 50  0001 C CNN
F 1 "GND" H 6150 4200 50  0000 C CNN
F 2 "" H 6150 4350 60  0000 C CNN
F 3 "" H 6150 4350 60  0000 C CNN
	1    6150 4350
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR040
U 1 1 563A4718
P 6150 3300
AR Path="/563A8614/563A4718" Ref="#PWR040"  Part="1" 
AR Path="/563A6BDC/563A4718" Ref="#PWR010"  Part="1" 
AR Path="/563A7438/563A4718" Ref="#PWR020"  Part="1" 
AR Path="/563A83B0/563A4718" Ref="#PWR030"  Part="1" 
F 0 "#PWR040" H 6150 3150 50  0001 C CNN
F 1 "+12V" H 6150 3440 50  0000 C CNN
F 2 "" H 6150 3300 60  0000 C CNN
F 3 "" H 6150 3300 60  0000 C CNN
	1    6150 3300
	1    0    0    -1  
$EndComp
$Comp
L BC557 Q205
U 1 1 563A471E
P 6050 2050
AR Path="/563A8614/563A471E" Ref="Q205"  Part="1" 
AR Path="/563A6BDC/563A471E" Ref="Q305"  Part="1" 
AR Path="/563A7438/563A471E" Ref="Q405"  Part="1" 
AR Path="/563A83B0/563A471E" Ref="Q505"  Part="1" 
F 0 "Q205" H 6250 2125 50  0000 L CNN
F 1 "BC557" H 6250 2050 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 6250 1975 50  0000 L CIN
F 3 "" H 6050 2050 50  0000 L CNN
	1    6050 2050
	1    0    0    1   
$EndComp
$Comp
L BC547 Q206
U 1 1 563A4725
P 6050 2700
AR Path="/563A8614/563A4725" Ref="Q206"  Part="1" 
AR Path="/563A6BDC/563A4725" Ref="Q306"  Part="1" 
AR Path="/563A7438/563A4725" Ref="Q406"  Part="1" 
AR Path="/563A83B0/563A4725" Ref="Q506"  Part="1" 
F 0 "Q206" H 6250 2775 50  0000 L CNN
F 1 "BC547" H 6250 2700 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 6250 2625 50  0000 L CIN
F 3 "" H 6050 2700 50  0000 L CNN
	1    6050 2700
	1    0    0    -1  
$EndComp
$Comp
L R R207
U 1 1 563A472C
P 5700 2050
AR Path="/563A8614/563A472C" Ref="R207"  Part="1" 
AR Path="/563A6BDC/563A472C" Ref="R307"  Part="1" 
AR Path="/563A7438/563A472C" Ref="R407"  Part="1" 
AR Path="/563A83B0/563A472C" Ref="R507"  Part="1" 
F 0 "R207" V 5780 2050 50  0000 C CNN
F 1 "1K" V 5700 2050 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5630 2050 30  0001 C CNN
F 3 "" H 5700 2050 30  0000 C CNN
	1    5700 2050
	0    1    1    0   
$EndComp
$Comp
L R R208
U 1 1 563A4733
P 5700 2700
AR Path="/563A8614/563A4733" Ref="R208"  Part="1" 
AR Path="/563A6BDC/563A4733" Ref="R308"  Part="1" 
AR Path="/563A7438/563A4733" Ref="R408"  Part="1" 
AR Path="/563A83B0/563A4733" Ref="R508"  Part="1" 
F 0 "R208" V 5780 2700 50  0000 C CNN
F 1 "1K" V 5700 2700 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 5630 2700 30  0001 C CNN
F 3 "" H 5700 2700 30  0000 C CNN
	1    5700 2700
	0    1    1    0   
$EndComp
$Comp
L BC547 Q203
U 1 1 563A473A
P 5350 2300
AR Path="/563A8614/563A473A" Ref="Q203"  Part="1" 
AR Path="/563A6BDC/563A473A" Ref="Q303"  Part="1" 
AR Path="/563A7438/563A473A" Ref="Q403"  Part="1" 
AR Path="/563A83B0/563A473A" Ref="Q503"  Part="1" 
F 0 "Q203" H 5550 2375 50  0000 L CNN
F 1 "BC547" H 5550 2300 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 5550 2225 50  0000 L CIN
F 3 "" H 5350 2300 50  0000 L CNN
	1    5350 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 2250 6150 2500
Wire Wire Line
	5550 2050 5450 2050
Wire Wire Line
	5450 2050 5450 2100
$Comp
L R R205
U 1 1 563A4744
P 5000 2300
AR Path="/563A8614/563A4744" Ref="R205"  Part="1" 
AR Path="/563A6BDC/563A4744" Ref="R305"  Part="1" 
AR Path="/563A7438/563A4744" Ref="R405"  Part="1" 
AR Path="/563A83B0/563A4744" Ref="R505"  Part="1" 
F 0 "R205" V 5080 2300 50  0000 C CNN
F 1 "10K" V 5000 2300 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4930 2300 30  0001 C CNN
F 3 "" H 5000 2300 30  0000 C CNN
	1    5000 2300
	0    1    1    0   
$EndComp
$Comp
L GND #PWR041
U 1 1 563A474B
P 5450 2500
AR Path="/563A8614/563A474B" Ref="#PWR041"  Part="1" 
AR Path="/563A6BDC/563A474B" Ref="#PWR011"  Part="1" 
AR Path="/563A7438/563A474B" Ref="#PWR021"  Part="1" 
AR Path="/563A83B0/563A474B" Ref="#PWR031"  Part="1" 
F 0 "#PWR041" H 5450 2250 50  0001 C CNN
F 1 "GND" H 5450 2350 50  0000 C CNN
F 2 "" H 5450 2500 60  0000 C CNN
F 3 "" H 5450 2500 60  0000 C CNN
	1    5450 2500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR042
U 1 1 563A4751
P 6150 2900
AR Path="/563A8614/563A4751" Ref="#PWR042"  Part="1" 
AR Path="/563A6BDC/563A4751" Ref="#PWR012"  Part="1" 
AR Path="/563A7438/563A4751" Ref="#PWR022"  Part="1" 
AR Path="/563A83B0/563A4751" Ref="#PWR032"  Part="1" 
F 0 "#PWR042" H 6150 2650 50  0001 C CNN
F 1 "GND" H 6150 2750 50  0000 C CNN
F 2 "" H 6150 2900 60  0000 C CNN
F 3 "" H 6150 2900 60  0000 C CNN
	1    6150 2900
	1    0    0    -1  
$EndComp
$Comp
L +12V #PWR043
U 1 1 563A4757
P 6150 1850
AR Path="/563A8614/563A4757" Ref="#PWR043"  Part="1" 
AR Path="/563A6BDC/563A4757" Ref="#PWR013"  Part="1" 
AR Path="/563A7438/563A4757" Ref="#PWR023"  Part="1" 
AR Path="/563A83B0/563A4757" Ref="#PWR033"  Part="1" 
F 0 "#PWR043" H 6150 1700 50  0001 C CNN
F 1 "+12V" H 6150 1990 50  0000 C CNN
F 2 "" H 6150 1850 60  0000 C CNN
F 3 "" H 6150 1850 60  0000 C CNN
	1    6150 1850
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 3800 6850 3800
Wire Wire Line
	6850 3800 6850 3150
Wire Wire Line
	6850 3150 7000 3150
Connection ~ 6150 3800
Wire Wire Line
	6150 2350 6850 2350
Connection ~ 6150 2350
Wire Wire Line
	6850 3000 7000 3000
Wire Wire Line
	6850 2350 6850 3000
Wire Wire Line
	4850 3750 4850 2700
Wire Wire Line
	4850 2700 5550 2700
Wire Wire Line
	4700 2300 4700 4150
Wire Wire Line
	4700 4150 5550 4150
$Comp
L BC547 Q201
U 1 1 563A476B
P 4200 2500
AR Path="/563A8614/563A476B" Ref="Q201"  Part="1" 
AR Path="/563A6BDC/563A476B" Ref="Q301"  Part="1" 
AR Path="/563A7438/563A476B" Ref="Q401"  Part="1" 
AR Path="/563A83B0/563A476B" Ref="Q501"  Part="1" 
F 0 "Q201" H 4400 2575 50  0000 L CNN
F 1 "BC547" H 4400 2500 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 4400 2425 50  0000 L CIN
F 3 "" H 4200 2500 50  0000 L CNN
	1    4200 2500
	1    0    0    -1  
$EndComp
$Comp
L BC547 Q202
U 1 1 563A4772
P 4200 3950
AR Path="/563A8614/563A4772" Ref="Q202"  Part="1" 
AR Path="/563A6BDC/563A4772" Ref="Q302"  Part="1" 
AR Path="/563A7438/563A4772" Ref="Q402"  Part="1" 
AR Path="/563A83B0/563A4772" Ref="Q502"  Part="1" 
F 0 "Q202" H 4400 4025 50  0000 L CNN
F 1 "BC547" H 4400 3950 50  0000 L CNN
F 2 "Housings_TO-92:TO-92_Inline_Wide" H 4400 3875 50  0000 L CIN
F 3 "" H 4200 3950 50  0000 L CNN
	1    4200 3950
	1    0    0    -1  
$EndComp
$Comp
L R R204
U 1 1 563A4779
P 4300 3600
AR Path="/563A8614/563A4779" Ref="R204"  Part="1" 
AR Path="/563A6BDC/563A4779" Ref="R304"  Part="1" 
AR Path="/563A7438/563A4779" Ref="R404"  Part="1" 
AR Path="/563A83B0/563A4779" Ref="R504"  Part="1" 
F 0 "R204" V 4380 3600 50  0000 C CNN
F 1 "1K" V 4300 3600 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4230 3600 30  0001 C CNN
F 3 "" H 4300 3600 30  0000 C CNN
	1    4300 3600
	1    0    0    -1  
$EndComp
$Comp
L R R203
U 1 1 563A4780
P 4300 2150
AR Path="/563A8614/563A4780" Ref="R203"  Part="1" 
AR Path="/563A6BDC/563A4780" Ref="R303"  Part="1" 
AR Path="/563A7438/563A4780" Ref="R403"  Part="1" 
AR Path="/563A83B0/563A4780" Ref="R503"  Part="1" 
F 0 "R203" V 4380 2150 50  0000 C CNN
F 1 "1K" V 4300 2150 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 4230 2150 30  0001 C CNN
F 3 "" H 4300 2150 30  0000 C CNN
	1    4300 2150
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR044
U 1 1 563A4787
P 4300 3450
AR Path="/563A8614/563A4787" Ref="#PWR044"  Part="1" 
AR Path="/563A6BDC/563A4787" Ref="#PWR014"  Part="1" 
AR Path="/563A7438/563A4787" Ref="#PWR024"  Part="1" 
AR Path="/563A83B0/563A4787" Ref="#PWR034"  Part="1" 
F 0 "#PWR044" H 4300 3300 50  0001 C CNN
F 1 "+3.3V" H 4300 3590 50  0000 C CNN
F 2 "" H 4300 3450 60  0000 C CNN
F 3 "" H 4300 3450 60  0000 C CNN
	1    4300 3450
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR045
U 1 1 563A478D
P 4300 2000
AR Path="/563A8614/563A478D" Ref="#PWR045"  Part="1" 
AR Path="/563A6BDC/563A478D" Ref="#PWR015"  Part="1" 
AR Path="/563A7438/563A478D" Ref="#PWR025"  Part="1" 
AR Path="/563A83B0/563A478D" Ref="#PWR035"  Part="1" 
F 0 "#PWR045" H 4300 1850 50  0001 C CNN
F 1 "+3.3V" H 4300 2140 50  0000 C CNN
F 2 "" H 4300 2000 60  0000 C CNN
F 3 "" H 4300 2000 60  0000 C CNN
	1    4300 2000
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR046
U 1 1 563A4793
P 4300 2700
AR Path="/563A8614/563A4793" Ref="#PWR046"  Part="1" 
AR Path="/563A6BDC/563A4793" Ref="#PWR016"  Part="1" 
AR Path="/563A7438/563A4793" Ref="#PWR026"  Part="1" 
AR Path="/563A83B0/563A4793" Ref="#PWR036"  Part="1" 
F 0 "#PWR046" H 4300 2450 50  0001 C CNN
F 1 "GND" H 4300 2550 50  0000 C CNN
F 2 "" H 4300 2700 60  0000 C CNN
F 3 "" H 4300 2700 60  0000 C CNN
	1    4300 2700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR047
U 1 1 563A4799
P 4300 4150
AR Path="/563A8614/563A4799" Ref="#PWR047"  Part="1" 
AR Path="/563A6BDC/563A4799" Ref="#PWR017"  Part="1" 
AR Path="/563A7438/563A4799" Ref="#PWR027"  Part="1" 
AR Path="/563A83B0/563A4799" Ref="#PWR037"  Part="1" 
F 0 "#PWR047" H 4300 3900 50  0001 C CNN
F 1 "GND" H 4300 4000 50  0000 C CNN
F 2 "" H 4300 4150 60  0000 C CNN
F 3 "" H 4300 4150 60  0000 C CNN
	1    4300 4150
	1    0    0    -1  
$EndComp
Connection ~ 4300 3750
Connection ~ 4700 2300
Connection ~ 4300 2300
Wire Wire Line
	4300 2300 4850 2300
Wire Wire Line
	4300 3750 4850 3750
$Comp
L R R201
U 1 1 563A47A4
P 3850 2500
AR Path="/563A8614/563A47A4" Ref="R201"  Part="1" 
AR Path="/563A6BDC/563A47A4" Ref="R301"  Part="1" 
AR Path="/563A7438/563A47A4" Ref="R401"  Part="1" 
AR Path="/563A83B0/563A47A4" Ref="R501"  Part="1" 
F 0 "R201" V 3930 2500 50  0000 C CNN
F 1 "10K" V 3850 2500 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 3780 2500 30  0001 C CNN
F 3 "" H 3850 2500 30  0000 C CNN
	1    3850 2500
	0    1    1    0   
$EndComp
$Comp
L R R202
U 1 1 563A47AB
P 3850 3950
AR Path="/563A8614/563A47AB" Ref="R202"  Part="1" 
AR Path="/563A6BDC/563A47AB" Ref="R302"  Part="1" 
AR Path="/563A7438/563A47AB" Ref="R402"  Part="1" 
AR Path="/563A83B0/563A47AB" Ref="R502"  Part="1" 
F 0 "R202" V 3930 3950 50  0000 C CNN
F 1 "10K" V 3850 3950 50  0000 C CNN
F 2 "Resistors_ThroughHole:Resistor_Horizontal_RM10mm" V 3780 3950 30  0001 C CNN
F 3 "" H 3850 3950 30  0000 C CNN
	1    3850 3950
	0    1    1    0   
$EndComp
Wire Wire Line
	3700 2500 3700 3000
Wire Wire Line
	3700 3150 3700 3950
Wire Wire Line
	3700 3000 3600 3000
Wire Wire Line
	3600 3150 3700 3150
Connection ~ 4850 3750
Text HLabel 3600 3000 0    60   Input ~ 0
Input_1
Text HLabel 3600 3150 0    60   Input ~ 0
Input_2
Text HLabel 7000 3000 2    60   Input ~ 0
Output_A
Text HLabel 7000 3150 2    60   Input ~ 0
Output_B
$EndSCHEMATC
