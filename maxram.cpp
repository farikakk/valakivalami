#include <cstdint>
#include <cstdio>

#define WIN32_LEAN_AND_MEAN
#include <Windows.h>

#pragma warning(disable : 6387)

static constexpr const uint64_t num = 16ull * 1024ull * 1024ull; // 16 MB a gepben ssd van :(

int main()
{
	uint64_t maxRam = 0;
	while (true)
	{
		if (void* freshlyAllocated = VirtualAlloc(nullptr, num, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE))
		{
			memset(freshlyAllocated, 8, num);

			maxRam += num;
			
			printf("uj alloc: %llu MB\n", (maxRam / 1024ull) / 1024ull);
			continue;
		}

		printf("jaj ne ennyit birt a geped :( %llu MB\n", (maxRam / 1024ull) / 1024ull);
		break;
	}

	Sleep(3 * 1000); // 3 mp
	return 42;
}