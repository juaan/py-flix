from user import *

userObj = User()

running = True
while running:
    print("Flix Membership CLI")
    print("1. Check Plan")
    print("2. Check User Plan")
    print("3. Upgrade User Plan")
    print("4. Subscribe New User")
    print("5. Exit")
    option = input("Pick option: ")

    if option == "1":
        userObj.check_all_plans()
        print("")
        print("")
    elif option == "2":
        username = input("input username: ")
        userObj.check_user_plans(username)
        print("")
        print("")
    elif option == "3":
        username = input("input username: ")
        new_plan = input("input new plan: ")
        userObj.upgrade_plan(username, new_plan)
        print("")
        print("")
    elif option == "4":
        username = input("input username: ")
        plan = input("input plan: ")
        ref_code = input("input referral code: ")
        userObj.subscribe_new_user(username, plan, ref_code)
        print("")
        print("")
    elif option == "5":
        running = False
    else:
        raise Exception("wrong option, available option (1,2,3,4, or 5)")
else:
    print('Done')
    # Do anything else you want to do here