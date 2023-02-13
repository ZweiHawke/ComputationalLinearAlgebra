#set variables
filenames = [
 "rbradshaw_mat1.txt", "rbradshaw_mat2.txt", "rbradshaw_mat3.txt",
 "rbradshaw_mat4.txt", "rbradshaw_mat5.txt", "rbradshaw_mat6.txt"
]
arr1 = []
arr2 = []
arrR = []
val1 = 0
val2 = 0
res = 0
running = True

print("Matrix multiplying program:")
for i in filenames:
	val2 += 1
	for j in filenames:
		val1 += 1
		arr1 = []
		arr2 = []
		arrR = []
		val = 0
		#first array
		f1 = open(filenames[val1 - 1], 'r')
		with f1 as file:
			for line in file:
				val = line.split(" ")
				val.pop()
				arr1.append(val)
		f1.close()
		#print(len(arr1))
		#print(len(arr1[0]))
		print(arr1)

		#second array
		f2 = open(filenames[val2 - 1], 'r')
		with f2 as file:
			for line in file:
				val = line.split(" ")
				val.pop()
				arr2.append(val)
		f2.close()
		#print(len(arr2))
		#print(len(arr2[0]))
		print(arr2)

		if len(arr1[0]) == len(arr2):
			print("Arrays are compatible.")
			f3 = open("rbradshaw_p3_out" + str(val1) + str(val2) + ".txt", 'w')
			arrR = []
			#create resultant array
			colExt = 0
			for c in arr1:
				rowExt = 0
				val = []
				for r in arr2[0]:
					iterVal = 0
					res = 0
					#add multiplied values
					for i in arr2:
						print(rowExt)
						res += float(arr2[iterVal][rowExt]) * float(arr1[colExt][iterVal])
						iterVal += 1
					val.append(res)
					rowExt += 1
				arrR.append(val)
				colExt += 1

			print(len(arrR))

			#write array to merger file
			col = 0
			for c in arrR:
				row = 0
				for r in arrR[0]:
					f3.write(str(round(arrR[col][row], 2)) + " ")
					#print(arrR[col][row])
					row += 1
				f3.write("\n")
				col += 1

			f3.close()
		else:
			print("Arrays are incompatible.")
	val1 = 0

