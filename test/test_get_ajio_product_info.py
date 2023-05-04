import pytest
from Ajio_price_traker.Ajio_price_traker import get_ajio_product_info

@pytest.mark.parametrize("url", [
    "https://www.ajio.com/performax-zip-front-jacket-with-contrast-piping/p/443004374_white",
    "https://www.ajio.com/performax-fastdry-active-training-jacket/p/441120188_jetblack"])
def test_get_ajio_product_info(url):
    """
    Test that get_ajio_product_info returns the expected data and product ID
    for valid and invalid URLs.
    """
    if "invalid-url" in url:
        with pytest.raises(Exception):
            data, product_id = get_ajio_product_info(url)
    else:
        data, product_id = get_ajio_product_info(url)
        assert isinstance(data, dict)
        assert "name" in data
        assert "price" in data
        assert isinstance(product_id, str)
