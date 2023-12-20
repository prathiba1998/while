#case-1-exception in outer try

try:
    print(50/0)
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#


#case-2-no exception
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#




#case-3-exception in outer try stmt 2
try:
    print("outer try block")
    print(20/0)
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case-4-inner try stmt 1
try:
    print("outer try block")#
    try:
        print(50/0)
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#


#case-5-inner try- stmt 2
try:
    print("outer try block")#
    try:
        print("inner try block")#
        print(50/0)
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#



#case6-inner except abnormal ter--
try:
    print(50/0)
    print("outer try block")#
    try:
        print("inner try block")#
    except ValueError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#



#case-7-inner excep--stmt 1
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print(50/0)
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case-8-inner excep--stmt 2
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")
        print(50/0)
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case-9-inner finally--stmt 1
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print(50/0)
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case 10-inner finally--stmt 2--
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
        print(50/0)
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case11-outer excep--abnormal term--
try:
    print(50/0)
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ValueError:
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#

#case 12-outer excep--stmt 1
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print(50/0)
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#


#case-13-outer excep--stmt 2
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
    print(50/0)
finally:
    print("outer finally block")#
print("outside the all block")#

#case 14-outer finally--stmt 1--
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print("outer except block")
finally:
    print(50/0)
    print("outer finally block")#
print("outside the all block")#


#case 15-excep--in inner,outer--
try:
    print("outer try block")#
    try:
        print("inner try block")#
    except ZeroDivisionError:
        print(50/0)
        print("inner except block")#
    finally:
        print("inner finally block")#
    print("outside the inner block")#
except ZeroDivisionError:
    print(50/0)
    print("outer except block")
finally:
    print("outer finally block")#
print("outside the all block")#



