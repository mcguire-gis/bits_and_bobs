#set baseline stats
base_pins= 10
base_score = 0
first_next_layer = 5
base_score =0
first_frame = 1

#set variables to baseline
def set_stats(base_pins,base_score,first_next_layer,first_frame):
    global pins, score, next_layer, frame
    pins = base_pins
    score = base_score
    next_layer = first_next_layer
    frame = first_frame

print("Strike Each Time")
set_stats(base_pins, base_score, first_next_layer, first_frame)
for i in range(1, 11):
    round_total = pins * 2
    score = score + round_total
    print("Frame: ", frame, " Pins: ", pins, " Frame score: ", round_total, " Cumulative Score: ", score)
    pins = pins + next_layer
    next_layer = next_layer + 1
    frame = frame + 1
print("Final score: ", score)

print ("\nMissing one each time")
set_stats(base_pins, base_score, first_next_layer, first_frame)
for i in range(1, 11):
    round_total = pins - 1
    score = score + round_total
    print("Frame: ", frame, " Pins: ", pins, " Frame score: ", round_total, " Cumulative Score: ", score)
    pins = pins + next_layer
    next_layer = next_layer + 1
    frame = frame + 1
print("Final score: ", score)

print("\nLast Pin Value")
missed_points = 0
set_stats(base_pins, base_score, first_next_layer, first_frame)
for i in range(1, 11):
    round_total = pins - 1
    potential = (round_total * 2) - round_total
    print("Frame: ", frame, " Pins:", pins, " Frame score: ", round_total, " Potential Score : ", pins * 2," Last Pin Value: ", (pins * 2) - round_total)
    missed_points = missed_points + ((pins * 2) - round_total)
    score = score + round_total
    pins = pins + next_layer
    next_layer = next_layer + 1
    frame = frame + 1
print("Final score: ", score, " Missed Points: ", missed_points)
frame = first_frame