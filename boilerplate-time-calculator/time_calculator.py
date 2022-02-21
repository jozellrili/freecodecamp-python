from datetime import datetime, timedelta, date

def add_time(start, duration, day = ''):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    start_time =  datetime.strptime(start, '%I:%M %p')
    time = duration.split(':')
    computed_time = start_time + timedelta(minutes=int(time[1]), hours=int(time[0]))

    delta = date(computed_time.year, computed_time.month, computed_time.day) - date(start_time.year, start_time.month, start_time.day)
    diff = delta.days
   
    desc = ''
    if (day != ''):
      if diff > 6:
        current_day = (diff + days.index(day.lower()))  % 7
      else:
         current_day = days.index(day.lower()) + diff
        
      desc = ', ' + days[current_day].capitalize()

    if diff == 1:
      desc += ' (next day)'
      
    if diff > 1:
      desc += ' (' + str(diff) +' days later)'

    new_time = datetime.strftime(computed_time, '%-I:%M %p') + desc

    return new_time