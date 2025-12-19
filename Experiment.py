def find_best_student(student_names, student_scores):
    highest_score=0
    high_score_index=0
    for score in range(len(student_scores)):
        if student_scores[score]>highest_score:
            highest_score=student_scores[score]
            high_score_index=score
    return student_names[high_score_index]

names = ["Alice", "Bob", "Charlie", "David"]
scores = [100, 92, 89, 95]
print(find_best_student(names,scores))
def remove_outliers(data, min_val, max_val):
    for number in data:
        if number<min_val or number>max_val:
            data.remove(number)
    return data


measurements=[8, 5, 12, 1, 9, 20, 15]
temps = [-5, 10, 0, 35, 15, 40, 20]
edge_case = [100, 1, 101, 2, 102]
print(remove_outliers(measurements,5,15))
print(remove_outliers(temps,0,30))
print(remove_outliers(edge_case,0,10))

def add_racer(racers, lap_times, new_racer, new_time):
    new_time=new_racer[1]
    new_racer=new_racer[0]
    racers.append(new_racer)
    lap_times.append(new_time)
def disqualify_racer(racers, lap_times, racer_to_disqualify):
    for racer in range(len(racers)):
        if racers[racer]==racer_to_disqualify:
            racers.pop(racer)
            lap_times.pop(racer)
            return True
        elif racers[racer]!=racer_to_disqualify:
            return False
        
def get_fastest_laps(racers, lap_times, count):
    rank_list=[]
    top_speed=0
    for racer in range(len(racers)):
        if lap_times[racer]>top_speed:
            top_speed=lap_times[racer]
            rank_list.append(racers[racer])
            rank_list.append(lap_times[racer])
    return rank_list
def manage_race_results(initial_racers, initial_times, new_racer_data, racer_to_disqualify, top_count):
    racers=initial_racers.copy()
    lap_times=initial_times.copy()
    added_list=add_racer(racers,lap_times,new_racer_data)
    disqualify_racer=disqualify_racer(racer_to_disqualify)
    fastest_laps=get_fastest_laps(racers,lap_times,count)
    return added_list,fastest_laps
racers = ["Axel", "Blaze", "Cruz", "Dash", "Echo"]
times = [95.42, 94.88, 96.10, 95.90, 94.99]
new_racer = ["Fang", 94.50]
disqualify_name = "Dash"
count = 3
print(manage_race_results(racers,times,new_racer,disqualify_name,count))








 





