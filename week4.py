#Var 7
def calculate_ticket_revenue(show_type, tickets_sold, time_slot):
    total=0
    if show_type=="blockbuster":
        if time_slot=="morning":
            total=(total+12)*tickets_sold
        elif time_slot=="afternoon":
            total+=18*tickets_sold
        elif time_slot=="evening":
            total+=25*tickets_sold
        else:
            print("Enter the time please!")
    elif show_type=="standard":
        if time_slot=="morning":
            total+=8*tickets_sold
        elif time_slot=="afternoon":
            total+=12*tickets_sold
        elif time_slot=="evening":
            total+=16*tickets_sold
        else:
            print("Enter the time please!")
    elif show_type=="classic":
        if time_slot=="morning":
            total+=5*tickets_sold
        elif time_slot=="afternoon":
            total+=8*tickets_sold
        elif time_slot=="evening":
            total+=10*tickets_sold
        else:
            print("Enter the time please!")
    else:
        print("Enter show correct type please!")
    return total

def calculate_occupancy_rate(theater_years, baseline_seats, filled_seats):
    expected_capacity=1000+(theater_years*100)
    seat_availability=expected_capacity-baseline_seats
    occupancy_per=(filled_seats-baseline_seats)/seat_availability*100
    return occupancy_per


def determine_popularity_status(occupancy_percent):
    if occupancy_percent<50:
        occupancy_percent= 'Low Demand'
    elif occupancy_percent<60:
        occupancy_percent="Moderate Demand"
    elif occupancy_percent<70:
        occupancy_percent="Good Demand"
    elif occupancy_percent<=85:
        occupancy_percent="High Demand"
    elif occupancy_percent>85:
        occupancy_percent="Sold out"
    return occupancy_percent
def calculate_total_profit(revenue, tickets, status_multiplier):
    base_profit=revenue*0.05+tickets*2
    if status_multiplier=="Low Demand":
        status_multiplier=0.5
    elif status_multiplier=="Moderate Demand":
        status_multiplier=1
    elif status_multiplier=="Good Demand":
        status_multiplier=1.2
    elif status_multiplier=="High Demand":
        status_multiplier=1.5
    elif status_multiplier=="Sold out":
        status_multiplier=1.8
    final_profit=base_profit * status_multiplier
    return final_profit

def needs_promotion(screening_days, total_tickets, avg_occupancy):
    if screening_days>=6 and avg_occupancy<50:
        return "Yes"
    elif total_tickets<100 and avg_occupancy<60:
        return "Yes"
    elif screening_days>=4 and avg_occupancy<40:
        return "Yes"
    else:
        return 'No'
    
print('MOVIE THEATER MANAGEMENT SYSTEM')
def generate_theater_report(movie_title, show_type, tickets, time_slot, theater_years, baseline_seats, filled_seats, screening_days):

    print("=======================================")
    print(f"Theater report for: {movie_title}")
    print("---------------------------------------")
    print()
    #show type
    print(f'Show Type: {show_type}')
    # Tickets Sold: 45
    print(f'Tickets Sold: {tickets}')
    # Time Slot: evening
    ticket_revenue = calculate_ticket_revenue(show_type, tickets, time_slot)
    # Ticket Revenue: $1125
    print(f'Ticket Revenue:{ticket_revenue}$')
    # Occupancy Analysis:
    print('Occupancy Analysis:')
    occupancy_analysis=calculate_occupancy_rate(theater_years,baseline_seats,filled_seats)
    # Experience: 3 years, Baseline: 800, Filled Seats: 1150
    print(f"   Experience:{theater_years} years, Baseline: {baseline_seats}, Filled Seats: {filled_seats}")
    # Occupancy: 70.0%
    print(f'   Occupancy: {round(occupancy_analysis,1)}%')
    # Popularity Status: High Demand
    popularity_status= determine_popularity_status(occupancy_analysis)
    print(f'   Popularity Status:{popularity_status}')
    # Total Profit: $219.4
    total_profit=calculate_total_profit(ticket_revenue, tickets, popularity_status)
    
    print(f'Total Profit:{round(total_profit,1)}')
    # Screening Days: 3
    print(f"Screening days: {screening_days}")
    # Promotion Needed: No
    prom_needed=needs_promotion(screening_days,tickets,occupancy_analysis)
    print(f"Promotion needed: {prom_needed}")
    

print()
generate_theater_report("Space Adventure", "blockbuster", 45 , "evening", 3, 800, 1150,3)

generate_theater_report('Comedy Night', 'standard', 60, 'afternoon', 5, 900, 1300,5)

generate_theater_report("Old Classic", "classic", 30, "morning", 8, 850, 950, 7)










    

    



        


