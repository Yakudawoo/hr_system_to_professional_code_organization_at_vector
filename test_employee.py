from employee import Employee

def test_employee():
    print("=== Testing Employee Class ===")
    
    # Create a new employee hero
    alice = Employee("Alice Johnson", "Frontend", 80000)
    alice.show_info()
    
    print("\n--- Adding productivity scores ---")
    # Add some productivity measurements
    alice.add_productivity_score(lines_of_code=200, bug_fix_time=3.5, features_completed=2)
    alice.add_productivity_score(lines_of_code=250, bug_fix_time=3.0, features_completed=3)
    
    # Show latest score
    latest = alice.get_latest_productivity()
    print(f"Latest productivity: {latest}")
    
    print("\n--- Testing level up ---")
    # Give experience points
    alice.level_up(150)  # Should level up to Level 2
    alice.show_info()

if __name__ == "__main__":
    test_employee()