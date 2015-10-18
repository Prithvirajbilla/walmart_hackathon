package com.grocerapp.thegrocerapp;

import android.app.IntentService;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v4.content.LocalBroadcastManager;
import android.util.Log;

import com.google.android.gms.gcm.GcmPubSub;
import com.google.android.gms.gcm.GoogleCloudMessaging;
import com.google.android.gms.iid.InstanceID;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by sushant on 10/18/15.
 */
public class RegistrationIntentService extends IntentService {
    private static final String TAG = "RegIntentService";
    private static final String[] TOPICS = {"global"};

    public RegistrationIntentService() {
        super(TAG);
    }

    @Override
    protected void onHandleIntent(Intent intent) {
        SharedPreferences sharedPreferences = PreferenceManager.getDefaultSharedPreferences(this);
        Log.d(TAG, "TESTING");
        Bundle bundle = intent.getExtras();
        String user = bundle.getString("user");

        try {
        // [START register_for_gcm]
        // Initially this call goes out to the network to retrieve the token, subsequent calls
        // are local.
        // [START get_token]
        InstanceID instanceID = InstanceID.getInstance(this);
        // R.string.gcm_defaultSenderId (the Sender ID) is typically derived from google-services.json.
        // See https://developers.google.com/cloud-messaging/android/start for details on this file.
        String token = instanceID.getToken(getString(R.string.gcm_defaultSenderId),
                GoogleCloudMessaging.INSTANCE_ID_SCOPE, null);
        // [END get_token]
        Log.d(TAG, "GCM Registration Token: " + token);

        // TODO: Implement this method to send any registration to your app's servers.
        sendRegistrationToServer(token, user);

        // [END register_for_gcm]
    } catch (Exception e) {
        Log.d(TAG, "Failed to complete token refresh", e);
        // If an exception happens while fetching the new token or updating our registration data
        // on a third-party server, this ensures that we'll attempt the update at a later time.
    }
    // Notify UI that registration has completed, so the progress indicator can be hidden.
    Intent registrationComplete = new Intent(QuickstartPreferences.REGISTRATION_COMPLETE);
    LocalBroadcastManager.getInstance(this).sendBroadcast(registrationComplete);
}

    /**
     * Persist registration to third-party servers.
     *
     * Modify this method to associate the user's GCM registration token with any server-side account
     * maintained by your application.
     *
     * @param token The new token.
     */
    private void sendRegistrationToServer(String token, String user) {
        // Add custom implementation, as needed.
        try {

            String url = "http://188.166.247.123/token?user=" + user + "&token=" + token;

            HttpClient client = new DefaultHttpClient();
            HttpGet request = new HttpGet(url);


            HttpResponse response = client.execute(request);
            Log.d(TAG, "\nSending 'GET' request to URL : " + url);

        } catch (Exception ex) {

        }
    }

    /**
     * Subscribe to any GCM topics of interest, as defined by the TOPICS constant.
     *
     * @param token GCM token
     * @throws IOException if unable to reach the GCM PubSub service
     */
    // [START subscribe_topics]
    private void subscribeTopics(String token) throws IOException {
        GcmPubSub pubSub = GcmPubSub.getInstance(this);
        for (String topic : TOPICS) {
            pubSub.subscribe(token, "/topics/" + topic, null);
        }
    }
    // [END subscribe_topics]
}
