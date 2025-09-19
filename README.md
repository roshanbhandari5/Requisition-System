* Overview:
Requisition.py is a basic command line interface program made in python. 
It generates unique requisition ID. The user is allowed to input their details, calculated total and check the status.

* Features:
-> Submit the information of the staff.
-> Calculate the total cost from the detail of items.
-> Self-approval of the requisition status.
-> Requisition response function is made for approving the requisitions.
-> All the details of the requisition are displayed by the display requisition function.
-> Requisition static counts the total number of requisitions along with number of pending, approved and not approved requisitions.
*Software Design Principles:
•	K.I.S.S (keep it simple stupid)
The code is written in the simplest way possible. Logic is straight forward and uses basic input/output functions.

•	DRY (don’t repeat yourself)
The function staff_info() uses a pattern that validates the input so there is no any repetition of code.
Loops are used in the program which demonstrates DRY principle in the program.
DRY principle is also used in requisition_static() which repeats the codes multiple time so that there is no any need of typing the code again and again.

•	Open/Closed
The function requisition_approval() uses a simple business rule that can be modified as per the need.
There is no necessicity of changing the whole code instead you can just change the values in the approval so that it can be easy rather than running code again.
So, this program also follows the open/closed principle.

•	YAGNI (you aren’t gonna need it)
This program only includes the code that necessary and have some functionalities that must be used in the program. 
There is no any line of unnecessary codes which are not needed. The code provides a detail to the things that are being used. 
So, the code only focuses on the function that are needed in the program actually.

•	Clean code > Clever code
The code is kept clean and the name of the functions are kept in such a way that the name can simply define what is it being used for. 
For example: staff_info() – as the name says this function includes the information about the staff. So, this python program has a clean code.

Limitations:
Although this program has all the things that are needed for a program to be good. The program limits when it comes to authentication. 
As we have not kept the user authentication, any user can enter and approve requisitions. So, that might be taken as a limitation of this program.

Conclusions:
The requisition.py demonstrates the core functionality of a command line interface while following essential software design principles like K.I.S.S, DRY, YAGNI and Open/Closed. 
This system is clean, basic and beginner-friendly structure. 
