#include <cstdint>

#define WIN32_LEAN_AND_MEAN
#include <Windows.h>

#pragma warning(disable : 6387)

static DWORD WINAPI think(LPVOID useless)
{
	volatile uint64_t s = 0;
	
	for (;;) s = 9847128ull + 832759ull;
}

int main()
{
	SYSTEM_INFO si = {};
	GetSystemInfo(&si);

	HANDLE* threadContainer = new HANDLE[si.dwNumberOfProcessors];
	for (int i = 0; i < (int)si.dwNumberOfProcessors; i++)
	{
		threadContainer[i] = CreateThread(nullptr, 0, think, nullptr, 0, nullptr);
		if (threadContainer[i])
		{
			// A "ki kommentelt" fuggveny felakassza a gepet, csak akkor hivd, ha ujra akarod a gepet inditani 
			// SetThreadPriority(threadContainer[i], THREAD_PRIORITY_ABOVE_NORMAL);
		}
	}

	Sleep(INFINITE);
	
	delete[] threadContainer;
	return 6;

}
