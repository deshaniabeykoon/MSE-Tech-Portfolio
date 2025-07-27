import os
from together import Together
from dotenv import load_dotenv
import PyPDF2

#openai.api_key = OPENAI_API_KEY

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
#client = Together(api_key=TOGETHER_API_KEY)
pdf_path = r"D:\Yoobee\Github\MSE800-PSE\Week13\Deshani Abeykoon - DE.pdf"

# --- Load PDF CV ---
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        return "\n".join(page.extract_text() for page in reader.pages)

def instructor_chatbot():
    client = Together(api_key=TOGETHER_API_KEY)

    """Command-line AI Resume Improver and recommender."""
    print("Welcome to Professional Resume Improver and recommender! Answer a few questions to get constructive feedback of your Resume.\n")

    name = input("What is your name? ")
    age = input("Enter your age: ")
    career_stage = input("What is your career stage? (e.g., student, early-career, mid-career, executive): ")
    industry = input("What is your target industry? ")
    target_role = input("What is your target role? ")
    #cv_text = input("Please paste your CV text here: ")
    
    cv_text = extract_text_from_pdf(pdf_path)

    # Construct prompt
    prompt = f"""
    You are a professional career advisor and CV expert. Your job is to review CVs and provide constructive feedback that helps improve the chances of getting hired.

    User Details:
    - Name: {name}
    - Age: {age}
    - Career Stage: {career_stage} (e.g., student, early-career, mid-career, executive)
    - Target Industry: {industry}
    - Target Role: {target_role}

    CV Content:
    {cv_text}

    Instructions:
    1. Give a short general evaluation of the CV.
    2. Point out areas for improvement (e.g., formatting, clarity, missing sections).
    3. Highlight the strengths.
    4. Recommend changes tailored for the target industry and role.
    5. Use a professional tone.
    6. If applicable, suggest keywords or skills that can improve ATS (Applicant Tracking System) score.
    """
    
    try:
        response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
        messages=[{"role": "system", "content": "You are a professional itinerary recommender."},
                      {"role": "user", "content": prompt}],
        #max_tokens=200,
        temperature=0.8,
        stream=True
        )

        print("\n My Name is Chris as AI Resume expert:")
        for token in response:
            if hasattr(token, 'choices'):
                print(token.choices[0].delta.content, end='', flush=True)
        
    except Exception as e:
        print("Error communicating with Meta Llama API:", e)

if __name__ == "__main__":
    instructor_chatbot()