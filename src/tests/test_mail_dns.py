import unittest
import dns.resolver
import os
from dotenv import load_dotenv

class TestDNSMigration(unittest.TestCase):
    domains = []

    mx_expected_result =[
        {'host': 'ASPMX.L.GOOGLE.COM.', 'pref': 5}, 
        {'host': 'ALT1.ASPMX.L.GOOGLE.COM.', 'pref': 10}, 
        {'host': 'ALT2.ASPMX.L.GOOGLE.COM.', 'pref': 10}, 
        {'host': 'ALT3.ASPMX.L.GOOGLE.COM.', 'pref': 15},            
        {'host': 'ALT4.ASPMX.L.GOOGLE.COM.', 'pref': 15} 
    ]

    def load_domains_from_file(fn):
        with open(fn) as f:
          domains = f.read().splitlines()

        return domains
        

    def setUp(self):
        load_dotenv()
        self.domains = TestDNSMigration.load_domains_from_file(os.getenv('DOMAIN_LIST_FILE'))
        
        self.maxDiff=None
        # TODO: Load list of domains from file

    def mx_result(domain):
        dns_result=dns.resolver.resolve(domain, 'MX')
        mx=[]

        for rdata in dns_result:
            mx.append(
                {'host': rdata.exchange.to_text(), 
                 'pref': rdata.preference}
            )     

        return mx       

    def spf_result(domain):
      pass

    def test_mx(self):
      for domain in self.domains:
          with self.subTest(domain=domain):
               mx_query_result = TestDNSMigration.mx_result(domain)

               try:
                   self.assertCountEqual(mx_query_result, 
                                     self.mx_expected_result, 
                                     f" {domain} - Does  not have expected MX")

               except AssertionError as e:
                   raise AssertionError(f"MX Records for {domain} are not see to company standard")
    @unittest.skip
    def test_spf(self):
      pass