# ui/terminal_ui.py

def get_user_action():
    print("\n🛠️  What would you like to do?")
    print("   [1] Feed")
    print("   [2] Let it rest")
    print("   [3] Perform weird ritual")
    print("   [4] Do nothing")
    print("   [q] Quit")
    return input("👉 Your choice: ").strip().lower()
