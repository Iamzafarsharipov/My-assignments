def add_racer(racers, lap_times, new_racer, new_time):

    racers.append(new_racer[0])
    new_time=new_racer[1]
    lap_times.append(new_racer[new_time])

def disqualify_racer(racers, lap_times, racer_to_disqualify):
    for i in range(len(racers)):
        if racers[i] ==racer_to_disqualify:
            racers.pop(i)
            lap_times.pop(i)
    return False

def get_fastest_laps(racers, lap_times, count):
    fastest_racers=[]
    lap_times2=lap_times
    for i in range(len(lap_times2)):
        if i > i+1 :
            lap_times2.append(i.index())
        else:
            lap_times2.append(i.index())
            




    


