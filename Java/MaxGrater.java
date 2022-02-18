class MaxGrater{
    public static void main(String[] args){
        int num1,num2,num3;
        num1=15;
        num2=10;
        num3=7;
        if (num1>num2){
            if (num1>num3){
                System.out.println(num1);
            }else{
                System.out.println(num3);
            }
        }else{
            if (num2>num3){
                System.out.println(num2);
            }else{
                System.out.println(num3);
            }
        }
    }
}