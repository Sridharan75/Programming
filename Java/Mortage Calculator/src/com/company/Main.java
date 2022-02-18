package com.company;

import java.text.NumberFormat;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        final byte MONTHS_IN_YEAR =12;
        final byte PERCENT =100;

        Scanner scanner = new Scanner(System.in);

        //Pricipal
        int principal=0;
        while(true) {
            System.out.print("Principal ($1K - $1M): ");
            principal = scanner.nextInt();
            if ((principal >= 1000) && (principal <= 1_000_000))
                break;
            System.out.println("Enter a number between 1,000 and 1,000,000.");
        }

        //Annual Interest Rate
        float annualInterestRate =0;
        while(true) {
            System.out.print("Annual Interest Rate: ");
            annualInterestRate = scanner.nextFloat();
            if ((annualInterestRate > 0) && (annualInterestRate <= 30))
                break;
            System.out.println("Enter a value greater than 0 and less than or equal to 30.");
        }

        float monthlyInterestRate = annualInterestRate/MONTHS_IN_YEAR/PERCENT; //monthInterestRate

        //Period
        byte years =0;
        while(true) {
            System.out.print("Period (Years): ");
            years = scanner.nextByte();
            if ((years > 1) && (years < 30))
                break;
            System.out.println("Enter a value between 1 and 30.");
        }
        int numberOfPayments =years*MONTHS_IN_YEAR;



    //Final Mortgage Calculations
        double mortgage =principal
                *((monthlyInterestRate*(Math.pow(1+monthlyInterestRate,numberOfPayments)))
                /((Math.pow(1+monthlyInterestRate,numberOfPayments))-1));

        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String result =currency.format(mortgage);
        System.out.println("Mortgage: " + result);

    }
}
