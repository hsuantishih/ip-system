import pytest
from utils.nckuccapi import NckuCcApi
import json

@pytest.fixture
def nckuccapi():
    return NckuCcApi()

def test_nckuccapi_getuserinfo_empty(nckuccapi):
    assert nckuccapi.GetUserInfo("") == {}

def test_nckuccapi_getuserinfo_wrong(nckuccapi):
    assert nckuccapi.GetUserInfo("Wrong ID") == {}

def test_nckuccapi_getuserinfo_correct(nckuccapi):
    result = nckuccapi.GetUserInfo("P76131466") 
    assert result['userid'] == 'P76131466'
    assert isinstance(result, dict), "Expected a dictionary"

def test_nckuccapi_authenticate_empty(nckuccapi):
    assert nckuccapi.Authenticate("", "") == {}

def test_nckuccapi_authenticate_wrongpwd(nckuccapi):
    result = nckuccapi.Authenticate("P76131466", "Wrong Password")
    assert result['status'] == 'Not authorized'

def test_nckuccapi_authenticate_wrongid(nckuccapi):
    result = nckuccapi.Authenticate("Wrong ID", "12345678")
    assert result['status'] == 'OK'

def test_nckuccapi_authenticate_correct(nckuccapi):
    result = nckuccapi.Authenticate("P76131466", "daniel9K3815")
    assert result['status'] == 'OK'
    assert isinstance(result, dict), "Expected a dictionary"