''' ##################################################
    This script creates the map sheet overview for the map 4000 of Berlin (Karte 4000 Berlin) in Soldner coordinate system    
    ##################################################    
'''

''' open csv file '''
txtFile = open('2015-07-29-k4-uebersicht.csv', 'w')

''' List of map sheet endings '''
abcd = ['_A', '_B', '_C', '_D']

''' write the header line '''
txtFile.write('%s;%s\n'%('kb', 'geom_3068'))

''' class for create map sheets in right order: XXX_A , XXX_B, XXX_C, XXX_D '''
#def writePolygon(this, kb):
    ##kb      = 0
    #left    = 0
    #right   = 0
    #top     = 0
    #bottom  = 0
    #for sheet in this:
        #if '_A' == sheet: 
            #left = center_x - 3200
            #bottom = center_y + 2400
        #if '_B' == sheet: 
            #left = center_x + 3200
            #bottom = center_y + 2400
        #if '_C' == sheet: 
            #left = center_x - 3200
            #bottom = center_y - 2400
        #if '_D' == sheet: 
            #left = center_x + 3200
            #bottom = center_y - 2400
        #right = center_x
        #top = center_y    
        #polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + sheet, left, top, right, top, right, bottom,left, bottom, left, top)
        #txtFile.write(polygon)

def firstSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        ''' x to the right '''
        if sheet == 1:
            left = center_x 
            right = center_x + 1600
        if sheet == 2:
            left = center_x + 1600 
            right = center_x + 1600 * 2
        if sheet == 3:
            left = center_x + 1600  * 2 
            right = center_x + 1600 * 3
        if sheet == 4:
            left = center_x + 1600  * 3
            right = center_x + 1600 * 4
        if sheet == 5:
            left = center_x
            right = center_x + 1600
        if sheet == 6:
            left = center_x + 1600
            right = center_x + 1600 * 2
        if sheet == 7:
            left = center_x + 1600  * 2
            right = center_x + 1600 * 3
        if sheet == 8:
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


''' 1: create north east map sheets '''
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

def secondSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        ''' x to the right '''
        if sheet == 1:
            left = center_x 
            right = center_x + 1600
        if sheet == 2:
            left = center_x + 1600 
            right = center_x + 1600 * 2
        if sheet == 3:
            left = center_x + 1600  * 2 
            right = center_x + 1600 * 3
        if sheet == 4:
            left = center_x + 1600  * 3
            right = center_x + 1600 * 4
        if sheet == 5:
            left = center_x
            right = center_x + 1600
        if sheet == 6:
            left = center_x + 1600
            right = center_x + 1600 * 2
        if sheet == 7:
            left = center_x + 1600  * 2
            right = center_x + 1600 * 3
        if sheet == 8:
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
        
#''' 2: create south east map sheets '''    
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

def thirdSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        ''' x to the right '''
        if sheet == 1:
            left = center_x - 1600
            right = center_x 
        if sheet == 2:
            left = center_x - 1600 * 2 
            right = center_x - 1600
        if sheet == 3:
            left = center_x - 1600  * 3 
            right = center_x - 1600 * 2
        if sheet == 4:
            left = center_x - 1600  * 4
            right = center_x - 1600 * 3
        if sheet == 5:
            left = center_x
            right = center_x - 1600
        if sheet == 6:
            left = center_x - 1600 * 2
            right = center_x - 1600
        if sheet == 7:
            left = center_x - 1600  * 3
            right = center_x - 1600 * 2
        if sheet == 8:
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

#''' 3: create south west map sheets '''
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

def fourthSector(kb):
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in range(1, 8 + 1):
        ''' x to the right '''
        if sheet == 1:
            left = center_x - 1600
            right = center_x 
        if sheet == 2:
            left = center_x - 1600 * 2 
            right = center_x - 1600
        if sheet == 3:
            left = center_x - 1600  * 3 
            right = center_x - 1600 * 2
        if sheet == 4:
            left = center_x - 1600  * 4
            right = center_x - 1600 * 3
        if sheet == 5:
            left = center_x
            right = center_x - 1600
        if sheet == 6:
            left = center_x - 1600 * 2
            right = center_x - 1600
        if sheet == 7:
            left = center_x - 1600  * 3
            right = center_x - 1600 * 2
        if sheet == 8:
            left = center_x - 1600  * 4
            right = center_x - 1600 * 3
        ''' y down '''    
        if sheet <= 4:
            top = center_y 
            bottom = center_y + 2400
        if sheet > 4:
            top = center_y + 2400 
            bottom = center_y + 2400 * 2
        '''' write to csv file'''    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + str(sheet), left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)


''' 4: create north west map sheets '''    
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