void merge(int* nums, int si, int mid, int ei) {
    
    int size = ei - si + 1;
    int newArr[size];

    int i = si;
    int j = mid + 1;
    int k = 0;

    while (i <= mid && j <= ei) {
        if (nums[i] <= nums[j]) {
            newArr[k] = nums[i];
            i++;
        } else {
            newArr[k] = nums[j];
            j++;
        }
        k++;
    }

    while (i <= mid) {
        newArr[k] = nums[i];
        i++;
        k++;
    }

    while (j <= ei) {
        newArr[k] = nums[j];
        j++;
        k++;
    }

    for (int l = 0; l < size; l++) {
        nums[si + l] = newArr[l];
    }
}

void divide(int* nums, int si, int ei) {
    
    if (si >= ei) {
        return;
    }

    int mid = si + (ei - si) / 2;

    divide(nums, si, mid);
    divide(nums, mid + 1, ei);

    merge(nums, si, mid, ei);
}

int* sortArray(int* nums, int numsSize, int* returnSize) {
    
    divide(nums, 0, numsSize - 1);

    *returnSize = numsSize;

    return nums;
}