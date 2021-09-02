class Main {
  public static void main(String[] args) {
    int resposta = fibonacciRecursiva(5);
    System.out.println(resposta);
  }

  public static int fibonacciRecursiva(int termo){
      if (termo < 2){
          return termo;
      }else{
          return fibonacciRecursiva(termo - 1) + fibonacciRecursiva(termo - 2);
      }
  }
}



// class Main {
//   public static void main(String[] args) {
//     int decimal = 13;

//     String str_hexadecimal = Integer.toString(decimal, 16); // decimal to binary
//     int decimal_from_hexadecimal =Integer.parseInt(str_hexadecimal, 16);

//     System.out.println(str_hexadecimal);
//   }
// }

// // Integer.toString(n,16) //decimal to Hex