from tabulate import tabulate
import traceback

class User:
    def __init__(self):
        # data user dengan username sebagai key
        self.users = {
            "shandy": {
                "name": "Shandy",
                "plan": "Basic Plan",
                "duration": 12,
                "referral_code": "shandy-2134"
            },
            "cahya": {
                "name": "Cahya",
                "plan": "Standard Plan",
                "duration": 24,
                "referral_code": "cahya-abcd",
            },
            "ana": {
                "name": "Ana",
                "plan": "Premium Plan",
                "duration": 5,
                "referral_code": "ana-2f9g",
            },
            "bagus": {
                "name": "Bagus",
                "plan": "Basic Plan",
                "duration": 11,
                "referral_code": "bagus-9f92",
            }
        }

        self.all_plans = {
            "headers": ["Basic Plan", "Standard Plan", "Premium Plan", "Services"],
            "datas": [
                [True, True, True, "can_stream"], 
                [True, True, True, "can_download"],
                [True, True, True, "has_SD"],
                [False, True, True, "has_HD"],
                [False, False, True, "has_UHD"],
                [1,2,4, "num_of_devices"],
                ["3rd party movie only", "Basic Plan Content + Sports (F1, Football, Basketball)", "Basic Plan + Standard Plan + PacFlix Original Series or Movie", "content"],
                [120_000, 160_000, 200_000, "price"]
            ]
        }
    
    def check_all_plans(self):
        """
            fungsi untuk menampilkan semua data plan flix
            input: username (string)
            output: -
        """
        print(tabulate(self.all_plans["datas"], headers=self.all_plans["headers"]))
    

    def check_user_plans(self, username: str):
        """
            fungsi untuk menampilkan data user, plan, dan durasi
            input: username (string)
            output: -
        """
        username_lower = username.lower()
        if self.users.get(username_lower) is not None:
            user = self.users[username_lower]
            print(f"user: {user['name']}, plan: {user['plan']}, duration: {user['duration']} months")

            plans = self.all_plans['headers']
            plan_details = self.all_plans['datas']

            for i in range(len(plans)):
                if user['plan'] == plans[i]:
                    headers = [user['plan'], 'Services']
                    datas = []
                    for d in plan_details:
                        datas.append([d[i], d[-1]])
                    print(tabulate(datas, headers=headers))

        else:
            raise Exception("Sorry, user not found")
    
    def upgrade_plan(self, username: str, new_plan: str):
        """
            fungsi untuk meng-upgrade plan user
            plan yang di upgrade harus lebih tinggi dari plan sebelumnya
            fungsi ini akan mengupdate data plan user dan menambah durasi 1 bulan, 
            lalu mengembalikan informasi biaya upgrade plan 
            input: username, new_plan (string)
            output: -
        """
        try:
            username_lower = username.lower()
            if self.users.get(username_lower) is not None:
                user = self.users[username_lower]
                old_plan = user["plan"]
                all_plan_data = self.all_plans['headers'][:-1]
                all_plan_price = self.all_plans['datas'][-1]
                old_plan_idx = all_plan_data.index(old_plan)
                new_plan_idx = all_plan_data.index(new_plan)
                total_payment = 0

                if old_plan_idx < new_plan_idx:
                    if user["duration"] > 12:
                        total_payment = all_plan_price[new_plan_idx] - (all_plan_price[new_plan_idx] * 0.05)
                    else:
                        total_payment = all_plan_price[new_plan_idx]
                else:
                    raise Exception("Sorry, cannot upgrade to lower plan")
                
                self.users[username_lower]["plan"] = new_plan
                print("Data plan user successfully updated")
                print(f"total payment: IDR {total_payment}")
            else:
                raise Exception("Sorry, user not found")
        except Exception:
            traceback.print_exc()

    def subscribe_new_user(self, username: str, plan: str, referral_code: str):
        """
            fungsi untuk meng-upgrade plan user
            input: username, plan, referral_code (string)
            output: -
        """
        try:
            username_lower = username.lower()
            if self.users.get(username_lower) is None:
                all_plan_data = self.all_plans['headers'][:-1]
                all_plan_price = self.all_plans['datas'][-1]
                plan_idx = all_plan_data.index(plan)
                total_payment = 0
                referral_exist = False
                if referral_code is not "":
                    for i in self.users:
                        if self.users[i]['referral_code'] == referral_code:
                            referral_exist = True
                    if referral_exist is True:
                        total_payment = all_plan_price[plan_idx] - (all_plan_price[plan_idx] * 0.04)
                    else:
                        raise Exception("Sorry referral code doesn't exist")
                else:
                    total_payment = all_plan_price[plan_idx]

                self.users.update({
                    username_lower: {
                        "name": username,
                        "plan": all_plan_data[plan_idx],
                        "duration": 1,
                        "referral_code": username_lower + "-1234"
                    }
                })

                print(f"Succesfully subscribed to plan {plan}")
                print(f"total payment: IDR {total_payment}")
            else:
                raise Exception("Sorry username already exist")
        except Exception:
            traceback.print_exc()

