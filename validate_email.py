import re

def fun(email: str):
    p = re.compile("[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\..{1,3}$")
    match = p.findall(email)

    if len(match) == 1 and match[0] == email:
        return True
    else:
        return False

def filter_emails(emails):
    return list(filter(fun, emails))

if __name__ == "__main__":
    N = int(input())
    emails = list()

    for _ in range (N):
        emails.append(input())