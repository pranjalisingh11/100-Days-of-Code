from django.template.defaulttags import spaceless

questions = [
    ["What is the capital of India?", "A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai", "A"],
    ["5 + 7 = ?", "A. 10", "B. 11", "C. 12", "D. 13", "C"],
    ["Which language is this program written in?", "A. C++", "B. Python", "C. Java", "D. HTML", "B"]
]

prizes = [1000, 2000, 5000]
amount = 0

for i in range(len(questions)):
    q = questions[i]
    print("\nQuestion for ₹", prizes[i])
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    ans = input("Your answer (A/B/C/D): ").strip().upper()
    # strip() - removes extra space
    # upper() - ensures user can type a or A (both become "A").

    if ans == q[5]:
        print("✅ Correct!")
        amount = prizes[i]
    else:
        print("❌ Wrong! Game Over.")
        break

print("\n🎉 You take home ₹", amount)
