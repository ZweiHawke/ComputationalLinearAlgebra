#set variables
filenames = [
 "rbradshaw_mat1.txt", "rbradshaw_mat2.txt", "rbradshaw_mat3.txt",
 "rbradshaw_mat4.txt", "rbradshaw_mat5.txt", "rbradshaw_mat6.txt"
]
arr1 = []
arr2 = []
arrR = []
name1 = ""
name2 = ""
val1 = 0
val2 = 0
menuStage = 0
running = True

print("Matrix adding program:")
while running:
	match menuStage:
	
		#ask for first name
		case 0:
			arr1 = []
			arr2 = []
			arrR = []
			val = 0
			print("Select the first matrix (1-6):")
			val = input(">>> ")
			val = int(val)
			if val >= 1 and val <= 6:
				name1 = filenames[val-1]
				val1 = val
				menuStage = 1
				
		#ask for second name
		case 1:
			print("Select the second matrix (1-6):")
			val = 0
			val = input(">>> ")
			val = int(val)
			if val >= 1 and val <= 6:
				name2 = filenames[val-1]
				val2 = val
				menuStage = 2

		#make arrays
		case 2:
			#first array
			f1 = open(name1, 'r')
			with f1 as file:
				for line in file:
					val = line.split(" ")
					val.pop()
					arr1.append(val)
			f1.close()
			#print(arr1)

			#second array
			f2 = open(name2, 'r')
			with f2 as file:
				for line in file:
					val = line.split(" ")
					val.pop()
					arr2.append(val)
			f2.close()
			#print(arr2)

			menuStage = 3

		#compute arrays
		case 3:
			f3 = open("rbradshaw_p2_out"+str(val1)+str(val2)+".txt",'w')
			
			if len(arr1) == len(arr2) and len(arr1[0]) == len(arr2[0]):
				print("Arrays are the same size.")
				print(name1)
				print(name2)
				arrR=[]
				col = 0
				#create resultant array
				for c in arr1:
					val = []
					row = 0
					for r in arr1[col]:
						val.append(float(arr1[col][row])+float(arr2[col][row]))
						row += 1
					arrR.append(val)
					col += 1

				print (arrR)

				#write array to merger file
				col = 0
				for c in arrR:
					row = 0
					for r in arrR[0]:
						f3.write(str(arrR[col][row])+" ")
						print (arrR[col][row])
						row += 1
					f3.write("\n")
					col += 1
				
			else:
				print("Arrays are not the same dimension.")
				f3.write("Arrays are not the same dimension.")

			f3.close()
			
			menuStage = 0