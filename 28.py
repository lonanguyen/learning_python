employee={'Jhon':2900,'Sarah':1800,'Joseph':2400}
print(employee['Sarah'])
print(employee['Jhon'])
print(employee['Joseph'])
employee1={'Ali':10000,'Jhon':15000,'Marry':5000}
for emp,salary in employee1.items():
	print("Salary of employee %s is %d" %(emp,salary))
	
core = {'A':100,'B':200,'C':300}
print(core['A'])
print(core['B'])
print(core['C'])

core01 = {'D':400,'E':500,'F':600}
for emp,core in core01.items():
	print("core of student %s is %d" %(emp,core))