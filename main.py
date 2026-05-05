from generator import generate_task
from utils import check_answer

def main():
    print("📚 Math Trainer запущено")
    print("Введи 'exit' щоб вийти")

    score = 0
    i = 1

    while True:
        question, answer = generate_task()

        print(f"\n🧮 Завдання {i}: {question}")
        user = input("✏️ Відповідь: ")

        if user.lower() == "exit":
            break

        if check_answer(user, answer):
            print("✅ правильно")
            score += 1
        else:
            print(f"❌ неправильно (відповідь: {answer})")

        i += 1

    print("\n🏁 Гра завершена")
    print(f"🎯 Твій результат: {score}")

if __name__ == "__main__":
    main()