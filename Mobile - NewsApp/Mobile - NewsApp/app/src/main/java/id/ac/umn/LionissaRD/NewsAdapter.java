package id.ac.umn.LionissaRD;

import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.support.annotation.NonNull;
import android.support.v4.app.NotificationCompat;
import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

public class NewsAdapter extends RecyclerView.Adapter<NewsAdapter.NewsViewHolder>
{
    private Context mCtx;
    private ArrayList<News> newsList;

    public NewsAdapter(Context mCtx, ArrayList<News> newsList)
    {
        this.mCtx = mCtx;
        this.newsList = newsList;
    }

    @NonNull
    @Override
    public NewsAdapter.NewsViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int i) {
        LayoutInflater inflater = LayoutInflater.from(mCtx);
        View view = inflater.inflate(R.layout.list_layout, null);
        NewsViewHolder holder = new NewsViewHolder(view);
        return holder;
    }

    @Override
    public void onBindViewHolder(@NonNull NewsAdapter.NewsViewHolder newsViewHolder, int i)
    {
        final News news = newsList.get(i);
        newsViewHolder.card_text.setText(news.getTitle());
        if(news.getUrlToImage().isEmpty())
        {
            Toast.makeText(mCtx, "Image(s) can't be downloaded", Toast.LENGTH_SHORT).show();
        }
        else
        {
            Picasso.get().load(news.getUrlToImage()).into(newsViewHolder.card_image);
        }

        newsViewHolder.cardView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v)
            {
                Intent intent = new Intent(mCtx, NewsDetails.class);

                intent.putExtra("title", news.getTitle());
                intent.putExtra("image", news.getUrlToImage());
                intent.putExtra("desc", news.getDescription());
                intent.putExtra("url", news.getUrl());
                intent.putExtra("author", news.getAuthor());

                mCtx.startActivity(intent);
            }
        });

        newsViewHolder.cardView.setOnLongClickListener(new View.OnLongClickListener(){
            @Override
            public boolean onLongClick(View v)
            {
                Toast.makeText(mCtx, "This news has been registered!", Toast.LENGTH_LONG).show();

                Handler handler = new Handler();
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        addNotification();
                    }
                }, 5000);


                return true;
            }
        });

    }

    @Override
    public int getItemCount() {
        return newsList.size();
    }

    class NewsViewHolder extends RecyclerView.ViewHolder
    {
        CardView cardView;
        ImageView card_image;
        TextView card_text;

        public NewsViewHolder(@NonNull View itemView)
        {
            super(itemView);
            cardView = itemView.findViewById(R.id.cardView);
            card_image = itemView.findViewById(R.id.card_image);
            card_text = itemView.findViewById(R.id.card_text);
        }
    }

    private void addNotification()
    {
        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(mCtx)
                        .setSmallIcon(R.drawable.ic_sentiment_very_satisfied_black_24dp)
                        .setContentTitle("Lionissa's News")
                        .setContentText("A news has been registered!");

        Intent notificationIntent = new Intent(mCtx, MainActivity.class);
        PendingIntent contentIntent = PendingIntent.getActivity(mCtx, 0, notificationIntent, PendingIntent.FLAG_UPDATE_CURRENT);
        builder.setContentIntent(contentIntent);

        NotificationManager notificationManager = (NotificationManager) mCtx.getSystemService(mCtx.NOTIFICATION_SERVICE);
        notificationManager.notify(1, builder.build());
    }
}
