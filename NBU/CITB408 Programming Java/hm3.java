import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Manufacturer {
  String manufacturerName;
  boolean  isLongTermWarranty;

  public Manufacturer(String name, boolean warranty) {
    manufacturerName = name;
    isLongTermWarranty = warranty;
  }
}


class ElectricDevice {
  Manufacturer manufacturer;
  int minWarranty;

  public ElectricDevice(Manufacturer manufacturerObj, int warranty) {
    manufacturer = manufacturerObj;
    minWarranty = warranty;
  }
    
  public int warranty() {
      if (manufacturer.isLongTermWarranty) {
          return 12 + minWarranty;
      }
      return minWarranty;
  }
}

class Cooker extends ElectricDevice {
    boolean isGas;
    
    public Cooker(Manufacturer manufacturerObj, int warranty, boolean isGas)
    {
        super(manufacturerObj, warranty);
        this.isGas = isGas;
    }
    
    @Override public int warranty() {
        
        int warrantyResult = minWarranty;
        if (manufacturer.isLongTermWarranty) {
              warrantyResult += 12;
         }
        if (isGas){
            warrantyResult += 12;
        }
        
      return warrantyResult;
    }
}

class WashingMachine extends ElectricDevice {
    boolean isDryer;
    
    public WashingMachine(Manufacturer manufacturerObj, int warranty, boolean isDryer)
    {
        super(manufacturerObj, warranty);
        this.isDryer = isDryer;
    }
    
    @Override public int warranty() {
        
        int warrantyResult = minWarranty;
        if (manufacturer.isLongTermWarranty) {
              warrantyResult += 12;
         }
        if (isDryer){
            warrantyResult += minWarranty / 2;
        }
        
      return warrantyResult;
    }
    
}



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String manufacturerName = bufferedReader.readLine();

        boolean isLongTermWarranty = Integer.parseInt(bufferedReader.readLine().trim()) != 0;

        int minWarranty = Integer.parseInt(bufferedReader.readLine().trim());

        boolean isGas = Integer.parseInt(bufferedReader.readLine().trim()) != 0;

        boolean isDryer = Integer.parseInt(bufferedReader.readLine().trim()) != 0;

        // Create object of type Manufacturer using the constructor with two parameters. Pass manufacturerName and isLongTermWarranty as arguments
        if (minWarranty < 6) {
            minWarranty = 6;
        }

        Manufacturer manufacturer = new Manufacturer(manufacturerName, isLongTermWarranty);
        // Create object of type ElectricDevice using the constructor with 2 parameters. Pass manufacturer and minWarranty as arguments: ElectricDevice electricDevice = new ElectricDevice(manufacturer, minWarranty);
        ElectricDevice device = new ElectricDevice(manufacturer, minWarranty);
        // Print on the console the warranty of the the object electricDevice, by calling warranty() method
        System.out.println(device.warranty());
        // Assign the electricDevice a new object of type Cooker using the constructor with 3 parameters. Pass manufacturer, price and minWarranty as arguments: electricDevice = new Cooker(manufacturer, minWarranty, isGas);
        device =  new Cooker(manufacturer, minWarranty, isGas);
        // Print on the console the warranty of the object electricDevice, by calling warranty() method
        System.out.println(device.warranty());
        // Assign the electricDevice a new object of type WashingMachine using the constructor with 3 parameters. Pass manufacturer, price and minWarranty as arguments: electricDevice = new WashingMachine(manufacturer, minWarranty, isDryer);
        device = new WashingMachine(manufacturer, minWarranty, isDryer);
        // Print on the console the warranty of the the object electricDevice, by calling warranty() method
        System.out.println(device.warranty());
        bufferedReader.close();
    }
}

