class UndergroundSystem:

    def __init__(self):
        #dictionary of checkin stationName and time of checkin. key is customer id and stationName and time are the values
        self.check_in = dict()
        #dictionary of start and stop station and time taken btwn them. key is the start and stop stations and value is the time
        self.travel = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        print(self.check_in)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in:
            startStation, t1 = self.check_in[id]
            
            # tuple of stations travelled
            stations = (startStation, stationName)
            print(stations)
            #determine time taken btwn stations
            if stations in self.travel:
                self.travel[stations].append(t - t1)
            else:
                self.travel[stations] = [t - t1]
            #checkout customer from sys by removing them from checkin dictionary
            print(self.travel)
            self.check_in.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stations = (startStation, endStation)
        print(stations)
        if stations in self.travel:
            time_taken_list = self.travel[stations]
            print(time_taken_list)
            return sum(time_taken_list) / len(time_taken_list)