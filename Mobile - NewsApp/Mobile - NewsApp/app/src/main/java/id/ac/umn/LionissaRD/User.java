package id.ac.umn.LionissaRD;

public class User
{
    private String username, password;

    public User()
    {

    }

    public User(String username, String password)
    {
        setUsername(username);
        setPassword(password);
    }

    public void setUsername(String username)
    {
        this.username = username;
    }

    public String getUsername()
    {
        return this.username;
    }

    public void setPassword(String password)
    {
        this.password = password;
    }

    public String getPassword()
    {
        return this.password;
    }
}
