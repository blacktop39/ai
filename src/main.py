from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

def main():
    # 환경변수 로드 (예: OPENAI_API_KEY)
    load_dotenv()
    
    # 프롬프트 템플릿 정의
    template = "Translate this text to French: {text}"
    prompt = PromptTemplate(template=template, input_variables=["text"])
    
    # OpenAI LLM 인스턴스 생성 (환경변수를 통해 API 키 관리)
    llm = OpenAI(temperature=0)
    
    # LangChain 체인 생성
    chain = LLMChain(llm=llm, prompt=prompt)
    
    # 체인 실행 예시
    input_text = "Hello, how are you?"
    result = chain.run(text=input_text)
    print("Translated text:", result)

if __name__ == "__main__":
    main()
