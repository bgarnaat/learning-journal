from journal.models import Entry, DBSession
from journal.views import my_view, compose, entry_detail
from pyramid.testing import DummyRequest
from pyramid.response import Response


def test_my_view(dbtransaction, new_entry):
    """Test my_view retunrs a lists entries in it's response object."""
    req = DummyRequest()
    resp = my_view(req)
    entries_dict = resp['entries']
    assert entries_dict[0] == new_entry


def test_entry_detail_view(dbtransaction, new_entry):
    """Test entry_detail returns a list of entries in it's reposnse object."""
    req = DummyRequest()
    req.matchdict = {'entry_id': new_entry.id}
    resp_dict = entry_detail(req)
    assert resp_dict['entry'] == new_entry


# def test_entry_detail_view(dbtransaction, new_entry):
#     """Test that list_view returns a Query of Entries."""
#     test_request = DummyRequest()
#     test_request.matchdict = {'detail_id': new_entry.id}
#
#     response_dict = detail_view(test_request)
#     assert response_dict['entry'] == new_entry


# class test_NewEntry(Form):
#     pass


# def test_compose(request):
#     pass


# def test_add_new_entry(dbtransaction):
#     from journal.views import compose
#     # req = DummyRequest(title='test title', text='test text')
#     req = testing.DummyRequest()
#     req.title = 'test title'
#     req.text = 'test text'
#     req.method = 'POST'
#     compose(req)
#
#     entries = DBSession.query(Entry).all()
#     assert req.title == entries[0].title




# def test_entry_detail(request):


# def test_edit_entry(request):

def test_home_page(app):
    response = app.get('/')
    assert response.status_code == 200

# def test_entry_page(app, add_entry):
#     import transaction
#     # from conftest import add_entry
#     add_entry()
#     transaction.commit()
#     response = app.get('/entry/1')
#     assert response.status_code == 200

def test_compose_page(app):
    response = app.get('/')
    assert response.status_code == 200

# def test_edit_page(app):
#     response = app.get('/')
#     assert response.status_code == 200
