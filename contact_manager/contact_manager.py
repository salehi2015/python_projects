import json

class ContactManager:
    def __init__(self , path= '-'):
        self.contact_list = []

        if path != '-':
            with open(path , "r") as f:
                data = f.read()
                self.contact_list = json.loads(data)


    def add(self,name , number):
        self.contact_list.append({"name": name , "number": number})

    def search(self, name):
        results = []
        for item in self.contact_list:
            if name.lower() in item['name'].lower():
                results.append(item['name'])
        print(results)

    def backup(self):
        with open("./contact_list.json" , "w") as f:
            f.write(json.dumps(self.contact_list))


    def print(self):
        print(f"your contact are: {self.contact_list}")


contact1 = ContactManager()
contact1.add("fafa" , 4444)
contact1.add("sara" , 1234)
contact1.add("ali" , 4545)
contact1.add("amir" , 2585)
contact1.add("negin" , 2222)
contact1.print()

contact1.search("a")
contact1.backup()
