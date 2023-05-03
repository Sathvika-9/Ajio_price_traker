
import pytest
from Ajio_price_traker.Ajio_price_traker import get_ajio_product_info


@pytest.mark.parametrize("url", [
    "https://www.ajio.com/performax-zip-front-jacket-with-contrast-piping/p/443004374_white",
    "https://www.ajio.com/performax-fastdry-active-training-jacket/p/441120188_jetblack",
    "https://www.ajio.com/invalid-url",  # This URL is invalid and should raise an exception
])
def test_get_ajio_product_info(url):
    try:
        data, product_id = get_ajio_product_info(url)
    except Exception as e:
        pytest.fail(f"Exception raised for URL {url}: {str(e)}")
    assert isinstance(data, dict)
    assert isinstance(product_id, str)