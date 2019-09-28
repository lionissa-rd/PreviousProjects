package id.ac.umn.LionissaRD;

public class News
{
    private String title, urlToImage, description, url, author, source;

    public News()
    {

    }

    public News(String title, String urlToImage, String description, String url, String author, String source)
    {
        setTitle(title);
        setUrlToImage(urlToImage);
        setDescription(description);
        setUrl(url);
        setAuthor(author);
        setSource(source);
    }

    public void setTitle(String title)
    {
        this.title = title;
    }

    public String getTitle()
    {
        return this.title;
    }

    public void setUrlToImage(String urlToImage)
    {
        this.urlToImage = urlToImage;
    }

    public String getUrlToImage()
    {
        return this.urlToImage;
    }

    public void setDescription(String description)
    {
        this.description = description;
    }

    public String getDescription()
    {
        return this.description;
    }

    public void setUrl(String url)
    {
        this.url = url;
    }

    public String getUrl()
    {
        return this.url;
    }

    public void setSource(String source)
    {
        this.source = source;
    }

    public String getSource()
    {
        return this.source;
    }

    public void setAuthor(String author)
    {
        this.author = author;
    }

    public String getAuthor()
    {
        return this.author;
    }
}

