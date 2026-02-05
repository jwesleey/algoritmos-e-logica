import java.util.Scanner;

public class EquacaoSegundoGrau {
    static void main() {

        Scanner sc = new Scanner(System.in);

        System.out.println("Digite a equação: AX² + BX + C = 0");
        System.out.println("Digite o valor de A: ");
        double a = sc.nextDouble();
        System.out.println("Digite o valor de B: ");
        double b = sc.nextDouble();
        System.out.println("Digite o valor de C: ");
        double c = sc.nextDouble();

        if (a == 0) {
            System.out.println("Não é equação de segundo grau.");
            return;
        }

        double delta = Math.pow(b, 2) - 4 * a * c;

        if (delta < 0) {
            System.out.println("Nenhuma raiz real.");
        } else if (delta == 0) {
            double x = -b / (2 * a);
            System.out.println("Raiz única: " + x);
        } else {
            double raizDelta = Math.pow(delta, 0.5);
            double x1 = (-b + raizDelta) / (2 * a);
            double x2 = (-b - raizDelta) / (2 * a);
            System.out.println("x1 = " + x1);
            System.out.println("x2 = " + x2);
        }
    }
}
