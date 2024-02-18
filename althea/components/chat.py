import reflex as rx
from althea import styles
from althea.components import loading_icon
from althea.state import QA, State

 
    
""" 
def message(qa: QA) -> rx.Component:

    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text(
                qa.question,
                bg=styles.border_color,
                shadow=styles.shadow_light,
                **styles.message_style,
            ),
            text_align="right",
            margin_top="1em",
        ),
        rx.chakra.box(
            rx.chakra.text(
                qa.answer,
                bg=styles.accent_color,
                shadow=styles.shadow_light,
                **styles.message_style,
            ),
            text_align="left",
            padding_top="1em",
        ),
        width="100%",
    )


def chat() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.box(rx.foreach(State.chats[State.current_chat], message)),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="hidden",
        padding_bottom="5em",
    ) 
 """
        
def cards() -> rx.Component:
    return rx.card(
    rx.link(
        rx.flex(
            rx.card("Card 1", size="1"),
            rx.card("Card 2", size="2"),
            rx.card("Card 3", size="3"),
            rx.card("Card 4", size="4"),
            rx.card("Card 5", size="5"),
            spacing="2",
            align_items="flex-start",
            flex_wrap="wrap",
    )
    ),
    as_child=True,
)
        

def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.text(
                "Explore the scientific literature",
                font_size="3xl",
                font_weight="bold",
                color="#FFFFFF",
                text_align="center",
                width="100%",
                margin_bottom="2em",
            ),
            rx.chakra.form(
                rx.chakra.form_control(
                    rx.chakra.hstack(
                        rx.chakra.input(
                            placeholder="Ask a research question",
                            id="question",
                            _placeholder={"color": "#fffa"},
                            _hover={"border_color": styles.accent_color},
                            style=styles.input_style,
                            
                        ),
                        rx.chakra.button(
                            rx.cond(
                                State.processing,
                                loading_icon(height="1em"),
                                rx.chakra.text("Send"),
                            ),
                            type_="submit",
                            _hover={"bg": styles.accent_color},
                            style=styles.input_style,
                        ),
                    ),
                    
                    is_disabled=State.processing,
                ),
                on_submit=State.process_question,
                reset_on_submit=False,
                width="100%",
            ),
            rx.chakra.text(
                "Althea is a research agent. Use discretion.",
                font_size="xs",
                color="#fff6",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        
        #how to access the value of `action_bar_at_top` 
        #position="absolute",
        position=rx.cond(
            State.submitted == True, "fixed", "absolute"
        ),
        top=rx.cond(
            State.submitted == True, "0%", "50%"
        ),
        left=rx.cond(
            State.submitted == True, "0%", "50%"
        ),
        
        transform=rx.cond(
            State.submitted == True, "", "translate(-50%, -50%)"
        ),
    
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        # border_top=f"1px solid {styles.border_color}",
        align_items="stretch",
        width="100%",
        #is_open=State.submitted,
        
        
    )

