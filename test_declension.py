
import declension
import pytest


def test_nominative():
    a_dec = declension.Declension(noun='rAma', gender='M')
    with pytest.warns(UserWarning):
        a_dec.nominative.singular = None
        a_dec['nominative']['singular'] = None
        a_dec.nominative = None
        a_dec['nominative'] = None

    assert a_dec.nominative.singular == 'rAmaH'
    assert a_dec.prathamA.ekavacana == 'rAmaH'
    assert a_dec['nominative']['singular'] == 'rAmaH'
    assert a_dec['prathamA']['ekavacana'] == 'rAmaH'
    assert a_dec.nominative.dual == 'rAmau'
    assert a_dec.prathamA.dvivacana == 'rAmau'
    assert a_dec['nominative']['dual'] == 'rAmau'
    assert a_dec['prathamA']['dvivacana'] == 'rAmau'
    assert a_dec.nominative.plural == 'rAmAH'
    assert a_dec.prathamA.bahuvacana == 'rAmAH'
    assert a_dec['nominative']['plural'] == 'rAmAH'
    assert a_dec['prathamA']['bahuvacana'] == 'rAmAH'
