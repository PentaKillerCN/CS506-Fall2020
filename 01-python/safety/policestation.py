def draw_policestation(height=20):
    print('      ---------------------------------------------')
    print('      |                                           |      ')
    print('      |               POLICE STATION              |      ')
    i = 8
    while(i<height):
        if i%3 == 0:
            if i + 4 > height:
                while i < height:
                    print('      |                                           |      ')
                    i += 1
            else:
                print('      |      _____        _____        _____      |      ')
                print('      |     |     |      |     |      |     |     |      ')
                print('      |     |     |      |     |      |     |     |      ')
                print('      |     |_____|      |_____|      |_____|     |      ')
                i += 4
        else:
            print('      |                                           |      ')
            i += 1
    print('      |                                   ______  |      ')
    print('      |                                  | BUPD | |      ')
    print('      |         _____   _________        |______| |      ')
    print('      |     ___|     | |    |    |       |        |      ')
    print('      |    |_  ___  _| |    |    |       |        |      ')
    print('      |      ()   ()   |    |    |       |        |      ')
    print('---------------------------------------------------------\n')    

    return
