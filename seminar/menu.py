import random


def create_city(name:str, population:int, county:str)->list: 
    city=[name,population,county] 
    return city

def get_name(city): 
    return city[0] 

def get_population(city): 
    return city[1] 

def get_county(city): 
    return city[2]   

def to_string(city): 
    return get_name(city)+" "+ str(get_population(city))+" "+get_county(city)



def display_menu(): 
            print("1.Sort the cities")
            print("2.Display the list of cities")
            print("3. Search for a city")
            print("4. Add a city from the console") 
            print("5. Add a number of random cities to the list" ) 
            print ("6. Quit") 

def sort_cities(cities): 
     ok=false 
     while (ok==false): 
          ok=True
          for i in range(o, len(cities)-1):
            if(get_population(cities[i])>get_population(cities[i+1])): 
                cities[i], cities[i+1]=cities[i+1], cities[i]
                ok=false

def display_cities(cities):
    for city in cities:
        print(to_string(city)) 

def add_city(cities): 
    name=input("Please insert a city name: ")
    population=int(input("Please insert the population: ")) 
    county=input("Please insert the county name: ") 
    city=create_city(name,population,county) 
    cities.append(city)  

def add_random(cities): 
    for i in range(o,n): 
        name="City"+str(i) 
        population=random.randint(a: 100, b: 2 000 000) 
        county="County"+str(i) 
        city= create_city(name, population, county) 
        cities.append(city) 

def search_str_matching(name: str,cities)->bool: 
    for city in (cities): 
        if name.lower() in get_name(city).lower(): 
            return True 
    return False 

def main():  
    cities=[["Targu Neamt", 20 000, "Neamt"],["Consanta", 300 000, "Constanta"], ["Galati", 100 000, "Galati"]]
    while True: 
        display_menu(): 
        o=int(input("Enter your option: "));  
        match o: 
            case 1: 
                #1. Sort the cities 
                sort_cities(cities)
                
            case 2: 
                #2. Display the list of cities  
                display_cities(cities)
            case 3: 
                #3. Search for a city (using partial, case-insensitive str matching) 
                str_name=input("Introduce the partial city name: ") 
                print(search_str_matching(str_name, cities)) 
            case 4: 
                #4. Add a city from the console 
                 add_city(cities)
            case 5: 
                #5. Add a number of ransdom cities to the list (the number is read from the console) 
                n=int(input("How many random cities? "))
                add_random(cities)
            case 6: 
                #6. QUit 
                break 
