    # def create_resume(job_description, old_resume= "None"):
    #     pass

# using google gemini api
import google.generativeai as genai
import textwrap

from IPython.display import Markdown
GOOGLE_API_KEY = 'AIzaSyCaS27iJdXSc2ZHlSWp1Za5uN8L0l1AdVs'
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-1.5-flash')


#  about section, project section, skills section as according to the jab description.

def create_resume(JOB_DESCRIPTION, oldResumeDetails="None"):
    template = f"""
    JOB DESCRIPTION:
    {JOB_DESCRIPTION}
    OLD RESUME SAMPLE DATA FOR REFERANCE:
    {oldResumeDetails}
    RESPONSE:
    On the basis of the given above job description and old resume data craete a new better resume
    It should be in proper format which can be directly pasted. Use html tags so that the response can be used as part of html webpage. 
    Must return with html tags 
    NOTE: ""Do not write any single extra character""
    NOTHING LIKE THIS: ""Result
Here is the resume content formatted with HTML tags as requested, based on the provided job description: ""
    """
        
    response = gemini_model.generate_content(template)

    # def to_markdown(text):
    #     text = text.replace('•', '  *')
    #     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    #     to_markdown(response.text)

    # # result =  gemini_model.invoke(template).content
    # result = to_markdown(response.text)
    result = response.text
    return result
# aboutReturn("Job description inclued looking for a software engineer having experiance in working with react framework and has aldo working expeirance in cloud platforms like gcp.")