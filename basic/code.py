# --------------
# Code starts here
class_1 = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Bengio"]
class_2 = ["Hilary Mason", "Carla Gentry", "Corinna Cortes"]
new_class = class_1 + class_2

print(new_class)
new_class.append("Peter Warden")
print(new_class)

new_class.remove("Carla Gentry")
# Code ends here


# --------------
# Code starts here
course = ["Math", "English", "History", "French", "Science"]
marks = [65, 70, 80, 70, 60]

courses = {i:j for i,j in zip(course, marks)}
total = 0
for k, v in courses.items():
    print("{} : {}".format(k,v))
    total += v
percentage = (total / 500) * 100
print(percentage)    
# Code ends here


# --------------
# Code starts here
s = ["Geoffrey Hinton", "Andrew Ng", "Sebastian Raschka", "Yoshua Benjio", "Hilary Mason", "Corinna Cortes", "Peter Warden"]
m = [78, 95, 65, 50, 70, 66, 75]

mathematics = {i:j for i,j in zip(s,m)}
topper = max(mathematics, key = mathematics.get)
print(topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
first_name, last_name = topper.split(" ")
full_name = last_name + " " + first_name

certificate_name = full_name.upper()
print(certificate_name)

# Code ends here


