# myapp/context_processors.py



from datetime import date

def current_date(request):
    return {'current_date': date.today()}


def account_context(request):
    account = request.session.get('Account')
    print("sdfdsfdsffs")
    print(account)  # 调试语句，检查 account 的值
    return {'account': account}