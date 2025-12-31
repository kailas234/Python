python_about="""Python is a high-level programming language
It is very easy to use
It is very simple to learn"""

print(len(python_about))

print(python_about[0],python_about[-1])

print(python_about[0:51])

Python_about=python_about.replace("Python","PYTHON")
print(Python_about)

print(Python_about.lower().strip())

splitedpara=Python_about.split()
print(splitedpara)

print("course" in Python_about)

print("The course description is {} characters long and has {} words.".format(len(Python_about),len(splitedpara)))
