#include <iostream>
#include <array>
using namespace std;
int main()
{
	float a = 3.14159;
	float b = 2.8321958;
	float* pointer;
	// 1. Create a pointer to a
	pointer = &a;
	// IMPORTANT: After this line, you cannot use the name 'a' until step 9, use 
	// the pointer instead!
		// 2. Print the value of the pointee, followed by an end of line
	cout << *pointer << endl;
		// 3. Add 7 to the value of the the pointee
	*pointer += 7;
		// 4. Print the value of the pointee, followed by an end of line
	cout << *pointer << endl;
		// Observe the output
		// 5. Point the pointer to b instead of a
	pointer = &b;
		// IMPORTANT: After this line, you cannot use the name 'b' anymore, just the 
		// pointer!
	cout << *pointer << endl;
		// 6. Print the value of the pointee, followed by an end of line
		// Observe the output
	*pointer *= 7;
		// 7. Multiple the value of the pointee by 5
	cout << *pointer << endl;
		// 8. Print the value of the pointee followed by an end of line
	pointer = &a;
		// 9. Set the pointer back to point to a again
	cout << *pointer << endl;
		// 10. Print out the value of the pointee
		return 0;
}