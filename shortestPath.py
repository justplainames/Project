class Node:
    def __init__(self):
        self.name = ""
        self.upperBound = {}
        self.neighbour = {}
        self.neighbourCount = len(self.neighbour)
    
    def populateUpperBound(self, locSet):
        for key, value in locSet.items():
            if locSet[key] != self.name:
                self.upperBound[key] = value
        
    

    
class Linkage:
    
    def __init__(self):
        self.head = None


locations = {"Dhoby Ghaut" : float('inf'),"City Hall" : float('inf'),"Outram Park" : float('inf'),"Paya Lebar" : float('inf')}

dhobyGhaut = Node()
dhobyGhaut.name = "Dhoby Ghaut"
dhobyGhaut.neighbour = {"Outram Park": 5, "City Hall": 2}
dhobyGhaut.populateUpperBound(locations)

outramPark = Node()
outramPark.name = "Outram Park"
outramPark.neighbour = {"City Hall": 6, "Dhoby Ghaut": 5} 
outramPark.populateUpperBound(locations)

cityHall = Node()
cityHall.name = "City Hall"
cityHall.neighbour = {"Dhoby Ghaut": 2, "Outram Park": 6}
cityHall.populateUpperBound(locations)

payaLebar = Node()
payaLebar.name = "Paya Lebar"
payaLebar.neighbour = {"City Hall": 11}
payaLebar.populateUpperBound(locations)


print(cityHall.upperBound)



