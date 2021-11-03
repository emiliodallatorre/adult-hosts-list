from io import TextIOWrapper


hosts: TextIOWrapper = open("hosts", "r")
hosts: list = hosts.readlines()

txt: TextIOWrapper = open("list.txt", "w")
for host in hosts:
    domain: str = host.split(" ")[-1]
    txt.write(domain)

txt.close()
