public class app {
    public static void main(String[] args) {
        String first_name = "Sritharan";
        String last_name = "SK";
        String full = String.format(first_name + last_name, args);
        System.out.println(full);
    }
}