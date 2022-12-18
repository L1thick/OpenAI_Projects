#include <Python.h>
#include <iostream>
#include <iomanip>
#include <Windows.h>
#include <cmath>
#include <string>
#include <fstream>
#include <stdlib.h> 

using namespace std;

void CallProcedure(string pName)							// Description: To call this function, simply pass the function name in Python that you wish to call.
{
	char* procname = new char[pName.length() + 1];
	std::strcpy(procname, pName.c_str());

	Py_Initialize();
	PyObject* my_module = PyImport_ImportModule("openAI_calls");
	PyErr_Print();
	PyObject* my_function = PyObject_GetAttrString(my_module, procname);
	PyObject* my_result = PyObject_CallObject(my_function, NULL);
	Py_Finalize();

	delete[] procname;
}

void FirsrtOpt() {
	system("CLS");												// Clear Screen.

	system("pause");											// Pause the output.
	system("CLS");												// Clear Screen.
}

void FourthOpt() {
	system("CLS");												// Clear Screen.
	system("exit");												// Ends the program.
	cout << "Program Exited" << endl;							// Displays goodbye message.
}

void OtherOpt() {
	cout << "Why did you even enter that?" << endl;				// Insult the users input choice.
	system("pause");											// Pause the output.
	system("CLS");												// Clear Screen.
}

void main()
{
	bool restart = false;

	do {
		int userin;
		CallProcedure("PrintMenu");
		cin >> userin;
		if (userin == 1) {
			FirsrtOpt();
			restart = true;
		}
		else if (userin == 4) {
			FourthOpt();
			restart = false;
		}
		else {
			OtherOpt();
			restart = true;
		}
	} while (restart);
}