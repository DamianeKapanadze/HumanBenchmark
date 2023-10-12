#include <windows.h> 
#include <iostream> 
#include <fstream>
using namespace std;

void GetScreenShot()
{
	int x1, y1, x2, y2, w, h;

	// get screen dimensions
	x1 = 765; //GetSystemMetrics(SM_XVIRTUALSCREEN);
	y1 = 270; //GetSystemMetrics(SM_YVIRTUALSCREEN);
	x2 = 1140; // GetSystemMetrics(SM_CXVIRTUALSCREEN);
	y2 = 650; //GetSystemMetrics(SM_CYVIRTUALSCREEN);
	w = x2 - x1;
	h = y2 - y1;

	// copy screen to bitmap
	HDC     hScreen = GetDC(NULL);
	HDC     hDC = CreateCompatibleDC(hScreen);
	HBITMAP hBitmap = CreateCompatibleBitmap(hScreen, w, h);
	HGDIOBJ old_obj = SelectObject(hDC, hBitmap);
	BOOL    bRet = BitBlt(hDC, 0, 0, w, h, hScreen, x1, y1, SRCCOPY);

	// save bitmap to clipboard
	OpenClipboard(NULL);
	EmptyClipboard();
	SetClipboardData(CF_BITMAP, hBitmap);
	CloseClipboard();

	// clean up
	SelectObject(hDC, old_obj);
	DeleteDC(hDC);
	ReleaseDC(NULL, hScreen);
	DeleteObject(hBitmap);
}

int main()
{
	GetScreenShot();

	Sleep(2000);
	INPUT Input = { 0 };
	Input.type = INPUT_MOUSE;

	POINT p;
	GetCursorPos(&p);
	cout << p.x << "  " << p.y << endl;
	Input.mi.dx = p.x;
	Input.mi.dy = p.y;

	// set move cursor directly
	//Input.mi.dwFlags = MOUSEEVENTF_MOVE;          
	

	//mouse setup shit
	INPUT in[4] = {};
	ZeroMemory(in, sizeof(in));
	in[0].type = 0;
	in[0].mi.dwFlags = MOUSEEVENTF_LEFTDOWN;
	in[1].type = 0;
	in[1].mi.dwFlags = MOUSEEVENTF_LEFTUP;


	SendInput(1, &Input, sizeof(INPUT));

	GetCursorPos(&p);
	cout << p.x << "  " << p.y << endl;

	Sleep(100);

	ofstream fout("RGB.txt", ofstream::app);
	// Assigning the device context to the current output device 
	HDC dng = GetDC(NULL);

	// Calling the getpixel function and passing in the device context and coordinates 
	// The coordinates should be inside the max resolution of the device context 
	// ex. screen coordinate X < 1919; in case of a full HD display 


	while (1) {
		GetCursorPos(&p);cout << p.x << "  " << p.y << endl;
		COLORREF c = GetPixel(dng, p.x, p.y);
		
		cout << "RGB (";
		cout << (int)GetRValue(c) << ", ";
		cout << (int)GetGValue(c) << ", ";
		cout << (int)GetBValue(c) << ")" << endl;

	}
	
	ReleaseDC(NULL, dng);
}
