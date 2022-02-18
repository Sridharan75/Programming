class GreetingTime{
    public static void greeting(int x,String y){
        if ((x>0)&&(x<12)){
            System.out.println("Good Morning! "+y+", Have a nice day!");
        }else if((x>12)&&(x<16)){
            System.out.println("Good Afternoon! "+y);
        }else if((x>16)&&(x<18)){
            System.out.println("Good Evening! "+y);
        }else{
            System.out.println("Good night! "+y);
        }
    }
    public static void main(String[] args){
        int time=19;
        String myName="Sri";
        greeting(time,myName);
    }
}