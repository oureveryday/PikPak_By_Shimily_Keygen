import hmac

key='lovePikPak#520_Shimily'
print("\n")
mac_address = input("机器码: ")
code = hmac.new(key.encode('UTF-8'),mac_address.encode('UTF-8'),"MD5").hexdigest().upper()
print("\n")
print("注册码: " + code)