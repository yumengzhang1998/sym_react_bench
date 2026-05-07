from topokin.states.filtering import minimum_lifetime_filter


def test_short_transient_removed():
    s = ["A","A","A","B","A","A","A"]
    assert minimum_lifetime_filter(s,2) == ["A"]*7
