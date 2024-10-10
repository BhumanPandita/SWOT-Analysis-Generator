import streamlit as st
from langchain import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

template = """
Conduct a detailed SWOT analysis for {company_product} in the {industry} industry, targeting {target_audience}. Please provide the following sections:

1. Strengths:
Identify the key advantages and unique resources of {company_product}. What differentiates it from competitors? Consider factors such as brand reputation, technology, and customer loyalty.

2. Weaknesses:
Discuss the areas where {company_product} may be lacking. What internal factors could hinder its success? Include aspects like resource limitations, market positioning, or operational inefficiencies.

3. Opportunities:
Explore external factors that could benefit {company_product}. What market trends, emerging technologies, or customer needs could be leveraged? Think about potential partnerships, expansion possibilities, and new market segments.

4. Threats:
Analyze potential challenges and risks in the external environment. What competitive pressures or market changes could negatively impact {company_product}? Consider factors like regulatory changes, economic conditions, and competitor actions.

Contextual Note: "Consider industry trends, customer feedback, and competitive landscape while formulating your analysis."

Also start as follows:
Company/Product Name as the Main Heading 

1. Strengths
Content.....

2.Weaknesses
Content....

3.Opportunities
Content....

4.Threats
Content....

Conclusion: Content....
"""


prompt_template = PromptTemplate(template = template,inputs = ['company_product','industry','target_audience'])

template_chain = prompt_template | model

st.set_page_config(
    page_title="Swot Analysis",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded",
    
)
st.header("SWOT Generator 📑")

st.subheader("Generate comprehensive SWOT analyses in seconds 😌")

name = st.text_input("Name of the Company/Product?")

inds = st.text_input("Industry which it belongs to?")

audn = st.text_input("Who is the target_audience?")

if st.button("Generate the Analysis",icon = "🚀"):
    st.write(template_chain.invoke({"company_product":name,"industry":inds,"target_audience":audn}).content)
