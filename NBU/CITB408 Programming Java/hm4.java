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


// // Interface
// interface Creature {
//   public void animalSound(); // interface method (does not have a body)
//   public void sleep(); // interface method (does not have a body)
// }

// // Pig "implements" the Animal interface
// class Pig implements Animal {
//   public void animalSound() {
//     // The body of animalSound() is provided here
//     System.out.println("The pig says: wee wee");
//   }
//   public void sleep() {
//     // The body of sleep() is provided here
//     System.out.println("Zzz");
//   }
// }

// // Abstract class
// abstract class Animal implements Creature{ 
//   // Abstract method (does not have a body)
//   public abstract void animalSound();
//   // Regular method
//   public void sleep() {
//     System.out.println("Zzz");
//   }
// }

// // Subclass (inherit from Animal)
// class Pig extends Animal {
//   public void animalSound() {
//     // The body of animalSound() is provided here
//     System.out.println("The pig says: wee wee");
//   }
// }





abstract class Product { 
    int multiplyBy;
    public Product( int multiplyBy ) {
        this.multiplyBy = multiplyBy;
    }

    public int mutiply(int val) {
       return multiplyBy * val;
    }
}

// class TimesTwo extends Product {
//     public TimesTwo() {
//         super(2);
//     }
// }

// class TimesWhat extends Product {
//     public TimesWhat(int what) {
//         super(what);
//     }
// }


//our task...

interface Deliverable
{
    public double deliveryPrice();
    public void setAdditionalPrice(double additionalPrice);
}

abstract class DeliverableItem implements Deliverable
{
    boolean toClientsAddress;
    double additionalPrice;

    public DeliverableItem( boolean toClientsAddress ) {
        this.toClientsAddress = toClientsAddress;
        
    }

    public abstract double deliveryPrice();
}


class Document extends DeliverableItem
{
   double minPrice; 

    public Document(boolean toClientsAddress, double minPrice) {
        super(toClientsAddress);
        this.minPrice = minPrice;
    }

    
    public double getAdditionalPrice() {
        return this.additionalPrice;
    }

    public void setAdditionalPrice(double additionalPrice) {
        if(toClientsAddress)
        {
            this.additionalPrice = additionalPrice; 
        }
        else {
            this.additionalPrice = 0.0;
        }
    }


    public double deliveryPrice()
    {
        double resultPrice = this.minPrice + getAdditionalPrice();
        return resultPrice;
    }
}

class Material
{
    String materialName;
    boolean isFragile;

    public Material(String materialName, boolean isFragile)
    {
        this.materialName = materialName;
        this.isFragile = isFragile;
    }

    public boolean IsFragile()
    {
        return this.isFragile;
    }
}

class WeightedItem extends DeliverableItem
{
    Material material; 
    double weight;
    double pricePerKg;

    public WeightedItem(boolean toClientsAddress, Material material, double weight, double pricePerKg) {
        super(toClientsAddress);
        this.material = material;
        this.weight = weight;
        this.pricePerKg = pricePerKg;
    }


    public double getAdditionalPrice() {
        return this.additionalPrice;
    }

    public void setAdditionalPrice(double additionalPrice) {
        if(toClientsAddress)
        {
            this.additionalPrice = additionalPrice; 
        }
        else {
            this.additionalPrice = 0.0;
        }
    }
    
    public double deliveryPrice(){
        double resultPrice;
        resultPrice = (weight * pricePerKg);

        resultPrice += getAdditionalPrice();

        if (material.IsFragile()){
            resultPrice *= 1.01;
        }
        return resultPrice;
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String materialName = bufferedReader.readLine();

        boolean isFragile = Integer.parseInt(bufferedReader.readLine().trim()) != 0;

        boolean toClientsAddress = Integer.parseInt(bufferedReader.readLine().trim()) != 0;

        double minPrice = Double.parseDouble(bufferedReader.readLine().trim());

        double weight = Double.parseDouble(bufferedReader.readLine().trim());

        double pricePerKg = Double.parseDouble(bufferedReader.readLine().trim());

        double additionalPrice = Double.parseDouble(bufferedReader.readLine().trim());


        // public class User {
        //     private String name;
        
        //     public String getName() { return this.name; }
        //     public void setName(String name) { this.name = name; }
        // }
        
        if (additionalPrice <= 0){
            additionalPrice = 1;
        }
        if (minPrice <= 0){
            minPrice = 1;
        }
        
        if (weight <= 0){
            weight = 1;
        }
        
        if (pricePerKg <= 0){
            pricePerKg = 1;
        }


        // Create an object of type Material using the constructor with two parameters. Pass materialName and isFragile as arguments.
        Material material = new Material(materialName, isFragile);

        // Create a reference of type Deliverable.
        Deliverable item;

        // Use the reference of type Deliverable to create an object of type Document. Use toClientsAddress and minPrice to the constructor of the Document.
        item = new Document(toClientsAddress, minPrice); 
        // Use the set method to give the value additionalPrice to the additional price when the shipment has to be delivered to the client's address.
        item.setAdditionalPrice(additionalPrice);
        // Print on the console the result of calling the shippingPrice() method: the method that has to return the total shipping price for the delivery.
        System.out.println(item.deliveryPrice());
        // Use the reference of type Deliverable to create an object of type WeightedItem. Use weight and pricePerKg to pass them to the constructor of the WeightedItem.
        item = new WeightedItem(toClientsAddress, material, weight, pricePerKg);
        item.setAdditionalPrice(additionalPrice);
        // Print on the console the result of calling the shippingPrice() method: the method that has to return the total shipping price for the delivery.
        System.out.println(item.deliveryPrice()); //setAdditionalPrice

        bufferedReader.close();
    }
    
}
