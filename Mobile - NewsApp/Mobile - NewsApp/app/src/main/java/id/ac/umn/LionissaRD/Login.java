package id.ac.umn.LionissaRD;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

public class Login extends AppCompatActivity {

    TextView login_username, login_password;
    EditText e_username, e_password;
    Button login_button;
    ImageButton aboutButton;

    @Override
    public void onBackPressed()
    {

    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        login_username = findViewById(R.id.login_username);
        login_password = findViewById(R.id.login_password);
        e_username = findViewById(R.id.login_username_edit);
        e_password = findViewById(R.id.login_password_edit);
        login_button = findViewById(R.id.login_button);
        aboutButton = findViewById(R.id.aboutButton);


        final DBAdapter dbAdapter = new DBAdapter(getApplicationContext(), null, null, 1);

        login_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String username = e_username.getText().toString();
                String password = e_password.getText().toString();

                dbAdapter.onOpen();
                dbAdapter.insertUser();
                User user = dbAdapter.getUser();

                if (username.length() > 1 && password.length() > 1)
                {
                    if (user != null)
                    {
                        if (username.equals(user.getUsername()) && password.equals(user.getPassword()))
                        {
                            Toast.makeText(getApplicationContext(), "Welcome!", Toast.LENGTH_LONG).show();
                            Intent intent = new Intent(Login.this, MainActivity.class);
                            startActivity(intent);
                            //change with intent if this is successful
                        }
                        else
                        {
                            Toast.makeText(getApplicationContext(), "Username and/or Password is wrong", Toast.LENGTH_LONG).show();
                        }
                    }
                    else
                    {
                        Toast.makeText(getApplicationContext(), "Database is empty", Toast.LENGTH_SHORT).show();
                    }
                }
                else
                {
                    Toast.makeText(getApplicationContext(), "Username and/or is too short", Toast.LENGTH_SHORT).show();
                }



                dbAdapter.close();
            }
        });

        aboutButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Login.this, About.class);
                startActivity(intent);
            }
        });
    }
}
