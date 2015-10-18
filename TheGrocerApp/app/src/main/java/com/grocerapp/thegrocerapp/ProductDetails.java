package com.grocerapp.thegrocerapp;

import android.content.DialogInterface;
import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;


public class ProductDetails extends ActionBarActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_product_details);
        // Get the message from the intent
        Intent intent = getIntent();
        Bundle bundle = getIntent().getExtras();
        ProductItem item = (ProductItem) bundle.getSerializable("item");

        Log.d("PRODUCTDETAILS", item.getCategory() + item.getHeadline() + item.getQuantity());
        View header = (View)getLayoutInflater().inflate(R.layout.activity_product_details, null);

        TextView name = (TextView) header.findViewById(R.id.textViewName);
        name.setText("Name: " + item.getHeadline());

        TextView quantity = (TextView) header.findViewById(R.id.textViewQuantity);
        quantity.setText("Quantity: " + item.getQuantity());

        TextView category = (TextView) header.findViewById(R.id.textViewCategory);
        category.setText("Category: " + item.getCategory());


        Button bt = (Button) header.findViewById(R.id.button);
        bt.setOnClickListener(new  View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
                Toast.makeText(getApplicationContext(), "Item added to cart",
                        Toast.LENGTH_LONG).show();
            }});
        setContentView(header);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_product_details, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
