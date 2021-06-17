# Shodan domain search
from shodan import shodan

SHODAN_API_KEY = "{RwrUWVl9PHcBnCjBaUdrSaSNK7giXW2U}"
api = shodan.Shodan(SHODAN_API_KEY)

print(api.dns.domain_info(domain=input("Enter a domain name: "), history = False, type = None, page = 1))
