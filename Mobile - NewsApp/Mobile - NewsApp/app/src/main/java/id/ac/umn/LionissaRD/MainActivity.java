package id.ac.umn.LionissaRD;

import android.app.PendingIntent;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v4.app.NotificationCompat;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;

import javax.net.ssl.HttpsURLConnection;

public class MainActivity extends AppCompatActivity {

    //menampilkan headline Indonesia.
    String API_URL = "https://newsapi.org/v2/top-headlines?country=id&apiKey=";
    String API_KEY = "8cd9050c2832488bb2f463f057aeefdd";

    RecyclerView main_recyclerView;
    ArrayList<News> newsList;
    NewsAdapter newsAdapter;

    @Override
    public void onBackPressed()
    {
        Toast.makeText(getApplicationContext(), "You've logged in", Toast.LENGTH_SHORT).show();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        main_recyclerView = findViewById(R.id.main_recyclerView);
        main_recyclerView.setHasFixedSize(true);

        main_recyclerView.setLayoutManager(new LinearLayoutManager(this));

        Log.d("debug", "test x");
        new AccessJSONServiceTask().execute(API_URL + API_KEY);

        newsList = new ArrayList<>();
        newsAdapter = new NewsAdapter(MainActivity.this, newsList);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        Intent intent;

        switch(item.getItemId())
        {
            case R.id.menu_dialog_about:
                intent = new Intent(MainActivity.this, About.class);
                startActivity(intent);
                break;
            case R.id.menu_dialog_logout:
                intent = new Intent(MainActivity.this, Login.class);
                startActivity(intent);
                break;
        }

        return super.onOptionsItemSelected(item);
    }

    private class AccessJSONServiceTask extends AsyncTask<String, Void, String>
    {
        @Override
        protected String doInBackground(String... urls)
        {
            Log.d("debug", "test 6");
            String result = "";
            URL url;
            HttpsURLConnection urlConnection = null;

            try{
                url = new URL(urls[0]);
                urlConnection = (HttpsURLConnection) url.openConnection();
                InputStream inputStream = urlConnection.getInputStream();
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
                result = bufferedReader.readLine();
                Log.d("debug", "Show me: " + result);
                parseResult(result);
                return result;
            }
            catch (MalformedURLException e)
            {
                e.printStackTrace();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }

            return null;
        }

        @Override
        protected void onPostExecute(String result)
        {
            if(result != null)
            {
                Log.d("debug", "Show me the result: " + result);
                main_recyclerView.setAdapter(newsAdapter);
            }
            else
            {
                Toast.makeText(getApplicationContext(), "Data can't be loaded", Toast.LENGTH_SHORT).show();
            }
        }
    }

    private void parseResult(String result)
    {
        try
        {
            JSONObject response = new JSONObject(result);
            JSONArray posts = response.optJSONArray("articles");
            News news;
            for(int i = 0; i < posts.length(); i++)
            {
                news = new News();
                JSONObject post = posts.optJSONObject(i);

                String title = post.optString("title");
                Log.d("debug", "Title: " + title);
                news.setTitle(title);

                String image = post.optString("urlToImage");
                Log.d("debug", "Image: " + image);
                news.setUrlToImage(image);

                String description = post.optString("description");
                Log.d("debug", "Description: " + description);
                news.setDescription(description);

                String url = post.optString("url");
                Log.d("debug", "Url: " + url);
                news.setUrl(url);

                String author = post.optString("author");
                Log.d("debug", "Author: " + author);
                news.setAuthor(author);

                newsList.add(news);
            }
        }
        catch (JSONException e)
        {
            e.printStackTrace();
        }
    }



}
