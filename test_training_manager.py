from training_manager import TrainingManager
from employee import Employee
from training import Training

def test_training_manager():
    print("=== Testing Training Manager ===")
    
    # Create training manager
    manager = TrainingManager()
    
    # Add employees
    employees = [
        Employee("Alice Johnson", "Frontend", 75000),
        Employee("Bob Smith", "Backend", 85000),
        Employee("Carol Davis", "Data Science", 95000),
    ]
    
    for emp in employees:
        manager.add_employee(emp)
    
    # Add trainings
    trainings = [
        Training("ChatGPT for Developers", "GenAI", "Beginner", 16, 500),
        Training("React Mastery", "Technical", "Advanced", 40, 1200),
        Training("Leadership Skills", "Soft Skills", "Intermediate", 24, 700),
    ]
    
    for train in trainings:
        manager.add_training(train)
    
    print("\n--- Enrolling and Completing Trainings ---")
    
    # Enroll employees in different trainings
    enrollments = [
        ("Alice Johnson", "ChatGPT for Developers"),
        ("Bob Smith", "React Mastery"), 
        ("Carol Davis", "Leadership Skills"),
        ("Alice Johnson", "Leadership Skills"),  # Alice takes 2 trainings
    ]
    
    for emp_name, training_name in enrollments:
        manager.enroll_employee(emp_name, training_name)
        manager.simulate_training_completion(emp_name, training_name)
    
    # Show final summary
    manager.show_summary()

if __name__ == "__main__":
    test_training_manager()