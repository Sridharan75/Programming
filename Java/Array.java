class Array{
    public static void main(String[] args){
        int[][] myNum={{1,2,3,4,5},{6,7,8,9,10}};
        for(int i=0;i<5;i++){
            System.out.print(myNum[0][i]+" ");
        }
        System.out.println();
        for(int j=0;j<5;j++){
            System.out.print(myNum[1][j]+" ");
        }
    }
}