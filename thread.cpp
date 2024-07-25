// g++ -pthread -o thread thread.cpp

#include <iostream>
#include <thread>
#include <chrono>
#include <cmath>
#include <vector>

using namespace std;
using namespace std::chrono;

static const int N_JOBS = 4;
static const int LOAD = 20000000000;

void summarizator(int *arr, int i, double *summ)
{
    int begin = i * LOAD / N_JOBS;
    int end = (i + 1) * LOAD / N_JOBS;
    double res = 0;
    for (int k = begin; k < end; k++)
    {
        res += sqrt(arr[k]);
    }
    summ[i] = res;
}

int main()
{
    int *arr = new int[LOAD];
    for (int i = 0; i < LOAD; i++)
    {
        arr[i] = i;
    }

    auto start = system_clock::now();

    thread threads[N_JOBS];
    double summ[N_JOBS];

    for (int i = 0; i < N_JOBS; i++)
    {
        threads[i] = thread(summarizator, arr, i, summ);
    }

    for (int i = 0; i < N_JOBS; i++)
    {
        threads[i].join();
    }

    double res = 0;
    for (int i = 0; i < N_JOBS; i++)
    {
        res += summ[i];
    }

    auto stop = system_clock::now();

    auto elapsed = duration_cast<milliseconds>(stop - start);

    cout << "Threads result (C++): " << long(res) << ", time: " << elapsed.count() / 1000.0 << "\n";

    return 0;
}
