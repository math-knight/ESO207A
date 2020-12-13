#include <iostream>
using namespace std;

long long MergeAndCount(int A[], int B[], int start, int mid, int end){
    //initialize variables
    int p = start;
    int q = mid + 1;
    int r = start;
    long long count = 0;
    
    while((p <= mid) && (q<= end)){
        if(A[p] <= A[q]){
            B[r] = A[p]; //pick elements from left subarray
            p++;
            r++;
        }
        else{
            //A[p] > A[q]
            B[r] = A[q]; //pick elements from the right subarray
            count += (mid - p + 1); //A[p,p+1...,mid] > A[q] as subarrays are sorted
            q++;
            r++;
        }
    }
    //either one or both of the subarrays have been exhausted
    
    while(p <= mid){
        //left subarray is remaining
        B[r] = A[p];
        r++;
        p++;
    }
    
    while(q <= end){
        //right subarray is remaining
        B[r] = A[q];
        r++;
        q++;
    }
    
    for(int i=start; i<=end; i++){
        //copy sorted array onto the original
        A[i] = B[i];
    }
    
    return count;
}

long long InversionCount(int A[], int B[], int start, int end){
    long long count = 0;
    if(start<end){
        int mid = (start + end)/2; //integer division
        count += InversionCount(A, B, start, mid); //count inversions in left half
        count += InversionCount(A, B, mid+1, end); //count inversions in right half
        count += MergeAndCount(A, B, start, mid, end); //count inversions across the halves (merge step)
    }
    return count;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    //read input  
    int k;
    cin >> k;
    for(int i=0;i<k;i++){
        int n;
        cin >> n;
        int A[n] = {0}; //input array
        int B[n] = {0}; //auxiliary array (used for sorting)
        for(int j=0;j<n;j++)
            cin >> A[j];
        //find and output inversion count
        long long count = InversionCount(A, B, 0, n-1);
        cout << count << endl;
    }
    return 0;
}

//Rahul Sethi
//190668
//sethir@iitk.ac.in