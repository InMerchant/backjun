import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = 1, b = 1, c = 2, d = 2, e = 2, f = 8;

        a -= sc.nextInt();
        b -= sc.nextInt();
        c -= sc.nextInt();
        d -= sc.nextInt();
        e -= sc.nextInt();
        f -= sc.nextInt();

        System.out.print(a +" "+ b +" "+ c +" " + d +" " + e +" " + f);
    }
}