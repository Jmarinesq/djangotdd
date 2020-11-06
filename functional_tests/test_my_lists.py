from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .management.commands.create_session import create_preauthenticated_session
from .server_tools import create_session_on_server
from .base import FunctionalTest
from unittest import skip
User = get_user_model()
import time


class MyListTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        if self.staging_server:
            session_key = create_session_on_server(self.staging_server, email)
        else:
            session_key = create_preauthenticated_session(email)
        ## to set a cookie we need to first visit the domain.
        ## 404 pages load the quickest!
        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(
            dict(
                name=settings.SESSION_COOKIE_NAME,
                value=session_key,
                path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        # Edith is a logged-in user
        self.create_pre_authenticated_session(email)

        # She goes to the home page and starts a list
        self.browser.get(self.live_server_url)

        self.wait_to_be_logged_in(email)
        self.add_list_item('Reticulate splines')
        time.sleep(0.7)
        self.add_list_item('Immanentize eschaton')

        first_list_url = self.browser.current_url

        # She notices a "My Lists" link, for the first time.
        self.browser.find_element_by_link_text('My lists').click()

        # She sees that her list is in there, named according to its
        # first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Reticulate splines')
        )

        self.browser.find_element_by_link_text('Reticulate splines').click()

        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )

        # She decides to start another list, just to see
        self.browser.get(self.live_server_url)


        self.add_list_item('Click cows')
        second_list_url = self.browser.current_url

        # Under "My Lists", her new list appears
        self.browser.find_element_by_link_text('My lists').click()

        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Click cows')
        )
        self.browser.find_element_by_link_text('Click cows').click()

        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )

        # She logs out.  The "My Lists" option disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_elements_by_link_text('My lists'),
                []
            )
        )








