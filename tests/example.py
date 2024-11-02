from fidelity import fidelity

browser = fidelity.FidelityAutomation(headless=False, save_state=False)
browser.login(username="USER", password="PASS", totp_secret="TOTP_SECRET")
browser.page.pause()
