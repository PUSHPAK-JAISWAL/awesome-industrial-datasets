# [Gas sensor arrays in open sampling settings](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+arrays+in+open+sampling+settings)

![](https://img.shields.io/badge/sector-chemical-red.svg)
![](https://img.shields.io/badge/labeled-yes-blue.svg)
![](https://img.shields.io/badge/time--series-yes-blue.svg) ![](<https://img.shields.io/badge/simulation-yes-blue.svg>)    

Parameter | Value
---- | ----
Data Set Characteristics | Multivariate, Time-Series
Attribute Characteristics	| Real
Associated Tasks	| Classification
Number of Instances	| 18000
Number of Attributes	| 1950000
Date Donated | 2013-06-05
Source | UCI Machine Learning Repository
Dataset size | 7.8GB (compressed)


## Source

Creators:\
Alexander Vergara (vergara '@' ucsd.edu)\
BioCircutis Institute\
University of California San Diego\
San Diego, California, USA

Donors of the Dataset:\
Alexander Vergara (vergara '@' ucsd.edu)\
Jordi Fonollosa (fonollosa '@' ucsd.edu)\
Marco Trincavelli (marco.trincavelli '@' oru.se)\
Nikolai F. Rulkov (nrulkov '@' ucsd.edu)\
Ramon Huerta (rhuerta '@' ucsd.edu)


## Data Set Information

- Number of instances: 18000 times-series measurements recorded from a 72 metal-oxide gas sensor array-based chemical detection platform.

- Number of attributes (features): Every measurement contains 72 time-series recorded during 260 seconds, each collected at a sample rate of 100 Hz (samples per second).
The dataset also contains time, temperature, and relative humidity information.
The resulting dataset ultimately includes 75-time series composed of 26000 points.


This archive contains 18000 time-series measurement recordings collected from an array of 72 metal-oxide gas sensors composing our sensing platform utilized in the detection and identification of potentially-dangerous chemical gaseous substances under complex environmental conditions, as reported in the related manuscript below. Our primary purpose is to make our dataset freely accessible on-line to the chemo-sensing research and machine-learning communities, as well as other interested communities, to develop alternative competitive solutions relevant to gas-sensing discrimination tasks in open sampling settings, such as the one pursued here, and/or navigation. The dataset can be used exclusively for research purposes. Commercial purposes are fully excluded.

The dataset was gathered from December 2010 to April 2012 (16 months) in a 2.5 m Ã— 1.2 m Ã— 0.4 m wind tunnel research test-bed facility situated at the BioCircuits Institute, University of California San Diego. Specifically, our customized research facility, endowed with a computer-supervised mass flow controller-based continuous flow gas delivery system, operates in a propulsion open-cycle mode, by continuously drawing external turbulent air into and throughout the tunnel and exhausting it back to the outside, thereby creating a relatively less-turbulent airflow moving downstream towards the end of the test field, which is particularly suitable for applications pursued here that require injecting chemical poisonous agents or explosive mixtures because it prevents saturation. Being operated by a fully computerized environment controlled by a player/stage robot server software programmed on C++ on a PC fitted with the appropriate serial cards and with minimum human intervention, the designed wind tunnel test-bed facility provides versatility for releasing the chemical substances of interest at the desired concentrations with high accuracy and in a highly reproducible manner during the entire experiment and simultaneously in preserving the appropriate environmental conditions to generate chemical gas plumes exhibiting turbulent patterns. A graphical illustration of the designed wind tunnel test-bed facility considered in this study along with the characteristics of the geometry of the problem as well as the exact locations of the chemical analyte source and chemo-sensory platform is presented in Figure 2 of the manuscript cited below. Actual pictures of the designed wind tunnel are also presented in the Supplementary Material, Figure S.1 of the accompanying manuscript.
The resulting dataset induces a ten-class gas discrimination problem, comprising recordings from ten distinct pure chemical gases, namely Acetone, Acetaldehyde, Ammonia, Butanol, Ethylene, Methane, Methanol, Carbon Monoxide, Benzene, and Toluene. The goal is to identify and discriminate the mentioned chemical hazards at relevant concentrations regardless of the location of the sensory system platform within the annotated wind tunnel research facility as well as the environmental and parametric conditions induced in the setting (Please see manuscript for more details). See Table 1 on Vergara et a. 2013 (manuscript below) for specifics on the identity of chemical analyte hazards as well as their nominal concentration values at the outlet of the gas source in parts-per-million by volume (ppmv). Please refer to the manuscript below for a more details of the wind tunnel test-bed facility as well as for specifics on the collection procedure followed and the operating and environmental parameters utilized during the creation of the aforementioned dataset.

## Attribute Information
The response of the sensor platform is read-out in the form of the resistance across the active sensitive film of each of the 72 gas sensors integrating the sensor array; hence, each measurement produced a 72-channel time series, each of which represented by a 260-second time series collected at a sample rate of 100 samples per second (Hz), reflecting all the environmental changes in the evaluated scenario. For a more detailed analysis and discussion on the processing of the time series as well as a graphical illustration of them please refer to Sections 2 and 3 and Figure 4, respectively, of the manuscript below.

For manipulation purposes, the data is organized into eleven folders, each containing the number of measurements per chemical class identity and nominal concentration indicated above and described in the Table 2 of the manuscript. For example the folder named Toluene_200 means the name of the gas identity is Toluene, which has been dosed at 200 ppmv. Each folder contains 6 folders, each representing the line location within the test area of the wind tunnel (location 1, L1, to location 6, L6, being L1 the closest point to the gas source) from which the set of time-series were recorded. In each of these folders there are 300 files, each of which corresponding to the number of measurements recorded at each location in the tunnel. The name of each file contains the exact log information of each of the measurements performed during the entire experiment, which is organized as follows. The first 12 digits of the file name (e.g., 201106060617) indicate the date and time at which each specific measurement was collected, starting from the year, month, day, and time. The last 4 digits in the following 19 characters of the name file, (e.g., board_setPoint_500V), indicate the fixed operating temperature value, represented by a voltage value applied to the embedded heating element in the chemical sensor, applied to the entire sensing platform, which can adopt nominal values from 4 to 6 V with an resolution value of 0.5 V. Note that the value 500V in the example is a graphical representation of the 5V value applied to the sensors heater. For more details on the operating principles of the chemical sensors utilized in our platform please refer to Section 2 of the manuscript. The last 3 digits in the following 16 characters of the file name (e.g., fan_setPoint_060) indicates the set-point value of the nominal rotational speeds of the multiple-step motor-driven exhaust fan utilized to induce the distinct artificial airflows speed in the wind tunnel. Only three values were adopted in this condition: the value 000in the file name, which indicates the slowest rotational speed (1500 rpm), the value 060, indicating the mid-point rotational speed value of the fan (3900rpm), and the value 100, which refers to the fastest induced speed of the fan, 5500 rpm. The last 14 characters of the following string of 27 characters (e.g., mfc_setPoint_Toluene_200ppm) describe the analyte identity and concentration value for each particular measurement. Thus, the just mentioned example represents the class corresponding to the chemical analyte identity Toluene dosed at the nominal concentration value of 200 ppm. Finally, the last 2 or 3 digits in the name (e.g., p7) describe the line point location at which the chemo-sensory platform was located in the wind tunnel. Note that there is a shift of two numbers in the value of this position, i.e., the value p7 in actuality represents the line location 4 illustrated in Figure 2 of the cited manuscript. For example, in
201106060617_board_setPoint_500V_fan_setPoint_060_mfc_setPoint_Toluene_200ppm_p7
the entire text line stands for a stand-alone measurement of the chemo-sensory platform located at the line location L4 and in response to 200 ppm of Toluene collected on June 06 of 2011, at 06:17 am (PST), with an operating voltage applied to the heater of 5V and a nominal rotational speed of the exhaust fan of 3900 rpm.

Having described the naming configuration adopted in the generated dataset, we describe the organization of the information in each of the attached files of the dataset. The data format encloses information relevant to each measurement file, containing all the time series indicated above (9 portable modules Ã— 8 sensors, temperature and humidity values (oC and %, respectively), exhaust fan set-point and reading values, mass flow controller set-point and actual reading values (%), and reading time (ms)), which is organized as follows:
Reading time (ms) fan_set_point fan_reading* mcf1_setpoint mcf2_setpoint mcf3_setpoint mcf1_read mcf2_read mcf3_read T RH 1 board1(Ã— 8 chemical sensors) 1 board2(Ã— 8 chemical sensors) 1 .... 1 board9(Ã— 8 chemical sensors)

where: Reading time (ms) is the time step for each recording (in ms, at a sample rate of 100 Hz), fan_set_point and fan_reading, is the set-point and actual reading of the exhaust fan, respectively, mcf1_setpoint to mcf3_setpoint are the opening degree set-point values given to the mass flow controllers 1 to 3 during the experiment, respectively, mcf1_read to mcf1_readare the measured opening degree of mass flow controllers 1 to 3, respectively, T and R are the temperature and relative humidity values (in oC and %, respectively) during the entire experiment, and board1(Ã— 8 chemical sensors) to âboard9(Ã— 8 chemical sensors) are the 72 time series collected as a function of time from the 8 gas sensors (in KÎ©) integrating modules 1 to 9 in each location, respectively, each separated by the number 1 that stands as indicator label, forming thus the 72 time-series chemical sensor responses that is fetched to the classifier for training as described in the study. Note that there is a blank space between and among each column in the dataset.

Thus, for example, in line1:
22250 0 0 100 100 100 103 103 105 22.22 63.43 1 476 555 803 497 775 885 873 843 1 346 545 635 616 571 552 773 745 1 397 509 660 638 755 744 745 657 1 420 510 525 531 504 650 719 715 1 2201 449 652 1228 847 654 850 737 1 370 459 650 445 756 773 847 803 1 345 457 587 554 757 704 769 818 1 354 407 499 696 786 686 757 733 1 339 418 547 567 653 573 773 84

The number 22225 stands for the recording made at time 22.25s, the following two numbers stand for the set-point and measured value of the fan speed, the following 6 numbers indicate the set-point (in this case, 100) and actual measured values of the MFC (103, 103, 105), the numbers 22.22 and 63.43 stand for the temperature and humidity values at that specific time recording, whereas the remaining 80 columns list the actual time series values for each measurement recording organized as described above, and in which the number 1 indicates the boundary between each sensor module board. The first and ninth boards correspond to the positions closer to the walls, whereas the board 5 is located in the main line orthogonal to the gas plume. For the exact location of each board, please refer to Figure 2 of the mentioned Journal article.
*: we found out that the exhaust fan actual reading value registered on each file is not completely accurate, showing a 0 or other random values for some of the measurement recordings. Please discard this information value and utilize only the set point information for processing purposes; The value is accurate.
Finally, to make the results presented in the associated article reproducible for the user of this read-me file, please use the hyper-parameter values described in the manuscript for the training task.

## Resourses
- [UCI](https://archive.ics.uci.edu/ml/datasets/Gas+sensor+arrays+in+open+sampling+settings): Database source link.


## Citation Request

1. Alexander Vergara, Jordi Fonollosa, Jonas Mahiques, Marco Trincavelli, Nikolai Rulkov, RamÃ³n Huerta, On the performance of gas sensor arrays in open sampling systems using Inhibitory Support Vector Machines, Sensors and Actuators B: Chemical, Available online 18 May 2013, ISSN 0925-4005, 10.1016/j.snb.2013.05.027. ([Web Link])