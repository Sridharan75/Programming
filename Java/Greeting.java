class Greeting{
    public static void main(String[] args){
        int time=18;
        if ((time>0)&&(time<12)){
            System.out.println("Good Morning!");
        }else if((time>12)&&(time<16)){
            System.out.println("Good Afternoon");
        }else if((time>16)&&(time<18)){
            System.out.println("Good Evening");
        }else{
            System.out.println("Good night");
        }
    }
}