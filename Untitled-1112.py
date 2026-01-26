def countVisitors(entry):
    if not len(entry):
        RaiseError('Bei einem leeren Array kann der Monat nicht bestimmt werden.')
    days_in_month = entry[0].getDaysOfMonth()
    countVisArr = []
    dayDict = {}

    for day in range(0, days_in_month):
        dayDict[day + 1] = []

    for element in entry:
        dayDict[element.getDay()].append(element)

    for day in range(0, days_in_month):
        if not len(dayDict[day+1]):
            # no visitors on this day
            countVisArr.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        current_hour = 9
        visIn = 0
        visOut = 0
        visCurrent = 0
        dayArr = []

        for element in dayDict[day+1]:
            while current_hour < element.getHour():
                # we need a while loop here to account for hours without change in visitors 
                visCurrent -= visOut
                dayArr.append(visCurrent)
                visOut = 0
                visIn = 0
                current_hour += 1
            if element.comeInOut == 0:
                # visitors coming in
                visIn += element.noPeople
                visCurrent += element.noPeople
            if element.comeInOut == 1:
                # one visitor is leaving
                visOut += 1

        # now we have the visitors from start of day until the last time entry.
        # The park should be empty.

        while current_hour < 19:
            dayArr.append(0)
 