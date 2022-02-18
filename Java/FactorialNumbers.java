class FactorialNumbers{
    public static void main(String[] args){
        int n=10;
        long fact=1;
        if (n>=1){
            int i=1;
            while(i<=n){
                fact=fact*i;
                i++;
            }System.out.println("Factorial of "+n +" is : "+fact);
        }else if(n==0){
            System.out.println("Factorial of 0 is : 1");
        }else{
            System.out.println("Sorry, factorial does not exist for negative numbers");
        }
    }
}