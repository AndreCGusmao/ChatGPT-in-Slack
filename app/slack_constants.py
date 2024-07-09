from app.env import OPENAI_TIMEOUT_SECONDS

TIMEOUT_ERROR_MESSAGE = (
    f":warning: Desculpe! Parece que a OpenAI não respondeu dentro do prazo de {OPENAI_TIMEOUT_SECONDS} segundos. "
    "Por favor, tente sua solicitação novamente mais tarde. "
)

DEFAULT_LOADING_TEXT = ":loading: Um momento, por favor..."
