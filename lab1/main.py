from AirplaneF import Airplane
from FlightF import Flight
from FlightCenter import Airplanes, Flights
import pickle

airplanes = Airplanes()
#airplane = Airplane(1, "Avrora", "Boing 747")
#airplanes.add(airplane)
#airplane = Airplane(0, "Irina", "Boing 727")
#airplanes.add(airplane)
#flight = Flight(1, 1, "Spain")
flights = Flights()
#flights.addFlight(flight, airplanes)
#flight = Flight(1, 2, "Italia")
#flights.addFlight(flight, airplanes)
#print "\n%s" % airplane
#print "\n%s" % flight
#print "\n%s" % airplanes
#print "\n%s" % flights

input = open('airplanes.pkl', 'rb')
airplanes = pickle.load(input)
input.close()
input = open('flights.pkl', 'rb')
flights = pickle.load(input)
input.close()

nFlag = True
n = 0;
while nFlag:
    print "\n 1. review"
    print "\n 2. add Flight"
    print "\n 3. add Airplane"
    print "\n 4. del Flight"
    print "\n 5. del Airplane"
    print "\n 6. change Airplane by id"
    print "\n 7. change Flight by id"
    print "\n 8. Find Airplane to Spain"
    print "\n 0. exit"
    n = int(raw_input())
    if n == 0:
        nFlag = False
    else:
        if n == 1:
            print "\n\nairplanes:"
            print "\n%s" % airplanes
            print "\n\nflights:"
            print "\n%s" % flights

        if n == 2:
            print "\n\nAdd Flight:"
            print "\ninput id"
            bufId = int(raw_input())
            print "\ninput Airplane id"
            bufaid = int(raw_input())
            print "\ninput destination"
            bufName = raw_input()
            if  flights.unique(bufId):
                if airplanes.existsId(bufaid):
                    flight = Flight(bufaid, bufId, bufName)
                    flights.addFlight(flight, airplanes)
                    print "\n Ok"
                else:
                    print "\n try another Airplane id"
            else:
                print "\n try another id"

        if n == 3:
            print "\n\nAdd Airplane:"
            print "\ninput id"
            bufId = int(raw_input())
            print "\ninput name"
            bufName = raw_input()
            print "\ninput model"
            bufModel = raw_input()
            if not airplanes.existsId(bufId):
                airplane = Airplane(bufId, bufName, bufModel)
                airplanes.add(airplane)
                print "\n Ok"
            else:
                print "\n try another id"

        if n == 4:
            print "\n\nDel Flight:"
            print "\ninput fid"
            bufId = int(raw_input())
            if  not flights.unique(bufId):
                flights.deleteF(bufId)
                print "\n Ok"
            else:
                print "\n try another id"

        if n == 5:
            print "\n\nDel Airplane:"
            print "\ninput id"
            bufId = int(raw_input())
            if airplanes.existsId(bufId):
                if  not flights.exists(bufId):
                    airplanes.deleteA(bufId)
                    print "\n Ok"
                else:
                    print "\n previously delete flights"
            else:
                print "\n try another id"
        if n == 6:
            print "\nChange Airplane by id:"
            print "\nAirplanes:"
            print "\n%s" % airplanes
            print "\ninput id"
            bufId = int(raw_input())
            if airplanes.existsId(bufId):
                airplanes.deleteA(bufId)
                print "\ninput new name"
                bufName = raw_input()
                print "\ninput new model"
                bufModel = raw_input()
                airplane = Airplane(bufId, bufName, bufModel)
                airplanes.add(airplane)
                print "\n Ok"
            else:
                print "\n try another id"

        if n == 7:
            print "\nchange Flight by id:"
            print "\nFlights:"
            print "\n%s" % flights
            print "\ninput fid"
            bufId = int(raw_input())
            if not flights.unique(bufId):
                flight = flights.retF(bufId)
                flights.deleteF(bufId)
                print "\ninput new Airplane id"
                bufaid = int(raw_input())
                print "\ninput new destination"
                bufName = raw_input()
                if airplanes.existsId(bufaid):
                    flight = Flight(bufaid, bufId, bufName)
                    flights.addFlight(flight, airplanes)
                    print "\n Ok"
                else:
                    print "\n try another aid"
                    flights.addFlight(flight, airplanes)

            else:
                print "\n try another id"

        if n == 8:
            print "\nAirplanes to Spain:"
            airplanes.spainDestination(flights);
        str = raw_input()
output = open('airplanes.pkl', 'wb')
pickle.dump(airplanes, output, 2)
output.close()
output = open('flights.pkl', 'wb')
pickle.dump(flights, output, 2)
output.close()