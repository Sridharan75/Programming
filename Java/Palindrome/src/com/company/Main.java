package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Get number from User
        System.out.print("Enter a number (to check if is that Palindrome or Not) :");
        int number=scanner.nextInt();

        int reversedNumber=0,temp=number,remainder;

        //Reverse the number
        while(number>0){
            remainder=number%10;
            reversedNumber=(reversedNumber*10)+remainder;
            number=number/10;
        }

        //Check if it palindrome or not.
        if (temp==reversedNumber)
            System.out.println("The Number "+temp+" is Palindrome.");
        else
            System.out.println("The Number "+temp+" Isn't Palindrome.");
        
    }
}
