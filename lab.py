print("Howdy Team!")
print("Team Lab 3")
print("Team members: Alyssa, Brisania, Gabe, Vincent")
print("Activity 1")
#A
pounds=int(input("What is the force in pounds?")
newtons=(pounds*4.44822)
print(pounds+" pounds force in Newtons is "+newtons+" newtons.")


# Activity 2
time_1 = float(input("Enter time one: "))
x_1 = float(input("Enter the first x position: "))
y_1 = float(input("Enter the first y position: "))
z_1 = float(input("Enter the first z position: "))
time_5 = float(input("Enter time two: "))
x_2 = float(input("Enter the second x position: "))
y_2 = float(input("Enter the second y position: "))
z_2 = float(input("Enter the second z position: "))

delta_time = time_5 - time_1
time_sec = delta_time/4
time_2 = time_sec + time_1
time_3 = time_sec*2 + time_1
time_4 = time_sec*3 + time_1
new_time = time_1

print(f"{'X':>10}{'Y':>10}{'Z':>10}{'Time':>10}")
print("-" * 40)

for t in [0, 0.25, 0.5, 0.75, 1]:
    v_int_x = (1 - t) * x_1 + t * x_2
    v_int_y = (1 - t) * y_1 + t * y_2
    v_int_z = (1 - t) * z_1 + t * z_2
    print(f"{v_int_x:>10.2f}{v_int_y:>10.2f}{v_int_z:>10.2f}{new_time:>10.2f}")
    new_time = new_time + time_sec
# V_interp = (1 - t) * A + t * B
# v_1 = (1-t) * 

# V_interp = (1 - t) * A + t * B
# I think t should be time in the formula becasue that part of the formula determines the position on the interpolated vectors. ex: t=1 is 100% of the vector, and t=0.5 is 50% of the vector.
# It seems like there is supposed to be V_interp calculations for each component of the two positions: x, y, and z.
# A is your starting 3D vector (x_1, y_1, z_1)
# B is your ending 3D vector (x_2, y_2, z_2)
