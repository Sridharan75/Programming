package com.company;

public class Main {

    public static void main(String[] args) {
        var textBox1=new TextBox();
        var textBox2=new TextBox();
        textBox1.setText("Box 1");
        textBox2.setText("Box 2");
        System.out.println(textBox1.text.toUpperCase());
        System.out.println(textBox2.text);
    }
}
