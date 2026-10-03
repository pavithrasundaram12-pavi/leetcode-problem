int kthSmallest(int** a, int aSize, int* aColSize, int k) {
    
    int rows = aSize;
    int cols = aColSize[0];

    int start = a[0][0];
    int end = a[rows - 1][cols - 1];

    while (start < end) {
        
        int mid = start + (end - start) / 2;

        int j = cols - 1;
        int cnt = 0;

        for (int i = 0; i < rows; i++) {
            
            while (j >= 0 && a[i][j] > mid) {
                j--;
            }

            cnt += (j + 1);
        }

        if (cnt < k) {
            start = mid + 1;
        }
        else {
            end = mid;
        }
    }

    return start;
}