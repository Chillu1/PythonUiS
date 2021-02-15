from matplotlib import *
from numpy import *
import matplotlib.pyplot as plt

GRAVITASJON = 9.81

brukerinput = input("Skriv inn intervallstørrelsen: ")
intervallstorrelse = int(brukerinput)
brukerinput = input("Skriv inn antall intervaller: ")
antall_intervaller = int(brukerinput)
if antall_intervaller >= 0.0 and intervallstorrelse > 0.0:
    distanceList = []
    timeList = []

    for antall_sekunder in range(intervallstorrelse,
                                 intervallstorrelse*(antall_intervaller) + 1,
                                 intervallstorrelse):
        fart = GRAVITASJON*antall_sekunder
        distanse = 0.5*fart*antall_sekunder
        distanceList.append(distanse)
        timeList.append(antall_sekunder)
else:
    print("Antall intervaller kan ikke være negativt! Intervallstørrelse må være "
          "positivt!")

plt.plot(timeList,distanceList)
plt.ylabel("Distance (m)")
plt.xlabel("Time (s)")
plt.show()