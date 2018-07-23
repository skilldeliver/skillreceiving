import java.util.Scanner;

public class SquareOfStars_6 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int number = Integer.parseInt(scanner.nextLine());

        //ред 1
        System.out.println(repeatStr("*", number));

        //средни редове
        for (int i = 0; i < number - 2; i++) {
            System.out.println("*" + repeatStr(" ", number - 2) + "*");

        }


        //последен ред
        System.out.println(repeatStr("*", number));


    }

    // Метод за повтаряне на определен символ няколко пъти (в лекция 4 или 5 ще бъде показана). Използва се като напишем repeatStr
    // ( първо пишем символа, който искаме да повторим след това запетая и пишем колко пъри искаме да го повторим)

    static String repeatStr(String str, int count) {
        String text = "";
        {
            for (int j = 0; j < count; j++) {
                text = text + str;
            }

        }
        return text;
    }
}
















