public class Bug3 {
    // Return the number of even values in the array.
    public static int countEven(int[] numbers) {
        int count = 0;

        for (int i = 0; i < numbers.length - 1; i++) {
            if (numbers[i] % 2 == 0) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] values = {2, 3, 4, 6};
        System.out.println(countEven(values)); // Expected: 3
    }
}
