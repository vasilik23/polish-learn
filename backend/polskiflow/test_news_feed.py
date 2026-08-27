from unittest.mock import Mock, patch

from django.core.cache import cache
from django.test import SimpleTestCase

from polskiflow.news_feed import CACHE_KEY, latest_official_news


RSS = b'''<?xml version="1.0"?><rss><channel>
<item><title>Nowe dane o gospodarce</title><link>https://stat.gov.pl/aktualnosci/dane/</link><pubDate>Wed, 26 Aug 2026 10:00:00 GMT</pubDate></item>
<item><title>Unsafe host</title><link>https://example.com/trap</link></item>
</channel></rss>'''


class OfficialNewsFeedTests(SimpleTestCase):
    def setUp(self):
        cache.delete(CACHE_KEY)

    @patch("polskiflow.news_feed.urlopen")
    def test_reads_only_allowlisted_https_links(self, mocked_urlopen):
        response = Mock()
        response.read.return_value = RSS
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        mocked_urlopen.return_value = response

        items = latest_official_news()

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Nowe dane o gospodarce")
        self.assertEqual(items[0]["source"], "Główny Urząd Statystyczny")
        self.assertEqual(items[0]["category"], "economy")

    @patch("polskiflow.news_feed.urlopen")
    def test_combines_sources_and_filters_by_category(self, mocked_urlopen):
        links = {
            "stat.gov.pl": ("Dane gospodarcze", "https://stat.gov.pl/aktualnosci/dane/"),
            "polityka": ("Debata polityczna", "https://www.rmf24.pl/fakty/polityka/news-debata,nId,1"),
            "polsatsport": ("Wynik meczu", "https://www.polsatsport.pl/wiadomosc/2026-08-26/mecz/"),
            "kultura": ("Nowy film", "https://www.rmf24.pl/kultura/news-film,nId,2"),
        }

        def response_for(request, timeout, context):
            key = next(key for key in links if key in request.full_url)
            title, link = links[key]
            response = Mock()
            response.read.return_value = (
                f'<?xml version="1.0"?><rss><channel><item><title>{title}</title>'
                f'<link>{link}</link><pubDate>Wed, 26 Aug 2026 10:00:00 GMT</pubDate>'
                '</item></channel></rss>'
            ).encode()
            response.__enter__ = Mock(return_value=response)
            response.__exit__ = Mock(return_value=False)
            return response

        mocked_urlopen.side_effect = response_for

        items = latest_official_news()

        self.assertEqual(len(items), 4)
        self.assertEqual({item["source"] for item in items}, {"Główny Urząd Statystyczny", "RMF24", "Polsat Sport", "RMF24 Kultura"})
        self.assertEqual([item["title"] for item in latest_official_news(category="sport")], ["Wynik meczu"])
        self.assertEqual(len(latest_official_news(category="unknown")), 4)

    @patch("polskiflow.news_feed.urlopen", side_effect=OSError)
    def test_network_failure_returns_empty_feed(self, _mocked_urlopen):
        self.assertEqual(latest_official_news(), [])
