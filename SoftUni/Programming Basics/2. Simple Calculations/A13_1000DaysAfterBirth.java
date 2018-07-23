import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;
public class N_1000DaysAfterBirth {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(Console.nextLine(), formatter);
        date = date.plusDays(999);
        System.out.println(formatter.format(date));
    }
}
