def validate_feedback_length ():
    while True:
        feedback = input("Enter ypur feedback:  ")
        if len(feedback) < 10:
            print("Feedback must be at least ten characters")
        else:
            return feedback

def validate_feed_rating ():
     try:
            rating = int(input("Enter your satisfaction rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid rating. Please enter a number between 1 and 5.")
     except ValueError:
            print("Invalid input. Please enter a number.")
      
def classify_feedback(feedback): 
    if "bad" in feedback or "poor" in feedback or "inappropriate" in feedback or "disgusting" in feedback:
        return "Negative"
    elif "excellent" in feedback or "good" in feedback or "amazing" in feedback or "great" in feedback:
        return "Positive"
    else:
        return "Neutral"
    


def main ():
     all_feedback =[]
     while True:
          print("\nWelcome to the customer Feedback system!")
          feedback = validate_feedback_length()
          rating = validate_feed_rating ()
          classification = classify_feedback(feedback)
          word_count = len(feedback.split())
          print("\nFeefback Summary: ")
          print(f"- original Feedback: {feedback}")
          print(f"- Satisfaction Rating: {rating}")
          print(f"- Feedback Classification: {classification}")
          print(f"- Total Word Count: {word_count}")
          all_feedback.append({"feedback": feedback, "rating": rating, "classification": classification})
          another = input("Would you like to enter another feedback? (yes/no): ").strip().lower()
          if another != "yes":
            break
main()