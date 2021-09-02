public class FibonacciRecursivaAps {

    public static void main(String[] args) {
    // Print do retorno da função/método fibonacci
    // 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    // número da posição 6 é 8 
        System.out.println(fibonacciRecursiva(6)); // 8
    }

    public static int fibonacciRecursiva(int termo) {
        // condição de parada da função, se termo for menor que dois retorna o mesmo.
        if (termo < 2) {
            return termo;
        }
        // caso if não seja verdadeiro a função irá retorna a chamada da função até que condição seja verdadeira
        return fibonacciRecursiva(termo - 1) + fibonacciRecursiva(termo - 2);
    }
}
