import reflex as rx

from gixia.components.header import header
from gixia.core.service import service
from gixia.states.base_state import BaseState


class PaperState(BaseState):

    arxiv_id: str = ""
    title: str = ""
    authors: str = ""
    abstract: str = ""

    def on_load(self):
        self.arxiv_id = self.router.page.params.get("_arxiv_id")
        paper = service.get_paper(self.arxiv_id)
        if paper:
            self.title = paper.title
            self.authors = ', '.join(paper.authors)
            self.abstract = paper.abstract

@rx.page(route="/paper/[_arxiv_id]", on_load=PaperState.on_load)
def paper() -> rx.Component:
    return rx.container(
        header(),
        rx.hstack(
            rx.vstack(
                rx.heading(
                    PaperState.title,
                    size="7",
                ),
                rx.text(
                    PaperState.authors,
                    size="2",
                    color="gray",
                ),
                rx.text(
                    PaperState.abstract,
                    size="3",
                    color=rx.color("black", 8),
                ),
                width="50%",
                margin="40px",
                margin_right="0px",
            ),
            rx.vstack(
                rx.heading(
                    "8.2",
                    font_family="Hanken Grotesk",
                    font_size="100px",
                    align="center",
                    justify="center",
                    margin="50px",
                ),
                rx.hstack(
                    rx.button(
                        "Want to Read",
                        size="3",
                    ),
                    rx.button(
                        "Mark as Read",
                        size="3",
                    ),
                    align="center",
                    margin="20px",
                ),
                rx.hstack(
                    rx.text("9", width="10%", align="center", size="1"),
                    rx.vstack(
                        rx.heading("Brandon Wu", size="1"),
                        rx.text(
                            "The paper is still LLMs all the way down. The evaluation is suitable to compare different systems for idea generation, but still contains no evaluation of the produced ideas themselves. The text is still written in a very selling manner, overestimating the capabilities of LLMs by assuming that hey would be able to reason over scientific research methods.",
                            size="1",
                        ),
                        width="90%",
                    ),
                    width="100%",
                ),
                rx.hstack(
                    rx.text("4", width="10%", align="center", size="1"),
                    rx.vstack(
                        rx.heading("Alex", size="1"),
                        rx.text(
                            "It would be great to see more concrete analyses on the relationship between automatic and human evaluations (e.g. rank correlations). From Figure 4 and 6 they seem to be in agreement, but this point would be much stronger if there was an explicit comparison.",
                            size="1",
                        ),
                        width="90%",
                    ),
                    width="100%",
                ),
                rx.hstack(
                    rx.text("1", width="10%", align="center", size="1"),
                    rx.vstack(
                        rx.heading("Feifei Liu", size="1"),
                        rx.text(
                            "The paper is clearly written and well-structured, making it easy to follow.",
                            size="1",
                        ),
                        width="90%",
                    ),
                    width="100%",
                ),
                width="50%",
                margin="40px",
                align="center",
            ),
            margin_top="50px",
        ),
        size="4",
        background_color=rx.color("gold", 3),
    )