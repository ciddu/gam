puzzle = {1:2, 2:2, 3:2, 4:2}
solution = {1:{1:1, 2:0, 3:0, 4:1}, 2:{1:1, 2:1, 3:0, 4:0}, 3:{1:0, 2:1, 3:1, 4:0}, 4:{1:0, 2:0, 3:1, 4:1}}

MESSAGE = "Enter the lines you select with square number in pattern (s1,s2,s3,s4,sqno.)"


def check_solution(puzzle, enter_put):
	sqaure_number = enter_put[4]
	total_sum = sum(enter_put) - sqaure_number

	if total_sum == puzzle[sqaure_number]:
		ran = range(0, 4)
		for i in ran:
			if int(enter_put[i]) == solution[sqaure_number][i+1]:
				print 'side' +str(i+1)+  'is correct'
			else:
				print 'side' +str(i+1)+  'is incorrect'

		enter_input = input(MESSAGE)
		check_solution(puzzle, enter_input)
	else:
		print 'Sum is'+str(total_sum)+ '. Actual sum for sqaure '+str(puzzle[sqaure_number])


enter_input = input(MESSAGE)
check_solution(puzzle, enter_input)