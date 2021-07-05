import requests
import json

saral_api = "http://saral.navgurukul.org/api/courses"
saral_url = requests.get(saral_api)
data = saral_url.json()
with open("courses.json","w") as saral_data :
    json.dump(data,saral_data,indent=4)


serial_no = 1
for courses in data["availableCourses"]:
    print(serial_no ,".",courses["name"],courses["id"])
    serial_no += 1
course = int(input("enter the course number: "))
print(data["availableCourses"][course-1]["name"])


user_input1=input("Do you want to previous : ").lower()
if user_input1 == "p" :
    serial_no = 1
    for courses in data["availableCourses"]:
        print(serial_no ,". ",courses["name"],courses["id"])
        serial_no += 1
       
            
    course = int(input("enter the course number: "))
    print(data["availableCourses"][course-1]["name"])  


saral_api_1 = ("http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][course-1]["id"])+"/exercises")
saral_url_1=requests.get(saral_api_1)
data_1 = saral_url_1.json()
with open ("parents.json","w") as saral_data_1 :
    json.dump(data_1,saral_data_1,indent=4)      
        

no=0
List=[]
print("slu",data_1["data"][1]["slug"])
for child in range(len(data_1["data"])):
    no+=1
    print("        ",no,".",data_1["data"][child]["name"])
    serial_no_1=1
    if data_1["data"][child]["childExercises"] == List:
        print("             ",serial_no_1,".",data_1["data"][child]["slug"])
        serial_no_1 += 1
    else:

        serial_no=1
        for Question in range(len(data_1["data"][child]["childExercises"])):
            print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
            serial_no+=1
Slug= int(input("Enter the number of parents no :"))
print(data_1["data"][Slug-1]["name"])
number1=input("Do you want to previous or next: ").lower()
if number1 == "p":
    no=0
    List=[]
    for child in range(len(data_1["data"])):
        no+=1
        print("        ",no,".",data_1["data"][child]["name"])
        serial_no_1=1
        if data_1["data"][child]["childExercises"] == List:
            print("             ",serial_no_1,".",data_1["data"][child]["slug"])
            serial_no_1 += 1
        else:

            serial_no=1
            for Question in range(len(data_1["data"][child]["childExercises"])):
                print("              ",serial_no,".",data_1["data"][child]["childExercises"][Question]["name"])
                serial_no+=1
    Slug= int(input("Enter the number of slug :"))
    print(data_1["data"][Slug-1]["name"])
    serial_no=1
    for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
        if data_1["data"][child]["childExercises"] == List:
            print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
            serial_no+=1

slug_ind=[]
no=0
List=[]
for child in range(len(data_1["data"])):
    no+=1
    serial_no_1=1
    if data_1["data"][child]["childExercises"] == List:
        serial_no_1 += 1

        serial_no=1
        for Question in range(len(data_1["data"][Slug-1]["childExercises"])):
            if data_1["data"][child]["childExercises"] == List:
                print("              ",serial_no,".",data_1["data"][Slug-1]["childExercises"][Question]["name"])
                slug = data_1["data"][Slug-1]["childExercises"][Question]["slug"]
                parent = data_1["data"][Slug-1]["childExercises"][Question]['id']
                slug1 = requests.get(" http://saral.navgurukul.org/api/courses/"+parent+"/exercise/getBySlug?slug="+slug)

                slug2 = slug1.json()
                slug_ind.append(slug2["content"])
                serial_no+=1
        break
question_1 = int(input("Enter the question  number: "))
question=question_1-1
print(slug_ind[question])
while question_1 > 0:
    next_question = input("Do you want next or previous: ").lower()
    if question_1 == len(slug_ind):
         print("next page")
    if next_question == "p":
        if  question_1 == 1:
            print("no more question")
            break
        elif question_1 > 0:
            question_1 = question_1 - 2
            print(slug_ind[question_1])
    elif next_question == "n":
        if  question_1 < len(slug_ind):
            index = question_1 + 1
            print(slug_ind[index-1])
            question += 1
            question_1 = question_1 + 1
            if question == (len(slug_ind)-1):
                print("next page")
                break