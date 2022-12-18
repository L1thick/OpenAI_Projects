#include <Python.h>
#include <iostream>
#include <iomanip>
#include <Windows.h>
#include <string>
#include <fstream>
#include <stdlib.h> 

using namespace std;

void CallProcedure(string pName)
{
	char* funcName = new char[pName.length() + 1];
	strcpy(funcName, pName.c_str());
	Py_Initialize();
	PyObject* pyDoc = PyImport_ImportModule("openAI_calls");
	PyObject* pyFunc = PyObject_GetAttrString(pyDoc, funcName);
	PyObject* results = PyObject_CallObject(pyFunc, NULL);
	Py_Finalize();
	delete[] funcName;
}

void FirsrtOpt() {
	system("CLS");												// Clear Screen.
	CallProcedure("twoFiveSix");
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