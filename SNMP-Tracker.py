from pysnmp import hlapi
import time
from datetime import datetime

# define SNMP get function
def get(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.getCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]

# define SNMP walk function
def walk(target, oids, credentials, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
    handler = hlapi.nextCmd(
        engine,
        credentials,
        hlapi.UdpTransportTarget((target, port)),
        context,
        *construct_object_types(oids)
    )
    return fetch(handler, 1)[0]

def construct_object_types(list_of_oids):
  object_types = []
  for oid in list_of_oids:
    object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
    return object_types

def fetch(handler, count):
  result = []
  for i in range(count):
    try:
        error_indication, error_status, error_index, var_binds = next(handler)
        if not error_indication and not error_status:
            items = {}
            for var_bind in var_binds:
                items[str(var_bind[0])] = cast(var_bind[1])
            result.append(items)
        else:
            raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
    except StopIteration:
        break
  return result

def cast(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        try:
            return float(value)
        except (ValueError, TypeError):
            try:
                return str(value)
            except (ValueError, TypeError):
                pass
    return value

# config sleep time
sleep_time=10
host_name=get('10.0.0.1', ['1.3.6.1.2.1.1.5.0'], hlapi.CommunityData('util'))['1.3.6.1.2.1.1.5.0']
interface_name=walk('10.0.0.1', ['.1.3.6.1.2.1.31.1.1.1.1'], hlapi.CommunityData('util'))['1.3.6.1.2.1.31.1.1.1.1.1']
interface_speed= walk('10.0.0.1', ['1.3.6.1.2.1.2.2.1.5'], hlapi.CommunityData('util'))['1.3.6.1.2.1.2.2.1.5.1']


while(True):
# calculate util %
    first_read=walk('10.0.0.1', ['.1.3.6.1.2.1.2.2.1.10'], hlapi.CommunityData('util'))['1.3.6.1.2.1.2.2.1.10.1']
    time.sleep(sleep_time)
    second_read=walk('10.0.0.1', ['.1.3.6.1.2.1.2.2.1.10'], hlapi.CommunityData('util'))['1.3.6.1.2.1.2.2.1.10.1']
    util_per= ((second_read - first_read) * 8 *  100 ) / (sleep_time * interface_speed)
# get the time and record the reading
    date_time=datetime.now()
    with open("Link_utilization.txt", "a") as f:
        f.write(f"{date_time},{host_name},{interface_name} ,{interface_speed} ,{util_per}\n")
    print ("app ran")
 


