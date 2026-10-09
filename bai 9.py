km = float (input())
if km <= 0:
    print("Quang duong khong hop le")
elif km <= 1:
    tien = 11000
    print("tien cuoc:", tien,"dong")
elif km <= 30:
    tien = 11000 + ( km  -1 ) * 9000
    print("tien cuoc:", tien,"dong")
else:
    tien = 4 * 11000 + 9000 + ( km -30 ) *10000
    print("tien cuoc:", tien,"dong")
