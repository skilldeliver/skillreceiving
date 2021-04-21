package com.company;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.List;


abstract class Sportist
{
    String name;
    final Date dateOffiling;
    double mainCompensation;

    public Sportist(String name, Date dateOffiling, double mainCompensation) {
        this.name = name;
        this.dateOffiling = dateOffiling;
        this.mainCompensation = mainCompensation;
    }

    public void increaeComponesation(double value){
        this.mainCompensation += value;
    }

    public boolean filledEarlier(Sportist sportist){
        return this.dateOffiling.before(sportist.dateOffiling);
    }

    public double salary(){
        int year = Calendar.getInstance().get(Calendar.YEAR);
        int difference = this.dateOffiling.getYear() - year;
        return this.mainCompensation + (difference/100.0 * this.mainCompensation);
    }
}

enum Style {
    FREE_STYLE,
    BREASTSTROKE,
    BUTTERFLY,
    BACKSTROKE
}

class Swimmer extends Sportist
{
    Style style;
    boolean competesInOpenWater;

    public Swimmer(String name, Date dateOffiling, double mainCompensation, Style style, boolean competesInOpenWater) {
        super(name, dateOffiling, mainCompensation);
        this.style = style;
        this.competesInOpenWater = competesInOpenWater;
    }

    public Swimmer largerSalary(Swimmer swimmer){
        if (this.salary() > swimmer.salary()){
            return this;
        }
        return swimmer;
    }

    public double salary(){
        if (competesInOpenWater) {
            return super.salary() * 1.05;
        }
        return super.salary();
    }

    public boolean styleIsFreeStyle(){
        return this.style == Style.FREE_STYLE;
    }
}

class SwimmingCompetion{
    Date dateOfConduction;
    boolean ConductionInOpenWaters;
    List<Swimmer> swimmerList;

    public SwimmingCompetion(Date dateOfConduction, boolean ConductionInOpenWaters) {
        this.dateOfConduction = dateOfConduction;
        swimmerList = new ArrayList<Swimmer>();
    }

    public void addSwimmer(Swimmer swimmer){
        if (swimmer.competesInOpenWater == ConductionInOpenWaters) {
            swimmerList.add(swimmer);
        }
    }

    public double totalCompensation(Style style){
        double result = 0.0;
        for (int counter = 0; counter < swimmerList.size(); counter++) {
            Swimmer swimmer = swimmerList.get(counter);
            if (swimmer.style == style){
                result += swimmer.salary();
            }
        }
        return result;
    }

    public double averageCompensation(Style style){
        double result = 0.0;
        int count = 0;

        for (int counter = 0; counter < swimmerList.size(); counter++) {
            Swimmer swimmer = swimmerList.get(counter);
            if (swimmer.style == style){
                result += swimmer.salary();
                count += 1;
            }
        }
        return result / count;
    }


}

public class Main {

    public static void main(String[] args) throws IOException, ParseException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String competitionName = bufferedReader.readLine();
        boolean ConductionInOpenWaters = Integer.parseInt(bufferedReader.readLine().trim()) != 0;
        Date dateOfConduction = new SimpleDateFormat("dd-MM-yyyy").parse(bufferedReader.readLine());

        SwimmingCompetion swimmingCompetion = new SwimmingCompetion(dateOfConduction, ConductionInOpenWaters);
        int numberOfSwimmers = Integer.parseInt(bufferedReader.readLine().trim());

        for (int i = 0; i < numberOfSwimmers; i++) {
            String name = bufferedReader.readLine();
            Date dateOffiling =  new SimpleDateFormat("dd-MM-yyyy").parse(bufferedReader.readLine());
            double mainCompensation = Double.parseDouble(bufferedReader.readLine().trim());
            boolean competesInOpenWater = Integer.parseInt(bufferedReader.readLine().trim()) != 0;
            String style = bufferedReader.readLine();
            Style enumStyle;

            if (style.equals("FREE_STYLE")) {
                enumStyle = Style.FREE_STYLE;
            }
            else if (style.equals("BREASTSTROKE")){
                enumStyle = Style.BREASTSTROKE;
            }
            else if (style.equals("BUTTERFLY")){
                enumStyle = Style.BUTTERFLY;
            }
            else if (style.equals("BACKSTROKE")){
                enumStyle = Style.BACKSTROKE;
            }
            Swimmer swimmer = new Swimmer(name, dateOffiling, mainCompensation, enumStyle, competesInOpenWater);
            swimmingCompetion.addSwimmer(swimmer);
        }
    }
}
