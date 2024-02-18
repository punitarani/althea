import json
import os

import reflex as rx
import requests



class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


DEFAULT_CHATS = {
    "Althea does research": [],
}


class State(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = DEFAULT_CHATS

    # The current chat name.
    current_chat = "Althea does research"

    # The current question.
    question: str
    
    # Is the question submitted
    submitted: bool = False

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""

    # Whether the drawer is open.
    drawer_open: bool = False

    # Whether the modal is open.
    modal_open: bool = False


    def create_chat(self):
        """Create a new chat."""
        # Add the new chat to the list of chats.
        self.current_chat = self.new_chat_name
        self.chats[self.new_chat_name] = []

        # Toggle the modal.
        self.modal_open = False

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open
        
    def bar_top(self):
        self.submitted = not self.submitted

    def delete_chat(self):
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = DEFAULT_CHATS
        self.current_chat = list(self.chats.keys())[0]
        self.toggle_drawer()

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name
        self.toggle_drawer()

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())

    async def process_question(self, form_data: dict[str, str]):
        self.submitted = True
        question = form_data["question"]
        
        if question == "" or question is None:
            self.submitted = False
            return
        
        self.chats[self.current_chat] = [] 

        answer = "Response here Response here Response here Response here Response here Response here Response here Response here Response here Response here Response here Response here Response here"  # Simulate fetching an answer
        
        self.chats[self.current_chat].append(QA(question=question, answer=answer))

        self.chats = dict(self.chats)

        print(f"Question: {question}, Response: {answer}")
