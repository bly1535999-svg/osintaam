import requests

class OSINTSearch:
    def __init__(self):
        self.email_api = 'https://api.emailchecker.io/v1/check'  # Replace with a legitimate API
        self.username_api = 'https://api.usernamecheck.com/v1/search'  # Replace with a legitimate API
        self.domain_api = 'https://api.domaintools.com/v1/'  # Replace with a legitimate API
        self.phone_api = 'https://api.phonelookup.com/v1/search'  # Replace with a legitimate API
        self.tor_api = 'https:// api.torproject.org/'  # Replace with a legitimate API

    def check_email_breach(self, email):
        response = requests.get(f'{self.email_api}?email={email}')
        return response.json()

    def search_username(self, username):
        response = requests.get(f'{self.username_api}?username={username}')
        return response.json()

    def gather_domain_info(self, domain):
        response = requests.get(f'{self.domain_api}/{domain}')
        return response.json()

    def check_phone_breach(self, phone):
        response = requests.get(f'{self.phone_api}?phone={phone}')
        return response.json()

    def monitor_tor(self):
        response = requests.get(f'{self.tor_api}')
        return response.json()

# Example usage:
osint = OSINTSearch()
print(osint.check_email_breach('example@example.com'))
print(osint.search_username('exampleUser'))
print(osint.gather_domain_info('example.com'))
print(osint.check_phone_breach('+1234567890'))
print(osint.monitor_tor())