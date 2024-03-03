def calculate_manhattan_distance(x1, y1, x2, y2):
    x=0
    y=0
    if(x1 - x2 < 0) :
        x = (x1 - x2) * -1
    if(y1 - y2 < 0) :
        y = (y1 - y2) * -1
    return (x + y) * 1.5

def calculate_time_to_destination(x1, y1, x2, y2, M):
    distance = calculate_manhattan_distance(x1, y1, x2, y2)
    time = distance / M
    return time

print("Test Case 1")
M = int(input("Masukkan nilai M: "))
print("Masukkan Koordinat awal robot")
x1 = int(input("x: "))
y1 = int(input("y: "))
print("Masukkan Koordinat akhir robot")
x2 = int(input("x: "))
y2 = int(input("y: "))

time_to_destination = calculate_time_to_destination(x1, y1, x2, y2, M)
print("Robot akan tiba di tujuan setelah", time_to_destination, "detik")