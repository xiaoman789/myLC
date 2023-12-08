public class Leetcode_704_search {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right ){
            int middle = (left+right)/2;
            if(nums[right] > target){
                right = middle;
            }
            else if (nums[left] > target){
                
            }
        }
        return target;
    }
    public static void main(){

    }
}
