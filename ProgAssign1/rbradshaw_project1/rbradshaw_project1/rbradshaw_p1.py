firstName = 5
lastName = 8

# ARRAY 1
# initialize file stream and write
f1 = open("rbradshaw_mat1.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = firstName, firstName

# make array
for r in range(rows):
	row = []
	# row initial value
	val = -4 + r
	for c in range(cols):
		#row iterated value
		val += rows
		row.append(val)
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f1.write(str(arr[r][c]) + " ")
	f1.write("\n")

# close stream
f1.close()

# ARRAY 2
# initialize file stream and write
f2 = open("rbradshaw_mat2.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = firstName, lastName
# initial value
val = -1

# make array
for r in range(rows):
	row = []
	# row initial value
	for c in range(cols):
		#row iterated value
		val += 3
		row.append(val)
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f2.write(str(arr[r][c]) + " ")
	f2.write("\n")

# close stream
f2.close()

# ARRAY 3
# initialize file stream and write
f3 = open("rbradshaw_mat3.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = firstName, firstName

# make array
for r in range(rows):
	row = []
	# row initial value
	val = -1 + (r * 0.2)
	for c in range(cols):
		#row iterated value
		val += 1
		row.append(round(val, 2))
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f3.write(str(arr[r][c]) + " ")
	f3.write("\n")

# close stream
f3.close()

# ARRAY 4
# initialize file stream and write
f4 = open("rbradshaw_mat4.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = 4, 6

# make array
for r in range(rows):
	row = []
	# row initial value
	val = 18 - r * 2
	for c in range(cols):
		#row iterated value
		val -= 8
		row.append(val)
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f4.write(str(arr[r][c]) + " ")
	f4.write("\n")

# close stream
f4.close()

# ARRAY 5
# initialize file stream and write
f5 = open("rbradshaw_mat5.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = 4, 6
# initial value
val = -7.5

# make array
for r in range(rows):
	row = []
	# row initial value
	for c in range(cols):
		#row iterated value
		val += 1.5
		row.append(val)
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f5.write(str(arr[r][c]) + " ")
	f5.write("\n")

# close stream
f5.close()

# ARRAY 6
# initialize file stream and write
f6 = open("rbradshaw_mat6.txt", "w")
# initialize array to write
arr = []
# row and column size
rows, cols = 2, 4
# initial value
val = -20

# make array
for r in range(rows):
	row = []
	# row initial value
	for c in range(cols):
		#row iterated value
		val += 10
		row.append(val)
	arr.append(row)

# write array
for r in range(rows):
	for c in range(cols):
		f6.write(str(arr[r][c]) + " ")
	f6.write("\n")

# close stream
f6.close()

