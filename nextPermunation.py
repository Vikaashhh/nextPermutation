class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        
        #step 1:- Right se phela index dhoondo jahan arr[i] < arr[i+1]
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
            
        if i >= 0:
            #step 2:- Right se phela aisa element dhoondo jo arr[i] se bada ho
            j = n - 1
            while arr[j] <= arr[i]:
                j -= 1
                
            #step 3:- swap i and j
            arr[i], arr[j] = arr[j], arr[i]
            
        #step 4:- Reverse the elements from i+1 to end
        left, right = i + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
 
 # Driver Code Starts

if __name__ == "__main__":
    arr = [3, 2, 1]
    print("Original:", arr)

    ob = Solution()
    ob.nextPermutation(arr)

    print("Next Permutation:", arr)

# } Driver Code Ends