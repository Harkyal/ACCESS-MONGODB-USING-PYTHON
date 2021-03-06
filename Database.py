import pymongo
client = pymongo.MongoClient("mongodb+srv://c0753356:Lambton%40123@cluster0.gnf79.mongodb.net/Company?retryWrites=true&w=majority")
db = client.test
collection1 = client.Company.Department
collection2 = client.Company.Employee
collection3 = client.Company.Job_History
Department_Data = [
    {
        "Department_ID":"101",
        "Department_Name":"Administration",
        "Manager_ID":"401",
        "Location_ID":"1001"
    },
    {
        "Department_ID":"102",
        "Department_Name":"Marketitng",
        "Manager_ID":"402",
        "Location_ID":"1003"
    },
    {
        "Department_ID":"103",
        "Department_Name":"Shipping",
        "Manager_ID":"403",
        "Location_ID":"1001"
    },
    {
        "Department_ID":"104",
        "Department_Name":"IT",
        "Manager_ID":"404",
        "Location_ID":"1005"
    },
    {
        "Department_ID":"105",
        "Department_Name":"Sales",
        "Manager_ID":"405",
        "Location_ID":"1007"
    }

]

Employee_Data=[
    {
        "Employee_ID":"301",
        "First_Name":"Vikas",
        "Last_Name":"Harkyal",
        "Contact":"457-458-7894",
        "Job_iD":"901",
        "Department_ID":"104"
    },
    {
        "Employee_ID": "302",
        "First_Name": "Gurpreet",
        "Last_Name": "Kaur",
        "Contact": "437-589-7842",
        "Job_iD": "902",
        "Department_ID": "105"
    },
    {
        "Employee_ID": "303",
        "First_Name": "Binod",
        "Last_Name": "Desai",
        "Contact": "647-478-8897",
        "Job_iD": "903",
        "Department_ID": "101"
    },
    {
        "Employee_ID": "304",
        "First_Name": "Ramanpreet",
        "Last_Name": "Kaur",
        "Contact": "478-847-5478",
        "Job_iD": "904",
        "Department_ID": "103"
    },
    {
        "Employee_ID": "305",
        "First_Name": "Jasbeer",
        "Last_Name": "Kaur",
        "Contact": "444-875-9861",
        "Job_iD": "905",
        "Department_ID": "102"
    }
]

Job_History_Data=[
    {
        "Employee_ID":"301",
        "Start_Date":"2018-04-11",
        "End_Date":"2020-08-17",
        "Job_id":"IT_Programmer",
        "Department_ID":"104"
    },
    {
        "Employee_ID":"302",
        "Start_Date":"2019-06-13",
        "End_Date":"2020-07-14",
        "Job_id":"SA_REP",
        "Department_ID":"105"
    },
    {
        "Employee_ID":"303",
        "Start_Date":"2019-04-18",
        "End_Date":"2020-02-22",
        "Job_id":"Administrator",
        "Department_ID":"101"
    },
    {
        "Employee_ID":"304",
        "Start_Date":"2017-04-25",
        "End_Date":"2020-06-14",
        "Job_id":"Shipping_Executive",
        "Department_ID":"103"
    },
    {
        "Employee_ID":"305",
        "Start_Date":"2019-08-14",
        "End_Date":"2020-07-15",
        "Job_id":"Marketing_Manager",
        "Department_ID":"102"
    }
]

#collection1.insert_many(Department_Data)
#collection2.insert_many(Employee_Data)
#collection3.insert_many(Job_History_Data)

#Find All data of any specific collection

#print('Find all Collections')
#for x in client.Company.Job_History.find():
 # print(x)

#Find data of any particular condition

#print('Find document')
#for x in client.Company.Department.find({"Department_ID": "101"}):
 #   print(x)


#  --- Upadte the Document--------

#myquery = {"Department_ID": "102"}
#newvalues = {"$set": {"Employee_ID": "305"}}
#client.Company.Job_History.update_one(myquery, newvalues)

#  -----Delete the Document------

#myquery = {"Employee_ID": "101"}
#client.Company.Job_History.delete_one(myquery)