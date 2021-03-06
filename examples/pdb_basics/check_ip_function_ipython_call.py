import ipaddress

def check_ip(ip_address, verbose=False):
    import IPython; IPython.embed()
    try:
        ipaddress.ip_interface(ip_address)
        return True
    except ValueError as err:
        if verbose: print(err)
        return False



if __name__ == "__main__":
    result = check_ip('10.1.1.1/24')
    result = check_ip('10.1.1.1000/24')
    print('Function result:', result)

