from FlightF import Flight

class Airplanes(object):
    def __init__(self):
        self.airplanes = []

    def add(self, airplane):
        self.airplanes.append(airplane)

    def __str__(self):
        return '\n'.join(str(airplane) for airplane in self.airplanes)

    def existsId(self, aid):
        result = False
        for airplane in self.airplanes:
            result = result or (airplane.aid == aid)
        return result
    def deleteA(self, aid):
        for airplane in self.airplanes:
            if (airplane.aid == aid):
                self.airplanes.remove(airplane)
    def spainDestination(self, flights):
        for flight in flights.flights:
            if (flight.fdestination == "Spain"):
                print "\n   Flight N %d:" % flight.fid
                for airplane in self.airplanes:
                    if (airplane.aid == flight.aid):
                        print "\n       %s" % airplane
class Flights(object):
    def __init__(self):
        self.flights = []

    def exists(self, aid):
        result = False
        for flight in self.flights:
            if (flight.aid == aid):
                result = True
        return result

    def retF(self, fid):
        result = Flight(0,0,'zero')
        for flight in self.flights:
            if (flight.fid == fid):
                result = flight
        return result

    def unique(self, fid):
        result = True
        for flight in self.flights:
            if (flight.fid == fid):
                result = False
        return result

    def deleteF(self, fid):
        for flight in self.flights:
            if (flight.fid == fid):
                self.flights.remove(flight)

    def addFlight(self, flight, airplanes):
        if airplanes.existsId(flight.aid):
            if self.unique(flight.fid):
                self.flights.append(flight)
    def __str__(self):
        return '\n'.join(str(flight) for flight in self.flights)
