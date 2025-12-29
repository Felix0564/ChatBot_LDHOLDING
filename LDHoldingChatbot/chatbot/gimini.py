# gimini.py (ou renommez-le groq_config.py)
from langchain_groq import ChatGroq
from django.conf import settings

# Utilisation de Llama 3.3-70b pour une qualité professionnelle
llm = ChatGroq(
    temperature=0.4,
    model_name="llama-3.3-70b-versatile",
    groq_api_key=settings.GROQ_API_KEY
)