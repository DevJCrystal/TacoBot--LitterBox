package com.jacrystal.tacobot__litterbox;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class urlSettings extends AppCompatActivity {

    SharedPreferences sharedpreferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_url_settings);

        sharedpreferences = getApplicationContext().getSharedPreferences("AppKey", 0);
        final EditText editBox = findViewById(R.id.urlBox);

        editBox.setText(sharedpreferences.getString("url", "https://www.google.com"));

        findViewById(R.id.saveButton).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                SharedPreferences.Editor editor = sharedpreferences.edit();
                editor.putString("url", editBox.getText().toString());
                editor.apply();
            }
        });
    }
}
