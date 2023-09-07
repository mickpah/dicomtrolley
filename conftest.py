"""Pytest fixtures shared by both tests and docs modules"""
import pytest
import requests

from dicomtrolley.mint import Mint
from dicomtrolley.trolley import Trolley
from dicomtrolley.wado_uri import WadoURI
from tests.mock_responses import MockUrls


@pytest.fixture
def a_session(requests_mock):
    """Calling requests_mock fixture here will mock all calls to requests"""
    return requests.session()


@pytest.fixture
def a_mint(a_session):
    """Mint search with faked urls"""
    return Mint(session=a_session, url=MockUrls.MINT_URL)


@pytest.fixture
def a_wado(a_session):
    return WadoURI(session=a_session, url=MockUrls.WADO_URI_URL)


@pytest.fixture
def a_trolley(a_mint, a_wado) -> Trolley:
    """Trolley instance that will not hit any server"""
    return Trolley(searcher=a_mint, downloader=a_wado, query_missing=True)
