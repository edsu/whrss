During the Trump administration the [White House Website] disabled the RSS feed for its Wordpress site. *whrss.py* generated an RSS feed by scraping the White House blog website. During the four long years of the Trump administration I ran this script from cron every 30 minutes to create an RSS feed that was available at:

[https://inkdroid.org/rss/whitehouse.xml](https://inkdroid.org/rss/whitehouse.xml)

On January 20, 2021 whitehouse.gov began providing an RSS feed again, and so the script was retired, and the old RSS URL permanently redirected to the new location.

[https://whitehouse.gov/feed/](https://whitehouse.gov/feed)

The main impetus for doing this was to use [diffengine] to publish [whitehouse_diff]. But maybe you'll find the RSS useful for other things too?

[White House Website]: https://www.whitehouse.gov/news/ 
[diffengine]: https://github.docnow/diffengine
[whitehouse_diff]: https://twitter.com/whitehouse_diff
