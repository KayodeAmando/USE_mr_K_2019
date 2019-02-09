import random

# ----------------------------
def get_random_list(array_len, min_val=0, max_val=1000, verbose=0):

	my_lst = [random.randint(min_val, max_val) for _ in range(array_len)]

	if verbose:
		print('The input list:\n{}\n'.format(my_lst))

	return my_lst
# ----------------------------

VERBOSE = 1
EXAMPLE = 6

# ----------------------------

if EXAMPLE == 1:

	my_lst = get_random_list(array_len=20, verbose=VERBOSE)

	min_sum_tmp = my_lst[0] + my_lst[1] 
	min_sum_idx = 0

	for idx in range(2, len(my_lst), 2):	
		sum_tmp = my_lst[idx] + my_lst[idx + 1] 
		if sum_tmp < min_sum_tmp:
			min_sum_tmp = sum_tmp
			min_sum_idx = idx

	if VERBOSE:
		print('\nThe answer:\nindex --> {}\npair --> {}\nmin_sum --> {}\n'.format(min_sum_idx, (my_lst[min_sum_idx], my_lst[min_sum_idx + 1]), min_sum_tmp))


elif EXAMPLE == 2:

	my_lst = get_random_list(array_len=20, min_val=-1000, verbose=VERBOSE)

	counter_positive = 0

	# for idx, item in enumerate(my_lst):
	for item in my_lst:
		if item > 0:
			counter_positive += 1
		if counter_positive == 3:
			break

	if counter_positive < 3:
		print('SOOBSHENIYE!')
	else:
		print(item)

		# print(idx + 1) # use with enumerate
		print(my_lst.index(item) + 1) # use without enumerate


elif EXAMPLE == 3:

	my_lst = get_random_list(array_len=40, min_val=-10000, max_val=10000, verbose=VERBOSE)

	minval_current = 1000
	
	for item in my_lst:

		condition_1 = 100 <= item <= 999
		condition_2 = item % 10 != 4

		if condition_1 and condition_2:
			if item < minval_current:
				minval_current = item

	if minval_current == 1000:
		print('SOOBSHENIYE!')
	else:
		print(minval_current)
	
		 
elif EXAMPLE == 4: # 2019, 15.25		
	
	my_lst = get_random_list(array_len=30, min_val=-10000, max_val=10000, verbose=VERBOSE)

	# -------------------------
	# opt 1:
	# my_lst_filtered = [item for item in my_lst if item % 3]
	# fin = max(my_lst_filtered)

	# opt 2
	fin = -float('inf')
	for item in my_lst:
		if item % 3 and item > fin:
			fin = item

	print('Max value from the filteled list: {}\n'.format(fin))
	# -------------------------

	for item in my_lst:
		if item > fin:
			print('The value above: {}'.format(item))		
	

elif EXAMPLE == 5:
	n = 40

	my_lst = get_random_list(array_len=n, min_val=-10000, max_val=10000, verbose=VERBOSE)


	plotina = 0
	
	for indx in range(n-1):
		klop = my_lst[indx]*my_lst[indx+1]
		if not klop % 2 and klop > 0:
			plotina += 1

	print(plotina)



elif EXAMPLE == 6:

	my_lst = get_random_list(array_len=40, min_val=-10000, max_val=10000, verbose=VERBOSE)

	# ---------------------
	# option 1
	counter = 0
	for item in my_lst:
		if 99 < item < 1000:
			counter += 1

	if counter:
		print(counter)
	else:
		print('NOOOOOOOOOOOOOO!')

	# ---------------------
	# option 2
	# counter = len([item for item in my_lst if 99 < item < 1000])
	# print(('NOOOOOOOOOOOOOO!', counter)[bool(counter)])


			
		











	
















