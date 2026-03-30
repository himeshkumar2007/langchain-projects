from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from  dotenv import load_dotenv
load_dotenv()
 
groq_api_key=os.getenv("groq_api_key")
model=ChatGroq(model='groq/compound-mini',groq_api_key=groq_api_key)

genric_template="translate the following into {language}:"

prompt=ChatPromptTemplate.from_messages(
    [("system",genric_template),("user","{text}")]
)

parser=StrOutputParser()

chain=prompt|model|parser

app=FastAPI(title="langchain server",version="1.0",description="simple runnable server using langchain runnable interface")

add_routes(
    app,
    chain,
    path="/chain"
)
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)