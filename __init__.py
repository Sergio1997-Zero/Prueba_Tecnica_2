import os
import json


class create:

    def create_user():

        while True:

            id = input("Enter your id: ")

            if id.isdigit():

                break

            else:

                print("Please enter a valid id")
            
        name = input("Enter name: ")

        last_name = input("Enter last name: ")

        while True:

            age = input("Enter your age: ")

            if age.isdigit():

                break

            else:

                print("Please enter a valid age")

        email = input("Enter email: ")

        save.save_dates(id,name,last_name,age,email)

class save:
    
    def save_dates(id,name,last_name,age,email):

        struct = {}

        struct["id"] = int(id)
        struct["name"] = name
        struct["last_name"] = last_name
        struct["age"] = int(age)
        struct["email"] = email

        file = os.environ.get("DB_USER")

        with open(file) as f:

            json_data = json.load(f)

            json_data["Users"].append(struct)

            json.dump(json_data,open(file,"w"),indent=4)
         
class modify:
    
    def modify():

        print("Select the number you want to do : \n1. Modify id \n2. Modify name \n3. Modify last name \n4. Modify age \n5. Modify email \n6. Exit")

        number = int(input("Enter the number: "))
    
        while number != 6:

            if number == 1:
                    
                modify.modify_user_id()

            elif number == 2:
                    
                modify.modify_user_name()

            elif number == 3:
                        
                modify.modify_user_last_name()


            elif number == 4:
                            
                modify.modify_user_age()


            elif number == 5:

                modify.modify_user_email()
            
            elif number == 6:
                pass

            print("Select the number you want to do : \n1. Modify id \n2. Modify name \n3. Modify last name \n4. Modify age \n5. Modify email \n6. Exit")

            number = int(input("Enter the number: "))

    def modify_user_id():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id you want to modify: ")

        chec = find_user.find_user(search,option)

        if chec != None:

            new_id = input("Enter the new id: ")
            
            with open(file) as f:
                data = json.load(f)
            for item in data['Users']:
                
                if item[option] == int(search):

                    item[option] = int(new_id)
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

    def modify_user_name():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id of user you want to modify the name: ")

        chec = find_user.find_user(search,option)

        if chec != None:
            
            new_id = input("Enter the new name: ")
            
            with open(file) as f:
                data = json.load(f)
            for item in data['Users']:
                
                if item[option] == int(search):

                    option = "name"

                    item[option] = new_id
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

    def modify_user_last_name():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id of user you want to modify the last name: ")

        chec = find_user.find_user(search,option)

        if chec != None:
            
            new_id = input("Enter the new  last name: ")
            
            with open(file) as f:
                data = json.load(f)
            for item in data['Users']:
                
                if item[option] == int(search):

                    option = "last_name"

                    item[option] = new_id
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

    def modify_user_age():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id of user you want to modify the age: ")

        chec = find_user.find_user(search,option)

        if chec != None:
            
            new_id = input("Enter the new age: ")
            
            with open(file) as f:
                data = json.load(f)
            for item in data['Users']:
                
                if item[option] == int(search):

                    option = "age"

                    item[option] = int(new_id)
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

    def modify_user_email():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id of user you want to modify the email: ")

        chec = find_user.find_user(search,option)

        if chec != None:
            
            new_id = input("Enter the new email: ")
            
            with open(file) as f:
                data = json.load(f)
            for item in data['Users']:
                
                if item[option] == int(search):

                    option = "email"

                    item[option] = new_id
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

class delete:
    
    def delete_user():

        file = os.environ.get("DB_USER")

        option = "id"

        search = input("Enter the id you want to delete: ")

        chec, pos = find_user.find_user(search,option)
        
        if chec != None:

            with open(file) as f:
                data = json.load(f)

            del data["Users"][pos]
            
            json.dump(data,open(file,"w"),indent=4)
        else:
            print("User not found")

class to_list:
    
    def to_list_user():

        file = os.environ.get("DB_USER")

        with open(file) as f:

            json_data = json.load(f)

            sorted_obj = dict(json_data)

            workflows = sorted_obj["Users"]

            sorted_json_data = sorted(workflows, key=lambda d: d["age"])
        
        return print(json.dumps(sorted_json_data, indent=4, sort_keys=True))

class find_user:

    def find_user(param,option):

        file = os.environ.get("DB_USER")

        with open(file) as f:

            data = json.load(f)

        pos = 0

        for i in data["Users"]:

            if str(i[option]) == param:

                return i, pos
            else:
                pos += 1

        return None, None
    
class options:

    def __init__():

        print("Select the number you want to do : \n1. Create users \n2. List of users \n3. Modify users \n4. Delete users \n5. Exit")

        number = int(input("Enter the number: "))

        while number != 5:

            if number == 1:

                create.create_user()

            elif number == 2:

                to_list.to_list_user()

            elif number == 3:
                modify.modify()

            elif number == 4:
                delete.delete_user()

            elif number == 5:

                pass

            print("Select the number you want to do : \n1. Create users \n2. List of users \n3. Modify users \n4. Delete users \n5. Exit")

            number = int(input("Enter the number: "))
        

if __name__ == "__main__":

    options.__init__()