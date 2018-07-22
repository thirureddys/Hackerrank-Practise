import re
##
##for _ in range(int(raw_input())):
##    s = raw_input().rstrip()
##    if re.search(r'^[456]\d{3}(\?|(-)|)(\d{4}\1){2}\d{4}$', s) not re.search(r'(\d)(-|\1){4}', s):
##        print "Valid"
##    else:
##        print "Invalid"


##cards=['4123456789123456','5123-4567-8912-3456','61234-567-8912-3456','4123356789123456','5133-3367-8912-3456','5123 - 3567 - 8912 - 3456']
##
##for i in cards:
##    #s = raw_input().rstrip()
##    if re.search(r'^[456]\d{3}(\?|(-)|)(\d{4}\1){2}\d{4}$',i) not in re.search(r'(\d)(-|\1){4}', i):
##        print "Valid"
##    else:
##        print "Invalid"



cr1='5133-3367-8912-3456'
m1=re.match(r'(\d)(-|\1){4}', cr1)
print m1
