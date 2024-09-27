#----------------------------------------------------
# Assignment 1: Mini-Beartracks
# Mini-Beartracks
# Author: Khevish Singh Jankee
# Collaborators/References:
#----------------------------------------------------
def menu():
	''' 
	Display the menu contents for user selection and validates the user input
	Inputs: NA
	Returns user_input(int) number 1-4
	'''
	# initialize variables
	border="="*26
	user_input=""
	# display menu
	print(border)
	print("Welcome to Mini-Beartracks")
	print(border)
	print()
	print("What would you like to do?")
	print("1. Print timetable")
	print("2. Enroll in course")
	print("3. drop course")
	print("4. Quit")
	# prompt user to input a choice
	user_input=input("> ")
	print()
	# validate user input which need to be between 1 - 4
	while user_input not in ["1","2","3","4"]:
		# display error message
		print("Sorry invalid entry. Please enter a choice from 1 to 4")
		user_input=input('>')
	return int(user_input)
    
def mwf_courses(courses,classes,time):
	'''
	check if course time is the same as current time and course is on Monday, Wednesday and Friday only
	Inputs: 
	     courses (list): a list of courses for one student
	     classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	     time  (string): the current time
	Returns a list with course name and seats available; otherwise "" if there is no course at the current time
	'''
	
	for course in courses:
		# check for courses at current time and on mon,wed,fri(MWF)
		if classes[course][0][1]==time and classes[course][0][0]=="MWF":
			# seperate course name from course number/level
			course_name=course.split()
			# truncate course name if its length is greater than 4
			if len(course_name[0])>4:
				return [course_name[0][0:3]+"* "+course.split()[1],classes[course][1]]
			else:
				return [course,classes[course][1]]
	return ""
			
def tr_courses(courses,classes,time):
	'''
	check if course time is the same as current time and course is on Tuesday and Thursday only
	Inputs: 
	     courses (list): a list of courses for one student
	     classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	     time  (string): the current time
	Returns a list with course name and seats available; otherwise "" if there is no course at the current time
	'''	
	for course in courses:
		# check for courses at current time and on tues,thurs(TR)
		if classes[course][0][1]==time and classes[course][0][0]=="TR":
			# seperate course name from course number/level			
			course_name=course.split()
			# truncate course name if its length is greater than 4			
			if len(course_name[0])>4:
				return [course_name[0][0:3]+"* "+course.split()[1],classes[course][1]]
			else:
				return [course,classes[course][1]]
	return ""
		
def display_lines(courses,classes,time)	:
	'''
	display the course name and seats available at a specific time with appropriate formatting
	Inputs: 
	     courses (list): a list of courses for one student
	     classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	     time  (string): the current time
	Returns None
	'''	
	# initiallize variables
	spaces=" "*10
	margin=" "*6	
	seperator="|"
	spaces_sep=spaces+seperator
	space_line='|'+(spaces_sep)*5
	# check for courses at current time
	mwf=mwf_courses(courses,classes,time)
	tr=tr_courses(courses,classes,time)
	
	if mwf=="" and tr=="": # no course at current time
		print(time.ljust(len(margin))+space_line)
		print(margin+space_line)
		
	elif tr=="" and mwf!="": # course only on Monday,Wednesday, Friday
		#display time, course name and available seats with appropriate formatting
		print(time.ljust(len(margin))+seperator+(mwf[0].center(len(spaces))+seperator+spaces+seperator)*2+mwf[0].center(len(spaces))+seperator)
		print(margin+seperator+(str(mwf[1]).center(len(spaces))+seperator+spaces+seperator)*2+str(mwf[1]).center(len(spaces))+seperator)
	
	elif tr!="" and mwf=="": # course only on Tuesdays and thursdays
		#display time, course name and available seats with appropriate formatting		
		print(time.ljust(len(margin))+seperator+(spaces+seperator+tr[0].center(len(spaces))+seperator)*2+spaces+seperator)
		print(margin+seperator+(spaces+seperator+str(tr[1]).center(len(spaces))+seperator)*2+spaces+seperator)
	
	else: # course on all 5 days
		#display time, course name and available seats with appropriate formatting		
		print(time.ljust(len(margin))+seperator+(mwf[0].center(len(spaces))+seperator+tr[0].center(len(spaces))+seperator)*2+mwf[0].center(len(spaces))+seperator)
		print(margin+seperator+(str(mwf[1]).center(len(spaces))+seperator+str(tr[1]).center(len(spaces))+seperator)*2+str(mwf[1]).center(len(spaces))+seperator)
		
def display_timetable(courses,classes):
	'''
	display the timetable with course name and seats available with appropriate formatting
	Inputs: 
	     courses (list): a list of courses for one student
	     classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	Returns None
	'''	
	# initiallize variables
	margin=" "*6
	print(margin+("".join([day.center(11) for day in ["Mon",'Tues','Wed','Thurs','Fri']])))	
	times=['8:00','8:30','9:00','9:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30']
	border="-"*10+"+"
	spaces=" "*10+"|"
	seperator="-"*10+'|'
	line=margin+"+"+border*5
	space_line='|'+spaces*5
	print(line)
	
	for time in times:
		# display courses and seats for specific time and days
		display_lines(courses,classes,time)
		#check for specific times for different display specification
		if time in['10:30','13:30','16:30']:
			print(line)
		elif time in ['9:00','12:00','15:00']:
			print(margin+'|'+(spaces+seperator)*2+spaces)
		elif time in ['8:30','9:30','11:30','12:30','14:30','15:30']:
			print(margin+'|'+(seperator+spaces)*2+seperator)
		else:
			print(margin+space_line)

def create_student():
	'''
	create a student dictionary with student id, faculty, student name and courses. 
	Inputs:NA
	Returns a dictionary with all students information related to their student id.{student_id:[faculty, Name,[courses],...}
	'''
	#initiallize variable
	students={}
	# read in file students.txt to extract all informations(faculty,name) about students
	reader=open("students.txt","r")
	for line in reader.readlines():
		information=line.split(",")
		students[information[0].strip()]=[information[1].strip(),information[2].strip(),[]]
	reader.close()
	
	# read in file enrollment.txt to extract information about which course each student is enrolled in
	reader=open("enrollment.txt","r")
	for line in reader.readlines():
		information=line.split(":")
		students[information[1].strip()][2].append(information[0].strip())
	reader.close()
	
	return students

def create_classes():
	'''
	create a classes dictionary with course name, day, time, seats. {course_name:[[day, time], seats],...}
	Inputs:NA
	Returns a dictionary with all classes information related to the course name.
	'''	
	# initialize variable
	classes={}
	# read in file courses.txt to extract information about course name, day, time, seats
	reader=open("courses.txt","r")
	for line in reader.readlines():
		information=line.split(";")
		classes[information[0].strip()]=[information[1].strip().split(),int(information[2].strip())]
	
	return classes

def choice1(students,classes):
	'''
	menu option 1) print the timetable of a student
	Inputs: 
	    students(dictionary): contains student_id, faculty, name, courses. {student_id:[faculty, Name,[courses],...}
	    classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	Returns None
	'''
	# prompt user to input student id
	student_id=input('Student ID: ')
	# check if student_id is valid then print timetble otherwise display error message
	if not student_id in students:
		print('Invalid Student ID. Cannot print timetable')
	else:
		print("Timetable for {0} in the faculty of {1}".format(students[student_id][1].upper(),students[student_id][0]))
		display_timetable(students[student_id][2],classes)	
		
def check_conflict(student_classes,classes,course):
	'''
	determine if a course is in conflict with an already enrolled course
	Inputs: 
	    student_classes(list): contains all courses a specific student is enrolled in
	    classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	    course (string): a course the student want to enroll in
	Returns True if there is a conflict; otherwise False
	'''	
	# check if there is a time conflict between the course and already enrolled courses
	for name in classes:
		if " ".join(classes[name][0])==" ".join(classes[course][0]) and name in student_classes:
			return True
	return False
	
	
def choice2(students,classes):
	'''
	menu option 2) allows a student to enroll in a course
	Inputs: 
	    students(dictionary): contains student_id, faculty, name, courses. {student_id:[faculty, Name,[courses],...}
	    classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	Returns a list which contains [True,student_id,course name] ;otherwise [False]
	'''	
	# promt user to input student id
	student_id=input('Student ID: ')
	if not student_id in students:
		print('Invalid Student ID. Cannot continue with course enrollment.')
	else:
		# prompt user to input course name
		course=input("course name: ").upper()
		# check if course is valid and if there is no conflict else display error message
		if course in classes:
			if not check_conflict(students[student_id][2],classes,course):
				if classes[course][1]>0:
					print("{0} has successfully been enrolled in {1} on {2}".format(students[student_id][1],course," ".join(classes[course][0])))
					return [True,student_id,course]
				else:
					print("Cannot enroll. {0} is already at capacity. Please contact advisor to get on waiting list".format(course))
			else:
				print("Schedule conflict: already registered for course on"," ".join(classes[course][0]))		
		else:
			print('Invalid course name')	
	return [False]

def choice3(students,classes):
	'''
	menu option 3) allows a student to drop a course
	Inputs: 
	    students(dictionary): contains student_id, faculty, name, courses. {student_id:[faculty, Name,[courses],...}
	    classes (dictionary): contains course name, day, time, seats available {name:[[day,time],seats]}
	Returns a list which contains [True,student_id,course name] ;otherwise [False]
	'''	
	# promt user to input student_id
	student_id=input('Student ID: ')
	# check if student_id is valid otherwise display error message
	if not student_id in students:
		print('Invalid student ID. Cannot continue with course drop.')
	else:
		#display list of enrolled courses
		print("Select course to drop:")
		for course in students[student_id][2]:
			print("- ",course)
			
		course=input("> ").upper()
		# check if course name is valid then drop otherwise display error message
		if course in classes:
			if course in students[student_id][2]:
				print("{0} has successfully dropped {1}".format(students[student_id][1],course))
				return [True,student_id,course]
			else:
				print("Drop failed. {0} is not currently registered in {1}.".format(students[student_id][1],course))		
		else:
			print('Drop failed. {0} is not currently registered in {1}.'.format(students[student_id][1],course))	
	return [False]

def update_file(students):
	'''
	menu option 3) allows a student to drop a course
	Inputs: 
	    students(dictionary): contains student_id, faculty, name, courses. {student_id:[faculty, Name,[courses],...}
	Returns None
	'''
	# open file enrollment.txt to overwrite its content with the updated version
	writer=open("enrollment.txt","w")
	for student_id in students:
		for course in students[student_id][2]:
			writer.write(course+": "+student_id+"\n")
			
	writer.close()
	
def main():
	# create student and classes dictionaries
	students=create_student()
	classes=create_classes()
	#get menu choice
	menu_choice=menu()
	
	# check if menu choice is 4 the stop else loop
	while menu_choice!=4:
		
		if menu_choice==1:
			# display time table
			choice1(students,classes)
			
		elif menu_choice==2:
			# enroll in class
			update_enrollment=choice2(students,classes)
			# check if there is any changes then update in students and classes dictionaries
			if update_enrollment[0]:
				students[update_enrollment[1]][2].append(update_enrollment[2])
				classes[update_enrollment[2]][1]+=1
		else:
			# drop class
			update_enrollment=choice3(students,classes)
			# check if there is any changes then update in students and classes dictionaries			
			if update_enrollment[0]:
				students[update_enrollment[1]][2].remove(update_enrollment[2])
				classes[update_enrollment[2]][1]-=1
			
		print()
		menu_choice=menu()
	print("Goodbye")
	# update file with latest information
	update_file(students)	
			
	
	
main()
