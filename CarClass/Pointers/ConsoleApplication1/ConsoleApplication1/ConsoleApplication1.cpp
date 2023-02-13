#include <iostream>
#include <string>
using namespace std;

string messageAdvance(string& task);
string messageRetreat(string& task);

int main() {
	bool running = true;
	int task = 0;
	int shift = 0;
	int stage = 0;
	string code = "You're gonna suck my dick and mean it young man";

	cout << "Welcome to the Tali-banned Encrypter!" << endl
		<< "Make a selection from the menu and then follow the prompts." << endl;

	while (running) {
		shift = 0;
		cout << "*************************************" << endl
			<< "* 1 - Encrypt a message" << endl
			<< "* 2 - Decrypt a message" << endl
			<< "* 3 - Brute - force decrypt a message" << endl
			<< "* 4 - Quit" << endl
			<< "*************************************" << endl
			<< "Please make a menu selection (1-4):" << endl;

		while (stage == 0) {
			cin >> task;
			if (task >= 1 && task <= 4) {
				stage += 1;
			}
			else {
				cout << "Invalid choice, Please make a menu selection (1-4):" << endl;
			}
		}

		while (stage == 1) {
			getline(cin, code);
			switch (task) {
			case 1: {
				cout << "Please enter the message to encrypt:" << endl;
				getline(cin, code);
				cout << "Please enter the shift value (1-25):" << endl;
				stage += 1;
			} break;
			case 2: {
				cout << "Please enter the message to decrypt:" << endl;
				getline(cin, code);
				cout << "Please enter the shift value (1-25):" << endl;
				stage += 1;
			} break;
			case 3: {
				cout << "Please enter the message to decrypt:" << endl;
				getline(cin, code);
				stage += 1;
			} break;
			case 4: {
				getline(cin, code);
				cout << "Thank you Caesar!  See ya!" << endl;
				running = false;
				stage = -1;
			} break;
			}
		}

		while (stage == 2) {
			switch (task) {
			case 1: {
				cin >> shift;
				if (shift >= 1 && shift <= 25) {
					for (int i = 0; i < shift - 1; i++) {
						messageAdvance(code);
					}
					cout << "Encrypted as:" << endl << messageAdvance(code) << endl;
					stage = 0;
				}
				else {
					cout << "Invalid choice, Please enter the shift value (1-25):"
						<< endl;
				}
			} break;

			case 2: {
				cin >> shift;
				if (shift >= 1 && shift <= 25) {
					for (int i = 0; i < shift - 1; i++) {
						messageRetreat(code);
					}
					cout << "Decrypted as:" << endl << messageRetreat(code) << endl;
					stage = 0;
				}
				else {
					cout << "Invalid choice, Please enter the shift value (1-25):"
						<< endl;
				}
			} break;

			case 3: {
				cout << "Decrypted as:" << endl;
				for (int i = 0; i < 25; i++) {
					cout << messageRetreat(code) << endl;
				}
				stage = 0;
			} break;
			}
		}
	}
	return 0;
}

string messageAdvance(string& task) {
	for (int i = 0; i < task.length(); i++) {
		if (task[i] >= 'A' && task[i] < 'Z') {
			task[i] += 1;
		}
		else if (task[i] == 'Z') {
			task[i] = 'A';
		}
		else if (task[i] >= 'a' && task[i] < 'z') {
			task[i] += 1;
		}
		else if (task[i] == 'z') {
			task[i] = 'a';
		}
	}
	return task;
}

string messageRetreat(string& task) {
	for (int i = 0; i < task.length(); i++) {
		if (task[i] > 'A' && task[i] <= 'Z') {
			task[i] -= 1;
		}
		else if (task[i] == 'A') {
			task[i] = 'Z';
		}
		else if (task[i] > 'a' && task[i] <= 'z') {
			task[i] -= 1;
		}
		else if (task[i] == 'a') {
			task[i] = 'z';
		}
	}
	return task;
}
