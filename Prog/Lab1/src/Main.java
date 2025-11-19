public class Main {
    public static void main(String[] args) {
        long[] l = setEvenNumbers(new long[9]);
        float[] x = setRandomNumbers(new float[13]);
        double[][] l1 = setMatrix(new double[9][13], l, x);

        // showMatrix(l1);
        task();
    }

    public static void task() {
        int a = 1;
        int b = 2;
        System.out.printf("%d + %d = %d", a, b, a+b);
    }

    public static long[] setEvenNumbers(long[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = (i + 3) * 2L;
        }
        return array;
    }

    public static float[] setRandomNumbers(float[] array) {
        for (int i = 0; i < array.length; i++) {
            array[i] = -5.0f + (float)(Math.random() * 14.0f);
        }
        return array;
    }

    public static double[][] setMatrix(double[][] array, long[] l, float[] x) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                switch((int)l[i]) {
                    case 16 ->
                        array[i][j] = Math.atan(1/(Math.pow(Math.exp(Math.pow(2*Math.pow(Math.cos(x[j]),2),Math.E)),Math.pow(((2/3d+x[j])/0.25),x[j]))));
                    case 6,8,10,20 ->
                        array[i][j] = Math.cos(Math.cbrt(Math.atan((x[j]+2)/14)));
                    default ->
                        array[i][j] = Math.asin(Math.sin(Math.pow(Math.pow(x[j],(4-x[j])/x[j]), Math.log(Math.exp(x[j])))));
                }
            }
        }
        return array;
    }

    public static void showMatrix(double[][] array) {
        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array[i].length; j++) {
                System.out.printf("%.2f", array[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}