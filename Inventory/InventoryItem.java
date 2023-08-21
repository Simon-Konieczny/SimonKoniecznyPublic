package Inventory;

public class InventoryItem {
    private String ItemName;
    private int ItemQuantity;
    private double ItemPrice;
    private double ItemsValue;

    public InventoryItem(String name, int quan, double price){
        this.ItemName = name;
        this.ItemQuantity = quan;
        this.ItemPrice = price;
        this.ItemsValue = this.ItemQuantity*ItemPrice;
    }

    //Getters and setters
    public double getValue(){
        return this.ItemsValue;
    }
    @Override
    public String toString(){
        return ItemName + " | Quantity: " + ItemQuantity + " | Price per piece: " + ItemPrice + " | Value: " + ItemsValue;
    }
}
