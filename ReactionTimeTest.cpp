#include <windows.h> 
#include <iostream> 
#include <fstream>
using namespace std;

int main()
{
	INPUT Input = { 0 };
	Input.type = INPUT_MOUSE;

	Input.mi.dx = -9500;
	Input.mi.dy = 30000;

	// set move cursor directly
	Input.mi.dwFlags = MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE;

	//mouse setup shit
	INPUT in[4] = {};
	ZeroMemory(in, sizeof(in));
	in[0].type = 0;
	in[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
	in[1].type = 0;
	in[1].mi.dwFlags = MOUSEEVENTF_LEFTUP;

	
	SendInput(1, &Input, sizeof(INPUT));

	Sleep(100);

	ofstream fout("RGB.txt", ofstream::app);
	// Assigning the device context to the current output device 
	HDC dng = GetDC(NULL);

	// Calling the getpixel function and passing in the device context and coordinates 
	// The coordinates should be inside the max resolution of the device context 
	// ex. screen coordinate X < 1919; in case of a full HD display 

	POINT p;
	GetCursorPos(&p);

	while (1) { 
		COLORREF c = GetPixel(dng, p.x, p.y);
		if ((int)GetRValue(c) >= 65 && (int)GetRValue(c) <= 75) { //green or blue
			SendInput(2, in, sizeof(INPUT));        //press mouse
			cout << "\n\n\n\n pressed\n\n\n\n";
			Sleep(100);
		}
		
		if (GetKeyState('Q') & 0x8000) { //q for quit
			exit(0);
		}
		cout << "RGB (";
		cout << (int)GetRValue(c) << ", ";
		cout << (int)GetGValue(c) << ", ";
		cout << (int)GetBValue(c) << ")" << endl;
		
	}
	/*
	fout << "RGB (";
	fout << (int)GetRValue(c) << ", ";
	fout << (int)GetGValue(c) << ", ";
	fout << (int)GetBValue(c) << ")" << endl;
	//fout << "x: " << p.x << "     y:" << p.y << endl;

	cout << "RGB (";
	cout << (int)GetRValue(c) << ", ";
	cout << (int)GetGValue(c) << ", ";
	cout << (int)GetBValue(c) << ")" << endl;
	cout << "x: " << p.x << "     y:" << p.y << endl;
	// Releasing the Handle 
	*/
	ReleaseDC(NULL, dng);
}
