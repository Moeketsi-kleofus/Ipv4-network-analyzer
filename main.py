from ipaddress import IPv4Network
import pandas as pd
try:
    user_network=IPv4Network(input("Enter network address :"),strict=True)
    info=" Is private : {0} \n Network address/Id :{1} \n Broadcast address :{2} \n Netmask :{3} \n Number of network mask bits :{4} \n Number of ip addresses on this network:{5} \n First userble ip address :{6} \n Last userble ip address :{7}\n Number of userble ip addresses on this network :{8} \n Userble ip addresses on this network :{data}"
    results=info.format(user_network.is_private,user_network.network_address,user_network.broadcast_address,user_network.netmask,user_network.prefixlen,user_network.num_addresses,user_network[1],user_network[-2],user_network.num_addresses - 2,data=pd.DataFrame(user_network.hosts()))
    print(results)
except Exception as e:
    print("Error of some kind occured, {}".format(e))


