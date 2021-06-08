class Station:
    def __init__(self, navn):
        self.navn = navn
        self.tidspunkter = dict()

    def set_data(self, tidspunkt, minimumstemperatur):
        if tidspunkt in self.tidspunkter:
            if minimumstemperatur < self.tidspunkter[tidspunkt]:
                self.tidspunkter[tidspunkt] = minimumstemperatur
        else:
            self.tidspunkter[tidspunkt] = minimumstemperatur

    def __str__(self):
        return f"{self.navn}, {self.tidspunkter}"


hoyeste_middelvind: float = 0

station_dictionary: dict = {}
station_dictionary_tidspunkt: dict = {}

station_tidspunkt_minimumstemperatur: dict[str, Station] = {}
minimumstemperaturer: dict[str, int] = {}

if __name__ == "__main__":
    file = open("vaerdata_3_stasjoner_80426309_1619003189276.csv", "r")
    list_lines = file.readlines()
    first_line = list_lines.pop(0)  # Skip first line

    for line in list_lines:

        line = line.strip()

        if line.startswith("Name") or line.startswith("Data"):
            continue

        splitted_line = line.split(";")

        # TODO splitted_lines into proper names

        if splitted_line[6] != "-":
            splitted_line[6] = splitted_line[6].replace(",", ".")
            middelvind = float(splitted_line[6])
            if middelvind >= hoyeste_middelvind:
                hoyeste_middelvind = middelvind
        # print(splitted_line)#Debug

        if splitted_line[0] in station_dictionary:
            if station_dictionary[splitted_line[0]] < splitted_line[4]:
                station_dictionary[splitted_line[0]] = splitted_line[4]
                station_dictionary_tidspunkt[splitted_line[0]] = splitted_line[2]
        else:
            station_dictionary[splitted_line[0]] = splitted_line[4]
            station_dictionary_tidspunkt[splitted_line[0]] = splitted_line[2]

        tidspunkt_space_index = splitted_line[2].find(" ")
        tidspunkt = splitted_line[2][tidspunkt_space_index + 1:]
        potensial_minimumstemperatur = splitted_line[5]

        if splitted_line[0] not in station_tidspunkt_minimumstemperatur:
            station_tidspunkt_minimumstemperatur[splitted_line[0]] = Station(splitted_line[0])
        station_tidspunkt_minimumstemperatur[splitted_line[0]].set_data(tidspunkt, potensial_minimumstemperatur)

    print(f"Høyeste middelvind: {hoyeste_middelvind}")
    print(station_dictionary_tidspunkt)
    print(station_dictionary)
    print("Stavanger - Våland og Bergen - Florida hadde høyest maksimumstemperatur")

    # Did it partially "wrong", instead of having minimum temp for all tidspunkt, I have min temp for all stations for all tidspunkt instead
    # Guess one could say I "overdid" the task
    for station in station_tidspunkt_minimumstemperatur.values():
        print(station)#Prints all stations & all their min temperatur tidspunkt
        #for i in range(24):
        #    for tidspunkt in station.tidspunkter:
        #        if tidspunkt in minimumstemperaturer:
        #            if tidspunkt >minimumstemperaturer[tidspunkt]:
        #                minimumstemperaturer[tidspunkt] = tidspunkt
        #        else:
        #            minimumstemperaturer[tidspunkt] = tidspunkt#TODO


    file.close()
