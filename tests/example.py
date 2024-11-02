from fidelity import fidelity

browser = fidelity.FidelityAutomation(headless=False, save_state=False)
step_1, step_2 = browser.login(username="USER", password="PASS", save_device=True)
if step_1 and step_2:
    print("Logged in")
elif step_1 and not step_2:
    print("2FA code needed")
    code = input("Enter the code\n")
if browser.login_2FA(code):
    print("Logged in")
else:
    print("Browser not logged in")
    exit(1)

account_info = browser.getAccountInfo()
accounts = account_info.keys()
# Test the transaction
success, errormsg = browser.transaction("INTC", 1, 'buy', accounts[0], True)
if success:
    print("Successfully tested transaction")
else:
    print(errormsg)
