from employee import Employee
from training import Training
from enrollment import Enrollment

def test_enrollment():
    print("=== Testing Enrollment Class ===")
    
    # Create employee and training
    bob = Employee("Bob Smith", "Backend", 90000)
    genai_training = Training("GitHub Copilot Mastery", "GenAI", "Intermediate", 20, 800)
    
    # Add initial productivity score
    bob.add_productivity_score(lines_of_code=180, bug_fix_time=4.0, features_completed=2)
    
    print("--- Before Training ---")
    bob.show_info()
    
    # Create enrollment
    enrollment = Enrollment(bob, genai_training)
    enrollment.start_training()
    
    # Simulate training completion with improved productivity
    print("\n--- Completing Training ---")
    improved_productivity = {
        'lines_of_code_per_day': 250,  # 39% improvement
        'bug_fix_hours': 2.8,          # 30% faster
        'features_completed': 3        # 50% more features
    }
    enrollment.complete_training(improved_productivity)
    
    print("\n--- After Training ---")
    bob.show_info()
    enrollment.show_results()

if __name__ == "__main__":
    test_enrollment()