import java.util.Scanner;

public class Sleeping {
  public static void main(String[] args) throws Exception {
    // Scanner sc = new Scanner(new java.io.File("1.in"));
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();

    for (int i = 0; i < T; i++) {
      int N = sc.nextInt();
      int[] nums = new int[N];
      long totalSum = 0;
      for (int j = 0; j < N; j++) {
        nums[j] = sc.nextInt();
        totalSum += nums[j];
        for (int k = 0; k < N; k++) {

        }
      }
      System.out.println(solve(N, nums, totalSum));
    }

    sc.close();
  }

  private static int solve(int N, int[] nums, long totalSum) {
    long curSum = 0;
    int minPartition = Integer.MAX_VALUE;
    for (int i = 0; i < N; i++) {
      curSum += nums[i];
      if (curSum != 0 && totalSum % curSum == 0) {
        int partition = partition(curSum, nums, i+1, N);
        if (partition != -1) {
          minPartition = Math.min(minPartition, partition);
        }
      }
    }
    if (minPartition == Integer.MAX_VALUE) {
      return 0;
    }
    return minPartition;
  }

  private static int partition(long targetSum, int[] nums, int idx, int N) {
    long curSum = 0;
    int parts = 1;
    while (idx < N) {
      curSum += nums[idx];
      if (curSum > targetSum) {
        // cant form
        return -1;
      } else if (curSum == targetSum) {
        // found one
        curSum = 0;
        parts++;
      }
      idx++;
    }
    return N - parts;
  }
}
