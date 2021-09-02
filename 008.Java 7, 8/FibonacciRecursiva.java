public class FibonacciRecursiva {

    public static int fibonacciRecursiva(int termo) {

        if (termo < 2){
            return termo;
        } 

        return fibonacciRecursiva(termo - 1) + fibonacciRecursiva(termo - 2);

    }

    public static void main(String[] args) {
        System.out.println(FibonacciRecursiva.fibonacciRecursiva(1));
    }
}