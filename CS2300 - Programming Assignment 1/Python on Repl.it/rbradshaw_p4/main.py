vec = [[-1, -2], [-3, 3], [2, -1], [3, 1], [1, 3]]
vecName = ["r", "s", "u", "v", "w"]
vec1 = [0, 2, 1]
vec2 = [1, 3, 3]
iterVal = 0

#dot product
for i in vec1:
	resVec = []
	vecPos = 0
	f1 = open(
	 "rbradshaw_p4_" + str(vecName[vec1[iterVal]]) + str(vecName[vec2[iterVal]]) +
	 ".txt", "w")
	#iterate over vector size
	prod = 0
	for j in range(2):
		vecPos += vec[vec1[iterVal]][prod] * vec[vec2[iterVal]][prod]
		prod += 1
	f1.write(str(vecPos) + "\n")
	f1.close()
	iterVal += 1
