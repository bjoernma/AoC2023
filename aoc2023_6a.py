# 6a input
#lrace_duration = [7,15,30] # in ms
#lrecord_race_distance = [9,40,200] # mm
# 6a my input
#lrace_duration = [46,82,84,79]
#lrecord_race_distance = [347, 1522, 1406, 1471]
# 6b my input
lrace_duration = [46828479]
lrecord_race_distance = [347152214061471]
# 6b test input
lrace_duration = [71530] # in ms
lrecord_race_distance = [940200] # mm

total_product = 1
for race_duration, record_race_distance in zip(lrace_duration, lrecord_race_distance):
	round_cnt_record = 0
	for time in range(race_duration):
		speed = time # in m/s
		distance = (race_duration - speed) * speed
		print(f'{speed=} {distance=}')
		if distance > record_race_distance:
			round_cnt_record += 1
			# the following lines belong to 6b: The answer is symmetric so it\'s enough to find the first speed that is faster and calculate the answer.
			first = speed
			print(f'First possible {speed=} found. Symmetric so its {race_duration-2*speed+1=}')
			break
	
	print(f'{round_cnt_record=}')
	total_product *= round_cnt_record

print(f'{total_product=}')
71530-15

