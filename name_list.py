main_list = ['Lee', 'Stan', 'Barry', 'Cerl', 'John', 'Eddy', 'Uli', 'Kareeen', 'Joa', 'Zauzanne', 'Joanne', 'Alexandr']
print("main_list:", main_list)

print("Sorted by length:", sorted(main_list, key=len))

list_3 = []
list_4 = []
list_5 = []
list_6 = []
list_7 = []
list_8 = []
n = 0


print("\n3-letter names:")
for i in main_list:
	if (len(main_list[n])) == 3:
 		print("found:", main_list[n])
 		list_3.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0
 			
	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0


print("\n4-letter names:")
for i in main_list:
	if (len(main_list[n])) == 4:
 		print("found:", main_list[n])
 		list_4.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0
 			
	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0


print("\n5-letter names:")
for i in main_list:
	if (len(main_list[n])) == 5:
 		print("found:", main_list[n])
 		list_5.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0
 			
	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0


print("\n6-letter names:")
for i in main_list:
	if (len(main_list[n])) == 6:
 		print("found:", main_list[n])
 		list_6.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0

	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0


print("\n7-letter names:")
for i in main_list:
	if (len(main_list[n])) == 7:
 		print("found:", main_list[n])
 		list_7.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0
 			
	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0


print("\n8-letter names:")
for i in main_list:
	if (len(main_list[n])) == 8:
 		print("found:", main_list[n])
 		list_8.append(main_list[n])
 		n=n+1
 		if n >= len(main_list):
 			n=0
 			
	else:
 		n=n+1
 		if n >= len(main_list):
 			n=0








