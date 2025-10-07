

artist = str(input("Artist name: "))
tour = str(input("Tour name: "))
location = str(input("Enter the location: "))
year = int(input('Which year concert is gonna be in: '))
month = int(input('Which month concert is gonna be on: '))
day = int(input('Which day concert is gonna be on: '))
hour = int(input('Please tell the time(hour, 0-23): '))
minute = int(input('Please tell the minute: '))



ticket_holder_name = str(input("Whats your name: "))

print('*'*40)
print('        -- ADMIT ONE: VIP PASS --       ')
print('*'*40)
print(f'\n\nArtist:     [{artist}]')
print(f'Tour:       [{tour}]')
print(f'Location:   [{location}]')
print(f'Date:       [{year}.{month}.{day},  {hour}:{minute}]')

print('\n')
print('-'*40)
print(f'Issued to:  [{ticket_holder_name}]')
print(f'Event code: [{artist}-{location}-VIP]')
print('-'*40)

print("      *** Enjoy the Show! ***    ")
print('*'*40)