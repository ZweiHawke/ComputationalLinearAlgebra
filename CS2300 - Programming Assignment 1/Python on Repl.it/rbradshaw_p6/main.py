#set variables
filenames = [
 "rbradshaw_mat1.txt", "rbradshaw_mat2.txt", "rbradshaw_mat3.txt",
 "rbradshaw_mat4.txt", "rbradshaw_mat5.txt", "rbradshaw_mat6.txt"
]
arr1 = []
val1 = 0

print("Matrix multiplying program:")

for i in filenames:
	arr1 = []
	val = 0
	val1 += 1
	#first array
	f1 = open(filenames[val1 - 1], 'r')
	with f1 as file:
		for line in file:
			val = line.split(" ")
			val.pop()
			arr1.append(val)
	f1.close()
	print(arr1)

	fr = open("rbradshaw_p6_mat" + str(val1) + ".txt", 'w')
	row = 0
	for c in arr1[0]:
		col = 0
		for r in arr1:
			fr.write(str(arr1[col][row]) + " ")
			col += 1
		fr.write("\n")
		row += 1
	fr.close()
