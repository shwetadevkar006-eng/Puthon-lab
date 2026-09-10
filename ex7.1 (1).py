# Automated Email Symbol Scanner

def scan_email(text):
    symbols = ['@', '.', '!']

    print("Symbol occurrences:")
    for symbol in symbols:
        count = text.count(symbol)
        print(f"'{symbol}': {count}")


# Example email/text block
email_text = """
Hello John! Please contact me at john.doe@example.com.
My backup email is john@example.com!
Thanks!
"""

scan_email(email_text)