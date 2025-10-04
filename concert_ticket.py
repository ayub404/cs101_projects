import datetime

def ticket_gen():
    
    current_datetime = datetime.datetime.now().replace(microsecond=0)
    

    artist_name = str(input("Enter artist name: "))
    tour_name = str(input("Enter your tour name: "))
    city = str(input("Enter your city: "))
    ticket_holders_name = str(input("Enter your full_name: "))
    date_input = input("Enter date & time(year, month, day, hour,  minute, sec): ")

    year, month, day, hour, minute, sec = map(int, date_input.split(","))
    date = datetime.datetime(year,month, day, hour, minute, sec )

# 
# 
#   

    ticket = (
        
            f"""







***************************************************
            -- ADMIT ONE: VIP PASS --
***************************************************
{        f"Artist:      [{artist_name.upper()}]\n"
        f"Tour:        [{tour_name.upper()}]\n"
        f"Location:    [{city.upper()}]\n"
        f"Date:        [{date}]"}
        
-------------------------------------------------
Issued to:   [{ticket_holders_name.upper()}] 
Issued date: [{current_datetime}]   
Event code:  [{artist_name.upper()}-[{city.upper()}]-VIP]
-------------------------------------------------
        *** Enjoy the Show! ***
*************************************************
""")
    print()
    print(ticket)


ticket_gen()
