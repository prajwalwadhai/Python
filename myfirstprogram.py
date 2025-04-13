
#define MOD 1000000007

// Function to compute (base^exp) % mod using modular exponentiation
long long power_mod(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Structure to store range start and end
typedef struct {
    int start;
    int end;
} Range;

// Comparison function for sorting ranges based on start value
int compare_ranges(const void* a, const void* b) {
    return ((Range*)a)->start - ((Range*)b)->start;
}

// Function to compute the number of valid ways to distribute ranges
int distributeRanges(int ranges_rows, int ranges_columns, int** ranges) {
    if (ranges_rows == 0) return 0; // Edge case: No ranges

    // Convert to struct array for easier sorting
    Range rangeList[ranges_rows];
    for (int i = 0; i < ranges_rows; i++) {
        rangeList[i].start = ranges[i][0];
        rangeList[i].end = ranges[i][1];
    }

    // Step 1: Sort ranges based on start value
    qsort(rangeList, ranges_rows, sizeof(Range), compare_ranges);

    // Step 2: Merge overlapping ranges to find independent components
    int components = 0;
    int prev_start = rangeList[0].start;
    int prev_end = rangeList[0].end;

    for (int i = 1; i < ranges_rows; i++) {
        int start = rangeList[i].start;
        int end = rangeList[i].end;

        if (start <= prev_end) {  // Overlapping range, merge it
            if (end > prev_end) {
                prev_end = end;
            }
        } else {  // Non-overlapping, start a new component
            components++;
            prev_start = start;
            prev_end = end;
        }
    }

    // Count the last component
    components++;

    // Step 3: Compute the number of valid distributions
    if (components == 1) return 2; // If only 1 component, exactly 2 valid ways

    long long total_ways = power_mod(2, components, MOD);
    return (total_ways - 2 + MOD) % MOD;  // Exclude the all-in-one-group cases
}