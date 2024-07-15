from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import  HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_community.llms import OCIGenAI
import oci

# Step 1 - setup OCI Generative AI llm

# service endpoint
endpoint = "https://inference.generativeai.us-chicago-1.oci.oraclecloud.com"

# use default authN method
llm = OCIGenAI(
    model_id="cohere.command",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id="ocid1.user.oc1..aaaaaaaasmynpjr3xdbzlouj7fk4whl5kxwmzjwwny45tostkhdsgdq2hy5a",
    model_kwargs={"max_tokens":200},
)

# Step 2 - invoke llm with a fixed text input

response = llm.invoke("Tell me one fact about space", temperature=0.7)
print("Case 1 Response - > " + response)


