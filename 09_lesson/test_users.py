import pytest

from users_page import get_users_page


@pytest.fixture(scope="module")
def users_page():
    return get_users_page()


def test_create_user(users_page):
    max_id = users_page.get_max_user_id()
    test_user_id = max_id + 1
    test_email = "create_user_autotest@example.com"
    test_subject_id = 1

    users_page.create_user(
        user_id=test_user_id,
        email=test_email,
        subject_id=test_subject_id,
    )

    user = users_page.get_user(test_user_id)

    assert user is not None
    assert user.user_id == test_user_id
    assert user.user_email == test_email
    assert user.subject_id == test_subject_id

    users_page.delete_user(test_user_id)


def test_update_user_email(users_page):
    max_id = users_page.get_max_user_id()
    test_user_id = max_id + 1
    original_email = "before_update_autotest@example.com"
    updated_email = "after_update_autotest@example.com"
    test_subject_id = 1

    users_page.create_user(
        user_id=test_user_id,
        email=original_email,
        subject_id=test_subject_id,
    )

    users_page.update_user_email(
        user_id=test_user_id,
        new_email=updated_email,
    )

    user = users_page.get_user(test_user_id)

    assert user is not None
    assert user.user_email == updated_email

    users_page.delete_user(test_user_id)


def test_delete_user(users_page):
    max_id = users_page.get_max_user_id()
    test_user_id = max_id + 1
    test_email = "delete_user_autotest@example.com"
    test_subject_id = 1

    users_page.create_user(
        user_id=test_user_id,
        email=test_email,
        subject_id=test_subject_id,
    )

    users_page.delete_user(test_user_id)

    user = users_page.get_user(test_user_id)

    assert user is None
