import reflex as rx
from althea import styles
from althea.components import loading_icon
from althea.state import QA, State

def message(qa: QA) -> rx.Component:
    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text(
                qa.answer,
                bg=styles.bg_medium_color,
                border= "1px solid",
                border_color= "#fff3",
                shadow= "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                **styles.message_style,
            ),
            text_align="left",
            padding_top="8em",
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
        overflow="auto",
        padding_bottom="5em",
        display=rx.cond(State.submitted, "block", "none"),
    )
 
 
def boxes_component() -> rx.Component:
    """Component to render the boxes to the right under the action bar."""
    box_style = {
        "background_color": styles.bg_medium_color, 
        "color": styles.text_light_color,
        "border": "1px solid",
        "border_color": "#fff3",
        "border_radius": "var(--chakra-radii-md)",
        "shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
        "padding": "16px",
        "width": "70%",
        "margin_bottom": "12px", 
        "height": "auto",
    }

    boxes_container_style = {
        "position": "fixed",
        "top": "240px", 
        "right": "0rem",
        "width": "700px", 
        "max_height": "calc(100vh - 120px)", 
        "overflow_y": "auto",  
        "padding_bottom": "1rem", 
    }

    return rx.chakra.box(
        rx.chakra.box(
            rx.chakra.text("Chart", font_weight="bold"),
            "Content of the first box",
            **box_style,
            #top="100%",
        ),
        rx.chakra.box(
            rx.chakra.text("Research Gap", font_weight="bold"),
            "Content of the second box", 
            **box_style,
            #top="calc(100% + 220px)",
        ),
        **boxes_container_style,
        display=rx.cond(State.submitted, "block", "none"),
        
    )


def layout() -> rx.Component:
    """The main layout of the application."""
    return rx.chakra.box(
        action_bar(),
        boxes_component(), 
        chat(),
        min_height="100vh",  
        #position="relative",
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
                "Althea is a research assistant. Use with discretion.",
                font_size="xs",
                color="#fff6",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        boxes_component(),
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
        align_items="stretch",
        width="100%",
        #is_open=State.submitted,
    )

