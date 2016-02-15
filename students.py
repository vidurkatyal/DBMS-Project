import pickle
from archives import *
from relations import *
from courses import *
from course_allocations import *
from utils import write_com
import datetime

students = []
def Students():
	try:
		with open('files/students.dat','rb+') as f:
			students = pickle.load(f)
	except:
		print 'hi'
		students = []

	ch = int(raw_input('1 for add\n2 for del\n3 for upd\n4 all students'))
	if ch == 1:
		student = {} #each st is a dict
		student['name'] = raw_input('Enter name : ')
		student['rollno'] = raw_input('Roll No : ')
		student['dob'] = raw_input('DOB : ')
		student['sex'] = raw_input('Sex : ')
		student['address'] = raw_input('Address : ')
		student['branch'] = raw_input('Branch : ')
		student['type'] = raw_input('UG/PG : ')
		student['sem'] = raw_input('Sem : ')

		flag=1
		
		try:
			semester=int(student['sem'])
			if(student['type']=='UG' and semester>8):
				print('Only upto 8 semesters')
				flag=0

			if(student['type']=='PG' and semester>2):
				print('only upto 2 semesters')
				flag=0
		except:
			print 'only integer values allowed'

		if(flag==1):
			try:
				with open('files/course_allocations.dat', 'rb+') as f:
					existing = pickle.load(f)
			except:
				existing = []

			try:
				with open('files/relations.dat', 'rb+') as f:
					relations  = pickle.load(f)
			except:
				relations = []

<<<<<<< HEAD
		for i in existing:
			if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
				relation = {}
				relation['co_alloc_id'] = i['co_alloc_id']
				relation['rollno'] = student['rollno']
				relation['dor'] = datetime.datetime.now()
				if relation not in relations:
					relations.append(relation)
					print relations
					writer2f(relations)
=======
			for i in existing:
				if i['type'] == student['type'] and i['branch']== student['branch'] and i['sem']== student['sem']:
					relation = {}
					relation['co_alloc_id'] = i['co_alloc_id']
					relation['rollno'] = student['rollno']
					if relation not in relations:
						relations.append(relation)
						print relations
						writer2f(relations)
>>>>>>> b866a2e21719e658646ccefec12ebbd4773918e9


			if student not in students:
				students.append(student)
			writes2f(students)	

	elif ch == 2:
		rno = raw_input("roll no to be deleted")
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rno:
				del students[stu]
				#del allocations
				writes2f(students)
	elif ch == 3:
		rno = raw_input("roll no to be updated")
		for stu in xrange(len(students)):
			if(students[stu]['rollno']) == rno:
				students[stu]['name'] = raw_input('Enter name')
				#upd allocations
				writes2f(students)

	elif ch== 4:
		print 'Name\tRoll No\tsex\tDOB\t\tBranch\tSem\ttype\n'
		for i in xrange(len(students)):
			print (students[i]['name']+'\t'+students[i]['rollno']+'\t'+students[i]['sex']+'\t'+students[i]['dob']+'\t'+students[i]['branch']+'\t'+students[i]['sem']+'\t'+students[i]['type']+'\n')
	

def writes2f(students):
	with open('files/students.dat','wb') as f:
		pickle.dump(students,f)