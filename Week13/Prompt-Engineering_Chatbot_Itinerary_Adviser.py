import openai
import os
from together import Together

TOGETHER_API_KEY = "ef30e93374cdab33b70f740c5991e8f737cf835ac6a847fc080f0a937b3327dc"
#OPENAI_API_KEY = "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"
#openai.api_key = OPENAI_API_KEY

client = Together(api_key=TOGETHER_API_KEY)

def instructor_chatbot():
    """Command-line AI Itinerary Chatbot."""
    print("Welcome to AI Itinerary recommender! Answer a few questions to get personalized itenary advice.\n")
    
    days = input("How many (days): ")
    start_date = input("What is the start date (YYYY-MM-DD): ")
    location = input("Where is the destination (city name): ")
    age = input("Enter your age: ")
    amount = input("What is your budget (in NZD): ")
    interests = input("What are your interests? (e.g., culture, adventure, food, etc.): ")
    travel_mode = input("What is your preferred mode of travel? (e.g., walking, cycling, driving, etc.): ")
    kids_traveling = input("Are you traveling with kids? (yes/no): ")
    overnight_stay = input("Do you need overnight stay recommendations? (yes/no): ")
    type_of_accommodation = input("What type of accommodation do you prefer? (e.g., hotel, hostel, Airbnb, etc.): ")
    
    # fitness_goal = input("What is your fitness goal? (e.g., lose weight, build muscle, endurance, etc.): ")
    
    # Construct prompt
    prompt = f"""
    You are a professional trouist recommender. Provide an itinerary recommendation based on user data.
    
    User Details:
    - days: {days} days
    - start_date: {start_date} (YYYY-MM-DD)
    - destination: {location} city
    - age: {age} years
    - budget (NZD): {amount}
    - interests: {interests}
    - travel_mode: {travel_mode}
    - kids_traveling: {kids_traveling}
    - overnight_stay: {overnight_stay}
    - type_of_accommodation: {type_of_accommodation}

    Based on your personal information, 
    Then, give a structured itinerary with a name of the place, address and short description for each day seperatly in order with maximom three activities in a day.
    """
    
    try:
        """ response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a professional itinerary recommender."},
                      {"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        ) """
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=[{"role": "system", "content": "You are a professional itinerary recommender."},
                      {"role": "user", "content": prompt}]
            #max_tokens=200,
            #temperature=0.7
        )
        #print(response.choices[0].message.content)
        
        print("\n My Name is Hadi as AI Itinerary expert:")
        print(response.choices[0].message.content)
        #print(response["choices"][0]["message"]["content"])
        
    except Exception as e:
        print("Error communicating with OpenAI API:", e)

if __name__ == "__main__":
    instructor_chatbot()