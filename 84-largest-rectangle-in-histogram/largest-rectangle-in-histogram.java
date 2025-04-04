import java.util.Deque;
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        Deque<Integer> stack = new ArrayDeque<>();
        int[] nextLesser = new int[n];
        int[] prevLesser = new int[n];
        Arrays.fill(prevLesser, -1);
        Arrays.fill(nextLesser, n);

        for (int i = 0; i < n; i++)    {
            int h = heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] >= h) {
                stack.pop();
            }
            prevLesser[i] = stack.isEmpty() ? -1: stack.peek();
            stack.push(i);
        }
        stack.clear();
        for (int i = n-1; i >= 0; i--)    {
            int h = heights[i];
            while (!stack.isEmpty() && heights[stack.peek()] >= h) {
                stack.pop();
            }
            nextLesser[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        int maxArea = 0;
        for (int i = 0; i<n; i++ )  {
            int prev = prevLesser[i];
            int next = nextLesser[i];
            int width = next - prev - 1;
            maxArea = Math.max(maxArea, width*heights[i]);
        }
        return maxArea;
    }
}