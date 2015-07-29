''' ##################################################
    This script creates the map sheet overview for the map 4000 of Berlin (Karte 4000 Berlin) in Soldner coordinate system    
    ##################################################    
'''

''' open csv file '''
txtFile = open('2015-07-29-k4-uebersicht.csv', 'w')

''' write the header line '''
txtFile.write('%s;%s\n'%('kb', 'geom_3068'))

''' implement functions '''
def xToTheEast(sheet):
    ''' x to the left '''
    if sheet in (1,5):
        left = center_x - 1600
        right = center_x 
    if sheet in (2,6):
        left = center_x - 1600 * 2 
        right = center_x - 1600
    if sheet in (3,7):
        left = center_x - 1600  * 3 
        right = center_x - 1600 * 2
    if sheet in (4,8):
        left = center_x - 1600  * 4
        right = center_x - 1600 * 3
    return left, right

def xToTheWest(sheet):
    ''' x to the right '''
    if sheet in (1,5):
        left = center_x 
        right = center_x + 1600
    if sheet in (2,6):
        left = center_x + 1600 
        right = center_x + 1600 * 2
    if sheet in (3,7):
        left = center_x + 1600  * 2 
        right = center_x + 1600 * 3
    if sheet in (4,8):
        left = center_x + 1600  * 3
        right = center_x + 1600 * 4
    return left, right

def yUp(sheet):
    ''' y up '''
    if sheet <= 4:
        top = center_y + 2400
        bottom = center_y
    if sheet > 4:
        top = center_y + 2400 * 2
        bottom = center_y + 2400
    return top, bottom

def yDown(sheet):
    ''' y down '''    
    if sheet <= 4:
        top = center_y 
        bottom = center_y - 2400
    if sheet > 4:
        top = center_y - 2400 
        bottom = center_y - 2400 * 2
    return top, bottom



''' 1: create north east map sheets '''
def firstSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        #left, right = xToTheEast(sheet)
        #top, bottom = yUp(sheet)
        ''' x to the right '''
        if sheet in (1,5):
            left = center_x 
            right = center_x + 1600
        if sheet in (2,6):
            left = center_x + 1600 
            right = center_x + 1600 * 2
        if sheet in (3,7):
            left = center_x + 1600  * 2 
            right = center_x + 1600 * 3
        if sheet in (4,8):
            left = center_x + 1600  * 3
            right = center_x + 1600 * 4

        ''' y up '''
        if sheet <= 4:
            top = center_y + 2400
            bottom = center_y
        if sheet > 4:
            top = center_y + 2400 * 2
            bottom = center_y + 2400
        '''' write to csv file'''    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + str(sheet), left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)


minimum = 101
maximum = 121
column = 2
center_x = 40000
while 1 < 2:
    center_y = 10000
    for kbNumber in range(minimum, maximum + 10, 10):
        print kbNumber
        firstSector(kbNumber)    
        center_y += 2400 * 2
    center_x += 1600 * 4
    minimum += 1
    maximum += 1
    column -= 1
    if column == 0:
        break

#''' 2: create south east map sheets '''    
def secondSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        left, right = xToTheEast(sheet)
        #top, bottom = yDown(sheet)
        ''' x to the right '''
        if sheet in (1,5):
            left = center_x 
            right = center_x + 1600
        if sheet in (2,6):
            left = center_x + 1600 
            right = center_x + 1600 * 2
        if sheet in (3,7):
            left = center_x + 1600  * 2 
            right = center_x + 1600 * 3
        if sheet in (4,8):
            left = center_x + 1600  * 3
            right = center_x + 1600 * 4
        
        ''' y down '''    
        if sheet <= 4:
            top = center_y 
            bottom = center_y - 2400
        if sheet > 4:
            top = center_y - 2400 
            bottom = center_y - 2400 * 2
        '''' write to csv file'''    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + str(sheet), left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)
        
minimum = 201
maximum = 211
column = 2
center_x = 40000
while 1 < 2:
    center_y = 10000
    for kbNumber in range(minimum, maximum + 10, 10):
        print kbNumber
        secondSector(kbNumber)    
        center_y -= 2400 * 2
    center_x += 1600 * 4
    minimum += 1
    maximum += 1
    column -= 1
    if column == 0:
        break

#''' 3: create south west map sheets '''
def thirdSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        #left, right = xToTheWest(sheet)
        #top, bottom = yDown(sheet)
        ''' x to the left'''
        if sheet in (1,5):
            left = center_x - 1600
            right = center_x 
        if sheet in (2,6):
            left = center_x - 1600 * 2 
            right = center_x - 1600
        if sheet in (3,7):
            left = center_x - 1600  * 3 
            right = center_x - 1600 * 2
        if sheet in (4,8):
            left = center_x - 1600  * 4
            right = center_x - 1600 * 3
        
        
        ''' y down '''    
        if sheet <= 4:
            top = center_y 
            bottom = center_y - 2400
        if sheet > 4:
            top = center_y - 2400 
            bottom = center_y - 2400 * 2
        '''' write to csv file'''    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + str(sheet), left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)

minimum = 301
maximum = 311
column = 6
center_x = 40000
while 1 < 2:
    center_y = 10000
    for kbNumber in range(minimum, maximum + 10, 10):
        print kbNumber
        thirdSector(kbNumber)    
        center_y -= 2400 * 2
    center_x -= 1600 * 4
    minimum += 1
    maximum += 1
    column -= 1
    if column == 0:
        break    

''' 4: create north west map sheets '''    
def fourthSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        #left, right = xToTheEast(sheet)
        #top, bottom = yUp(sheet)
        ''' x to the left'''
        if sheet in (1,5):
            left = center_x - 1600
            right = center_x 
        if sheet in (2,6):
            left = center_x - 1600 * 2 
            right = center_x - 1600
        if sheet in (3,7):
            left = center_x - 1600  * 3 
            right = center_x - 1600 * 2
        if sheet in (4,8):
            left = center_x - 1600  * 4
            right = center_x - 1600 * 3
        
        ''' y up '''    
        if sheet <= 4:
            top = center_y 
            bottom = center_y + 2400
        if sheet > 4:
            top = center_y + 2400 
            bottom = center_y + 2400 * 2
            
        '''' write to csv file'''    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + str(sheet), left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)


minimum = 401
maximum = 451
column = 6
center_x = 40000
while 1 < 2:
    center_y = 10000
    for kbNumber in range(minimum, maximum + 10, 10):
        print kbNumber
        fourthSector(kbNumber)    
        center_y += 2400 * 2
    center_x -= 1600 * 4
    minimum += 1
    maximum += 1
    column -= 1
    if column == 0:
        break   

''' close csv file '''
txtFile.close()