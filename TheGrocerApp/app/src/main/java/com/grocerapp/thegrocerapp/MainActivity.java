package com.grocerapp.thegrocerapp;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v4.content.LocalBroadcastManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.ProgressBar;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GoogleApiAvailability;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Serializable;
import java.util.ArrayList;


public class MainActivity extends AppCompatActivity {
    private static final int PLAY_SERVICES_RESOLUTION_REQUEST = 9000;
    private static final String TAG = "MainActivity";

    private TextView mInformationTextView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ArrayList image_details = getListData();
        final ListView lv1 = (ListView) findViewById(R.id.custom_list);
        lv1.setAdapter(new CustomListAdapter(this, image_details));
        lv1.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> a, View v, int position, long id) {
                Object o = lv1.getItemAtPosition(position);
                ProductItem productItem = (ProductItem) o;
                Intent intent = new Intent(v.getContext(), ProductDetails.class);
                intent.putExtra("item",(Serializable) productItem);
                startActivity(intent);
            }
        });

    }



    private ArrayList getListData() {
        ArrayList<ProductItem> results = new ArrayList<ProductItem>();
        InputStream in = getResources().openRawResource(R.raw.sku);
        InputStreamReader is = new InputStreamReader(in);
        StringBuilder sb=new StringBuilder();
        BufferedReader br = new BufferedReader(is);
        try {
            String line = br.readLine();
            while (line != null) {
                String[] arr = line.split(",");
                ProductItem newsData = new ProductItem();
                newsData.setHeadline(arr[1]);
                newsData.setCategory(arr[2]);
                newsData.setQuantity(arr[3]);
                results.add(newsData);
                line = br.readLine();
            }
            br.close();
        } catch (IOException ex) {
            Log.d(TAG, ex.getLocalizedMessage());
        }

        // Add some more dummy data for testing
        return results;
    }

}
