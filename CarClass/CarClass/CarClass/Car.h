#include <string>
#ifndef CAR_H
#define CAR_H
using namespace std;

class Car {
public:
	Car();
	Car(string make, string model);

	void setMake(string input);
	void setModel(string input);
	string getMake();
	string getModel();

private:
	string make;
	string model;
};
#endif
#pragma once
