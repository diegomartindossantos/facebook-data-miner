import pytest



@pytest.fixture()
def people_names():
    return ['John Doe', 'Donald Duck', 'Szett Droxler', 'Foo Bar', 'Tőke Hal', 'Dér Dénes', 'Teflon Musk', 'Daisy Duck',
            'Guy Fawkes', 'Benedek Elek']

@pytest.fixture
def people(get_people):
    return get_people()

def test_specific_people_has_or_has_not_got_messages(people):
    # TODO LATER parametrize
    import pandas as pd
    assert isinstance(people.data.get('Benedek Elek').messages, pd.DataFrame)
    assert isinstance(people.data.get('Teflon Musk').messages, pd.DataFrame)
    assert isinstance(people.data.get('Tőke Hal').messages, pd.DataFrame)
    assert not isinstance(people.data.get('John Doe').messages, pd.DataFrame)
    assert not isinstance(people.data.get('Szett Droxler').messages, pd.DataFrame)
    assert not isinstance(people.data.get('Daisy Duck').messages, pd.DataFrame)
    assert not isinstance(people.data.get('Guy Fawkes').messages, pd.DataFrame)


def test_people_name(people, people_names):
    people_without_groups = [p for p in people.data.keys() if not p.startswith('group')]
    assert sorted(people_names) == sorted(people_without_groups)


def test_some_convos_are_with_friends(people):
    assert people.data.get('Teflon Musk').friend
    assert not people.data.get('Benedek Elek').friend


def test_specific_people_has_or_has_not_got_media(people):
    assert people.data.get('Teflon Musk').media_dir

#TODO LATER test individuals too