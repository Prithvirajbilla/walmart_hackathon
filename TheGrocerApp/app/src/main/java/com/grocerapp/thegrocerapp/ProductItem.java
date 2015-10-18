package com.grocerapp.thegrocerapp;

import java.io.Serializable;

/**
 * Created by sushant on 10/18/15.
 */
public class ProductItem implements Serializable{
    private String name;
    private String category;
    private String quantity;
    public String getHeadline() {
        return name;
    }

    public void setHeadline(String headline) {
        this.name = headline;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getQuantity() {
        return quantity;
    }

    public void setQuantity(String quantity) {
        this.quantity = quantity;
    }
}