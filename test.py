from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import  HumanMessagePromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from LoadProperties import LoadProperties
from langchain_community.llms import OCIGenAI
import oci
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Step 1 - setup OCI Generative AI llm

properties = LoadProperties()

# use default authN method
llm = OCIGenAI(
    model_id="cohere.command",
    service_endpoint=properties.getModelName(),
    compartment_id=properties.getCompartment(),
    model_kwargs={"max_tokens":200},
)

# Step 2 - invoke llm with a fixed text input

response = llm.invoke("Tell me one fact about space", temperature=0.7)
print("Case 1 Response - > " + response)


