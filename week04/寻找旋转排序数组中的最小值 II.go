func findMin(nums []int) int {
    left, right := 0, len(nums) - 1
     for left < right{
         min := (left + right) >> 1
         if nums[min] > nums[right]{
             left = min + 1
         }else if nums[min] < nums[right] {
			right = min
		}else {
			right --
		}
     }
     return nums[left]
}