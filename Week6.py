def calculate_roi(movie_tuple):

    budget=movie_tuple[2]
    revenue=movie_tuple[3]
    ROI=revenue/budget
    return ROI
def find_most_profitable_movie(movies):
    highest_roi=0
    best_movie_id=""
    for movie in movies:
        roi=calculate_roi(movie)
        if roi>highest_roi:
            highest_roi=roi
            best_movie_id=movie[0]




    
movies = [
    ('M01', 'Sci-Fi', 200, 800),  # ROI: 4.0
    ('M02', 'Comedy', 50, 250),   # ROI: 5.0
    ('M03', 'Sci-Fi', 150, 500),  # ROI: 3.33
    ('M04', 'Action', 250, 700),  # ROI: 2.8
    ('M05', 'Comedy', 30, 150)    # ROI: 5.0
]