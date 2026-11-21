#pip install -U "langchain[openai]"
import os
from langchain.chat_models import init_chat_model

os.environ["OPENAI_API_KEY"]="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"
model=init_chat_model("gpt-6-luna")

"""response=model.invoke("can you predict AI jobs in 2030")

print(response.content)"""

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


# 1. Create prompt template
template = """
Translate the following sentence into {target_language}
using simple and easy words.

Sentence: {sentence}
"""

language_prompt = PromptTemplate(
    input_variables=["sentence", "target_language"],
    template=template
)

# 2. Initialize LLM
llm = ChatOpenAI(
    model="gpt-6-luna",
    temperature=1
)

# 3. Create LCEL chain
chain = language_prompt | llm

# 4. Invoke the chain
result = chain.invoke({
    "sentence": "Generative AI & LLM is the future for next 3 years",
    "target_language": "Hindi"
})

# 5. Display output
print(result.content)
