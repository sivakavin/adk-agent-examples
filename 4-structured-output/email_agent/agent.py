from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

## define output schema
class EmailOutput(BaseModel):
    subject:str = Field(
        description="The subject of the email.should be concise and descriptive."
    )
    body:str = Field(
        description="The body of the email. should be clear and to the point."
    )

## Create email generation agent
root_agent = LlmAgent(
    name = "email_agent",
    model = "gemini-2.5-flash-lite",
    instruction = """
    You are a helpful assistant for generating professional emails. You will be given a topic and you need to generate a concise and descriptive subject and a clear and to the point body for the email.
    
    GUIDELINES:
    - create an appropriate subject line (concise and relevant)
    - keep the body clear and to the point
    - ensure the email is professional in tone
    - Write a well-structured email body with:
    * Professional greeting 
    * Appropriate closing
    * Your name as signature
    - Suggest relevant attachments if applicable (empty list if none needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON matching this structure:
    { "subject": "Subject line here",
    "body": "Email body here with proper paragraphs and formatting"
    } 

    DO NOT include any explanations or additional text outside the JSON response.

    """,
    description = "Generate profession email with structured subject and body.",
    output_schema = EmailOutput,
    output_key = "email"
)
