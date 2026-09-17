#why use sets
#suppose students have selected subjects

subject = {"python", "java", "python", "SQL", "java"}

print(subject  )print(subject) = {'java', 'SQL', 'python'}

#add valuse to a set
subject = {"python", "java"}

subjects.add("SQL")
print(subject)
#remove values from a set
subjects.remove("java")
print(subjects)
#sets do not allow duplicate values
number = {1, 2, 2, 3, 3, 4}

print(number)
student = {name:abhisarika , marks:98 , subjects:python}
print(student.key())
print(student.value())
print(student.items())
#dictionaries in python
#dictionaries is a collection of key-value pairs that is unordered and mutable
student = {
    "name": "abhisarika",
    "age":00,
    "coures": "python"
}
print(student)
#access the elements in the dic
print(student[name])
print(student[age])
print(student[subject])
#change values in a dictionary
student["age"] = 11
print(student["age"])
#add new data to a dictionary
student["city"] = "kandukur"
print(student)
#remove data 
student.pop("city")
print(student)
student = {"name":"abhisarika","marks":"98","course":"python"}
print(student.get('name'))
print(student.get('marks'))
print(student.get('course'))
#update the value of specified key
student.update({"marks":18})
print(student)
#pop removes the specified key and the value
student.pop("marks")
print(student)

#popitem()
student={"name":"abhisarika","marks":98,"subject":"python"}
student.popitem()
print(student)

#set defualt
student={"name":"abhisarika"}
student.setdfault("age",12)
print(student)
#clear method
student.clear()
print(student)

student={"name":"abhisarika","age":19}
new_student = student.copy()
print(new_student)
#order of evulation(bodmas)
result=2+13*2
prints(result)

