def add_racer(racers, lap_times, new_racer, new_time):
    racers.append(new_racer[0])
    new_time=(new_racer[1])
    lap_times.append(new_time)
def disqualify_racer(racers, lap_times, racer_to_disqualify):
    for i in range(len(racers)):
        if racers[i] ==racer_to_disqualify:
            racers.pop(i)
            lap_times.pop(i)
        else:
            return False

def get_fastest_laps(racers, lap_times, count):
    fastest_racers=[]
    count=len(fastest_racers)
    fastest_tim=0
    for time in range(len(lap_times)):
        if lap_times[time]>fastest_tim and racers[time] not in fastest_racers:
            while count<4:
                if count>3:
                    break
                else:
                    fastest_racers.append(racers[time])
    return fastest_racers
def manage_race_results(initial_racers, initial_times, new_racer_data, racer_to_disqualify, top_count):
    new_time=new_racer_data[1]
    racers=add_racer(initial_racers,initial_times,new_racer_data,new_time)
    lap_times=add_racer(initial_racers,initial_times,new_racer_data,new_time)
    racer_to_disqualify=disqualify_racer(racers,lap_times,racer_to_disqualify)
    count=top_count
    fastest_laps=get_fastest_laps(racers,lap_times,count)
    
    return fastest_laps,racers
racers = ["Axel", "Blaze", "Cruz", "Dash", "Echo"]
times = [95.42, 94.88, 96.10, 95.90, 94.99]
new_racer = ["Fang", 94.50]
disqualify_name = "Dash"
count = 3

manage_race_results(racers,times,new_racer,disqualify_name,count)
#Parallel lists
#1
def info_student(names,ages):
    for name in range(len(names)):
        print(f"{names[name]} is {ages[name]} years old")

names=["Ali","Mirza","Temur"]
ages=[13,14,15]
info_student(names,ages)
#2
def market_calc(products,prices):

    for product in range(len(products)):
        print(f"{products[product]}:{prices[product]}")

    
products=["bag","knife","biscuits",'bags']
prices=[11,12,13,11]
print(market_calc(products,prices))

#3
def best_student(names,scores):
    highest_score=0
    index_best_student=None
    for score in range(len(scores)):
        if scores[score]>highest_score:
            highest_score=scores[score]
            index_best_student=score
    return names[index_best_student],scores[index_best_student]
names=["Ali","Nozim","Sarvar","Javohir"]
scores=[91,87,93,100]
print(best_student(names,scores))

#4 Intermediate
def salary_data(employees,hours,hourly_rates):
    for employee in range(len(employees)):
        salary=hours[employee]*hourly_rates[employee]
        print(f"{employees[employee]}:{salary}$")

employees=["Ali","Nozim","Sarvar","Javohir"]
hours=[11,12,13,14]
hourly_rates=[3,4,5,6]
salary_data(employees,hours,hourly_rates)

#5
def find_lowest_temp(cities,temperatures):
    lowest_temperature=0
    index_lowest_temp=None
    for temperature in range(len(temperatures)):
        if temperatures[temperature]<temperatures[temperature+1] and temperature<len(temperatures):
            lowest_temperature=temperatures[temperature]
            index_lowest_temp=temperature
    return cities[index_lowest_temp],lowest_temperature

cities=["Berlin","London","Astana","Moscow"]
temperatures=[33,19,-11,17]
find_lowest_temp(cities,temperatures)


            




    


