package id.ac.umn.LionissaRD;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;

public class DBAdapter extends SQLiteOpenHelper
{
    private static final int DATABASE_VERSION = 1;
    private static final String DATABASE_NAME = "Credential.db";
    private static final String TABLE_CONTACTS = "users";

    public static final String COLUMN_USERNAME = "user_name";
    public static final String COLUMN_PASSWORD = "user_password";

    SQLiteDatabase db;


    public DBAdapter(Context context, String name, SQLiteDatabase.CursorFactory factory, int version)
    {
        super(context, DATABASE_NAME, factory, DATABASE_VERSION);
        Log.d("debug", "constructor ok");
    }

    @Override
    public void onCreate(SQLiteDatabase db)
    {
        //CREATE TABLE user (username TEXT PRIMARY KEY NOT NULL, password TEXT NOT NULL)
        Log.d("debug", "onCreate in");
        String CREATE_USER_TABLE =
                "CREATE TABLE " + TABLE_CONTACTS
                + "(" + COLUMN_USERNAME + " TEXT PRIMARY KEY NOT NULL,"
                + COLUMN_PASSWORD + " TEXT NOT NULL" + ")";
        db.execSQL(CREATE_USER_TABLE);
        Log.d("debug", "onCreate out");

    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion)
    {
        Log.d("debug", "onUpgrade in");
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_CONTACTS);
        onCreate(db);
        Log.d("debug", "onUpgrade out");
    }


    @Override
    public synchronized void close()
    {
        Log.d("debug", "close in");
        super.close();
        Log.d("debug", "close out");
    }

    public void onOpen()
    {
        Log.d("debug", "onOpen in");
        super.onOpen(db);
        db = this.getWritableDatabase();
        Log.d("debug", "onOpen out");
    }

    public void insertUser ()
    {
        onUpgrade(db, 1, 1);
        //INSERT INTO user (username, password) VALUES ('user', 'useruser')
        Log.d("debug", "insertUser in");
        String INSERT_USER =
                "INSERT INTO " + TABLE_CONTACTS
                + "(" + COLUMN_USERNAME + "," + COLUMN_PASSWORD + ")"
                + " VALUES "
                + "(" + "\'user\'" + "," + "\'useruser\'" + ")";
        db.execSQL(INSERT_USER);
        Log.d("debug", "insertUser out");
    }

    public User getUser()
    {
        Log.d("debug", "getUser in");
        String query =
                    "SELECT * FROM " + TABLE_CONTACTS;

        Cursor cursor = db.rawQuery(query, null);
        User user = new User();
        if(cursor.moveToFirst())
        {
            cursor.moveToFirst();
            user.setUsername(cursor.getString(0));
            user.setPassword(cursor.getString(1));
            cursor.close();
        }
        else
        {
            user = null;
        }
        Log.d("debug", "getUser out");

        return user;
    }

}
