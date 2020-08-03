import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+str(query_char) #We send our first characters of out hashed password
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API')
    return res


#crazy slicing
def get_pass_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines()) #this is a tuple
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()  #
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_api_data(first5)
    return get_pass_leaks_count(response,tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} , you should change the password')
    else:
        print('your password has not been pownes')
    return 'done'


sys.exit(main(sys.argv[1:]))
