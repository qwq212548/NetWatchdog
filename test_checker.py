from netwatchdog import checker

def test_ping_google():
    success, output = checker.ping_host("8.8.8.8", count=1)
    assert success

def test_check_port_80():
    assert checker.check_port("google.com", 80)

def test_dns_lookup():
    ip = checker.dns_lookup("google.com")
    assert ip is not None
