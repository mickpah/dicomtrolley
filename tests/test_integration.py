"""Any test that does not belong to a single module

Initially created this to test casting between different query types.
Is casting between queries working as intended? This is slightly murky to me.
Test to clarify
"""
import pytest

from dicomtrolley.dicom_qr import DICOMQuery
from dicomtrolley.exceptions import DICOMTrolleyError
from dicomtrolley.mint import MintQuery
from tests.conftest import set_mock_response
from tests.mock_responses import MINT_SEARCH_INSTANCE_LEVEL_ANY


def test_mint_from_query(requests_mock, a_mint):
    """Mint find_studies uses Query.from_basic_query(). Does pass through special
    parameters correctly?
    """

    # Query.from_basic_query()
    set_mock_response(requests_mock, MINT_SEARCH_INSTANCE_LEVEL_ANY)

    a_mint.find_studies(MintQuery(limit=10))
    assert requests_mock.request_history[-1].qs.get("limit") == ["10"]
    requests_mock.reset_mock()


def test_dicom_query_mint_cast(requests_mock, a_mint):
    """Feeding one Query type into a different type searcher. Maybe not probable
    but definitely allowed. Does that work?
    """

    set_mock_response(requests_mock, MINT_SEARCH_INSTANCE_LEVEL_ANY)
    with pytest.raises(DICOMTrolleyError):
        # should fail, casting to mint would lose unsupported StudyID parameter
        a_mint.find_studies(DICOMQuery(StudyID=123))
