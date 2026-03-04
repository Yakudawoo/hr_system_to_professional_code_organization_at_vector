from training import Training

def test_training():
    print("=== Testing Training Class ===")
    
    # Create different types of training
    trainings = [
        Training("ChatGPT for Developers", "GenAI", "Intermediate", 24, 750),
        Training("React Advanced Patterns", "Technical", "Advanced", 40, 1200),
        Training("Team Leadership", "Soft Skills", "Beginner", 16, 500)
    ]
    
    for training in trainings:
        training.show_info()
        print(f"   Expected improvements: {training.expected_improvements}")
        print()

if __name__ == "__main__":
    test_training()