calculateFlight(geoPositions: GeoPos[]) : GeoPos []
    flight_positions = new GeoPos[geoPositions.length]
    flightPositions[0] = geoPositions[0]
    currentPos = geoPositions[0]
    geoPositions.remove(0)
    # Ermittele naheliegende Geopos

    while geoPositoins.length() > 0
        distanz = getDistance(currentPos, geoPositions[0])
        closestPosIndex = 0
        
        for i = 1; i<geoPositions.length; i+=1
            newDistanz = getDistance(currentPos, geoPositions[i])
            if  newDistanz < distanz
                distanz = newDistanz 
                closestPosIndex = i

        nextTarget = geoPositions[closestPosIndex]
        flight_positions.push(nextTarget)
        geoPositions.remove[closestPosIndex]
        


    
