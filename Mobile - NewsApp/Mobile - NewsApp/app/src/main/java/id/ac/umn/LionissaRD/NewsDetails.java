package id.ac.umn.LionissaRD;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Intent;
import android.os.Handler;
import android.support.design.widget.FloatingActionButton;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class NewsDetails extends AppCompatActivity {

    TextView details_title, details_desc, details_author, details_read;
    ImageView details_image;
    FloatingActionButton details_button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_news_details);

        details_title = findViewById(R.id.details_title);
        details_desc = findViewById(R.id.details_desc);
        details_author = findViewById(R.id.details_author);
        details_read = findViewById(R.id.details_read);
        details_image = findViewById(R.id.details_image);
        details_button = findViewById(R.id.details_button);

        Intent intent = getIntent();

        if(intent.hasExtra("title"))
        {
            String title = intent.getStringExtra("title");
            details_title.setText(title);
        }

        if(intent.hasExtra("image"))
        {
            String image = intent.getStringExtra("image");
            Picasso.get().load(image).into(details_image);
        }

        if(intent.hasExtra("desc"))
        {
            String desc = intent.getStringExtra("desc");
            details_desc.setText(desc);
        }

        if(intent.hasExtra("url"))
        {
            String url = intent.getStringExtra("url");
            //details_read.setText(url);
            String readhere = "Baca beritanya sekarang di <a href='" + url + "'>sini</a>";
            details_read.setText(Html.fromHtml(readhere, Html.FROM_HTML_MODE_LEGACY));
            details_read.setMovementMethod(LinkMovementMethod.getInstance());
        }

        if(intent.hasExtra("author"))
        {
            String author = intent.getStringExtra("author");
            details_author.setText(author);
        }

        details_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "This news has been registered!", Toast.LENGTH_SHORT).show();
                Handler handler = new Handler();
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        addNotification();
                    }
                }, 5000);
            }
        });

    }

    private void addNotification()
    {
        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(getApplicationContext())
                        .setSmallIcon(R.drawable.ic_sentiment_very_satisfied_black_24dp)
                        .setContentTitle("Lionissa's News")
                        .setContentText("A news has been registered!");

        Intent notificationIntent = new Intent(getApplicationContext(), MainActivity.class);
        PendingIntent contentIntent = PendingIntent.getActivity(getApplicationContext(), 0, notificationIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        builder.setContentIntent(contentIntent);

        NotificationManager notificationManager = (NotificationManager) getApplicationContext().getSystemService(getApplicationContext().NOTIFICATION_SERVICE);
        notificationManager.notify(1, builder.build());
    }
}
