"""
'Welcome to K Cinema'
By me
"""
def booking():
    #Tuple Movie choices
    movies = ('Call me by your name','Perks of being a Wallflower','Twilight')
    sessions = ('morning', 'afternoon', 'evening')
    seats_movie1 =([2,4], [5,6], [9,10,11,12])
    seats_movie2 =([1,2,3,4], [5,8], [9,10,11,])
    seats_movie3 =([1,4], [5,6,7,8], [9,10,11,12])

    print('Welcome to K cinema')
    #name = input ('What's your name'?')
    #phone_number = input ('What's your phone number?')
    name = 'Khaliun'
    phone_number = 99294545

    print('Available movies')
    print('*******************************')
    for movie in movies:
        print(movie)

    movie_choice = None
    while movie_choice not in movies:
        movie_choice = input ('Please enter your movie: ')

    print('Available sessions')
    print('*******************************')
    for session in sessions:
        print(session)

    session_choice = None
    while session_choice not in sessions:
        session_choice = input ('Please enter your session: ')

    #getting the index of the chosen movie and session
    movie_index = movies.index(movie_choice)
    session_index = sessions.index(session_choice)
    seats_movie = None
    print('Available seats')
    print('*******************************')
    match movie_index:
        case 0:
            seats_movie = seats_movie1
        case 1:
            seats_movie = seats_movie2
        case 2:
            seats_movie = seats_movie3
    #String with the available seats
    seats_text = ""
    for seat_number in range(1,16):
        if seat_number in seats_movie[session_index]:
            seats_text = seats_text + " X"
        else:
            seats_text = seats_text + f" {seat_number}"

    print (seats_text)
    seat_choice = None
    while seat_choice not in range(1,16):
        try:
            seat_choice = int(input ('Please enter your seat: '))
        except:
            print("Wrong seat.")
            seat_choice = None

    #Finally print user's choices
    print (f"Movie: {movie_choice}, Session: {session_choice}, Seat: {seat_choice}")
    #Place or cancel order
    place_order = ''
    while place_order.lower() not in ('yes', 'no'):
        place_order = input('Would you like to place your order (yes/no)? ')

    if place_order == 'yes':
        print('Your order is processed')
    else:
        print ('Your order has been cancelled')

    print()

book_again='yes'
while book_again=='yes':
    booking()
    #Book again
    while book_again.lower() not in ('yes','no'):
        book_again = input('Would you like to book again (yes/no)? ')

    if book_again == 'no':
        print("Thank you")
