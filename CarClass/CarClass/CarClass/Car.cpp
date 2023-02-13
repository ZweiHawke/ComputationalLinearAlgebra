#include "Car.h"
#include <iostream>
#include <string>

using namespace std;

void Car::setMake(string input) {
	make = input;
}

void Car::setModel(string input) {
	model = input;
}

string Car::getMake() {
	return make;
}

string Car::getModel() {
	return model;
}

Car::Car() {
	setMake("Peel");
	setModel("P50");
}

Car::Car(string make, string model) {
	setMake(make);
	setModel(model);
}