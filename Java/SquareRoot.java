import java.util.Scanner;

public class SquareRoot {
    public static void main(String[] agrs) {
        var scanner = new Scanner(System.in);
        System.out.print("Input a number (for Square root& Square): ");
        int numberFromUser = scanner.nextInt();

        System.out.println("\t\t\tThe Square root of " + numberFromUser + " is " + Math.sqrt(numberFromUser));
        System.out.println("\t\t\tThe Square of " + numberFromUser + " is " + numberFromUser * numberFromUser);
    }

}