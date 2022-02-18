package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Number: ");
        int number = scanner.nextInt();

        String five="Fizz";
        String three="Buzz";
        if((number%5==0)&&(number%3==0)){
            System.out.println(five+three);
        }
        else if (number%5==0){
            System.out.println(five);
        }
        else if(number%3==0){
            System.out.println(three);
        }
        else{
            System.out.println(number);
        }

    }
}
