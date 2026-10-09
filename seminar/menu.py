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
    retrun get_name(city)+" "+ str(get_population(city))+" "+get_county(city)



def display_menu(): 
            print("1.Sort the cities")
            print("2.Display the list of cities")
            print("3. Search for a city")
            print("4. Add a city from the console") 
            print("5. Add a number of random cities to the list" ) 
            print ("6. ") 





def main():  
    cities=[["Targu Neamt", 20 000, "Neamt"],["Consanta", 300 000, "Constanta"], ["Galati", 100 000, "Galati"]]
    while True: 
        display_menu(): 
        o=int(input("Enter your option: "));  
        match o: 
            case 1: 
                #1. Sort the cities 
                pass
            case 2: 
                #2. Display the list of cities 
                pass
            case 3: 
                #3. Search for a city (using partial, case-insensitive str matching) 
                pass
            case 4: 
                #4. Add a city from the console 
                pass 
            case 5: 
                #5. Add a number of ransdom cities to the list (the number is read from the console) 
                pass 
            case 6: 
                #6. QUit
                pass
