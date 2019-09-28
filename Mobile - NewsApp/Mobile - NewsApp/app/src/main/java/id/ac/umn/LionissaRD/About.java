package id.ac.umn.LionissaRD;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Html;
import android.text.method.LinkMovementMethod;
import android.widget.TextView;

public class About extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_about);

//        TextView textView12 = findViewById(R.id.textView12);
//        String linkText12 = "See the video <a href='https://www.youtube.com/watch?v=11kMehSu-2Q'>here</a>.";
//        textView12.setText(Html.fromHtml(linkText12, Html.FROM_HTML_MODE_LEGACY));
//        textView12.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView7 = findViewById(R.id.textView7);
        String linkText7 = "This project is powered by <a href='https://newsapi.org/'><strong>NewsAPI.org</strong></a>";
        textView7.setText(Html.fromHtml(linkText7, Html.FROM_HTML_MODE_LEGACY));
        textView7.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView13 = findViewById(R.id.textView13);
        String linkText13 = "See the codes <a href='https://github.com/itsSiddharthGupta/Top-10-News-Of-The-Day'>here</a>";
        textView13.setText(Html.fromHtml(linkText13, Html.FROM_HTML_MODE_LEGACY));
        textView13.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView15 = findViewById(R.id.textView15);
        String linkText15 = "See the codes <a href='https://github.com/JEEricsson/test-News'>here</a>";
        textView15.setText(Html.fromHtml(linkText15, Html.FROM_HTML_MODE_LEGACY));
        textView15.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView17 = findViewById(R.id.textView17);
        String linktext17 = "See the codes <a href='https://github.com/square/picasso'>here</a>";
        textView17.setText(Html.fromHtml(linktext17, Html.FROM_HTML_MODE_LEGACY));
        textView17.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView19 = findViewById(R.id.textView19);
        String linktext19 = "Read the article <a href='https://stackoverflow.com/questions/34916781/calling-web-api-and-receive-return-value-in-android'>here</a>";
        textView19.setText(Html.fromHtml(linktext19, Html.FROM_HTML_MODE_LEGACY));
        textView19.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView21 = findViewById(R.id.textView21);
        String linktext21 = "Read the article <a href='https://stackoverflow.com/questions/35721692/java-lang-illegalargumentexception-path-must-not-be-empty-in-picasso'>here</a>";
        textView21.setText(Html.fromHtml(linktext21, Html.FROM_HTML_MODE_LEGACY));
        textView21.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView23 = findViewById(R.id.textView23);
        String linktext23 = "Read the article <a href='https://www.google.com/amp/s/www.androidauthority.com/how-to-create-android-notifications-707254/amp/'>here</a>";
        textView23.setText(Html.fromHtml(linktext23, Html.FROM_HTML_MODE_LEGACY));
        textView23.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textView25 = findViewById(R.id.textView25);
        String linktext25 = "Read the article <a href='https://coderanch.com/t/654627/string-intent-null-object-reference'>here</a>";
        textView25.setText(Html.fromHtml(linktext25, Html.FROM_HTML_MODE_LEGACY));
        textView25.setMovementMethod(LinkMovementMethod.getInstance());

        TextView textview29 = findViewById(R.id.textView29);
        String linktext29 = "Read the article <a href='https://stackoverflow.com/questions/19096475/android-i-need-to-delay-a-notification'>here</a>";
        textview29.setText(Html.fromHtml(linktext29, Html.FROM_HTML_MODE_LEGACY));
        textview29.setMovementMethod(LinkMovementMethod.getInstance());
    }
}
