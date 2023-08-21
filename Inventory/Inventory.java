package Inventory;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Inventory extends JFrame{
    private ArrayList<InventoryItem> inventoryItems;

    private JLabel nameLabel;
    private JLabel quantityLabel;
    private JLabel priceLabel;

    private JTextField nameField;
    private JTextField quantityField;
    private JTextField priceField;

    private JButton addButton;
    private JTextArea inventoryArea;
    private JTextArea summaryArea;

    public Inventory(){
        inventoryItems = new ArrayList<>();

        nameLabel = new JLabel("Item Name: ");
        quantityLabel = new JLabel("Quantity: ");
        priceLabel = new JLabel("Price per item: ");

        nameField = new JTextField(15);
        quantityField =  new JTextField(5);
        priceField =  new JTextField(10);

        addButton = new JButton("Add Item");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e){
                addItem();
            }
        });

        inventoryArea = new JTextArea(20,50);
        inventoryArea.setEditable(false);

        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(5, 2, 5, 5));
        inputPanel.add(nameLabel);
        inputPanel.add(nameField);
        inputPanel.add(quantityLabel);
        inputPanel.add(quantityField);
        inputPanel.add(priceLabel);
        inputPanel.add(priceField);
        inputPanel.add(addButton);

        summaryArea = new JTextArea(1,50);
        summaryArea.setEditable(false);

        JScrollPane scrollPane = new JScrollPane(inventoryArea);

        setLayout(new FlowLayout());
        add(inputPanel);
        add(scrollPane);
        add(summaryArea);
        setTitle("Inventory Management");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        pack();
        setLocationRelativeTo(null);
        setVisible(true);
        updateInventoryDisplay();
    }

    private void addItem(){
        String itemName = nameField.getText();
        int quantity = Integer.parseInt(quantityField.getText());
        double price = Double.parseDouble(priceField.getText());

        InventoryItem item = new InventoryItem(itemName, quantity, price);
        inventoryItems.add(item);

        updateInventoryDisplay();
        clearInputFields();
    }

    private void updateInventoryDisplay(){
        inventoryArea.setText("");
        for(InventoryItem item : inventoryItems){
            inventoryArea.append(item.toString()+"\n");
        }
        summaryArea.setText(new Summary(inventoryItems).toString());
    }

    private void clearInputFields(){
        nameField.setText("");
        quantityField.setText("");
        priceField.setText("");
    }

    public static void main(String[] args){
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run(){
                new Inventory();
            }
        });
    }
}
