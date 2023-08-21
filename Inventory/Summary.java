package Inventory;
import java.util.ArrayList;

public class Summary{
    private ArrayList<InventoryItem> itemsArray;
    private int numOfItems;
    private double totalVal;

    public Summary(ArrayList<InventoryItem> items){
        this.itemsArray = new ArrayList<>(items);
        this.totalVal = 0;
        this.numOfItems = itemsArray.size();

        for(InventoryItem item : this.itemsArray){
            this.totalVal += item.getValue();
        }
    }

    @Override
    public String toString(){
        return "Total Items: " + this.numOfItems + " valued at: " + this.totalVal;
    }
}
