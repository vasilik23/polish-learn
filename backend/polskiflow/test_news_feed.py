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

    @patch("polskiflow.news_feed.urlopen", side_effect=OSError)
    def test_network_failure_returns_empty_feed(self, _mocked_urlopen):
        self.assertEqual(latest_official_news(), [])
