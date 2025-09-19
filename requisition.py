counter = 10000   #Global counter to generate unique ID.
requisitions = []
class requisitionsystem():   #class is declared
    def __init__(self):
        global counter
        counter += 1
        self.requisition_id = counter
        self.date = ''
        self.staff_id = ''
        self.staff_name = ''
        self.status = "pending"
        self.approval  = "Not yet approved"

    def staff_info(self):  #declaring a function for the staff info
        while True:
            self.date = input("Enter the date in dd/mm/yyyy format: ")
            if self.date.strip():
                break
            else:
                print("Dont leave the input empty. Please provide a input.")
        while True:
            self.staff_id = input("Enter the Id of the staff: ")
            if self.staff_id.strip():
                break
            else:
                print("Dont leave the input empty. Please provide a input.")
        while True:
            self.staff_name =  input("Enter the name of the staff: ")
            if self.staff_name.strip():
                break
            else:
                print("Dont leave the input empty. Please provide a input.")

    def requisitions_total(self):  #declaring a function for calculating the total
        total = 0
        while True:
            item = input("Enter the name of the item or type 'done' to finish: ")
            if item.lower() == 'done':
                break
            while True:
                try:
                    price = float(input("Enter the price of item: "))
                    if price >= 0:
                        total = total + price
                        break
                    else:
                        print("Price can never be negative. Input a positive integer")
                except ValueError:
                    print("This is not a valid input")
        self.total = total

    def requisition_approval(self): #declaring a function for approval
        if self.total < 500:   #open/closed principle so that we can modify approval logiv without touching other code
            self.status = "Approved"
            self.ref_num = str(self.staff_id) + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.ref_num = "Refrence number will be displayed once the status is approved."

    def requisition_response(self):   #declaring a function to get the requisition response. (pending, approved or not approved)
        if self.status != "Pending":
            print("The requisition is not pending.")
            return
        while True:
            decision = input(f"Do you want to approve Requisition ID {self.requisition_id}? (approved/not approved): ").strip().lower()
            if decision in ["approved", "not approved"]:
                if decision == "approved":
                    self.status = "Approved"
                    self.ref_num = self.staff_id + str(self.requisition_id)[-3:]
                else:
                    self.status = "Not approved"
                    self.ref_num = "Refrence number will be displayed once the status is approved."
            break

    def display_requisitions(self):  #function responsible for displaying data
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.ref_num}")

    def requisition_static(self):  #DRY principle is used to avoid duplication code 
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            elif requisition.status == "Not approved":
                not_approved += 1

        total_req = approved + pending + not_approved

        print("\nRequisition Statistics:")
        print(f"Total requisitions submitted: {total_req}")
        print(f"Approved: {approved}")
        print(f"Pending: {pending}")
        print(f"Not Approved: {not_approved}\n")

    #program execution starts here

while True:
    requisition = requisitionsystem()  #creating object
    requisition.staff_info()  #inputting the staff details
    requisition.requisitions_total()  #input the ptice and calculate the total.
    requisition.requisition_approval()  #approval based on business rule
    requisitions.append(requisition)  #storing in list. Append is used to  modify the elements
    add_requisition = input("Do you want to add another requisition? (y/n): ")
    if add_requisition.lower() == 'n':
        break

print("\nPending Requisitions")
for requisition in requisitions:
        requisition.requisition_response()

for requisition in requisitions:
    requisition.display_requisitions()

requisition.requisition_static()  #Final status