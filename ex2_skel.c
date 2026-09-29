#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Defines a new type 'point3d' as an array of 3 floats
typedef float point3d[3];

void count(point3d const *P, const int n, unsigned counters[8])
{
	for (int i = 0; i < 8; ++i)
		counters[i] = 0;
	for (int i = 0; i < n; ++i)
		if (P[i][0] < 0.0f && P[i][1] < 0.0f && P[i][2] < 0.0f)
			++counters[7];
		else if (P[i][0] < 0.0f && P[i][1] < 0.0f && P[i][2] >= 0.0f)
			++counters[3];
		else if (P[i][0] < 0.0f && P[i][1] >= 0.0f && P[i][2] < 0.0f)
			++counters[5];
		else if (P[i][0] < 0.0f && P[i][1] >= 0.0f && P[i][2] >= 0.0f)
			++counters[1];
		else if (P[i][0] >= 0.0f && P[i][1] < 0.0f && P[i][2] < 0.0f)
			++counters[6];
		else if (P[i][0] >= 0.0f && P[i][1] < 0.0f && P[i][2] >= 0.0f)
			++counters[2];
		else if (P[i][0] >= 0.0f && P[i][1] >= 0.0f && P[i][2] < 0.0f)
			++counters[4];
		else
			++counters[0];
}

// Generates a random float between 0.0 and 1.0
float frand01()
{
	float r = 1.0f / RAND_MAX;
	return rand() * r;
}

int main()
{
	// Number of points for the test
	const int n = 8000000;

	// Allocate dynamic memory to store the 3D points
	point3d *points = (point3d *)malloc(sizeof(point3d) * n);

	// Generate random points within the range [-1.0, 1.0] for each coordinate
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < 3; ++j)
			points[i][j] = 2.0f * frand01() - 1.0f;

	unsigned counters[8];

	// Record the start time to measure execution speed
	clock_t start_time = clock();

	// Call the count function to process the points
	count(points, n, counters);

	// Record the end time
	clock_t end_time = clock();

	// Calculate the total execution time in seconds
	double t = (double)(end_time - start_time) / CLOCKS_PER_SEC;

	// Free the dynamically allocated memory
	free(points);

	// Print the total execution time
	printf("count() execution time: %f sec\n", t);

	return 0; // Indicate successful execution
}